UPDATED = "2026-11-08"

# English YouTube intent pages: searches for things we don't sell (cheap, instant, free, free
# trial, panels). Each answers honestly, then leads to the monthly package. Keys and placeholders:
# docs/CONTENT.md; angles: docs/keywords/WRITING.md.

PAGES = [
    # --- Subscribers ----------------------------------------------------------------------
    {
        "service": "subscribers",
        "modifier": "cheap",
        "slug": "youtube/subscribers/cheap",
        "label": "Cheap YouTube subscribers?",
        "plan": "starter",
        "title": "Buy YouTube Subscribers for $1? What They Cost You | Growsterr",
        "description": "$1 YouTube subscribers never watch and get cleaned out. For {starter_price} a month, {starter_name} typically brings {starter_audience} real viewers who subscribe.",
        "h1": ("$1 YouTube subscribers ", "never watch a single video."),
        "intro": "Thinking of buying YouTube subscribers for $1? At that price you get accounts that will never watch, like or comment, and YouTube regularly removes spam accounts from subscriber counts. We charge more and bring viewers: {starter_audience} new subscribers in a typical month with {starter_name}, at {starter_price}, every one a person who found your channel and decided to subscribe.",
        "hero": {"image": "youtube-subscribers", "alt": "A YouTube channel's subscriber count growing with real viewers"},
        "sections": [
            {
                "h2": "The cost of a subscriber who never watches",
                "p": [
                    "On YouTube, what subscribers do matters more than how many there are. A list full of accounts that never press play makes each new upload look less interesting than it is.",
                    "So a cheap subscriber isn't cheap. You pay once in money and again in the views you don't get.",
                ],
            },
            {
                "h2": "What a real subscriber costs",
                "p": [
                    "Take {starter_name}: {starter_price} a month, and typically {starter_audience} subscribers who are real viewers from the place you choose. Per person that's a matter of cents, and their likes and comments are part of the price.",
                ],
            },
            {
                "h2": "A low price without the risk",
                "ul": [
                    "No password and no access to your Google account: only your channel handle.",
                    "Monthly billing by card through Stripe, cancellable from your account.",
                    "Subscribers, likes and comments in one price, from the same people.",
                ],
            },
        ],
        "faqs": [
            ("How much do real YouTube subscribers cost?", "Our packages start at {starter_price} a month. {starter_name} typically brings {starter_audience} new subscribers; {rising_name}, at {rising_price}, brings {rising_audience}; {pro_name}, at {pro_price}, brings {pro_audience}."),
            ("Why do some sites sell subscribers so cheaply?", "Because they sell accounts, not viewers. Creating or renting accounts in bulk costs very little; finding people who want to watch your channel doesn't."),
            ("Is there a very cheap option for a small channel?", "{starter_name} is made for new and small channels, and it's our lowest price."),
            ("Can cheap subscribers get my channel in trouble?", "They can. YouTube's fake engagement policy covers bought subscribers, and channels that use them risk having videos removed or the channel penalised."),
            ("Are views included in the price?", "Yes. Your new subscribers watch, like and comment on their own, all inside the package. We don't put a number on views, since each one is someone choosing to press play."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "fast",
        "slug": "youtube/subscribers/fast",
        "label": "Fast YouTube subscribers?",
        "title": "Buy YouTube Subscribers Fast: Real, Not Instant | Growsterr",
        "description": "Real, instant and active YouTube subscribers can't all be true. Ours are real and active: your campaign starts in days and subscribers arrive daily.",
        "h1": ("Real, active and instant? ", "Only two of those can be true."),
        "intro": "Want to buy YouTube subscribers fast, real, instant and active all at once? Only two of those can be true together. Instant subscribers aren't people, and real people don't subscribe the second you pay. We bring real, active subscribers quickly: the campaign is live within the first days, and from there {pick_name} typically adds {pick_audience} a month, a few every day.",
        "hero": {"image": "youtube-subscribers", "alt": "New subscribers joining a YouTube channel day after day"},
        "sections": [
            {
                "h2": "Why instantly means fake on YouTube",
                "p": [
                    "A real person subscribes after watching something: a video, a Short, a channel trailer. That takes minutes at least, and it happens when they get round to it. Subscribers who appear by the hundred right after a payment skipped the watching, which tells you they weren't people.",
                ],
            },
            {
                "h2": "How fast real subscribers come",
                "p": [
                    "Setup takes the first days after you order. From then on, new viewers find your channel every day, and those who like what they watch subscribe. The dashboard shows each day as we measure it, so you see the pace from the first week.",
                ],
            },
            {
                "h2": "Speed you can use",
                "ul": [
                    "Upload while the campaign runs, so new subscribers have something to watch next.",
                    "Tidy your channel page: a clear banner, a trailer and playlists in a sensible order.",
                    "Choose {pro_name} for the biggest monthly range: typically {pro_audience} new subscribers.",
                ],
            },
        ],
        "faqs": [
            ("How quickly will my subscriber count go up?", "Within the first days of your campaign: a few at a time at first, then every day through the month."),
            ("Can you add 1,000 subscribers instantly?", "No, nobody can with real people. A thousand in an hour means a thousand accounts that will never watch, and those are the ones YouTube clears out."),
            ("Are your subscribers active?", "They're real people who subscribed after seeing your channel, so they're as active as any viewer: they watch, like and comment when a video interests them."),
            ("Which package is fastest?", "{pro_name} brings the most each month: typically {pro_audience} new subscribers. {starter_name} and {rising_name} bring smaller ranges, spread the same way across the month."),
            ("Will fast growth hurt my channel?", "Not at this pace. Subscribers arrive daily from real viewers, which is how growing channels gain them anyway."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "free",
        "slug": "youtube/subscribers/free",
        "label": "Free YouTube subscribers?",
        "plan": "starter",
        "tool": "growth-calculator",
        "title": "Buy YouTube Subscribers Free? Here's a Better Plan | Growsterr",
        "description": "Free YouTube subscribers come from sub-for-sub swaps or bots. We don't offer them, but our free growth calculator shows how long real growth takes.",
        "h1": ("Free YouTube subscribers? ", "Plan for real ones instead."),
        "intro": "Looking to buy YouTube subscribers free, or 1,000 for $5? Neither brings people who watch: free offers rely on sub-for-sub swaps or bot accounts. We don't give subscribers away. The free part of this page is the growth calculator: put in where your channel stands and where you want it, and it estimates the months each package typically needs.",
        "hero": {"image": "youtube-channel", "alt": "A YouTuber planning a subscriber goal for the coming months"},
        "sections": [
            {
                "h2": "Sub-for-sub and other free tricks",
                "ul": [
                    "Sub-for-sub groups: you subscribe to strangers, they subscribe back, and nobody watches anybody.",
                    "Free subscriber sites that ask you to sign in with Google, then use your account to subscribe to others.",
                    "Tiny free batches from bot accounts, offered so you'll buy a bigger one.",
                ],
                "p": [
                    "All of them fill your count with people who have no interest in your videos, which is worse than having fewer subscribers.",
                ],
            },
            {
                "h2": "About that 1,000",
                "p": [
                    "A thousand subscribers is a milestone for many channels, often because of YouTube's Partner Program. Bought or swapped subscribers add no watch time, and YouTube treats them as fake engagement. We don't promise monetization either: we bring real viewers, and the rest depends on your videos and on YouTube.",
                ],
            },
            {
                "h2": "Plan it with the growth calculator",
                "p": [
                    "The calculator near the top is free and works in your browser. Enter your subscriber count where it asks for followers today, and your target as the goal. It works out how many months each package typically needs, from each package's typical monthly range.",
                ],
            },
        ],
        "faqs": [
            ("Can I get YouTube subscribers for free?", "Not real ones from us. Each subscriber we bring is a viewer reached by a paid campaign. The calculator here is the free part, with no limit on how often you use it."),
            ("Is 1,000 YouTube subscribers for $5 real?", "No real campaign can find a thousand people who want your channel for five dollars. At that price the subscribers are accounts, not viewers."),
            ("How long does it take to reach 1,000 real subscribers?", "That depends on your starting point. {starter_name} typically brings {starter_audience} new subscribers a month; put your own numbers into the calculator above to see the months for your channel."),
            ("Is sub-for-sub against YouTube's rules?", "Yes. YouTube's fake engagement policy covers trading subscriptions, so it can put a channel at risk. It also brings subscribers who never watch."),
            ("Where should a small channel start?", "With {starter_name}, at {starter_price} a month, and no contract beyond the month you're in."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "free-trial",
        "slug": "youtube/subscribers/free-trial",
        "label": "YouTube subscribers free trial?",
        "plan": "starter",
        "title": "Buy YouTube Subscribers With a Free Trial? | Growsterr",
        "description": "No free trial of YouTube subscribers here: a one-day sample proves nothing. Your first month shows real viewers, measured, with no contract.",
        "h1": ("A free trial of YouTube subscribers ", "would prove nothing. A month will."),
        "intro": "If you want to buy YouTube subscribers after a free trial, we'll be straight with you: we don't offer one. A trial of 100 subscribers in a day would only show that a seller has accounts to spare. Your first month is how you judge us: {starter_name} at {starter_price}, real viewers arriving from the first days, a dashboard of what we measured, and no contract beyond the month.",
        "hero": {"image": "youtube-hub", "alt": "A YouTube channel's analytics during a first month of real growth"},
        "sections": [
            {
                "h2": "What a trial can't show you",
                "p": [
                    "The question isn't whether a number can go up. It's whether real people watch, like and stay, and that takes weeks to see. A one-day sample is a sales trick, not a test.",
                ],
            },
            {
                "h2": "How to check us during the month",
                "ul": [
                    "Open the dashboard every few days: visits from the campaign and new subscribers, as measured.",
                    "Look at your video analytics: are new viewers watching?",
                    "Read the comments: people writing about your videos in their own words.",
                    "Decide before the renewal date; you can cancel from your account at any point.",
                ],
            },
        ],
        "faqs": [
            ("Do you have a free trial for YouTube?", "No. We don't run trials on any platform. A month is the shortest package, and you can cancel before the next one starts."),
            ("Why no trial when other sites offer one?", "Every subscriber we bring comes from a real campaign that costs money from day one. Sellers who can afford free samples are usually sending accounts, not viewers."),
            ("What happens if I cancel after one month?", "Nothing more is charged, and the paid month runs to its end. Real subscribers aren't taken back; they stay unless they decide to leave."),
            ("Will I see results within the first month?", "You'll see the pace: new subscribers arriving daily, typically {starter_audience} over the month with {starter_name}. Typical, not fixed, because each one is someone deciding for themselves."),
            ("Can I try a smaller package first?", "{starter_name} is our smallest and the natural place to start. You can move up later if your channel needs more."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "smm-panel",
        "slug": "youtube/subscribers/smm-panel",
        "label": "YouTube subscribers from SMM panels?",
        "title": "Buy YouTube Subscribers on an SMM Panel? | Growsterr",
        "description": "SMM panels sell YouTube subscribers and views by the thousand, with refills because they drop. We're an agency: real viewers and a measured dashboard.",
        "h1": ("Panel subscribers come with a refill button. ", "Ours don't need one."),
        "intro": "Before you buy YouTube subscribers or views on an SMM panel, notice the refill option panels often list beside them: they expect the numbers to drop. Panels resell bot traffic in bulk. We work as an agency instead: people on our team look after your campaign, real viewers find your channel and subscribe, and the dashboard reports what we measured.",
        "hero": {"image": "youtube-channel", "alt": "A creator checking a dashboard of measured new YouTube subscribers"},
        "sections": [
            {
                "h2": "Subscribers and views by the thousand",
                "p": [
                    "On a panel, YouTube subscribers, views and watch time sit in one list, priced per thousand, with notes about start times and refills. Nobody looks at your channel. The order joins a queue, and accounts do what the queue says.",
                    "Panel views work the same way: plays without anyone deciding to watch, the kind YouTube works to filter out of view counts.",
                ],
            },
            {
                "h2": "What changes with an agency",
                "ul": [
                    "People instead of queues: your channel is shown to real viewers every day.",
                    "Every subscriber, like, view and comment traces back to a person.",
                    "A team behind your campaign, and a way to reach us when you have questions.",
                    "A dashboard of what we measured, not a counter that needs topping up.",
                ],
            },
        ],
        "faqs": [
            ("Are panel subscribers real people?", "No. Panels resell bulk traffic from accounts that subscribe on instruction, which is why refills are part of the offer."),
            ("Do you sell YouTube views on their own?", "No. Views aren't a separate line. They come from the people our campaign reaches, the same ones who subscribe, like and comment."),
            ("Can panel views get my channel in trouble?", "Yes. Artificial views break YouTube's fake engagement rules; they may be stripped from your count, and repeated use puts the channel at risk."),
            ("Do you offer a reseller panel?", "No. We don't sell in bulk or through resellers: every package is a campaign built around one channel. Agencies with several channels can contact us to talk it over."),
            ("What does a package bring each month?", "{pick_name} typically brings {pick_audience} new subscribers a month, real viewers arriving across all 30 days."),
        ],
    },
    # --- Views ----------------------------------------------------------------------------
    {
        "service": "views",
        "modifier": "cheap",
        "slug": "youtube/views/cheap",
        "label": "Cheap YouTube views?",
        "plan": "starter",
        "title": "Buy Views on YouTube Cheap? What a Dollar Gets You | Growsterr",
        "description": "Cheap YouTube views at a dollar per thousand are plays, not viewers. Our monthly package brings real people who watch, subscribe and comment.",
        "h1": ("Cheap YouTube views ", "are plays, not viewers."),
        "intro": "If you plan to buy views on YouTube cheap, say a thousand for a dollar, know what arrives: plays from scripts or bulk accounts that watch a few seconds at most, and YouTube can strip them from your count. Views aren't something we sell separately. Our monthly package brings real people to your channel, and they watch, like, comment and subscribe by choice.",
        "hero": {"image": "youtube-viewers", "alt": "Real viewers watching a YouTube video through to the end"},
        "sections": [
            {
                "h2": "What a view is worth",
                "p": [
                    "A view helps when a person watches. How long they stay, whether they like it and which video they click next are what show YouTube a video deserves more viewers. A cheap view adds one to the counter and gives YouTube nothing to go on.",
                    "A big view count with almost no watch time also sends a mixed signal, and the bought plays can be removed anyway.",
                ],
            },
            {
                "h2": "A YouTube views package, the honest kind",
                "p": [
                    "We do sell a package, just not a pack of views. {starter_name} is {starter_price} a month: typically {starter_audience} new subscribers, {starter_likes} likes and {starter_comments} comments from real viewers, plus the views those same people give your videos.",
                    "Views aren't counted in advance. They follow your content rather than a quota, because every one is somebody's choice.",
                ],
            },
            {
                "h2": "Price per view or price per viewer",
                "p": [
                    "Count viewers, not views. One real subscriber can watch dozens of your videos in the months they stay. A dollar's worth of scripted plays watches nothing after today.",
                ],
            },
        ],
        "faqs": [
            ("How much do YouTube views cost with you?", "Views aren't priced on their own. The lowest package, {starter_name}, is {starter_price} a month and brings subscribers, likes and comments, with views from those same people."),
            ("Why are views for 1 dollar so cheap?", "Because nobody watches them. Scripts and bulk accounts can produce plays for almost nothing, and plays are all they produce."),
            ("Will cheap views bring me real viewers?", "Unlikely. YouTube looks at how people respond to a video, not only at the count, and bought views don't respond."),
            ("Can I choose which videos get viewers?", "No. The campaign promotes your channel as a whole, and viewers pick what to watch. Strong titles and thumbnails help them find your best work."),
            ("Is there a very cheap package just for views?", "No views-only option exists below {starter_name} at {starter_price} a month, because views come from the people a package brings."),
        ],
    },
    {
        "service": "views",
        "modifier": "fast",
        "slug": "youtube/views/fast",
        "label": "Fast YouTube views?",
        "title": "Buy YouTube Views Fast? How Real Viewers Arrive | Growsterr",
        "description": "Instant YouTube views, premiere views included, come from scripts. Real viewers find your channel from the first days of your campaign and keep coming.",
        "h1": ("Fast YouTube views? ", "Viewers don't come by delivery."),
        "intro": "Want to buy YouTube views fast, with instant delivery? Views delivered on a timer come from scripts, not people: a real viewer clicks when a video catches their eye. We don't sell or deliver views. We bring real people to your channel every day from the first days of your campaign, and they watch, like and subscribe on their own.",
        "hero": {"image": "youtube-viewers", "alt": "Viewers discovering a creator's new YouTube upload"},
        "sections": [
            {
                "h2": "Fast delivery is a parcel word",
                "p": [
                    "Delivery times make sense for things in boxes. For views, a delivery speed means a machine is pressing play, and those plays come with no watch time worth having.",
                ],
            },
            {
                "h2": "Premiere views need real people",
                "p": [
                    "A premiere is a moment: people waiting, chatting and watching together. Bought premiere views can fill a counter but never the chat. We can't bring an audience to a set minute either, and we won't pretend to.",
                    "What helps is a bigger base of real subscribers, who can see the premiere on their home page or in their subscriptions feed and tap to be reminded.",
                ],
            },
            {
                "h2": "How quickly real views build",
                "ul": [
                    "In the first days, your campaign goes live and new viewers reach your channel.",
                    "Each upload this month is there for the people who subscribed last week.",
                    "Views keep coming from those subscribers for as long as they enjoy your videos.",
                ],
            },
        ],
        "faqs": [
            ("How fast will my views go up?", "Once the campaign is live, which happens in its first days, views rise as new people find your channel. They grow with your audience instead of jumping on one video."),
            ("Can you send instant views to a new upload?", "No. Instant views come from scripts. Real views on a new upload come from people who see it in their feed or recommendations, and our job is to grow that group."),
            ("Can you fill my premiere with live viewers?", "No one can promise real people at a given minute. Growing real subscribers before a premiere gives you more people who may tune in."),
            ("Are views counted in my package?", "They come inside it, without a set number. The same people who subscribe, like and comment also watch, so views follow your audience."),
            ("Which package brings the most views?", "We don't size packages by views. A bigger package reaches more people, so {pro_name}, with typically {pro_audience} new subscribers a month, usually means more people watching."),
        ],
    },
    {
        "service": "views",
        "modifier": "free",
        "slug": "youtube/views/free",
        "label": "Free YouTube views?",
        "plan": "starter",
        "tool": "engagement-calculator",
        "title": "Buy 1,000 YouTube Views Free? Why They Don't Help | Growsterr",
        "description": "Free YouTube views, Shorts views included, come from exchanges and scripts. We don't give views away; check your engagement with our free calculator.",
        "h1": ("1,000 free YouTube views ", "won't watch your video. Real people will."),
        "intro": "Offers to buy 1,000 YouTube views free, or free Shorts views, run on view exchanges, autoplay tricks or bot plays, and none of them brings someone who watches. We don't give views away. The engagement calculator below costs nothing, and it tells you what share of your subscribers react to a typical video. When you want more real people watching, our packages bring them.",
        "hero": {"image": "youtube-channel", "alt": "A YouTuber checking likes and comments on recent videos"},
        "sections": [
            {
                "h2": "Where free views come from",
                "ul": [
                    "View exchanges: you watch strangers' videos for credits, and they play yours with the sound off.",
                    "Embeds and autoplay tricks that count a play nobody chose.",
                    "Bot plays handed out in small batches to sell you bigger ones.",
                    "Free Shorts views from scripts that swipe away after a second.",
                ],
            },
            {
                "h2": "Check your engagement with the calculator",
                "p": [
                    "This calculator runs entirely in your browser, at no cost. Where it asks for followers, enter your subscribers; then add the average likes and comments on your recent videos. The result is the share of your audience that reacts, a far better health check than a view count.",
                ],
            },
            {
                "h2": "Free ways to earn more views",
                "ul": [
                    "Spend as long on the title and thumbnail as on the edit; they decide the click.",
                    "Get to the point in the first seconds of a video or a Short.",
                    "Add end screens and playlists so one view leads to the next.",
                    "Reply to comments; people come back to conversations.",
                ],
            },
        ],
        "faqs": [
            ("Can I get 1,000 YouTube views for free?", "Not from real people, and not from us. A free thousand comes from exchanges or scripts. The calculator on this page is the part that's genuinely free."),
            ("Are free Shorts views any different?", "No. They come from the same tricks. A Short only travels when real people watch it through, so plays from scripts don't help it."),
            ("Can free views get my channel penalised?", "It's a real risk. Views from automated systems or exchanges fall under YouTube's fake engagement policy, which lets YouTube remove them or act against the channel."),
            ("Do you have a free views package?", "No. The smallest package is {starter_name} at {starter_price} a month, and views come inside it, from the real people who subscribe."),
            ("What does the engagement rate tell me?", "How much of your audience is really there. A low rate with a big subscriber count usually means many subscribers have stopped watching, or never did."),
        ],
    },
    {
        "service": "views",
        "modifier": "free-trial",
        "slug": "youtube/views/free-trial",
        "label": "YouTube views free trial?",
        "plan": "starter",
        "title": "Buy YouTube Views on a Free Trial? Test Us Properly | Growsterr",
        "description": "There's no free trial of YouTube views, and we don't sell views alone. Test us with one month of real viewers and YouTube's own analytics instead.",
        "h1": ("A YouTube views trial ", "only proves a counter can move."),
        "intro": "Hoping to buy YouTube views on a free trial before paying anything? There's no trial here, and views are never sold by themselves either. A trial of a few thousand views in an hour would only show that someone has scripts. What we offer is a monthly package that brings real people to your channel, views included from those same people, and you can cancel any time.",
        "hero": {"image": "youtube-hub", "alt": "A creator comparing YouTube analytics with a growth dashboard"},
        "sections": [
            {
                "h2": "What a views trial measures",
                "p": [
                    "One thing: whether the number moves. It says nothing about who watched, for how long, or whether anyone came back. Those are the questions that matter, and only real viewers can answer them.",
                ],
            },
            {
                "h2": "Test us with YouTube's own numbers",
                "p": [
                    "In your first month, open YouTube Studio next to our dashboard. Look at returning viewers, average view duration and new subscribers. Real people leave a trail in those numbers that bought plays never do.",
                ],
            },
        ],
        "faqs": [
            ("Is there a trial for YouTube views?", "No trials, for views or anything else. The shortest commitment is one month of a package, and you can cancel before it renews."),
            ("Can I buy a small views package to test?", "We don't sell views as a separate package, small or large. {starter_name}, at {starter_price} a month, is the smallest way to start."),
            ("How can I tell real views from bought ones?", "Look past the count: watch time, returning viewers and the comments people write tell you who's really there."),
            ("What if I cancel after the first month?", "Your package stops when the paid month ends. Viewers who subscribed stay subscribed unless they choose to leave."),
            ("Do views come with subscribers?", "Yes. Every package brings new subscribers, likes and comments, and those same people watch your videos."),
        ],
    },
]
