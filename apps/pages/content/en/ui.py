"""English UI of the money pages: section titles and the blocks every page shares. Every other
language mirrors these keys one by one (check_pages lists the missing ones).

Placeholders, filled per page:
    {platform} Instagram · {audience} followers/subscribers · {follow} follow/subscribe
    {profile} profile/channel · {handle} username/channel handle · {content} posts/videos
    {service} followers, likes...
    {service_name} Followers, Likes... · {quantity} 1,000 (quantity pages only)
    {from_price} the lowest package price · {pick_name} {pick_price} the package this page preselects
    {starter_name} {starter_price} {starter_audience} {starter_likes} {starter_comments}
    and the same for rising_ and pro_: the packages and their typical monthly ranges.
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "followers", "tiktok": "followers", "youtube": "subscribers"},
    "follow": {"instagram": "follow", "tiktok": "follow", "youtube": "subscribe"},
    "profile": {"instagram": "profile", "tiktok": "profile", "youtube": "channel"},
    "handle": {"instagram": "username", "tiktok": "username", "youtube": "channel handle"},
    "content": {"instagram": "posts", "tiktok": "videos", "youtube": "videos"},
    "service_names": {"followers": "Followers", "subscribers": "Subscribers", "likes": "Likes",
                      "views": "Views", "comments": "Comments"},
    "service_words": {"followers": "followers", "subscribers": "subscribers", "likes": "likes",
                      "views": "views", "comments": "comments"},

    # Page chrome
    "home": "Home",
    "crumbs_label": "Breadcrumb",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "{platform} growth",
    "cta": "Start with {pick_name}",
    "cta_more": "See all packages",
    "trust": ["Real people, never bots", "We never ask for your password", "Monthly, cancel any time"],
    "product_name": "{platform} growth packages",
    "sticky_cta": "Start",

    # Packages
    "packages_title": "Choose your package",
    "packages_lead": "Three monthly packages. New {audience}, likes, views and comments come together, from the same real people.",
    "packages_note": "Typical monthly ranges, not a fixed count: every one of your new {audience} is a real person who chose to {follow}, so every month is a little different.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "What's included",
    "included_lead": "Every package brings the whole picture, from the same real people.",
    "included_items": {
        "audience": ("New {audience}", "Real people who discovered your {profile} and chose to {follow}. Typically {starter_audience} a month with {starter_name}."),
        "likes": ("Likes from the same people", "Typically {starter_likes} a month with {starter_name}, on the {content} they enjoy."),
        "comments": ("Comments in their own words", "Typically {starter_comments} a month with {starter_name}. Written by people, never scripted."),
        "views": ("Views that come with it", "The same people watch your {content} on their own. We don't count views in advance: each one is a person."),
        "days": ("Spread over 30 days", "A little every day, from the location you choose. Never all at once."),
        "dashboard": ("Your dashboard", "What we measured, day by day: visits from your campaign and the new {audience} they brought."),
    },

    # How it works: the subscription, step by step
    "steps_title": "How it works",
    "steps_lead": "A monthly subscription: you choose the package, we run the campaign, real people decide.",
    "steps": [
        ("Choose a package", "{starter_name}, {rising_name} or {pro_name}, billed monthly. Cancel any time from your account."),
        ("We start your campaign", "Tell us your {platform} {handle} and where your audience should come from. We never ask for your password."),
        ("Real people discover your {profile}", "Every day your {profile} is shown to real people. Those who like what they see {follow}, like and comment, on their own."),
        ("Your dashboard shows what we measured", "Visits from your campaign and the new {audience} they brought, day by day. Measured numbers, never guesses."),
    ],

    # Real people vs bots / instant
    "compare_title": "Real people, not bots",
    "compare_lead": "Instant means bots: no real person chooses to {follow} seconds after a payment.",
    "compare_cols": ("What changes", "Instant and bot services", "Growsterr"),
    "compare": [
        ("Who they are", "Bots and fake profiles", "Real people who chose to {follow}"),
        ("Speed", "Thousands in minutes", "A little every day, all month"),
        ("Likes and comments", "Sold separately, from more bots", "From the same people, inside your package"),
        ("Your reach", "Drops quietly: an audience that never engages tells {platform} your {content} aren't worth showing", "Grows with people who watch, like and come back"),
        ("Your password", "Often asked for", "Never"),
        ("What you see", "A number that can vanish in the next clean-up", "A dashboard of what we measured"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "How you get to {quantity} {service}",
    "quantity_lead": "We don't sell a fixed pack of {quantity}. Real people decide for themselves, so a monthly package gets you there at a natural pace.",
    "pace_title": "Typical pace with {pick_name}",
    "pace_month": "Month {n}",
    "pace_goal": "Goal: {quantity}",
    "pace_note": "Typical ranges from what real people do, never a promise. Some months bring more, some fewer.",
    "by_plan_title": "Time to {quantity}, by package",
    "a_month": "{range} a month",
    "when_first": "usually within the first month",
    "when_about": "usually about {n} months",
    "when_range": "usually {low}–{high} months",
    "views_pace": "Views come from the same real people who discover your {profile}, so we don't count them in advance. {pick_name} is the package that fits this goal best.",

    # FAQ, related pages, closing
    "faq_title": "Questions, answered",
    "related_title": "Keep exploring",
    "related": {
        "platform": "More on {platform}",
        "platforms": "On other platforms",
        "quantities": "Other goals",
        "modifiers": "Other ways to grow",
        "articles": "Read next",
        "hubs": "Grow with real people on",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Calculate",
        "followers": "Followers",
        "avg_likes": "Average likes per post",
        "avg_comments": "Average comments per post",
        "engagement_title": "Your engagement rate",
        "engagement_lead": "How many of your followers react to a typical post. Enter the numbers from your last few posts.",
        "engagement_result": "Your engagement rate is {rate}%.",
        "engagement_note": "The rate rises when the people who follow you actually care about your posts. Followers who never react lower it, whatever their number.",
        "growth_title": "How long to your goal?",
        "growth_lead": "Enter where you are and where you want to be. We work it out from each package's typical monthly range.",
        "current": "Followers today",
        "goal": "Your goal",
        "when_first": "usually within the first month",
        "when_range": "usually {low}–{high} months",
        "when_about": "about {n} months",
        "reached": "You're already there.",
        "growth_note": "Typical ranges, not a promise: real people decide for themselves whether to follow.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Guide",
        "alternative": "Compare",
        "payment": "Payments",
        "agency": "Growth agency",
        "tool": "Tool",
        "intent": "Straight answer",
    },
    "cta_title": "Ready to grow on {platform}?",
    "cta_text": "Choose a package and we start your campaign. Real people decide the rest, and your dashboard shows what we measured.",

    # Platform hubs
    "services_title": "What we grow on {platform}",
    "services_lead": "One package brings all of it, from the same real people.",
    "teasers": {
        "audience": "Real people who discover your {profile} and choose to {follow}.",
        "likes": "Likes from the people who enjoy your {content}.",
        "views": "Views from people who choose to watch, never from scripts.",
        "comments": "Comments written by real people, in their own words.",
    },
    "explore": "Explore",
    "in_package": "Inside every package",
    "goals_title": "More ways to grow on {platform}",
    "other_hubs_title": "We also grow",
}
