from django.conf import settings
from django.db import models

from .constants import PLATFORM_NAMES, PLATFORMS
from .plan import CHOICES as PLAN_CHOICES

PLATFORM_CHOICES = [(p, PLATFORM_NAMES[p]) for p in PLATFORMS]


class Customer(models.Model):
    """What a site account needs beyond Django's User (username = email)."""

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customer")
    email_verified = models.BooleanField("E-posta onaylı", default=False)
    lang = models.CharField("Dil", max_length=5, default="en")
    created_at = models.DateTimeField("Oluşturuldu", auto_now_add=True)

    class Meta:
        verbose_name = "Müşteri hesabı"
        verbose_name_plural = "Müşteri hesapları"

    def __str__(self):
        return self.user.email


class AgencySubscription(models.Model):
    """A monthly growth package for one Instagram, TikTok or YouTube account (see plan.py).
    Internal names say "followers" for every platform; on YouTube they are subscribers."""

    STATUS = [
        ("pending", "Ödeme bekleniyor"),
        ("requested", "Başvuru (ödeme kapalıyken)"),
        ("active", "Aktif"),
        ("past_due", "Ödeme başarısız"),
        ("canceled", "İptal edildi"),
    ]
    PLATFORMS = PLATFORM_CHOICES

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name="growth_subscriptions")
    email = models.EmailField("E-posta")
    platform = models.CharField("Platform", max_length=12, choices=PLATFORM_CHOICES, default="instagram")
    handle = models.CharField("Kullanıcı adı", max_length=30, help_text="@ olmadan")
    location = models.CharField("Hedef konum", max_length=120)
    phone = models.CharField("Telefon", max_length=20, blank=True, help_text="Influencer ile iletişim için (sipariş formu)")
    plan = models.CharField("Paket", max_length=12, choices=PLAN_CHOICES, default="starter")
    amount = models.DecimalField("Aylık tutar (USD)", max_digits=8, decimal_places=2)
    lang = models.CharField("Dil", max_length=5, default="en")
    status = models.CharField("Durum", max_length=12, choices=STATUS, default="pending")
    started_at = models.DateTimeField("Başladı", null=True, blank=True)
    current_period_end = models.DateTimeField("Dönem bitişi", null=True, blank=True)
    cancel_at_period_end = models.BooleanField("Dönem sonunda bitecek", default=False)
    canceled_at = models.DateTimeField("İptal", null=True, blank=True)
    CANCEL_SOURCES = [("account", "Hesap paneli"), ("stripe", "Stripe portalı / panel")]
    cancel_requested_at = models.DateTimeField("İptal talebi", null=True, blank=True)
    cancel_source = models.CharField("İptal nereden", max_length=10, choices=CANCEL_SOURCES, blank=True)
    reminded_for = models.DateTimeField("Hatırlatma gönderilen dönem", null=True, blank=True,
                                        help_text="Yenileme hatırlatması bu dönem bitişi için gönderildi")
    # Evidence of what the customer agreed to: the required terms box on the order form.
    terms_accepted_at = models.DateTimeField("Şartlar kabul edildi", null=True, blank=True)
    terms_version = models.CharField("Şart sürümü", max_length=20, blank=True)
    user_agent = models.CharField("Tarayıcı", max_length=300, blank=True)
    stripe_checkout_session_id = models.CharField(max_length=128, blank=True, db_index=True)
    stripe_subscription_id = models.CharField(max_length=64, blank=True, db_index=True)
    stripe_customer_id = models.CharField(max_length=64, blank=True, db_index=True)
    # Filled in by the growth system: Linksterr's numbers (linksterr.py) or the stats API (api.py).
    start_followers = models.PositiveIntegerField("Başlangıç takipçi", null=True, blank=True)
    current_followers = models.PositiveIntegerField("Güncel takipçi", null=True, blank=True)
    stats_at = models.DateTimeField("Son veri", null=True, blank=True)
    # Linksterr's estimate for the next 30 days at today's pace:
    # {"days": 30, "new_followers": 1230, "low": 1160, "high": 1290, "per_day": 41.0}
    projection = models.JSONField("30 gün tahmini", null=True, blank=True)
    notified = models.BooleanField("Bildirim gönderildi", default=False)
    mail_error = models.TextField("E-posta hatası", blank=True)
    note = models.TextField("Not", blank=True)
    ip = models.GenericIPAddressField(null=True, blank=True)
    # Where the order came from (static/js/app.js fills the order form's hidden fields):
    # the page whose button led to the order form, the first page of the visitor's first visit,
    # and the outside site that sent them there ("google.com", "instagram.com"; "" = typed in).
    # YouTube only: the video new viewers are sent to (they subscribe first, then watch).
    # Sent to Linksterr in /growth/api/subscriptions/: "" = never picked, "channel" = the customer
    # removed it (back to the channel page), else https://www.youtube.com/watch?v=<id>.
    video_url = models.CharField("YouTube videosu", max_length=300, blank=True)
    source_page = models.CharField("Satın aldığı sayfa", max_length=300, blank=True)
    landing_page = models.CharField("İlk geldiği sayfa", max_length=300, blank=True)
    referrer = models.CharField("Nereden geldi", max_length=300, blank=True)
    first_visit_at = models.DateTimeField("İlk ziyaret", null=True, blank=True)
    utm_source = models.CharField(max_length=150, blank=True)
    utm_medium = models.CharField(max_length=150, blank=True)
    utm_campaign = models.CharField(max_length=150, blank=True)
    gclid = models.CharField(max_length=150, blank=True)
    created_at = models.DateTimeField("Oluşturuldu", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Influencer paketi aboneliği"
        verbose_name_plural = "Influencer paketi abonelikleri"

    def __str__(self):
        return f"#{self.pk} @{self.handle} {self.platform_name} {self.get_plan_display()} · {self.get_status_display()}"

    @property
    def platform_name(self):
        return PLATFORM_NAMES[self.platform]

    def daily(self):
        """[{date, followers, likes, comments, visits, countries}] per day, oldest first, only
        measured numbers. New followers are what the growth system counted for the day (without
        that, the change in the account's follower count); likes and comments only when a system
        sent them (Linksterr measures neither); visits: people who opened the profile from our
        network (or None)."""
        rows, previous = [], self.start_followers
        for stat in sorted(self.stats.all(), key=lambda s: s.date):
            gained = stat.new_followers
            if gained is None and stat.followers is not None and previous is not None:
                gained = max(stat.followers - previous, 0)
            rows.append({"date": stat.date, "followers": gained, "likes": stat.likes, "comments": stat.comments,
                         "visits": stat.visits, "countries": stat.countries or {}})
            if stat.followers is not None:
                previous = stat.followers
        return rows

    @property
    def gained(self):
        """New followers since the package started (None before the first reading)."""
        counted = [d["followers"] for d in self.daily() if d["followers"] is not None]
        return sum(counted) if counted else None


class SubscriptionStat(models.Model):
    """One day of numbers from the growth system: the new followers we brought that day and
    the account's follower count; likes and comments only when a system measured and sent them.
    Feeds the dashboard. synced_at: when Linksterr's numbers for the day were last written."""

    subscription = models.ForeignKey(AgencySubscription, on_delete=models.CASCADE, related_name="stats")
    date = models.DateField("Gün", db_index=True)
    followers = models.PositiveIntegerField("Hesap takipçi", null=True, blank=True)
    # Sent by the growth system; when missing, the change in the follower count is used.
    new_followers = models.PositiveIntegerField("Yeni takipçi", null=True, blank=True)
    likes = models.PositiveIntegerField("Beğeni", null=True, blank=True, help_text="Yalnızca ölçülüp gönderildiyse")
    comments = models.PositiveIntegerField("Yorum", null=True, blank=True, help_text="Yalnızca ölçülüp gönderildiyse")
    # Delivery evidence from the growth system: how many real people were shown the profile,
    # went to it and said they followed, and from which countries ({"DE": {"impressions": ...}}).
    impressions = models.PositiveIntegerField("Gösterim", null=True, blank=True, help_text="Profilin gösterildiği kişi")
    visits = models.PositiveIntegerField("Profil ziyareti", null=True, blank=True)
    confirms = models.PositiveIntegerField("Takip onayı", null=True, blank=True, help_text="“Takip ettim” diyen kişi")
    countries = models.JSONField("Ülkeler", default=dict, blank=True)
    synced_at = models.DateTimeField("Linksterr'dan çekildi", null=True, blank=True)

    class Meta:
        ordering = ["date"]
        verbose_name = "Günlük veri"
        verbose_name_plural = "Günlük veriler"
        constraints = [models.UniqueConstraint(fields=["subscription", "date"], name="growth_stat_subscription_date")]

    def __str__(self):
        return f"#{self.subscription_id} {self.date} {self.followers}"


class AccountActivity(models.Model):
    """Sign-ins and dashboard visits of customer accounts: evidence that a customer used
    the service (Stripe dispute access_activity_log). Dashboard visits at most once an hour."""

    KINDS = [("login", "Giriş"), ("dashboard", "Panel görüntüleme"), ("cancel_page", "İptal sayfası")]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="growth_activity")
    kind = models.CharField("Ne", max_length=12, choices=KINDS)
    ip = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField("Tarayıcı", max_length=300, blank=True)
    at = models.DateTimeField("Zaman", auto_now_add=True, db_index=True)

    class Meta:
        ordering = ["-at"]
        verbose_name = "Hesap hareketi"
        verbose_name_plural = "Hesap hareketleri"

    def __str__(self):
        return f"{self.user} {self.kind} {self.at:%Y-%m-%d %H:%M}"


class Dispute(models.Model):
    """A Stripe dispute (chargeback) on one of our subscriptions. Evidence is staged on Stripe
    when it opens; the team reviews it and presses Submit in the Stripe Dashboard."""

    subscription = models.ForeignKey(AgencySubscription, on_delete=models.CASCADE, related_name="disputes")
    dispute_id = models.CharField(max_length=64, unique=True)
    amount = models.DecimalField("Tutar (USD)", max_digits=8, decimal_places=2)
    reason = models.CharField("Sebep", max_length=40, blank=True)
    status = models.CharField("Durum", max_length=40, blank=True)
    due_by = models.DateTimeField("Son kanıt tarihi", null=True, blank=True)
    evidence_staged = models.BooleanField("Kanıt Stripe'a yüklendi", default=False)
    error = models.TextField("Hata", blank=True)
    created_at = models.DateTimeField("Açıldı", auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "İtiraz (dispute)"
        verbose_name_plural = "İtirazlar (dispute)"

    def __str__(self):
        return f"{self.dispute_id} #{self.subscription_id} {self.status}"


class StripeEvent(models.Model):
    """Processed webhook event ids, so a retried delivery is handled once."""

    event_id = models.CharField(max_length=80, unique=True)
    type = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.type} {self.event_id}"
