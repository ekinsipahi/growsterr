"""English source of the core site: the chrome on every page (header, menu, footer, WhatsApp
button, error pages) and the core pages (home, pricing, how it works, about).

Every other language mirrors this file in apps/core/i18n/<code>.py: the same names, the same
keys, the same shapes, only the text translated (docs/I18N.md). A key a language leaves out is
shown in English; check with `python manage.py check_i18n <code>`.

    CHROME    header, menu, footer, WhatsApp button, 404 and 500 pages (every page of the site)
    HOME      /            served as /<code>/              once <code>.py defines HOME
    PRICING   /pricing/    served as /<code>/pricing/      once <code>.py defines PRICING
    HOW       /how-it-works/  served as /<code>/how-it-works/  once <code>.py defines HOW
    ABOUT     /about/      served as /<code>/about/        once <code>.py defines ABOUT
    UPDATED   the date the copy last changed (the sitemap's lastmod)

Copy rules (every language): real people only, never bots or "instant" (except to say we
aren't); likes, views and comments only inside packages, never sold on their own; numbers are
typical monthly ranges, never promises; never ask for a password; no "SEO", search engines,
keywords or rankings, "guarantee", "free", competitor names, crypto, verified or celebrity
comments, gender targeting, reviews, ratings or statistics. Founder wording stays
gender-neutral; the voice is the agency's ("we"), never "I".

Shapes: a tuple (before, highlighted, after) is a title whose middle part gets the coral
swoosh; translate all parts, any of them may be "". Lists and tuples keep their length and
order (icons and images are matched to them by position).

Placeholders, kept exactly as written (never translated):
    {price}                    the lowest monthly price, e.g. $79.99
    {starter} {rising} {pro}   each package's typical monthly follower range, e.g. 1,000–4,000
    {legal_name} {registry_code} {address} {sister_brand}   company facts (apps/core/company.py)
Brand and product names stay as they are: Growsterr, Sterr Agency, Instagram, TikTok, YouTube,
Stripe, Apple Pay, Google Pay, WhatsApp and the package names."""
from datetime import date

UPDATED = date(2026, 11, 8)

CHROME = {
    # <title> and description of a page that sets none of its own
    "meta_title": "Growsterr: real growth for Instagram, TikTok and YouTube",
    "meta_description": "Monthly growth packages for creators on Instagram, TikTok and YouTube. Real people, never bots.",
    # Header and menu
    "skip": "Skip to content",
    "home_label": "Growsterr home",
    "main_nav": "Main",
    "menu": "Menu",
    "nav_instagram": "Instagram",
    "nav_tiktok": "TikTok",
    "nav_youtube": "YouTube",
    "nav_pricing": "Pricing",
    "nav_how": "How it works",
    "nav_about": "About",
    "sign_in": "Sign in",
    "my_account": "My account",
    "get_started": "Get started",
    "theme": "Dark mode",
    "language": "Language",
    # Footer
    "footer_tagline": "Monthly growth packages for creators on Instagram, TikTok and YouTube. Real people who choose to follow you, never bots.",
    "footer_platforms": "Platforms",
    "footer_company": "Company",
    "footer_legal": "Legal",
    "contact": "Contact",
    "terms": "Terms of service",
    "privacy": "Privacy policy",
    "cookies": "Cookie policy",
    "refunds": "Refund policy",
    "rights": "All rights reserved.",
    "product_of": "A product of",
    "company_line": "Growsterr is a {sister_brand} product, run by {legal_name}, registry code {registry_code}, {address}.",
    "author_title": "Who's behind this page",
    "author_team": 'Written and checked by the Sterr Agency and Growsterr team.',
    "author_founder": 'Founded by',
    "author_since": 'in social media growth since 2022.',
    "author_updated": 'Last updated:',
    # The fixed WhatsApp button; wa_text is the message it prefills
    "wa_label": "WhatsApp",
    "wa_aria": "Chat with us on WhatsApp",
    "wa_text": "Hi Growsterr, I'd like to talk about growing my account.",
    # 404: a page that doesn't exist
    "not_found_title": "Page not found | Growsterr",
    "not_found_description": "This page doesn't exist. Monthly growth packages for creators on Instagram, TikTok and YouTube.",
    "not_found_h1": "This page took a different path.",
    "not_found_lead": "The page you're looking for has moved or never existed. These might help:",
    "not_found_home": "Back to the homepage",
    # 500: a server error (always shown in English: Django renders it without the request)
    "error_title": "Something went wrong | Growsterr",
    "error_h1": "Something went wrong on our side.",
    "error_lead": "It's not you: this page hit a problem on our end. Please try again in a moment.",
    "error_home": "Back to the homepage",
}

