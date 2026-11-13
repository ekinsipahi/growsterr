"""Dispute evidence for a subscription, in the shape of Stripe's dispute `evidence` fields
(English, for the card issuer). Staged on Stripe when a dispute opens (views._on_dispute)
and shown in the admin (Kanıt paketi) to print or check before pressing Submit."""
from django.conf import settings
from django.urls import reverse

from .constants import AUDIENCE, CARRYOVER_TERMS_VERSION, PROFILE_URL
from .models import AccountActivity
from .plan import PLAN_BY_KEY

TEXT_LIMIT = 19000  # Stripe allows 20,000 characters per text field
CANCEL_WAYS = {"account": "the Cancel button in their account",
               "stripe": "the Stripe billing portal"}
ACTIVITY = {"login": "signed in", "dashboard": "opened the growth dashboard", "cancel_page": "opened the cancel page"}
WORDS = {
    "followers": {"audience": "followers", "place": "profile", "follow": "follow, like and comment"},
    "subscribers": {"audience": "subscribers", "place": "channel", "follow": "subscribe, like and comment"},
}


def terms_url():
    """The subscription section of the terms (legal:terms, /terms/ until that app lands)."""
    try:
        path = reverse("legal:terms")
    except Exception:  # noqa: BLE001 - NoReverseMatch while the legal app is a placeholder
        path = "/terms/"
    return f"{settings.SITE_URL}{path}#subscription"


def _utc(value):
    return f"{value:%Y-%m-%d %H:%M} UTC" if value else "-"


def _n(value):
    return f"{value:,}" if value is not None else "-"


def delivery_log(sub):
    """One line per day the growth system reported, newest first."""
    words = WORDS[AUDIENCE.get(sub.platform, "followers")]
    stats = {s.date: s for s in sub.stats.all()}
    lines = []
    for day in reversed(sub.daily()):
        stat = stats[day["date"]]
        reach = []
        if stat.impressions is not None:
            reach.append(f"follow step shown {_n(stat.impressions)} times")
        if stat.visits is not None:
            reach.append(f"{_n(stat.visits)} visited the {words['place']}")
        if stat.confirms is not None:
            reach.append(f"{_n(stat.confirms)} tapped Done after the follow step")
        result = f"{_n(day['followers'])} new {words['audience']} (estimated)" if day["followers"] is not None else ""
        countries = ", ".join(f"{code} {_n(v.get('impressions'))}" for code, v in
                              sorted(stat.countries.items(), key=lambda kv: -kv[1].get("impressions", 0))[:6])
        parts = [p for p in ("; ".join(reach), result, f"countries (people shown): {countries}" if countries else "") if p]
        account = f" (account: {_n(stat.followers)} {words['audience']})" if stat.followers is not None else ""
        lines.append(f"{stat.date:%Y-%m-%d}: {'; '.join(parts) or 'reported'}{account}")
    return lines


def activity_log(sub):
    if not sub.user_id:
        return []
    return [f"{_utc(a.at)}: {ACTIVITY.get(a.kind, a.kind)} from IP {a.ip or '-'} ({a.user_agent[:90] or 'unknown browser'})"
            for a in AccountActivity.objects.filter(user_id=sub.user_id)[:300]]


def carryover_policy(sub):
    """Describe the make-good commitment without inventing delivery or historical consent."""
    if sub.terms_version == CARRYOVER_TERMS_VERSION and sub.terms_accepted_at:
        basis = (f"The recorded acceptance is for terms version {sub.terms_version}, which includes "
                 "the growth shortfall policy.")
    else:
        basis = (f"Recorded accepted terms version: {sub.terms_version or 'not recorded'}. "
                 f"The current growth shortfall policy is in terms version {CARRYOVER_TERMS_VERSION}; "
                 "we offer the make-good commitment below, but do not claim the customer accepted "
                 "this later wording at purchase.")
    return (
        f"{basis} If a paid month falls below its growth target (the lower end of the package's monthly "
        "follower/subscriber range unless a different target was confirmed in writing), the shortfall "
        "remains owed as additional growth. For example, a target of 1,000 and delivery of 800 leaves "
        "200 to complete; this is an illustration, not this customer's measured balance. Outstanding "
        "shortfalls from paid months are added together and reduced only by additional make-good delivery. "
        "They are completed on top of later months' targets, without an extra charge. Canceling the Stripe "
        "subscription or removing a payment method does not erase the obligation; no renewed subscription "
        "or payment is required to complete it. The profile must remain public and available. No fixed "
        "completion date is promised. This is growth still owed, not a cash balance or Stripe credit, "
        "and does not limit mandatory refund rights. This evidence generator has no separate monthly "
        "target or make-good ledger: the customer's exact outstanding balance is not established by "
        "this policy text or by the daily log alone. Attach the dated target, shortfall and make-good "
        "records for this customer before relying on a quantified balance. Outstanding or planned "
        "growth is not proof of completed delivery."
    )


