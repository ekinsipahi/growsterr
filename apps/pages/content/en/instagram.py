"""English Instagram pages: the hub, followers, and the 1,000-followers goal.
Keys and placeholders: docs/CONTENT.md. Numbers come from the packages ({starter_audience}...),
so they follow apps/growth/plan.py when prices or ranges change."""

UPDATED = "2026-11-08"

PAGES = [
    {
        # The hub: no service.
        "slug": "instagram",
        "label": "Instagram",
        "title": "Instagram Growth Packages for Creators | Growsterr",
        "description": "Grow on Instagram with real people: monthly packages bring new followers, likes and comments from people who chose to follow. From {from_price} a month.",
        "h1": ("Grow your Instagram ", "with real people."),
        "intro": "Looking to buy Instagram followers, likes or comments? Here is the honest version: monthly growth packages for creators and influencers. We put your profile in front of real people, and the ones who like what they see follow, like and comment. Your dashboard shows what we measured, day by day.",
        "hero": {"image": "instagram-hub", "alt": "An Instagram creator's profile with new followers, likes and comments arriving"},
        "sections": [
            {
                "h2": "Growth that looks like you earned it",
                "p": [
                    "Instagram rewards accounts that people actually engage with. Bots do the opposite: they sit in your follower count, never like, never watch, and teach the algorithm that your posts aren't worth showing.",
                    "We work the other way round. Your profile is shown to real people every day, and every follow is a choice someone made. That's why likes, views and comments arrive with your followers, not as a separate purchase.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Real people discovering a creator's Instagram posts and leaving comments"},
            },
            {
                "h2": "Made for creators who post with intent",
                "p": [
                    "Personal brand, niche page or small business: the packages grow with you. Start with {starter_name} and move up when your content is ready for more.",
                ],
                "ul": [
                    "Reels, carousels and photo posts all benefit.",
                    "You tell us the city, region or country your audience should come from.",
                    "Your account stays yours: we never ask for your password.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "A creator planning Instagram content at a desk"},
            },
        ],
        "faqs": [
            ("Are the followers real people?", "Yes. Every follower is a real person who saw your profile and chose to follow. We never use bots, fake profiles or instant delivery."),
            ("How many followers does a package bring?", "Typically {starter_audience} new followers a month with {starter_name}, {rising_audience} with {rising_name} and {pro_audience} with {pro_name}. These are typical ranges, not a fixed count: real people decide for themselves."),
            ("Do you need my Instagram password?", "Never. We only need your username. Keep your account public so the people who discover it can follow."),
            ("Can I buy likes or comments on their own?", "No. Likes, views and comments come inside every package, from the same real people who follow you. That's what keeps your numbers natural."),
            ("Can I cancel any time?", "Yes. Packages renew monthly and you can cancel from your account. The month you've paid for runs to its end."),
        ],
    },
    {
        "service": "followers",
        "slug": "instagram/followers",
        "label": "Instagram followers",
        "title": "Buy Real Instagram Followers, Every Month | Growsterr",
        "description": "Buy Instagram followers who are real people and chose to follow you, with likes and comments from the same people. Monthly packages from {from_price}.",
        "h1": ("Instagram followers ", "who chose to follow you."),
        "intro": "Buy Instagram followers the honest way: real people discover your profile every day, and the ones who like what they see follow you. Typically {starter_audience} new followers a month with {starter_name}, with likes and comments from the same people.",
        "hero": {"image": "instagram-followers", "alt": "An Instagram profile gaining new followers from real people"},
        "sections": [
            {
                "h2": "Why real followers are worth more",
                "p": [
                    "A follower only counts if a person is behind it. Real followers see your next post, like it, comment on it and share it, and that engagement is what Instagram looks at when it decides who else should see your content.",
                    "Bots can't do any of that. They lift a number for a few days, disappear in the next clean-up, and the ones that stay quietly pull your reach down.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Real people liking and commenting on a creator's Instagram post"},
            },
            {
                "h2": "Where your new followers come from",
                "p": [
                    "Tell us the city, region or country your audience should come from. We show your profile to real people there first; where the best-matching audience is bigger, more of them may come from nearby.",
                ],
            },
            {
                "h2": "What a month looks like",
                "ul": [
                    "First days: your campaign starts and the first visits arrive.",
                    "Every week: new followers, likes and comments, a few each day.",
                    "By the end of the month: typically {pick_audience} new followers with {pick_name}.",
                ],
            },
        ],
        "faqs": [
            ("How fast do the followers come?", "A little every day, across the whole month. Never all at once: real people follow at their own pace, and anything instant is a bot."),
            ("Will my new followers unfollow?", "Some may, the way any real audience changes. Real followers stay far more often than bots, which disappear in waves."),
            ("Do I get likes and comments too?", "Yes, from the same people: typically {pick_likes} likes and {pick_comments} comments a month with {pick_name}."),
            ("Is it safe for my account?", "We never ask for your password and never log in to your account. People find your profile and decide on their own, the way any follower finds you."),
            ("Can I choose where my followers are from?", "Yes. Tell us the city, region or country when you order. We aim there first; when a closely matching audience is bigger nearby, some of your followers may come from there."),
        ],
    },
    {
        "service": "followers",
        "quantity": 1000,
        "slug": "instagram/followers/1000",
        "label": "{quantity} Instagram followers",
        "title": "{quantity} Instagram Followers From Real People | Growsterr",
        "description": "Reach {quantity} Instagram followers with real people, not bots. {pick_name} typically brings {pick_audience} a month, with likes and comments too.",
        "h1": ("{quantity} Instagram followers, ", "every one of them real."),
        "intro": "We don't sell a pack of {quantity} bots. We grow your account with real people: {pick_name} typically brings {pick_audience} new followers a month, so {quantity} is usually within reach in your first month.",
        "hero": {"image": "instagram-followers-1000", "alt": "A rising line of new Instagram followers reaching a first milestone"},
        "sections": [
            {
                "h2": "Why not {quantity} followers in an hour?",
                "p": [
                    "Because no real person follows an account seconds after a payment. Services that deliver {quantity} followers in an hour deliver bots: they don't like, they don't comment, and they disappear in waves.",
                    "The ones that stay do more damage. Every follower who never engages lowers the share of your audience that does, and your posts quietly reach fewer people.",
                ],
            },
            {
                "h2": "Your first thousand, done properly",
                "p": [
                    "A first thousand real followers changes how new visitors see you. They're people who might watch your Reels, like your posts and come back, which is exactly what helps the next thousand find you.",
                ],
                "ul": [
                    "Real people who chose to follow, from the location you pick.",
                    "Likes and comments from the same people, inside the package.",
                    "A dashboard that shows what we measured, day by day.",
                ],
            },
        ],
        "faqs": [
            ("How long do {quantity} real followers take?", "At a typical pace, {pick_name} brings {pick_audience} new followers a month, so {quantity} is usually within reach in the first month. Real people follow at their own pace, so every month is a little different."),
            ("Is it a one-time pack of {quantity}?", "No. We sell growth as monthly packages. {pick_name} is {pick_price} a month, and you can cancel any time from your account."),
            ("Do I get likes and comments with them?", "Yes, from the same real people: typically {pick_likes} likes and {pick_comments} comments a month with {pick_name}."),
            ("What happens after {quantity}?", "Your package keeps running until you cancel, so your growth carries on month after month. When your content is ready for more, you can move up a package."),
        ],
    },
]