HOME = {
    "title": "Growsterr | Real growth on Instagram, TikTok and YouTube",
    "description": "Monthly growth packages for creators. Your profile is shown to real people who choose to follow, like, watch and comment. Never bots. From {price} a month.",
    "eyebrow": "The growth agency for creators",
    "h1": ("Grow with ", "real people", ". Every day."),
    "lead": "Monthly growth packages for Instagram, TikTok and YouTube. We show your profile to real people; the ones who like what they see follow you, like your posts, watch and comment. No bots, no password, cancel anytime.",
    "cta_primary": "See the packages",
    "cta_secondary": "How it works",
    "trust": ["Real people, never bots", "We never ask for your password", "Cancel anytime in your dashboard"],
    "hero_alt": "A creator filming a short video for their audience",
    "hero_profile": ("@yourname", "Your profile", "Follow"),
    "hero_chips": ("Chose to follow", "Likes from the same people"),
    "platforms_eyebrow": "Platforms",
    "platforms_title": ("Three platforms. ", "One way to grow."),
    "platforms_lead": "Followers or subscribers, likes, views and comments, all from the same real people, on the platform where you create.",
    "platforms": {
        "instagram": {
            "text": "Followers, likes, views and comments from real people who find your profile and like what they see.",
            "tags": ["Followers", "Likes", "Views", "Comments"],
            "link": "Instagram growth",
        },
        "tiktok": {
            "text": "Followers, likes, views and comments from people who discover your videos and want to see more.",
            "tags": ["Followers", "Likes", "Views", "Comments"],
            "link": "TikTok growth",
        },
        "youtube": {
            "text": "Subscribers, likes, views and comments from real viewers who choose to come back for your next video.",
            "tags": ["Subscribers", "Likes", "Views", "Comments"],
            "link": "YouTube growth",
        },
    },
    "how_eyebrow": "How it works",
    "how_title": ("One subscription. ", "Real growth every month."),
    "how_lead": "No setup calls, no contracts. Choose a package, and real people start finding your profile.",
    "how_link": "See how it works",
    # The four steps: (title, text)
    "steps": [
        ("Choose a package", "Pick your platform and package, then tell us your username and where your audience should come from. Never your password."),
        ("We start your campaign", "Once your first payment goes through, your campaign starts and your profile is shown to real people in our network."),
        ("Real people choose to follow", "People discover your profile every day. The ones who like what they see follow you, and many like, watch and comment too."),
        ("Your dashboard shows the numbers", "Profile visits and new followers, day by day, exactly as our delivery system measured them."),
    ],
    "real_eyebrow": "Real people vs instant",
    "real_title": ("Instant means bots. ", "We only work with real people."),
    "real_lead": "No real person follows an account seconds after a payment. When followers land all at once, they are bots, and bots quietly hurt your reach. Real growth takes the month, because every follow is someone's own choice.",
    # The comparison table: rows are (what, instant services, Growsterr)
    "compare": {
        "caption": "Instant services compared with Growsterr",
        "cols": ("What you get", "Instant services", "Growsterr"),
        "rows": [
            ("Who follows you", "Bots and empty profiles", "Real people with their own accounts"),
            ("How it arrives", "Thousands in minutes, all at once", "Every day, spread over the month"),
            ("Likes and comments", "Sold separately, from more bots", "From the same people who follow you"),
            ("Your reach", "Quietly drops: your posts reach fewer people", "An audience that watches, likes and comments"),
            ("Your password", "Often asked for", "Never"),
            ("What you see", "A number that can drop overnight", "Measured visits and follows, day by day"),
        ],
    },
    "packages_eyebrow": "Packages",
    "packages_title": ("Monthly packages. ", "Everything in one."),
    "packages_lead": "Followers, likes, views and comments come together, from the same real people. We never sell likes, views or comments on their own. Billed monthly, cancel anytime.",
    "packages_link": "Compare the packages",
    "tabs_label": "Choose a platform",
    "dash_eyebrow": "Your dashboard",
    "dash_title": ("You see what was measured. ", "Nothing else."),
    "dash_lead": "Every subscription comes with a dashboard. It shows what our delivery system measured for your profile, day by day, with no estimates dressed up as results.",
    # The dashboard illustration (it never shows numbers) and the five points beside it: (title, text)
    "dash": {
        "handle": "@yourname",
        "package": "Rising Influencer · Instagram",
        "active": "Active",
        "month": "This month",
        "tiles": ["New followers", "Profile visits", "Your followers now"],
        "chart": "New followers per day",
        "countries": "Visits by country",
        "caption": "An illustration of your dashboard. Your own numbers appear once your campaign is running.",
        "points": [
            ("Profile visits", "People from our network who opened your profile."),
            ("New followers", "The people we brought who chose to follow you."),
            ("Day by day", "Every day of the month, in a chart and a table."),
            ("Where they came from", "Visits by country, so you can watch your audience take shape."),
            ("A clear outlook", "An estimate for the next 30 days at today's pace, clearly marked as an estimate."),
        ],
    },
    "faq_eyebrow": "Questions",
    "faq_title": ("Good questions. ", "Straight answers."),
    # (question, answer)
    "faqs": [
        ("Are the followers real people?", "Yes, every one of them. Your profile is shown to real people, and only those who like what they see choose to follow. That's why growth takes the month instead of a minute."),
        ("Do you need my password?", "Never. We only need your username. Keep your account public while your package runs."),
        ("How many followers will I get?", "Each package has a typical monthly range: {starter} with Starter Creator, {rising} with Rising Influencer and {pro} with Pro Influencer. These are typical numbers, not a fixed count: real people decide for themselves, so every month is a little different."),
        ("Can I buy likes, views or comments on their own?", "No. They come inside every package, from the same real people who follow you. Likes and comments that don't come from a real audience do an account more harm than good."),
        ("When will I see results?", "Your campaign starts once your first payment goes through, and the first numbers appear in your dashboard within a few days. Growth then builds through the month."),
        ("Can I choose where my audience comes from?", "Yes. Tell us a city, region or country and we focus your campaign there. When the best-matching audience is somewhere else, more of it may come from there."),
        ("How do I cancel?", "Any time, in your dashboard. Canceling stops the next payment; the month you've paid for runs to its end and isn't refunded."),
        ("Which platforms do you work with?", "Instagram, TikTok and YouTube. Each platform is its own subscription, and you see all of them in one dashboard."),
    ],
    # The closing band: the primary button opens the order form, the secondary one the pricing page
    "cta": {
        "title": ("Ready to grow with ", "real people", "?"),
        "text": "Choose a package, tell us your username and where your audience should come from. We'll take it from there.",
        "primary": "Get started",
        "secondary": "See pricing",
    },
}