def build(sub):
    """Stripe dispute evidence fields for this subscription (text only; files are added by hand)."""
    package = PLAN_BY_KEY[sub.plan]
    words = WORDS[AUDIENCE.get(sub.platform, "followers")]
    low, high = package["followers"]
    terms = terms_url()
    profile = PROFILE_URL[sub.platform].format(sub.handle)
    delivery = delivery_log(sub)
    activity = activity_log(sub)
    reports = sub.stats.count()
    carryover = carryover_policy(sub)

    product = (
        f"Growsterr {sub.get_plan_display()}: a monthly growth subscription (${sub.amount:.2f} a month) for the "
        f"customer's {sub.platform_name} account @{sub.handle} ({profile}), target audience: {sub.location}. "
        f"During every 30-day period we promote the customer's public {words['place']} to real people through our "
        f"partner network; people who like it {words['follow']} on their own (typically {low:,}-{high:,} new "
        f"{words['audience']} a month, described on the site as a typical range, not a fixed count). It is a digital "
        f"promotion service scheduled across the paid period from the first payment; no password or account access is needed. The customer "
        f"follows the results day by day in their account dashboard at {settings.SITE_URL}{reverse('growth:account')}."
    )
    disclosure = (
        f"Before paying, the customer ticked a required box accepting our terms (version {sub.terms_version or '-'}, "
        f"accepted {_utc(sub.terms_accepted_at)} from IP {sub.ip or '-'}). The order form, Stripe Checkout and the welcome "
        f"email all say: billed monthly until canceled; cancel any time in the account; canceling stops the next payment "
        f"and the paid month runs to its end and isn't refunded. A reminder with the renewal date, the amount and how to "
        f"cancel is emailed 3 days before every renewal. Terms, subscription section: {terms}"
    )
    if sub.terms_version == CARRYOVER_TERMS_VERSION and sub.terms_accepted_at:
        disclosure += (
            " The accepted version also states that shortfalls from paid months are totaled and "
            "completed as additional growth, without another payment, even after Stripe cancellation "
            "or payment-method removal. This policy is not evidence that outstanding growth was delivered."
        )
    if sub.cancel_requested_at:
        rebuttal = (f"The customer canceled the renewal on {_utc(sub.cancel_requested_at)} through "
                    f"{CANCEL_WAYS.get(sub.cancel_source, 'Stripe')}. Cancellation stops future renewals; "
                    f"the paid package is scheduled to run to the end of its paid period. Any outstanding "
                    f"growth from paid months remains owed after cancellation. Payment and delivery records "
                    f"must be checked separately to establish what was charged and delivered.")
    else:
        rebuttal = ("The customer never canceled: there is no cancellation from the Cancel button in the account "
                    "or the billing portal on record, although canceling takes one click.")
    if sub.reminded_for:
        rebuttal += f" The renewal reminder, saying how to cancel, was emailed to {sub.email} before the renewal of {_utc(sub.reminded_for)}."
    rebuttal += f"\n\n{carryover}"
    summary = [
        f"Subscription started {_utc(sub.started_at)}; status {sub.status}; current period ends {_utc(sub.current_period_end)}.",
        f"Welcome email with the terms sent to {sub.email} on activation.",
        f"Account {words['audience']} at the start: {_n(sub.start_followers)}; latest: {_n(sub.current_followers)}"
        f" ({_utc(sub.stats_at)}); {reports} daily delivery reports on record.",
        "", "Growth shortfall and completion policy:", carryover,
        "", f"Daily delivery log (UTC days, from our delivery system). Visits are taps that opened the customer's "
            f"{words['place']}. New {words['audience']} are estimated: the day's views of the follow step times the "
            f"follow rate measured from the account's real counts, never more than the visits. 'Tapped Done' is the "
            f"visitor's own confirmation and is not a follow count:", *delivery,
    ]
    evidence = {
        "product_description": product,
        "customer_email_address": sub.email,
        "customer_name": (sub.user.get_full_name() if sub.user_id else "") or sub.email,
        "customer_purchase_ip": sub.ip or "",
        "service_date": f"{sub.started_at:%Y-%m-%d}" if sub.started_at else "",
        "cancellation_policy_disclosure": disclosure,
        "cancellation_rebuttal": rebuttal,
        "refund_policy_disclosure": ("Paid months are not refunded: the service starts with the payment and is delivered "
                                     "across the month. Shown on the order form, in Stripe Checkout, in the welcome email "
                                     f"and in the terms (subscription section): {terms}"),
        "refund_refusal_explanation": (
            "The daily delivery log below records the reported activity; it does not by itself establish "
            "that every monthly growth target was met or that service was delivered on unreported days. "
            "Any shortfall remains an obligation to complete, not completed delivery. The customer could "
            "cancel the next renewal in their account. A make-good commitment alone does not establish "
            "that a refund is unwarranted; review the disputed period, applicable terms and mandatory rights. "
            + carryover
        ),
        "access_activity_log": "\n".join(activity) or "No sign-ins on record.",
        "uncategorized_text": "\n".join(summary),
    }
    return {k: v[:TEXT_LIMIT] for k, v in evidence.items() if v}
