"""English YouTube pages: the hub and subscribers. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "youtube",
        "label": "YouTube",
        "title": "YouTube Growth Packages for Creators | Growsterr",
        "description": "Grow your YouTube channel with real people: monthly packages bring subscribers, likes and comments from viewers who chose to subscribe. From {from_price} a month.",
        "h1": ("Grow your YouTube channel ", "with real viewers."),
        "intro": "Looking to buy YouTube subscribers or views? Here is the honest version: monthly growth packages for creators. Real people discover your channel, watch your videos and subscribe when they like what they see. Your dashboard shows what we measured, day by day.",
        "hero": {"image": "youtube-hub", "alt": "A YouTube channel gaining subscribers, likes and comments from real viewers"},
        "sections": [
            {
                "h2": "Subscribers who watch are the ones that count",
                "p": [
                    "YouTube recommends videos that people watch, like and come back to. A subscriber who never watches is worse than none: they lower the share of your audience that engages.",
                    "Every subscriber we bring is a person who found your channel and chose to subscribe. Likes, views and comments come from the same people, inside your package.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Viewers watching a creator's YouTube video and writing comments"},
            },
            {
                "h2": "For channels that publish with care",
                "p": [
                    "Tutorials, vlogs, music or gaming: if you publish regularly, real viewers give every new video a better start. Begin with {starter_name} and move up when your channel is ready for more.",
                ],
                "ul": [
                    "You tell us the city, region or country your audience should come from.",
                    "Subscribers, likes and comments come together, from the same people.",
                    "Your channel stays yours: we never ask for your password.",
                ],
                "image": {"image": "youtube-channel", "alt": "A creator editing a YouTube video in a home studio"},
            },
        ],
        "faqs": [
            ("Are the subscribers real people?", "Yes. Every subscriber is a real person who found your channel and chose to subscribe. No bots, no fake accounts, nothing instant."),
            ("How many subscribers does a package bring?", "Typically {starter_audience} new subscribers a month with {starter_name}, {rising_audience} with {rising_name} and {pro_audience} with {pro_name}. Typical ranges, not a fixed count."),
            ("Do you need my Google or YouTube password?", "Never. We only need your channel handle, and your channel should be public."),
            ("Can I buy views or likes on their own?", "No. Views, likes and comments come inside every package, from the same real people who subscribe."),
            ("Can I cancel any time?", "Yes. Packages renew monthly and you can cancel from your account. The month you've paid for runs to its end."),
        ],
    },
    {
        "service": "subscribers",
        "slug": "youtube/subscribers",
        "label": "YouTube subscribers",
        "title": "Buy YouTube Subscribers Who Really Watch | Growsterr",
        "description": "Buy YouTube subscribers who are real people: viewers who found your channel and chose to subscribe, with likes and comments. From {from_price} a month.",
        "h1": ("YouTube subscribers ", "who actually watch."),
        "intro": "Buy YouTube subscribers the honest way: real people discover your channel, watch your videos and subscribe when they like what they see. Typically {starter_audience} new subscribers a month with {starter_name}, with likes and comments from the same viewers.",
        "hero": {"image": "youtube-subscribers", "alt": "A YouTube channel page with new subscribers from real viewers"},
        "sections": [
            {
                "h2": "A subscriber should be a viewer",
                "p": [
                    "On YouTube, a subscriber is only useful if they watch. Real subscribers see your next upload, watch it, like it and sometimes comment, and that's what YouTube looks at when it decides what to recommend.",
                    "Bot subscribers never watch. They make a channel look bigger while its videos reach fewer people.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Real viewers subscribing to a YouTube channel after watching a video"},
            },
            {
                "h2": "What a month looks like",
                "ul": [
                    "First days: your campaign starts and the first viewers arrive.",
                    "Every week: new subscribers, likes and comments, a few each day.",
                    "By the end of the month: typically {pick_audience} new subscribers with {pick_name}.",
                ],
            },
            {
                "h2": "Where your viewers come from",
                "p": [
                    "Tell us the city, region or country your audience should come from. We show your channel to real people there first; where the best-matching audience is bigger, more of them may come from nearby.",
                ],
            },
        ],
        "faqs": [
            ("How fast do the subscribers come?", "A little every day, across the whole month. Never all at once: real people subscribe at their own pace."),
            ("Will they watch my videos?", "They're real people who chose to subscribe after seeing your channel. What they watch next is up to them, like any audience, and that's exactly why it counts."),
            ("Do I get likes and comments too?", "Yes, from the same viewers: typically {pick_likes} likes and {pick_comments} comments a month with {pick_name}."),
            ("Do you need my password?", "Never. We only need your channel handle, and your channel should be public."),
        ],
    },
]