PRICING = {
    "title": "Pricing | Growsterr monthly growth packages",
    "description": "Monthly growth packages for Instagram, TikTok and YouTube, from {price} a month. Real people, never bots. Billed monthly, cancel anytime.",
    "eyebrow": "Pricing",
    "h1": ("Simple monthly packages. ", "Real people in every one."),
    "lead": "Three packages, the same on Instagram, TikTok and YouTube. Followers or subscribers, likes, views and comments come together, spread over 30 days. Billed monthly, cancel anytime.",
    "tabs_label": "Choose a platform",
    "included_eyebrow": "In every package",
    "included_title": ("Everything that makes growth ", "real."),
    # Eight cards: (title, text)
    "included": [
        ("Real people only", "Every new follower is a real person who saw your profile and chose to follow."),
        ("Likes, views and comments", "From the same people who follow you. Never sold on their own."),
        ("Spread over 30 days", "Growth every day of the month, never all at once."),
        ("The location you choose", "Name a city, region or country and we focus your campaign there."),
        ("Your dashboard", "Profile visits and new followers, measured day by day."),
        ("No password, ever", "We only need your username. Your account stays yours."),
        ("Monthly, cancel anytime", "Renews every month until you cancel in your dashboard."),
        ("Secure payment", "By Stripe: card, Apple Pay and Google Pay."),
    ],
    "compare_eyebrow": "Side by side",
    "compare_title": ("Compare the ", "packages."),
    "compare_lead": "The same on every platform. The ranges are typical months, not a fixed count: every follower is a real person who chooses to follow.",
    "compare_caption": "The three packages compared",
    "compare_feature": "What's included",
    "rows": {
        "followers": "New followers or subscribers a month",
        "likes": "Likes a month",
        "comments": "Comments a month",
        "views": "Views from the same people",
        "spread": "Spread over 30 days",
        "location": "From the location you choose",
        "dashboard": "Your dashboard",
        "price": "Price",
    },
    "yes": "Included",
    "no": "Not included",
    "billing_eyebrow": "Billing",
    "billing_title": ("Billing, ", "plainly."),
    "billing_lead": "Monthly, no contracts. Here is everything about payments, renewals and canceling.",
    # (question, answer)
    "billing_faqs": [
        ("How does billing work?", "Every package is a monthly subscription. You pay at the start of each month by card, Apple Pay or Google Pay, securely through Stripe. Prices are in US dollars."),
        ("Does my package renew automatically?", "Yes. Your package renews every month until you cancel, so your growth keeps building."),
        ("How do I cancel?", "Any time, in your dashboard. Canceling stops the next payment, and your package keeps running until the end of the month you've already paid for."),
        ("Can I get a refund for the current month?", "No. The month you've paid for isn't refunded, because its campaign is already running. When you cancel, it simply runs to its end and no further payments are taken."),
        ("Are the numbers fixed?", "No. They are typical monthly ranges. Every follower is a real person who chooses to follow, so every month is a little different."),
        ("Can I buy likes, views or comments on their own?", "No. They come inside every package, from the same real people who follow you."),
        ("Can I grow more than one platform?", "Yes. Each platform is its own subscription, and you see all of them in one dashboard."),
    ],
    # Followed by links to the terms and the refund policy (the legal pages are English only)
    "billing_more": "The full terms:",
    # The secondary button opens How it works
    "cta": {
        "title": ("Pick a package. ", "Grow with real people."),
        "text": "Start in a few minutes: your username, the location your audience should come from, and a secure monthly payment.",
        "primary": "Get started",
        "secondary": "How it works",
    },
}

