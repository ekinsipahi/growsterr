"""The four legal pages: title, dates and the numbered sections that make the table of contents.
The text of each section is in templates/legal/<key>.html, inside {% section "<id>" %}.

Section ids are anchors other pages link to: keep them stable. The order form links to
/terms/#subscription, the part customers accept with the terms box (TERMS_VERSION in
apps/growth/constants.py: bump it when that section changes)."""
from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True)
class LegalPage:
    key: str            # URL name in the "legal" namespace and template name
    title: str
    nav: str            # short name in the row of legal page links
    description: str    # meta description
    lead: str
    updated: date       # "Last updated" and the sitemap's lastmod
    sections: tuple     # ((id, title), ...) in page order

    def toc(self):
        return [{"id": sid, "title": title, "number": n} for n, (sid, title) in enumerate(self.sections, 1)]


UPDATED = date(2026, 11, 13)

PAGES = {page.key: page for page in (
    LegalPage(
        key="terms",
        title="Terms of Service",
        nav="Terms",
        description="The terms for Growsterr's monthly growth packages for Instagram, TikTok and YouTube: "
                    "real people, monthly renewal, cancel any time.",
        lead="The agreement between you and Growsterr for our monthly growth packages, in plain words.",
        updated=UPDATED,
        sections=(
            ("who-we-are", "Who we are"),
            ("service", "What we do"),
            ("real-people", "Real people, typical ranges"),
            ("account", "Your account and your order"),
            ("prices", "Prices and payment"),
            ("subscription", "Subscription, renewal and cancellation"),
            ("refunds", "Refunds"),
            ("disputes", "Payment disputes and our records"),
            ("acceptable-use", "Acceptable use"),
            ("platforms", "Instagram, TikTok and YouTube"),
            ("content", "Your content and ours"),
            ("liability", "Liability"),
            ("changes", "Changes to these terms"),
            ("law", "Governing law"),
            ("contact", "Company details and contact"),
        ),
    ),
    LegalPage(
        key="privacy",
        title="Privacy Policy",
        nav="Privacy",
        description="How Growsterr collects, uses and protects your personal data, who helps us, "
                    "and your rights under the GDPR.",
        lead="What we collect when you use Growsterr, why we need it, who helps us, and the choices you have.",
        updated=UPDATED,
        sections=(
            ("who-we-are", "Who we are"),
            ("data", "What we collect"),
            ("purposes", "Why we use it"),
            ("providers", "Who helps us"),
            ("transfers", "Transfers outside the EEA"),
            ("retention", "How long we keep it"),
            ("security", "Security"),
            ("rights", "Your rights"),
            ("age", "Age"),
            ("cookies", "Cookies"),
            ("changes", "Changes to this policy"),
            ("contact", "Contact"),
        ),
    ),
    LegalPage(
        key="cookies",
        title="Cookie Policy",
        nav="Cookies",
        description="Growsterr uses only the cookies the site needs to work. "
                    "No analytics or advertising cookies.",
        lead="Growsterr uses only the cookies it needs to work. No analytics, no advertising, no tracking.",
        updated=UPDATED,
        sections=(
            ("what", "What cookies are"),
            ("cookies-we-use", "The cookies we use"),
            ("browser-storage", "Stored in your browser"),
            ("payment-and-sign-in", "Payment and sign-in pages"),
            ("no-tracking", "No analytics or advertising"),
            ("control", "Managing cookies"),
            ("contact", "Contact"),
        ),
    ),
    LegalPage(
        key="refunds",
        title="Refund Policy",
        nav="Refunds",
        description="How payments, cancellations and refunds work for Growsterr's monthly growth packages.",
        lead="How payments, cancellations and refunds work, in plain words. Our Terms of Service have the full details.",
        updated=UPDATED,
        sections=(
            ("paid-month", "The month you've paid for"),
            ("cancel", "Canceling"),
            ("reminders", "Renewal reminders"),
            ("failed-payments", "If a payment fails"),
            ("when-we-refund", "When we do refund"),
            ("consumer-rights", "Your rights as a consumer"),
            ("questions", "Questions about a charge"),
        ),
    ),
)}
