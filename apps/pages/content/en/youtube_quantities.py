"""English YouTube quantity pages: like, subscriber and view goals, from five likes to a million
views. A quantity is a goal, never a pack; the engine draws the pace chart from the packages.
Views have no typical ratio, so every views page names its package ("plan"). We never promise
monetization, watch hours, or numbers on the one video a customer may name.
Keys and placeholders: docs/CONTENT.md. Brief: docs/keywords/WRITING.md."""

UPDATED = "2026-11-08"

PAGES = [
    # --- Likes ----------------------------------------------------------------------------
    {
        "service": "likes",
        "quantity": 5,
        "slug": "youtube/likes/5",
        "label": "{quantity} YouTube likes",
        "title": "Buy {quantity} YouTube Likes? Start With Real Viewers | Growsterr",
        "description": "Buy {quantity} YouTube likes for a few cents and bots land on your first video. Our packages bring real viewers instead, and far more than {quantity} likes a month.",
        "h1": ("Buy {quantity} YouTube likes? ", "Give your first video real viewers."),
        "intro": "Wanting to buy {quantity} YouTube likes usually means a new video with an empty like counter. {quantity} likes sold for a few cents come from accounts that never pressed play, and YouTube removes likes it judges fake. Our packages bring real people who watch and like what they enjoy, typically {pick_likes} likes a month with {pick_name}, which leaves {quantity} far behind.",
        "hero": {"image": "youtube-viewers", "alt": "The first real viewers liking a new creator's very first YouTube upload"},
        "sections": [
            {
                "h2": "Send new viewers to the video that matters",
                "p": [
                    "When you order, you can name one video. New viewers are sent to it: they subscribe to your channel first, then watch. You can swap the video later in your account.",
                    "What they do after pressing play is up to them, so we don't promise likes, comments or watch time on that video. We promise real people, and the monthly ranges they typically add up to.",
                ],
            },
            {
                "h2": "Before the first viewers arrive",
                "ul": [
                    "A thumbnail that reads at phone size.",
                    "A title that says what the video delivers, not just what it's called.",
                    "An opening that gets to the point within the first seconds.",
                    "A couple more uploads, so a new subscriber has somewhere to go next.",
                ],
            },
        ],
        "faqs": [
            ("Can I get {quantity} likes on my video today?", "Not as an order. Nobody real likes a video on cue, and quick packs are made of accounts that never watched. Once your campaign starts, real viewers begin arriving in the first days."),
            ("Does it matter which video I name?", "Pick the one that best shows what your channel is about. New viewers subscribe first and then watch it, so it's their introduction to you."),
            ("Will YouTube remove bot likes?", "It can, and its fake engagement policy says so. Removal is the mild outcome; a channel that keeps inflating its numbers can face more than that."),
            ("Is the smallest package too big for a new channel?", "{pick_name} is meant for new and small channels. It's {pick_price} a month, and cancelling before the next renewal takes a moment in your account."),
            ("Do I need to give you my Google login?", "No. We need your channel handle, plus the video link if you want to name one. Never a password."),
        ],
    },
    {
        "service": "likes",
        "quantity": 10,
        "slug": "youtube/likes/10",
        "label": "{quantity} YouTube likes",
        "title": "Buy {quantity} YouTube Likes? Make the Visible Number Real | Growsterr",
        "description": "Want to buy {quantity} YouTube likes? With dislikes hidden, the like count is what viewers see. Real people bring many times {quantity} likes a month.",
        "h1": ("Buy {quantity} YouTube likes? ", "The one public number should be real."),
        "intro": "Since YouTube hid public dislike counts, the like count is the only reaction viewers see under a video, so it's natural to want to buy {quantity} YouTube likes and fill it. A cents-priced pack of {quantity} is bots. Our packages bring real viewers who like what they enjoy, many times {quantity} a month, with {pick_name} usually bringing {pick_likes}.",
        "hero": {"image": "youtube-channel", "alt": "A creator checking the like count under a freshly published YouTube video"},
        "sections": [
            {
                "h2": "What viewers read from a like count",
                "p": [
                    "Someone deciding whether to watch glances at the like count as a quick hint of quality. It's a small hint, though: views, comments and how recent the video is say just as much.",
                    "A like count that doesn't fit the rest, lots of likes on few views or no comments at all, makes people trust the video less, not more.",
                ],
            },
            {
                "h2": "What YouTube reads instead",
                "p": [
                    "Behind the public number, YouTube has said it looks at what viewers actually do: whether they watched, for how long, whether they came back. Likes from accounts that never watched are the easiest part of that picture to throw out.",
                ],
            },
        ],
        "faqs": [
            ("Can viewers still see dislikes?", "Only the creator sees the dislike count, in YouTube Studio; viewers see likes. That's one reason the like number feels so important, and why a fake one is a bad trade."),
            ("Do dislikes from real viewers hurt?", "Real viewers can dislike a video, as any audience can. A few honest dislikes are part of having an audience; a channel padded with fake likes is the bigger problem."),
            ("How do likes from a package arrive?", "A few at a time, from the first days of your campaign through to the end of the month, on the videos new viewers decide to watch."),
            ("Can I choose which videos get the attention?", "On {rising_name} and {pro_name}, yes. Every package also lets you name one video that new viewers are sent to; they subscribe, then watch. Liking stays their call."),
            ("Are the likes from subscribers?", "From the same real people who subscribe through the campaign. Likes, subscriptions and comments arrive together because one set of viewers leaves all three."),
        ],
    },
    {
        "service": "likes",
        "quantity": 20,
        "slug": "youtube/likes/20",
        "label": "{quantity} YouTube likes",
        "title": "Buy {quantity} YouTube Likes? Likes Without Views Look Odd | Growsterr",
        "description": "Before you buy {quantity} YouTube likes, check your views: likes with nobody watching look odd. Real viewers bring both, and well past {quantity} likes a month.",
        "h1": ("Buy {quantity} YouTube likes? ", "Check your views first."),
        "intro": "If you're about to buy {quantity} YouTube likes for a video with a handful of views, picture how it reads: more likes than people who could have watched. A pack of {quantity} for small change is made of bots, and the numbers won't agree. Real viewers bring likes and views together; our packages bring well past {quantity} likes in a month, typically {pick_likes} with {pick_name}.",
        "hero": {"image": "youtube-viewers", "alt": "Viewers watching a YouTube video before some of them press like"},
        "sections": [
            {
                "h2": "Likes and views have to agree",
                "p": [
                    "Every like on YouTube should come from someone who watched. When a video's likes run ahead of its views, or arrive in a burst with no views around them, the numbers contradict each other.",
                    "Viewers notice the odd ones. YouTube can check far more than viewers can, including which accounts watched before they liked.",
                ],
            },
            {
                "h2": "How real viewers fill in the whole picture",
                "p": [
                    "When a real person finds your channel, they watch something. If they enjoy it, they might like it, subscribe, leave a comment or open another video. Every number moves a little, and together they make sense.",
                ],
            },
        ],
        "faqs": [
            ("What's a normal number of likes per view?", "It varies too much by topic and audience for any single figure to be honest. A better check: your likes should rise and fall with your views, never on their own."),
            ("Will views come with the likes?", "Yes, because the likes come from people who watched. We don't count views in advance, since each one is someone choosing to play a video, but every like starts with a view."),
            ("Can I have {quantity} likes on a video with few views?", "Not from us, and you wouldn't want them from anyone: likes that outnumber the likely viewers are the clearest giveaway there is."),
            ("Which videos will the likes be on?", "Whichever ones viewers pick. Name a video at checkout and newcomers are sent there first; after subscribing they watch it and decide for themselves whether to like it."),
            ("How much is the smallest package?", "{pick_name} is {pick_price} a month, with typically {pick_audience} new subscribers and {pick_likes} likes. There's no contract: cancelling happens in your account."),
        ],
    },
    {
        "service": "likes",
        "quantity": 25,
        "slug": "youtube/likes/25",
        "label": "{quantity} YouTube likes",
        "title": "Buy {quantity} YouTube Likes? Here's the Honest Answer | Growsterr",
        "description": "Buy {quantity} YouTube likes for a few cents? That's bots, and YouTube's rules cover them. Real viewers bring comfortably more than {quantity} likes a month.",
        "h1": ("Buy {quantity} YouTube likes? ", "Here's the honest answer."),
        "intro": "If you want to buy {quantity} YouTube likes, you can find them for a few cents almost anywhere. They come from accounts that never watched, and YouTube's fake engagement rules exist for exactly that. We do it the long way round: real people discover your channel, watch, and like what they enjoy. That's comfortably more than {quantity} likes a month, typically {pick_likes} with {pick_name}.",
        "hero": {"image": "youtube-hub", "alt": "A small YouTube channel receiving likes from viewers who watched its videos"},
        "sections": [
            {
                "h2": "What YouTube says about bought likes",
                "p": [
                    "YouTube doesn't allow anything that artificially inflates likes, views or comments, such as automated systems. Content can be removed, and repeated violations can put a channel at risk.",
                    "That's a lot of risk for {quantity} likes nobody will remember.",
                ],
            },
            {
                "h2": "How likes get to your videos with us",
                "ul": [
                    "Your channel is shown to real people through promoted campaigns in our partner network, every day.",
                    "Those who are interested watch, and many subscribe.",
                    "Some like the videos they enjoyed, usually {pick_likes} likes in a {pick_name} month.",
                    "Your dashboard shows the visits and new subscribers we measured.",
                ],
            },
            {
                "h2": "If you only have a couple of videos",
                "p": [
                    "That's fine for a start, but give new viewers a reason to stay: plan the next upload before the campaign brings them. People who subscribe and then find nothing new for weeks tend to forget why they came.",
                ],
            },
        ],
        "faqs": [
            ("Why are likes sold so cheaply elsewhere?", "Because they cost almost nothing to produce when no person is involved. A real like needs someone to find your video, watch it and choose to react, and that can't be done for a few cents."),
            ("Is {quantity} likes too small to bother with?", "As a goal, it's a fine first step, and a package passes it quickly. As a purchase on its own, it's too small to be done honestly: no real campaign is built around {quantity} people."),
            ("Do the likes come with comments?", "They do, from the same viewers: typically {pick_comments} comments a month with {pick_name}, written in their own words."),
            ("Can I name the video I want people to watch?", "One video, yes, at checkout or later in your account. New viewers land on it, subscribe first and then watch; whether they like it is up to them."),
            ("What if I stop after a month?", "The subscribers and their likes stay on your channel, because they're people, not a rental. Nothing renews once you cancel, and the month already paid for carries on."),
        ],
    },
    {
        "service": "likes",
        "quantity": 50,
        "slug": "youtube/likes/50",
        "label": "{quantity} YouTube likes",
        "title": "Buy {quantity} YouTube Likes? Let Your Channel Earn Them | Growsterr",
        "description": "Thinking of buying {quantity} YouTube likes? Bots land on one video and stop. Real viewers like across your channel, far beyond {quantity} a month with {pick_name}.",
        "h1": ("Buy {quantity} YouTube likes? ", "Let your whole channel earn them."),
        "intro": "When people buy {quantity} YouTube likes, they usually point them at one upload. A pack that size for a few cents is bots, and it stops where it started. Real viewers behave differently: they find one video, like it, and go looking for more. Our packages bring likes that way, far beyond {quantity} a month: typically {pick_likes} with {pick_name}.",
        "hero": {"image": "youtube-channel", "alt": "A YouTube channel page with viewers working through its older uploads"},
        "sections": [
            {
                "h2": "Your older videos are part of the deal",
                "p": [
                    "A viewer who enjoys one video often opens your channel page and works through the rest. Old uploads get watched again, and liked again, by people who weren't around when you posted them.",
                    "That's something a like pack can never do: it doesn't know your other videos exist.",
                ],
            },
            {
                "h2": "Make the channel easy to explore",
                "ul": [
                    "Group videos into playlists by topic, so one good video leads to the next.",
                    "Use end screens to point at the video a newcomer should watch second.",
                    "Link related uploads in your descriptions.",
                ],
            },
        ],
        "faqs": [
            ("Will old videos get likes too?", "Often, yes. People who like one video tend to look around, and the videos they enjoy get their likes, whatever the upload date."),
            ("Can I pick which video gets the {quantity} likes?", "No video gets a set number. You can pick one video for new viewers to start on, and {rising_name} and {pro_name} add a choice of which videos get the attention; the likes themselves stay with the viewers."),
            ("Do playlists help?", "They help viewers keep watching, which is what you want once a campaign brings them in. Someone who watches three of your videos has three chances to like, comment or subscribe."),
            ("How many likes does a month bring?", "With {pick_name}, typically {pick_likes}, from people who also subscribe and comment. The range grows with the package: {rising_likes} with {rising_name}, {pro_likes} with {pro_name}."),
            ("Is a like on an old video worth less?", "Not to you. It's a person telling you that video still works, and a reason to make more like it."),
        ],
    },
    {
        "service": "likes",
        "quantity": 100,
        "slug": "youtube/likes/100",
        "label": "{quantity} YouTube likes",
        "title": "Buy {quantity} YouTube Likes? Build Your First-Day Crowd | Growsterr",
        "description": "Want to buy {quantity} YouTube likes for each new upload? Subscribers who watch give a video its first-day likes. Our packages bring them every day.",
        "h1": ("Buy {quantity} YouTube likes for every upload? ", "Build the crowd that shows up on day one."),
        "intro": "People who want to buy {quantity} YouTube likes often mean on every new upload, so a video never starts empty. {quantity} likes for a few cents are bots, and they'd have to be bought again for every video. Subscribers come back on their own: they see your new upload and some like it on day one. Our packages bring those subscribers, and likes far above {quantity} a month: typically {pick_likes} with {pick_name}.",
        "hero": {"image": "youtube-subscribers", "alt": "Subscribers opening a creator's new YouTube upload on the day it goes live"},
        "sections": [
            {
                "h2": "Where first-day likes come from",
                "p": [
                    "A new upload appears in your subscribers' feeds and subscriptions tab, and those who know you tend to be the first to react. Strangers usually arrive later, once the video has something to show.",
                    "More real subscribers means a bigger first-day crowd, and a video that opens with likes and comments has more to offer the people who don't know you yet.",
                ],
            },
            {
                "h2": "Growing the crowd month by month",
                "p": [
                    "With {pick_name}, typically {pick_audience} new subscribers join each month. They chose to subscribe, so many will see your next upload; not all, because no audience watches everything.",
                    "Upload on a schedule they can learn, and the first day of each video gets busier.",
                ],
            },
        ],
        "faqs": [
            ("Can you add {quantity} likes to each new video?", "No, we don't put likes on uploads. We bring subscribers, and subscribers are the ones who like a new video early, on their own."),
            ("Do subscribers get notified of my uploads?", "Only those who turn on notifications; the rest see new uploads in their feed or subscriptions tab. Either way, more real subscribers means more people who can find each video early."),
            ("Why not order likes for each upload?", "Bought likes have to be bought again every time and never bring you closer to an audience. Subscribers keep turning up without being asked."),
            ("How long until uploads get {quantity} likes on their own?", "That depends on your videos and your rhythm, so we won't name a date. What we can tell you is how fast the audience grows: typically {pick_audience} new subscribers a month with {pick_name}."),
            ("Do the likes go to new videos or old ones?", "Both. New subscribers watch what you post next, and many look back through your channel first."),
        ],
    },
    {
        "service": "likes",
        "quantity": 1000,
        "slug": "youtube/likes/1000",
        "label": "{quantity} YouTube likes",
        "title": "Buy {quantity} YouTube Likes? Get a Thousand Real Viewers | Growsterr",
        "description": "Want to buy 1000 YouTube likes? A thousand real likes means real viewers behind them. {pick_name} usually adds {pick_likes} a month across your videos.",
        "h1": ("Buy {quantity} YouTube likes? ", "Get the viewers who'd give them."),
        "intro": "If you want to buy {quantity} YouTube likes, it helps to picture them: a thousand people who watched something of yours and wanted to say so. A bot pack can't fake that crowd for long. Our packages bring the real one, and with {pick_name} a month typically adds up to {pick_likes} likes across your videos, from people who also subscribe and comment.",
        "hero": {"image": "youtube-viewers", "alt": "A crowd of real viewers each liking a different video on one YouTube channel"},
        "sections": [
            {
                "h2": "What a thousand real likes come with",
                "p": [
                    "Behind a thousand real likes there are more viewers than that, because not everyone who enjoys a video presses the button. There are comments, new subscribers and replays from people who came back.",
                    "A thousand likes with nothing around them is the outline of a crowd with nobody inside.",
                ],
            },
            {
                "h2": "Across your videos, at the pace people choose",
                "p": [
                    "At a typical pace, {pick_name} passes {quantity} likes during the first month, spread over the videos people choose to watch.",
                    "Name one video and new viewers start there; on {rising_name} and {pro_name} you also choose which videos get the attention. Neither puts a fixed count on any video.",
                ],
            },
        ],
        "faqs": [
            ("Can I get {quantity} likes on a single video?", "Not as a promise. Likes follow what people watch, and we don't control that. If one video is your best, name it, so new viewers start there."),
            ("How long does {quantity} likes take?", "Usually within the first month with {pick_name}, counted across your channel. Real viewers set the pace, so some weeks bring more than others."),
            ("Would {quantity} bought likes hurt my channel?", "They can. YouTube removes engagement it judges fake, and a channel that keeps buying it risks more than the likes. Even before that, the numbers don't add up for anyone who looks."),
            ("Do I get subscribers with the likes?", "They arrive together, from the same people: typically {pick_audience} new subscribers a month with {pick_name}, plus {pick_comments} comments."),
            ("Is there a cheaper way to a thousand real likes?", "{pick_name} is our smallest package, at {pick_price} a month. Spread over everything it brings, the cost per real person is small; spread over a pack of bots, any price is too much."),
        ],
    },
    # --- Subscribers: small goals ---------------------------------------------------------
    {
        "service": "subscribers",
        "quantity": 20,
        "slug": "youtube/subscribers/20",
        "label": "{quantity} YouTube subscribers",
        "title": "Buy {quantity} YouTube Subscribers? Set Up for Real Ones | Growsterr",
        "description": "Starting a channel and want to buy {quantity} YouTube subscribers? A cents-priced pack can only be bots. Real subscribers arrive by the month, far past {quantity}.",
        "h1": ("Buy {quantity} YouTube subscribers? ", "Start your channel with real people."),
        "intro": "If you've just started a channel and want to buy {quantity} YouTube subscribers so it doesn't look empty, here's the straight answer. A pack of {quantity} for a few cents is bots, and YouTube regularly removes spam subscribers. Our packages bring real people who choose to subscribe, far past {quantity} in a month: typically {pick_audience} with {pick_name}.",
        "hero": {"image": "youtube-subscribers", "alt": "A brand-new YouTube channel gaining its first subscribers from real viewers"},
        "sections": [
            {
                "h2": "Set the channel up before anyone subscribes",
                "ul": [
                    "A channel name and handle that match what you make.",
                    "A banner and profile picture that look right on a phone.",
                    "A short description: what you upload and how often.",
                    "At least three videos, so a new subscriber has more than one thing to watch.",
                ],
                "image": {"image": "youtube-channel", "alt": "A new YouTuber designing a channel banner before the first upload"},
            },
            {
                "h2": "Why your first subscribers shape the channel",
                "p": [
                    "Early on, your subscribers are a big share of the people who see each upload. If the first {quantity} are bots, that share never watches, and every video starts slower than it should.",
                ],
            },
        ],
        "faqs": [
            ("Do I need a minimum number of videos?", "No minimum from us, but give people something to subscribe for. A few videos in the same style tell a new viewer what they'll get by subscribing."),
            ("How soon would I pass {quantity} subscribers?", "Usually within the first days of the campaign at a typical pace. Real people subscribe when they find you, so the exact day varies."),
            ("Will YouTube delete the subscribers you bring?", "YouTube removes spam and closed accounts. The people we bring are viewers who subscribed themselves, so a spam sweep isn't aimed at them; the odd person closing their account happens on every channel."),
            ("What does a new channel need from me?", "Your channel handle, where your viewers should come from and, if you like, one video to send them to. The channel has to be public, and nobody here will ever ask for your password."),
            ("Is {pick_name} right for a brand-new channel?", "It's built for new and small channels: {pick_price} a month for typically {pick_audience} new subscribers, and stopping it is up to you, at any time, from your account."),
        ],
    },
    {
        "service": "subscribers",
        "quantity": 25,
        "slug": "youtube/subscribers/25",
        "label": "{quantity} YouTube subscribers",
        "title": "Buy {quantity} YouTube Subscribers? Win Over Real Strangers | Growsterr",
        "description": "Want to buy {quantity} YouTube subscribers? Bots for cents won't watch. Strangers who chose your channel will, and packages bring far more than {quantity} a month.",
        "h1": ("Buy {quantity} YouTube subscribers? ", "Win over strangers who'll actually watch."),
        "intro": "Your first YouTube subscribers usually come from people who know you, and it's tempting to buy {quantity} YouTube subscribers to fill out the rest. A pack that small for a few cents is bots. The subscribers that move a channel forward are strangers who found a video and liked it; our packages bring far more than {quantity} of them a month, typically {pick_audience} with {pick_name}.",
        "hero": {"image": "youtube-viewers", "alt": "Strangers discovering a small YouTube channel and choosing to subscribe"},
        "sections": [
            {
                "h2": "Friends subscribe for you, strangers subscribe for the videos",
                "p": [
                    "Friends and family are real and their support counts, but they'd subscribe whatever you uploaded. A stranger subscribing is a different signal: someone with no reason to be kind decided your videos are worth more of their time.",
                    "Those are the viewers YouTube learns from when it works out who else might enjoy your channel.",
                ],
            },
            {
                "h2": "What strangers check before subscribing",
                "ul": [
                    "Whether the video they watched delivered what the title said.",
                    "Whether there's more of it on your channel.",
                    "Whether the channel looks alive: recent uploads, replies to comments.",
                    "Whether you speak their language, which is where choosing a location helps.",
                ],
            },
        ],
        "faqs": [
            ("Should I ask friends to subscribe?", "Sure, they're real people. Just don't count on them to watch everything; they'll support you, but the viewers who stay for the topic are the ones you grow with."),
            ("Who are the strangers you bring?", "Real YouTube users in the city, region or country you choose, who came across your channel through our campaign and subscribed because they liked it."),
            ("How quickly do strangers start subscribing?", "From the first days of the campaign, at their own pace. {quantity} usually passes early; the month typically ends at {pick_audience} with {pick_name}."),
            ("Will strangers comment?", "Some will, which is the best sign you're reaching the right people: typically {pick_comments} comments a month with {pick_name}, in their own words."),
            ("Why not buy {quantity} just to look less empty?", "Because they'll stay empty: bot subscribers don't watch, and a channel whose subscribers never watch looks emptier to YouTube, not fuller."),
        ],
    },
    {
        "service": "subscribers",
        "quantity": 50,
        "slug": "youtube/subscribers/50",
        "label": "{quantity} YouTube subscribers",
        "title": "Buy {quantity} Subscribers on YouTube? Read This First | Growsterr",
        "description": "Thinking of buying {quantity} subscribers on YouTube? On a small channel, bots become most of your audience. Packages bring real people instead, well over {quantity} a month.",
        "h1": ("Buy {quantity} subscribers on YouTube? ", "On a small channel, bots weigh more."),
        "intro": "If you want to buy {quantity} subscribers on YouTube, your channel is probably small, and that's exactly where bots do the most harm. A pack of {quantity} for a few cents can turn most of your audience into accounts that never watch. Our packages bring real subscribers instead, well over {quantity} a month: typically {pick_audience} with {pick_name}.",
        "hero": {"image": "youtube-subscribers", "alt": "A small YouTube channel whose subscribers are all real viewers"},
        "sections": [
            {
                "h2": "The math on a small channel",
                "p": [
                    "Picture a channel with 30 real subscribers who watch most uploads. Add {quantity} bots and more than half your subscribers never press play.",
                    "On a big channel, a few dozen fake accounts disappear in the crowd. On a small one, they are the crowd.",
                ],
            },
            {
                "h2": "Buy YouTube subscribers {quantity} at a time? Not real ones",
                "p": [
                    "{quantity} real people can't be ordered. They have to find a video, enjoy it and decide, and that never happens in a neat batch delivered within the hour.",
                    "What a package does is keep real people finding your channel every day, so {quantity} comes and goes early and the month keeps adding more.",
                ],
            },
        ],
        "faqs": [
            ("Is it worth starting a package with under 100 subscribers?", "Yes, as long as you have a few videos people can enjoy. Small channels feel real growth the most: each new subscriber is a big share of the audience."),
            ("Would {quantity} bot subscribers get my channel in trouble?", "YouTube's rules forbid inflating subscriber counts with automated systems, and it removes spam subscribers. Repeated fake engagement can lead to more than removal, so it's a poor trade for {quantity}."),
            ("Do the subscribers you bring watch my videos?", "They subscribed after seeing your channel, so many will. What they watch, and how much, is up to them; we never promise watch time."),
            ("Can you send subscribers from my country?", "Yes. Choose a city, region or country when you order and we aim there first. If the matching audience there is small, some subscribers may come from nearby."),
            ("What if my channel covers a niche topic?", "Niche channels suit real growth, because the people who subscribe are genuinely interested. Targeting is by place; your videos do the work of keeping the right viewers."),
        ],
    },
    {
        "service": "subscribers",
        "quantity": 200,
        "slug": "youtube/subscribers/200",
        "label": "{quantity} YouTube subscribers",
        "title": "Buy {quantity} YouTube Subscribers? Get a Real Community | Growsterr",
        "description": "Thinking of buying {quantity} YouTube subscribers? Cheap packs that size are bots. Real subscribers become regulars in your comments, many times {quantity} a month.",
        "h1": ("Buy {quantity} YouTube subscribers? ", "Get regulars, not a number."),
        "intro": "Gaming, crafts, fishing, music: hobby channels at a few hundred subscribers are where communities start, and it's tempting to buy {quantity} YouTube subscribers to speed that up. Pocket-money packs of {quantity} are bots, and bots never become regulars. Our packages bring many times {quantity} real subscribers a month, typically {pick_audience} with {pick_name}, with comments from the same people.",
        "hero": {"image": "youtube-channel", "alt": "A hobby YouTuber reading comments from regular viewers"},
        "sections": [
            {
                "h2": "At {quantity}, you know the names",
                "p": [
                    "A small channel's charm is that you recognise the people in your comments. They ask questions, suggest the next video, show up when you go live.",
                    "Bought subscribers add nothing to that, and they make your community look smaller than it is: a big number over a quiet comment section.",
                ],
            },
            {
                "h2": "Turning new subscribers into regulars",
                "ul": [
                    "Reply to comments, especially the first one on each video.",
                    "Ask a real question at the end of a video, then use the answers.",
                    "Heart and pin good comments; people notice.",
                    "Keep a schedule: regulars come back on the day they expect you.",
                ],
            },
        ],
        "faqs": [
            ("Do new subscribers join my live streams?", "Some may, if they're around and interested; that's their choice. We never promise a live audience at a set time, but real subscribers are the only ones who could turn up."),
            ("Will my community notice the new people?", "They'll notice more names in the comments and more going on under each video. Nothing else changes on your channel: we never log in or touch your settings."),
            ("How many comments does a package bring?", "Typically {pick_comments} a month with {pick_name}, written by real viewers in their own words. They come with the subscribers, not as a separate order."),
            ("Can I grow a gaming channel this way?", "Yes. Gaming viewers subscribe for a personality or a game they love; the campaign brings them to your channel, and your videos decide whether they stay."),
            ("What happens after {quantity}?", "The package keeps bringing people until you cancel, so {quantity} is a stop on the way. A typical month ends well beyond it: {pick_audience} with {pick_name}."),
        ],
    },
    {
        "service": "subscribers",
        "quantity": 300,
        "slug": "youtube/subscribers/300",
        "label": "{quantity} YouTube subscribers",
        "title": "Buy {quantity} YouTube Subscribers? Fix Discovery First | Growsterr",
        "description": "Stuck in the low hundreds and want to buy {quantity} YouTube subscribers? The problem is discovery. Real viewers fix it, and they arrive by the month, past {quantity}.",
        "h1": ("Buy {quantity} YouTube subscribers? ", "Your problem is discovery, not the count."),
        "intro": "Channels that want to buy {quantity} YouTube subscribers have often been uploading for months and stalled in the low hundreds. The videos are usually fine; too few new people see them. Buying {quantity} for a few cents gets you bots and changes nothing about that. Our packages bring real viewers to your channel every day, well past {quantity} a month: typically {pick_audience} with {pick_name}.",
        "hero": {"image": "youtube-hub", "alt": "A YouTube channel breaking out of a long plateau as new viewers find it"},
        "sections": [
            {
                "h2": "Why channels stall in the low hundreds",
                "p": [
                    "YouTube recommends a video more widely once it has signs that people enjoy it, and a small channel struggles to collect those signs because few people see it in the first place.",
                    "It's a loop: low reach, few signals, low reach. Bought subscribers make it worse, because they're subscribers who never watch.",
                ],
            },
            {
                "h2": "Breaking the loop with real viewers",
                "p": [
                    "A campaign puts your channel in front of new people every day. Those who like it watch, subscribe and react, and those reactions are exactly the signals your videos were missing.",
                    "Keep YouTube Studio open alongside our dashboard during the month: one shows your views and subscribers, the other the visits we measured.",
                ],
            },
        ],
        "faqs": [
            ("Is my content the problem?", "Maybe, maybe not, and a stall can't tell you which. Real viewers can: if they watch and subscribe, the videos work and reach was the issue; if they don't, you've learned what to change."),
            ("Will YouTube start recommending my videos?", "We can't promise what YouTube recommends. Real viewers give your videos the kind of signals recommendations are built on, which bought subscribers never do."),
            ("How long until I'm out of the low hundreds?", "With {pick_name}, a typical first month brings {pick_audience} new subscribers, so the low hundreds are usually behind you early on."),
            ("Should I change anything before starting?", "Make sure your best video is easy to find: name it at checkout so new viewers are sent there first. They subscribe, then watch, so it's your first impression."),
            ("Do you upload or edit videos for me?", "No. We don't touch your channel at all. You keep making videos; we bring people to them."),
        ],
    },
    {
        "service": "subscribers",
        "quantity": 400,
        "slug": "youtube/subscribers/400",
        "label": "{quantity} YouTube subscribers",
        "title": "Buy {quantity} YouTube Subscribers? Aim at Your City | Growsterr",
        "description": "Want to buy {quantity} YouTube subscribers for a local channel? Bots come from nowhere. Real people come from the city you choose, far more than {quantity} a month.",
        "h1": ("Buy {quantity} YouTube subscribers? ", "Aim for viewers in your own city."),
        "intro": "Teachers, coaches, restaurants, local bands: plenty of channels exist for people in one place. If you want to buy {quantity} YouTube subscribers for a channel like that, a cheap pack of {quantity} comes from accounts with no home town at all. Our packages bring real subscribers from the city, region or country you choose, far more than {quantity} a month: typically {pick_audience} with {pick_name}.",
        "hero": {"image": "youtube-viewers", "alt": "Viewers in one city watching a local business's YouTube channel"},
        "sections": [
            {
                "h2": "A local channel needs local viewers",
                "p": [
                    "A driving instructor in Leeds has no use for subscribers in another hemisphere. Tell us the city when you order, and the campaign shows your channel to people there first.",
                    "When the city can't supply enough matching viewers, we reach into the region around it.",
                ],
            },
            {
                "h2": "What local subscribers can do that others can't",
                "ul": [
                    "Watch for practical reasons: your prices, your timetable, your next gig.",
                    "Call, book or turn up, if what they see suits them.",
                    "Pass your videos on to friends nearby.",
                    "Leave comments other locals trust.",
                ],
            },
        ],
        "faqs": [
            ("Can I target a single city?", "Yes, name it when you order. If the city is small, the campaign may widen to the surrounding area to reach enough people who match."),
            ("Does it work for a business channel?", "Yes, for any public channel. Businesses usually care most about where viewers are, and that's the part you control."),
            ("Do I need to make videos in the local language?", "It helps a lot. People subscribe to videos they understand, so match the location you choose to the language you speak on camera."),
            ("Is a single city slower than a whole country?", "It can be, because fewer people match. The pace chart above shows a typical month; a tight local campaign may sit toward the lower end of it."),
            ("Do you make videos for local businesses?", "No, we grow the audience for videos you make. If you'd like to talk about something larger, write to us on WhatsApp or by email."),
        ],
    },
    {
        "service": "subscribers",
        "quantity": 500,
        "slug": "youtube/subscribers/500",
        "label": "{quantity} YouTube subscribers",
        "title": "Buy {quantity} YouTube Subscribers? The Honest Road to {quantity} | Growsterr",
        "description": "Aiming to buy {quantity} YouTube subscribers for the Partner Program? Bought ones don't help at review. Real viewers bring well over {quantity} a month.",
        "h1": ("Buy {quantity} YouTube subscribers? ", "Reach it with people YouTube will count."),
        "intro": "Many people who want to buy {quantity} YouTube subscribers have the Partner Program in mind: in many countries, {quantity} subscribers is part of its first, fan-funding level. A few cents' worth of {quantity} subscribers is bots, and YouTube reviews channels before admitting them. Our packages bring well over {quantity} real subscribers a month, typically {pick_audience} with {pick_name}. We never promise monetization.",
        "hero": {"image": "youtube-subscribers", "alt": "A growing YouTube channel approaching its first Partner Program milestone"},
        "sections": [
            {
                "h2": "Subscribers are only one part of the bar",
                "p": [
                    "YouTube's requirements also include recent uploads and watch hours or Shorts views, and those are parts no package should promise. Watch hours come from people choosing to watch, and YouTube decides who joins the program.",
                    "We help with the part we can: real people discovering your channel and subscribing because they want to.",
                ],
            },
            {
                "h2": "Why bought subscribers are a risk at review",
                "p": [
                    "When a channel applies, YouTube reviews it against its policies, and inflated numbers are the kind of thing that review exists to catch. Bought subscribers can't help you pass, and they can give YouTube a reason to say no.",
                ],
            },
        ],
        "faqs": [
            ("Will {quantity} subscribers get me monetized?", "No package can promise that. YouTube decides who joins its Partner Program, based on subscribers, watch hours or Shorts views, recent uploads and its policies. We bring real subscribers; the rest is your channel and YouTube's review."),
            ("Does the {quantity}-subscriber level exist in my country?", "YouTube offers it in many countries and keeps the list on its own help pages. Check there, since the rules change from time to time."),
            ("Do your subscribers count toward watch hours?", "Their watching counts the way any viewer's does, because they're real people. We don't promise how long anyone watches, so we never quote watch hours."),
            ("What should I do while the subscribers come in?", "Keep uploading: recent uploads are part of YouTube's bar, and every new video gives new subscribers something to watch."),
            ("What does {pick_name} include?", "Typically {pick_audience} new subscribers, {pick_likes} likes and {pick_comments} comments a month, spread over 30 days from the place you choose, for {pick_price}."),
        ],
    },
    # --- Subscribers: bigger goals --------------------------------------------------------
    {
        "service": "subscribers",
        "quantity": 1000,
        "slug": "youtube/subscribers/1000",
        "label": "{quantity} YouTube subscribers",
        "title": "Buy {quantity} YouTube Subscribers for $5? What It Buys | Growsterr",
        "description": "Buy 1,000 YouTube subscribers for $5 online and you get bots that never watch. Cheap, real and 1,000 don't fit together; here's what real costs instead.",
        "h1": ("Buy {quantity} YouTube subscribers for $5? ", "Here's what that money buys."),
        "intro": "If you want to buy {quantity} YouTube subscribers for $5, you'll find plenty of offers. At half a cent a subscriber, none of them are people: they're accounts made to be sold, and they never watch. A real {quantity} costs more because each one is a person who found your channel and chose to subscribe. With {pick_name}, that's typically {pick_audience} new subscribers in a month, for {pick_price}.",
        "hero": {"image": "youtube-subscribers", "alt": "A YouTube channel reaching its first thousand subscribers, all real viewers"},
        "sections": [
            {
                "h2": "What $5 for {quantity} subscribers really buys",
                "p": [
                    "No real person can be reached, shown a video and persuaded to subscribe for half a cent. What that price buys is a number pushed up by accounts nobody runs.",
                    "Those accounts don't watch, so they shrink the part of your audience that does, and YouTube removes spam subscribers when it finds them, so the number rarely even lasts.",
                ],
            },
            {
                "h2": "The {quantity}-subscriber mark and the Partner Program",
                "p": [
                    "{quantity} subscribers is one of the requirements of the YouTube Partner Program, alongside watch hours or Shorts views. That's why it's the number people most want to shortcut, and why YouTube reviews channels before they join.",
                    "Fake subscribers can't get you through that review. We bring real ones, without promising monetization or watch hours.",
                ],
            },
            {
                "h2": "Buying {quantity} subscribers on YouTube cheap, compared honestly",
                "p": [
                    "{pick_name} is {pick_price} a month for typically {pick_audience} real subscribers, plus their likes and comments. Per person, that's a small amount; per bot, $5 is money spent on a problem.",
                ],
            },
        ],
        "faqs": [
            ("Is there any real way to get {quantity} subscribers for $5?", "No. Five dollars can't pay for a thousand people to find your channel, watch and choose to subscribe. Whatever arrives at that price is automated, whatever the site calls it."),
            ("How long do {quantity} real subscribers take?", "With {pick_name}, usually within the first month at a typical pace. Every subscriber is someone deciding, so it's a range, not a countdown."),
            ("Will {quantity} subscribers get me into the Partner Program?", "Not on their own. YouTube also needs watch hours or Shorts views, and it reviews every channel. We don't promise monetization; we bring the real-subscriber part."),
            ("What happens to fake subscribers?", "YouTube removes spam and closed accounts from subscriber counts, so bought numbers tend to shrink. The channels that bought them keep the silence and lose the number."),
            ("Can I pay just once?", "No. It's a monthly subscription by card, Apple Pay or Google Pay through Stripe. Cancel from your account before the next month begins and nothing more is charged."),
        ],
    },
    {
        "service": "subscribers",
        "quantity": 10000,
        "slug": "youtube/subscribers/10000",
        "label": "{quantity} YouTube subscribers",
        "title": "Buy {quantity} YouTube Subscribers? Build a Real Show | Growsterr",
        "description": "Want to buy 10 000 YouTube subscribers? {pick_name} usually adds {pick_audience} real people a month. At this size, your channel has to run like a show.",
        "h1": ("Buy {quantity} YouTube subscribers? ", "Run your channel like a show people return to."),
        "intro": "Looking to buy {quantity} YouTube subscribers usually means you're past hobby size and thinking about what the channel could become. Real people are the only route there that lasts. {pick_name} typically brings {pick_audience} new subscribers a month, so {quantity} is usually weeks to a few months away, with likes and comments from the same viewers.",
        "hero": {"image": "youtube-channel", "alt": "A creator filming the next episode of a regular YouTube series"},
        "sections": [
            {
                "h2": "What changes on the way to {quantity}",
                "p": [
                    "At a few hundred subscribers, every video is a one-off. On the way to {quantity}, channels that keep growing start to work in series: recurring formats viewers can expect, on days they can expect them.",
                    "That's what turns new subscribers into returning viewers, and returning viewers are what YouTube tends to reward.",
                ],
            },
            {
                "h2": "What {pick_name} adds at this size",
                "ul": [
                    "Typically {pick_audience} new subscribers a month from the place you choose.",
                    "A choice of which videos get the attention, so newcomers meet your strongest series.",
                    "Priority placement for your campaign.",
                    "A direct WhatsApp line to our team.",
                ],
            },
        ],
        "faqs": [
            ("How long does {quantity} take with real subscribers?", "With {pick_name}, usually somewhere in the first few months; the table above shows each package's usual span. Real people set the speed, so treat it as a range."),
            ("Can I reach {quantity} on a smaller package?", "Yes, it just takes longer, at {starter_audience} a month on {starter_name} or {rising_audience} on {rising_name}. You can start small and move up once you've seen how your channel responds."),
            ("Do sponsors care about {quantity} subscribers?", "Sponsors tend to look at views per video and who's watching more than at the subscriber count. Real subscribers who watch help both; bought ones help neither."),
            ("Which videos should get the attention?", "Your best entry points: videos that make sense to someone who's never seen your channel and lead naturally to the next one. Not part three of a series."),
            ("Does YouTube treat a channel differently at {quantity}?", "Not in any official way we can point to. What changes is what you can do with an audience that size, if it's real."),
        ],
    },
    {
        "service": "subscribers",
        "quantity": 50000,
        "slug": "youtube/subscribers/50000",
        "label": "{quantity} YouTube subscribers",
        "title": "Buy 50k YouTube Subscribers? A Plan in Months | Growsterr",
        "description": "Want to buy 50k YouTube subscribers? Real ones take months, even with {pick_name} at {pick_audience} a month. Here's an honest plan toward {quantity}.",
        "h1": ("Buy 50k YouTube subscribers? ", "Here's the honest plan, month by month."),
        "intro": "If you want to buy 50k YouTube subscribers that are real people, plan for months. Anyone selling 50k by next week is selling bots. {pick_name}, our biggest package, typically brings {pick_audience} new subscribers a month, so {quantity} is a long project, and it's halfway to the Silver Creator Award, which YouTube only sends after reviewing the channel.",
        "hero": {"image": "youtube-hub", "alt": "A YouTube channel's subscriber line climbing steadily over many months"},
        "sections": [
            {
                "h2": "How the months usually go",
                "p": [
                    "The table above shows how long each package usually needs to bring {quantity} new subscribers. Treat it as a range for planning, not a deadline: some months bring more, some fewer.",
                    "Channels that keep growing between months are the ones that keep publishing. New subscribers arrive with the campaign; they stay for your uploads.",
                ],
            },
            {
                "h2": "Halfway to the Silver award",
                "p": [
                    "{quantity} is the halfway mark to the Silver Creator Award at 100,000. YouTube looks at each channel before sending it, and one inflated with fake subscribers is the kind it can turn down.",
                ],
            },
            {
                "h2": "A check-in rhythm",
                "ul": [
                    "Every month: set our dashboard beside the subscriber numbers in YouTube Studio.",
                    "Every quarter: look at which videos bring the most new subscribers, and make more like them.",
                    "Whenever your best work changes: update the video new viewers are sent to.",
                ],
            },
        ],
        "faqs": [
            ("Why can't real subscribers come faster?", "Because each one is a person who has to find your channel, watch and decide. Our biggest package reaches a lot of people every month, but people still take their time, and that pace is why the audience holds."),
            ("Is it worth paying for that many months?", "You're never paying for a promise about month twelve. Each month brings its own: typically {pick_audience} real subscribers, {pick_likes} likes and {pick_comments} comments with {pick_name}, and you can stop at any point."),
            ("Will my channel grow on its own as well?", "It often does, because real subscribers watch, share and give recommendations something to work with. We can't say by how much; that depends on your videos."),
            ("Do I keep the subscribers if I cancel halfway?", "Yes. They subscribed to your channel, not to us. A few will unsubscribe over time, as people do, but nothing is taken back when you stop."),
            ("My channel has a team. Does that change anything?", "Not much. We only need the channel handle and never touch the account, and {pro_name} includes a direct WhatsApp line, so your editor or manager can reach our team directly."),
        ],
    },
    {
        "service": "subscribers",
        "quantity": 100000,
        "slug": "youtube/subscribers/100000",
        "label": "{quantity} YouTube subscribers",
        "title": "Buy {quantity} YouTube Subscribers? It Takes Months | Growsterr",
        "description": "Want to buy YouTube subscribers, 100k of them? Real ones take many months, even on {pick_name}, and bought ones can cost you the Silver award.",
        "h1": ("Buy {quantity} YouTube subscribers? ", "A real 100k takes months. Here's how."),
        "intro": "Planning to buy {quantity} YouTube subscribers? You're probably thinking of the Silver Creator Award. Here's the honest picture: with real people it takes many months, often more than a year, even on {pick_name}, which typically brings {pick_audience} a month. And YouTube reviews a channel before sending the award, so a bought 100k can cost you the very thing you wanted.",
        "hero": {"image": "youtube-subscribers", "alt": "A YouTube creator's long climb toward one hundred thousand real subscribers"},
        "sections": [
            {
                "h2": "The Silver Creator Award is reviewed",
                "p": [
                    "YouTube reviews each channel before an award goes out, checking that it follows YouTube's rules, and fake engagement breaks them. Spam subscribers are also removed from counts along the way.",
                    "So if you buy YouTube subscribers to hit 100k, the count can stall at the very step you were buying it for.",
                ],
            },
            {
                "h2": "What a real 100k takes",
                "p": [
                    "Months of a package, and months of uploads. The table above gives {pick_name}'s usual span; at the slower end of its typical range, it's well beyond a year.",
                    "The campaign brings people; your videos keep them. As the channel grows, more of your new subscribers can come from YouTube recommending you, not only from us.",
                ],
            },
            {
                "h2": "Milestones on the way",
                "ul": [
                    "Every month: new subscribers in the {pick_audience} range on {pick_name}.",
                    "Halfway, at 50,000: a good moment to see which series brought the most people.",
                    "The last stretch: keep doing what got you there, because the channel doesn't stop at the award.",
                ],
            },
        ],
        "faqs": [
            ("Can I reach {quantity} within a year?", "Possibly, at the faster end of {pick_name}'s typical range and with uploads people share. At the slower end it takes longer, so plan for more than a year and treat anything sooner as a bonus."),
            ("Will bought subscribers stop me getting the award?", "They can. YouTube reviews channels before sending awards and removes spam subscribers, so a count built on bots may never reach the review, or fail it."),
            ("Is {pick_name} the only package that gets there?", "Every package gets there eventually; the table shows how long each one usually takes. For a goal this size, {starter_name}'s wait runs into years."),
            ("What about subscribers who leave?", "Over many months some people will unsubscribe, as they do on every channel. It's a trickle, not the sudden drops bought counts show when YouTube clears out spam."),
            ("Can you promise the Silver award?", "No. Only YouTube decides who gets it. We bring real subscribers, the only kind that can count toward it."),
        ],
    },
    # --- Views (no typical ratio: every page names its package) ---------------------------
    {
        "service": "views",
        "quantity": 50,
        "plan": "starter",
        "slug": "youtube/views/50",
        "label": "{quantity} YouTube views",
        "title": "Buy {quantity} YouTube Views? You Want {quantity} People, Not a Count | Growsterr",
        "description": "Want to buy {quantity} YouTube views? A pack that small for cents is bots, and YouTube can take them back. Real viewers find your channel by the thousand each month.",
        "h1": ("Buy {quantity} YouTube views? ", "What you want is {quantity} people."),
        "intro": "Wanting to buy {quantity} YouTube views usually means a new video nobody has seen yet. A pack of {quantity} views for small change is bots, and YouTube can remove views it decides aren't real, so the count may not even last. Our packages bring real people to your channel, far more than {quantity} a month: {pick_name} typically adds {pick_audience} new subscribers, each of them a viewer.",
        "hero": {"image": "youtube-viewers", "alt": "A handful of real people pressing play on a new creator's YouTube video"},
        "sections": [
            {
                "h2": "Why YouTube takes bought views back",
                "p": [
                    "YouTube checks views and filters out the ones it judges artificial, and it can lower a video's count after the fact. {quantity} views from a bot pack are exactly what that check exists for.",
                    "A count that goes up and then down is worse than one that never moved: it's the kind of wobble that viewers and YouTube both notice.",
                ],
            },
            {
                "h2": "How real viewers reach a new video",
                "p": [
                    "Name one video when you order, and new viewers go straight to it, subscribing to your channel before they watch. We don't count their views in advance, because each play is someone's choice, but every one of them is a person.",
                ],
            },
        ],
        "faqs": [
            ("Will my view count go up?", "Yes, as real people watch, but we don't put a number on it. We quote typical monthly ranges for subscribers, likes and comments, and those people watch along the way."),
            ("Why do views sometimes drop after a few days?", "Because YouTube keeps reviewing views after they're counted and removes the ones it judges artificial. Views from people who chose to watch aren't what that review is looking for."),
            ("Which package does this page suggest?", "{pick_name}, the smallest, at {pick_price} a month: typically {pick_audience} new subscribers and {pick_likes} likes, from people who watch what interests them."),
            ("Is {quantity} views a realistic goal for a first video?", "It's a modest one. Once the campaign starts, far more than {quantity} people a month discover your channel, so it's usually passed early on; we still never promise a count."),
            ("Can I see where the viewers come from?", "Your dashboard shows the visits and new subscribers we measured, day by day, and YouTube Studio shows your views and audience as usual."),
        ],
    },
    {
        "service": "views",
        "quantity": 100,
        "plan": "starter",
        "slug": "youtube/views/100",
        "label": "{quantity} YouTube views",
        "title": "Buy YouTube Views, {quantity} at a Time? Pick Who Watches | Growsterr",
        "description": "Want to buy YouTube views, {quantity} for a few cents? Those are bots from nowhere in particular. Real viewers come from the place you choose.",
        "h1": ("Buy YouTube views, {quantity} at a time? ", "Choose who watches instead."),
        "intro": "If you buy YouTube views in packs of {quantity}, you don't get to choose who watches, because nobody does. Packs of {quantity} for a few cents are bots, from nowhere in particular. Our packages bring real people from the city, region or country you choose, many more than {quantity} each month, and they watch the videos that interest them.",
        "hero": {"image": "youtube-viewers", "alt": "Viewers in one country watching a creator's video in their own language"},
        "sections": [
            {
                "h2": "YouTube Studio shows where viewers are",
                "p": [
                    "Your analytics break views down by country. A Spanish-language video with a burst of views from places where nobody speaks Spanish looks like what it is, to you and to YouTube.",
                    "Real viewers line up with your content: same language, same interests, the region you make videos for.",
                ],
            },
            {
                "h2": "Matching the location to the video",
                "ul": [
                    "Videos in one language: choose a country where it's spoken.",
                    "Local topics: name the city or region.",
                    "Music: pick the places your listeners are, or where you want them to be.",
                    "Not sure? Start with the country you live in and look at Studio after a month.",
                ],
            },
        ],
        "faqs": [
            ("Can I choose the country my viewers come from?", "Yes, choose a city, region or country at checkout. We aim there first; if the matching audience is bigger nearby, some viewers come from there."),
            ("Can I get exactly {quantity} views?", "No, and be wary of anyone who offers exact view counts: nobody can schedule a hundred real people to press play. We bring people; the views are theirs."),
            ("Do views from other countries hurt?", "Real viewers from anywhere are fine. What looks wrong is a pile of views from places unrelated to your video, all arriving at once."),
            ("Which videos will people watch?", "The ones that catch their interest. You can point new viewers at one video; they subscribe first and then watch it."),
            ("Which package fits {quantity} views?", "{pick_name}, the smallest. Views aren't counted in advance, but it typically brings {pick_audience} new subscribers a month, many more people than {quantity}."),
        ],
    },
    {
        "service": "views",
        "quantity": 500,
        "plan": "starter",
        "slug": "youtube/views/500",
        "label": "{quantity} YouTube views",
        "title": "Buy YouTube Views {quantity}? Get Your Project Seen | Growsterr",
        "description": "Want to buy YouTube views, {quantity} for a short film, demo or portfolio piece? Bots can't watch it. Real people can, far more than {quantity} of them a month.",
        "h1": ("Buy YouTube views, {quantity} for your project? ", "Get it seen by people."),
        "intro": "Short films, student projects, a band's first video, a portfolio piece: when the work matters, people look to buy YouTube views, {quantity} or so, to give it a start. A {quantity}-view pack for a few cents is bots, and they can't watch, react or remember it. Our packages bring real people to your channel, well beyond {quantity} a month, and they choose what to watch.",
        "hero": {"image": "youtube-channel", "alt": "A filmmaker uploading a finished short film to YouTube"},
        "sections": [
            {
                "h2": "A view count isn't an audience",
                "p": [
                    "If you're sending your link to a festival, a course or a client, the person reviewing it may glance at the view count, but the comments tell them more. Real viewers leave reactions that say the work landed; bots leave nothing.",
                ],
            },
            {
                "h2": "Make the channel worth subscribing to",
                "p": [
                    "One great video is a reason to watch; a few are a reason to subscribe. Put earlier work, a behind-the-scenes cut or a trailer on the channel so viewers who enjoy the project have somewhere to go.",
                    "Then name the project when you order: new viewers are sent to it, subscribing first and then watching. What they make of it is up to them.",
                ],
            },
        ],
        "faqs": [
            ("Will reviewers see real views?", "They'll see whatever YouTube shows: views, likes and comments from real people who chose to watch. Nothing about it needs explaining."),
            ("Can you promise {quantity} views on my project?", "No. Views aren't something we count ahead of time, and no single video gets a number. We bring real people to your channel, typically {pick_audience} new subscribers a month with {pick_name}, and they decide what to watch."),
            ("Is it fine to promote a student or personal project?", "Of course. Any public channel can run a campaign, and the people who find it are viewers like any others."),
            ("Will people comment on my work?", "Some will, in their own words, and that's often the most useful part: typically {pick_comments} comments a month with {pick_name}, from the same viewers."),
            ("Can I target the city where my film is set or screening?", "Yes, choose the city, region or country when you order, and your channel is shown to people there first."),
        ],
    },
    {
        "service": "views",
        "quantity": 1000,
        "plan": "starter",
        "slug": "youtube/views/1000",
        "label": "{quantity} YouTube views",
        "title": "Buy {quantity} YouTube Views Cheap? The Real Cost | Growsterr",
        "description": "Want to buy 1000 YouTube views cheap? Cheap views are plays nobody watched. Real viewers come inside a package: {pick_name}, {pick_price} a month.",
        "h1": ("Buy {quantity} YouTube views cheap? ", "Here's what cheap really costs."),
        "intro": "You can buy {quantity} YouTube views cheaply almost anywhere, and the price tells you what they are: plays generated without anyone watching. They can be filtered out, they don't count toward monetization, and they leave your other numbers flat. Real viewers cost more because they're people; ours come inside a package, starting at {pick_price} a month with {pick_name}.",
        "hero": {"image": "youtube-viewers", "alt": "Real viewers watching a YouTube video, each view belonging to a person"},
        "sections": [
            {
                "h2": "The hidden costs of a cheap thousand",
                "ul": [
                    "Filtered views: YouTube can remove plays it judges artificial, sometimes days later.",
                    "A lopsided video: a thousand views with almost no likes or comments looks bought.",
                    "Muddied analytics: Studio fills with viewers who don't exist, so you can't tell what's working.",
                    "Risk to the channel: YouTube's fake engagement policy covers bought views.",
                ],
            },
            {
                "h2": "Why we don't sell views by the thousand",
                "p": [
                    "Every view we bring is a person, and people can't be priced per play. So there's no view menu: a package brings real people to your channel every day, and they watch what interests them.",
                    "With {pick_name}, that's typically {pick_audience} new subscribers a month, and every one of them is a viewer too.",
                ],
            },
        ],
        "faqs": [
            ("Is there a cheaper package than {pick_name}?", "No, it's our smallest, at {pick_price} a month. You can cancel before the next renewal if one month is all you want."),
            ("Do cheap views count toward monetization?", "No. YouTube doesn't count artificial views toward its Partner Program, and we never promise monetization or watch hours either: real viewers watch, and YouTube decides the rest."),
            ("Will I pass {quantity} views?", "A package brings far more than {quantity} people to your channel in a typical month, and they watch what interests them. We still don't count views ahead of time or promise a number."),
            ("Can views be spread across several videos?", "Viewers spread themselves across the videos they like. On {rising_name} and {pro_name} you can also choose which videos get the attention."),
            ("What does a real view look like in Studio?", "A view with a viewer behind it: some time spent watching, sometimes a like or a comment, sometimes a new subscriber. In Studio those numbers move together."),
        ],
    },
    {
        "service": "views",
        "quantity": 5000,
        "plan": "rising",
        "slug": "youtube/views/5000",
        "label": "{quantity} YouTube views",
        "title": "Buy {quantity} YouTube Views? Grow the Whole Series | Growsterr",
        "description": "Want to buy 5000 YouTube views for a series? {pick_name} sends real people to the videos you choose. We don't count views; we bring people who watch.",
        "h1": ("Buy {quantity} YouTube views? ", "Grow the whole series, not one upload."),
        "intro": "When people want to buy {quantity} YouTube views, it's often for more than one video: a series, a season, a course. A bot pack can inflate a single upload; it can't make anyone watch episode two. {pick_name} brings real people to your channel daily and lets you choose which videos get the attention, so newcomers start where you want them to.",
        "hero": {"image": "youtube-channel", "alt": "A YouTube playlist of numbered episodes from one creator's series"},
        "sections": [
            {
                "h2": "Why {pick_name} suits a series",
                "p": [
                    "Views have no fixed ratio to anything we can quote, so we suggest the package by what the goal needs. For {quantity} views across several videos, the useful extra is choice: {pick_name} lets you decide which videos get the attention.",
                    "It also typically brings {pick_audience} new subscribers a month, the people who'll see the next episode.",
                ],
            },
            {
                "h2": "Building a series people binge",
                "ul": [
                    "Number episodes clearly in titles and thumbnails.",
                    "Put the series in a playlist, in order.",
                    "End each episode by pointing at the next.",
                    "Lead new viewers to episode one, not the latest.",
                ],
            },
        ],
        "faqs": [
            ("Can I split {quantity} views between videos?", "Views aren't something we split, because we don't count them. You choose which videos get the attention, and people watch what interests them from there."),
            ("Why not {starter_name}?", "It works too, and you can name one video on it. {pick_name} adds the choice of which videos get the attention and a bigger typical month, which suits a series."),
            ("Will people watch the whole series?", "Some will, some won't, and nobody can promise it. A clear playlist and good episode endings give them every reason to."),
            ("How do I see what viewers watch?", "YouTube Studio shows views for every video; our dashboard shows the visits and new subscribers the campaign brought."),
            ("Do campaign viewers count as normal views?", "They're real people pressing play, which is what a normal view is. We still never promise a count, watch time or monetization."),
        ],
    },
    {
        "service": "views",
        "quantity": 1000000,
        "plan": "pro",
        "slug": "youtube/views/1000000",
        "label": "{quantity} YouTube views",
        "title": "Buy 1 Million YouTube Views Cheap? What's Real | Growsterr",
        "description": "Want to buy 1 million YouTube views cheap? A cheap million is bots. A real one takes a channel, many months and real viewers. Here's where {pick_name} fits.",
        "h1": ("Buy 1 million YouTube views cheap? ", "A real million is built, not bought."),
        "intro": "An offer to buy YouTube views, 1 million of them, cheaply, is the clearest bot sale there is. No real crowd of a million people can be bought for pocket money, and YouTube removes artificial views. A real million comes from a channel people keep watching, over many months. {pick_name}, our biggest package, brings real people every day; we don't count views and won't promise a million.",
        "hero": {"image": "youtube-hub", "alt": "A YouTube channel whose library of videos has been watched by real viewers over years"},
        "sections": [
            {
                "h2": "Why a cheap million is always fake",
                "p": [
                    "A million real views means a very large number of people choosing to press play. Reaching that many people costs real money and takes time, so any offer that does it cheaply and quickly isn't reaching people at all.",
                    "What you'd get is a million plays and a video whose likes, comments and subscribers say otherwise. YouTube can strip the views, and the policy behind that can put the channel at risk.",
                ],
            },
            {
                "h2": "How real channels get to a million views",
                "p": [
                    "Real million-view totals are usually spread across a library: many videos, each watched by people who found one and stayed for more. Sometimes one video takes off, which no one can promise.",
                    "Our part is the steady base: real people discovering your channel every day, subscribing and watching. Your part is uploads they'll want to pass on.",
                ],
            },
            {
                "h2": "Months, honestly",
                "p": [
                    "We don't count views, so there's no pace chart for a million. What we can say: with {pick_name}, a month typically brings {pick_audience} new subscribers, and a million views needs many of them watching many videos. Plan in months and years, not days.",
                ],
            },
        ],
        "faqs": [
            ("Can you deliver 1 million views?", "No. We don't count views or promise a number, least of all a million. We bring real people to your channel; a million views is something a channel earns over time."),
            ("How long does a real million take?", "There's no honest single answer. It depends on how many videos you have, how often you upload and how much people share them. With a package running, plan in many months, not weeks."),
            ("Would a million bot views get my video removed?", "It can. Bought views fall under YouTube's fake engagement policy; videos can lose them, and repeat cases can lead to more serious action against the channel."),
            ("Why {pick_name} for a goal this size?", "Because a goal this large needs the most people every month: {pick_name} typically brings {pick_audience} new subscribers, with priority placement and a direct WhatsApp line to our team."),
            ("Can one video reach a million?", "It happens, but nobody can promise it, and we won't. Pick one video for new viewers to start with; they subscribe first and then watch, and the rest is up to them and to YouTube."),
        ],
    },
]