HOW = {
    "title": "How it works | Growsterr",
    "description": "How Growsterr grows your Instagram, TikTok or YouTube: your profile is shown to real people, they choose to follow, and your dashboard shows what was measured.",
    "eyebrow": "How it works",
    "h1": ("Real people discover you. ", "They choose to follow."),
    "lead": "Growsterr is a monthly subscription. We show your profile to real people every day; the ones who like what they see follow you, and often like, watch and comment too. Your dashboard shows what was measured, nothing more.",
    "glance": "In four steps",
    # The four steps; alt describes the step's photo
    "flow": [
        {"title": "Choose your package",
         "alt": "A creator choosing a package on their phone",
         "text": "Pick a platform and a package: Starter Creator, Rising Influencer or Pro Influencer. Tell us your username and the city, region or country your audience should come from.",
         "points": ["Your username only, never your password", "Keep your account public while your package runs", "Pay monthly by card, Apple Pay or Google Pay"]},
        {"title": "We start your campaign",
         "alt": "A creator's profile reaching new people",
         "text": "Once your first payment goes through, your campaign starts on its own. Your profile is shown to real people in our network, focused on the location you chose.",
         "points": ["Focused on the location you chose", "Bigger packages get more placement", "Runs every day, all month"]},
        {"title": "Real people choose to follow",
         "alt": "People discovering a creator's profile on their phones",
         "text": "People see your profile and decide for themselves. Those who like it follow you; many also like your posts, watch and comment. Nothing is automated, and nothing arrives all at once.",
         "points": ["Typically 2–3 likes for every new follower", "About one comment for every 10 new followers", "Views from the same people"]},
        {"title": "Your dashboard shows what was measured",
         "alt": "A creator checking their growth on a laptop",
         "text": "Your dashboard shows the profile visits that came from our network and the new followers who came with them, day by day. Next to them: where your visitors came from, and an estimate for the next 30 days, clearly marked as one.",
         "points": ["Day-by-day chart and table", "Visits by country", "Updated through the month"]},
    ],
    "month_eyebrow": "A month with Growsterr",
    "month_title": ("What a month ", "looks like."),
    # (when, what)
    "month": [
        ("Day 1", "Your campaign starts as soon as your first payment goes through."),
        ("First days", "The first visits and follows appear in your dashboard."),
        ("All month", "Growth builds every day, from people who choose to follow."),
        ("Day 30", "Your package renews and keeps going, or ends if you've canceled."),
    ],
    "why_eyebrow": "Why real people",
    "why_title": ("The hidden cost of ", "fake followers."),
    "why_text": [
        "Bots don't watch, like or buy. Every one of them lowers the share of your audience that engages, and the platforms read that as content nobody wants. Nobody tells you: your posts just reach fewer people, quietly.",
        "Bot accounts also get removed in waves, so the number drops, but the damage to your account stays. Real people are the only followers that never cost you that. That's why we only work with them.",
    ],
    "need_title": "What we need from you",
    "need": ["Your username", "The city, region or country your audience should come from", "An email and a phone number, so we can stay in touch"],
    "never_title": "What we never ask for",
    "never": ["Your password", "Access to your account", "Changes to your profile or your posts"],
    "faq_eyebrow": "Questions",
    "faq_title": ("How it works, ", "in detail."),
    # (question, answer)
    "faqs": [
        ("Who are the people who follow me?", "Real people with their own accounts, who saw your profile in our network and chose to follow. No bots, no fake profiles, no automation."),
        ("Why isn't it instant?", "Because real people don't follow on command. Growth that lands in minutes comes from bots; real growth is spread across the month."),
        ("Do I need to post while my package runs?", "It helps. People follow accounts they like, and fresh posts give them a reason to stay, like and comment."),
        ("What does the dashboard count?", "The profile visits that came from our network, and the new followers who came from those visits. Your account's own total also moves with your other growth and with unfollows, so it can differ."),
        ("Can I choose which posts get the attention?", "Yes, with Rising Influencer and Pro Influencer: you choose which posts get the attention."),
        ("What happens when I cancel?", "No further payments are taken. Your package keeps running until the end of the month you've paid for, and that month isn't refunded."),
    ],
    # The primary button opens the order form, the secondary one the pricing page
    "cta": {
        "title": ("Your audience is out there. ", "Let them find you."),
        "text": "Choose a package and your campaign starts with your first payment.",
        "primary": "Get started",
        "secondary": "See pricing",
    },
}

ABOUT = {
    "title": "About Growsterr | A growth agency for creators",
    "description": "Growsterr is a growth agency for creators on Instagram, TikTok and YouTube, and a brand of Sterr Technologies OÜ, the company behind Sterr Agency.",
    "eyebrow": "About",
    "h1": ("A growth agency for creators. ", "Built on real people."),
    "lead": "Growsterr helps creators and influencers grow on Instagram, TikTok and YouTube with real people, month by month. We work like an agency: clear packages, honest numbers and a team behind every campaign.",
    # (big value, label)
    "facts": [
        ("Real people", "Never bots, never instant"),
        ("Monthly", "Packages you can cancel anytime"),
        ("Turkey", "Headquarters"),
        ("Tallinn, EU", "Registered company"),
    ],
    "image_alt": "The Growsterr team at work",
    "family_eyebrow": "The Sterr family",
    "family_title": ("A brand of the team behind ", "Sterr Agency."),
    "family_text": [
        "Growsterr is a brand of Sterr Technologies OÜ, the company behind Sterr Agency: a growth agency headquartered in Turkey, with a team working across Europe and beyond.",
        "Growsterr brings that way of working to creators. The same care, the same open numbers, built for people who create.",
    ],
    "family_link": "Visit Sterr Agency",
    "founder_eyebrow": "Behind Growsterr",
    "founder_title": ("Founded by ", "Ekin Sipahi."),
    "founder_text": [
        "Growsterr was founded by Ekin Sipahi, a dentist who works on several projects at once: Sterr Agency, linksterr.com, dentaltourism.tr and now Growsterr. What connects them is one belief: good work deserves to be seen.",
        "That belief shapes Growsterr. A creator with something real to say deserves an audience that is real too: people who chose to be there, not numbers that disappear.",
    ],
    "founder_link": "Ekin Sipahi on Instagram",
    "values_eyebrow": "How we work",
    "values_title": ("Three rules ", "we never bend."),
    # (title, text)
    "values": [
        ("Real people only", "Every follow is a person's own choice. We don't sell bots, and we never will."),
        ("Only what was measured", "Your dashboard shows what our delivery system measured, not what we hoped for."),
        ("Clear, monthly, yours", "Simple packages, monthly billing, cancel anytime. We never ask for your password."),
    ],
    "mission": ("Our goal: ", "a brighter future", " where every creator gets the attention their work deserves."),
    "company_title": "Company details",
    # (label, value); the {sister_brand} row links to Sterr Agency's site
    "rows": [
        ("Brand", "Growsterr"),
        ("Legal name", "{legal_name}"),
        ("Registry", "Estonian Business Register · {registry_code}"),
        ("Registered address", "{address}"),
        ("Headquarters", "Turkey"),
        ("Sister brand", "{sister_brand}"),
    ],
    "contact_label": "Contact",
    # The primary button opens the order form, the secondary one the pricing page
    "cta": {
        "title": ("Grow with a team that ", "shows its work."),
        "text": "Monthly packages, real people and a dashboard that shows only what was measured.",
        "primary": "Get started",
        "secondary": "See pricing",
    },
}
