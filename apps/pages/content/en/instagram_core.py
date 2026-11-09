"""English Instagram pages: comments, likes, and the ways people ask for followers and likes
(gradual, organic, local, private accounts...). Keys and placeholders: docs/CONTENT.md. Numbers
come from the packages ({starter_likes}...), so they follow apps/growth/plan.py."""

UPDATED = "2026-11-08"

PAGES = [
    # --- Comments -----------------------------------------------------------------------
    {
        "service": "comments",
        "slug": "instagram/comments",
        "label": "Instagram comments",
        "title": "Buy Instagram Comments Written by Real People | Growsterr",
        "description": "Want to buy Instagram comments? Ours come inside every monthly package, written by real people in their own words. Typically {starter_comments} a month.",
        "h1": ("Buy Instagram comments ", "from people who mean them."),
        "intro": "If you're here to buy Instagram comments, know that we only bring them one way: inside a monthly package, from real people who discover your posts and have something to say. Typically {starter_comments} comments a month with {starter_name}, {pick_comments} with {pick_name}.",
        "hero": {"image": "instagram-real-people", "alt": "People leaving their own comments, questions and emoji under an Instagram post"},
        "sections": [
            {
                "h2": "What a real comment section looks like",
                "p": [
                    "Real comments are uneven. One person asks where the jacket is from, another tags a friend, someone else writes two words and an emoji. That unevenness is what makes a comment section believable, and it's exactly what scripted comments can't fake.",
                    "Comments bought in bulk tend to arrive as near-identical lines from accounts with no posts of their own. Anyone scrolling can spot them, including the brands and collaborators you'd like to impress.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "A creator at a desk replying to comments on an Instagram post"},
            },
            {
                "h2": "How many comments each package brings",
                "ul": [
                    "{starter_name}, at {starter_price} a month, typically brings {starter_comments} comments, on the posts people enjoy most.",
                    "{rising_name}, at {rising_price}, typically brings {rising_comments}, and you pick the posts that get the attention.",
                    "{pro_name}, at {pro_price}, typically brings {pro_comments}, plus priority placement and a direct WhatsApp line.",
                ],
            },
            {
                "h2": "Why comments only come with a package",
                "p": [
                    "A post with forty comments and a dozen likes tells everyone what happened. Comments only look right next to the follows, likes and views that real attention brings, so we bring the attention and let the comments grow out of it.",
                ],
            },
        ],
        "faqs": [
            ("Can I get Instagram comments without a package?", "No. Comments come only inside our monthly packages, from people who found your profile through our campaigns. Nobody writes them to order, which is why they read like conversation."),
            ("Can I choose what the comments say?", "No. People write in their own words, so there's nothing for us to script, and comments written to a brief rarely read like anyone's real reaction. What you can choose instead, with {rising_name} or {pro_name}, is where the attention goes: the posts you pick."),
            ("When do the comments appear?", "Through the month, a few at a time, as people discover your posts. A hundred comments in ten minutes would be a script, not an audience."),
            ("Do comments help my posts reach more people?", "Comments show that people care about a post, and Instagram notices that. Real ones add to it. We can't promise reach, and nobody honest can, but scripted comments only add noise."),
            ("Do you need my password?", "No. We need your Instagram username and the place your audience should come from. Keep the account public so people can read your posts and join in."),
        ],
    },
    # --- Followers: the ways people ask for them ---------------------------------------
    {
        "service": "followers",
        "modifier": "gradual",
        "slug": "instagram/followers/gradual",
        "label": "Gradual Instagram followers",
        "title": "Buy Instagram Followers Daily, Never in a Batch | Growsterr",
        "description": "Buy Instagram followers daily, not in one drop: real people find your profile every day for 30 days, so growth is gradual by nature, never one sudden batch.",
        "h1": ("Buy Instagram followers daily, ", "the way people really follow."),
        "intro": "If you'd rather buy Instagram followers daily than all at once, you're already thinking like an audience. Our campaigns show your profile to real people every day for 30 days, so followers arrive gradually, day after day: typically {pick_audience} over the month with {pick_name}.",
        "hero": {"image": "instagram-followers-1000", "alt": "A follower count climbing a little each day across a month"},
        "sections": [
            {
                "h2": "Drip feed is a setting. Daily growth is a campaign.",
                "p": [
                    "Some services sell a slow drip: a batch of accounts released a few at a time so the curve looks natural. The accounts are still bots; only the timing is disguised.",
                    "Our pace isn't a setting at all. Your profile is shown to people every day, and each follow happens when someone decides it should. The gradual curve is simply what people choosing looks like from the outside.",
                ],
            },
            {
                "h2": "Why slowly beats all at once",
                "ul": [
                    "A steady rise looks like what it is: an account people keep discovering.",
                    "Each day's new followers meet your next post while their interest is fresh.",
                    "There's no sudden spike for a brand, or a follower, to question.",
                    "You can see what's working, because every day is its own data point.",
                ],
            },
            {
                "h2": "Reading your daily numbers",
                "p": [
                    "Your dashboard lists, for each day, how many people visited your profile through the campaign and how many of them followed. Some days are busier than others: a strong post, a weekend, a holiday. Over the month those days add up to a typical range, not a fixed daily quota.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "A creator checking a day-by-day chart of profile visits and new followers"},
            },
        ],
        "faqs": [
            ("How many followers will I get each day?", "There's no fixed daily number, because people decide for themselves. Across the month {pick_name} typically brings {pick_audience}, so an average day brings a slice of that, some days more, some less."),
            ("Can I set the drip speed myself?", "No, and you don't need to. The speed comes from people, not a dial: the campaign runs every day and follows arrive whenever someone chooses."),
            ("Is gradual growth less risky than a big batch?", "Hundreds of followers in an hour is a pattern bots leave. Gradual growth from real people doesn't leave that pattern, because it isn't one. We can't speak for how Instagram treats any account; we can only make sure every follower we bring is a person."),
            ("Does gradual mean less growth?", "No. Gradual describes the shape, not the total. The month's typical range is the same whether a person follows on day two or day twenty-nine; it simply arrives the way an audience builds."),
            ("Do likes and comments come gradually too?", "Yes. The same people like and comment as they find your posts, so both build alongside your followers. With {pick_name} that typically comes to {pick_likes} likes and {pick_comments} comments across the month."),
        ],
    },
    {
        "service": "followers",
        "modifier": "live",
        "slug": "instagram/followers/live",
        "label": "Instagram followers: delivery and Live",
        "title": "Instagram Followers With Fast Delivery, Explained | Growsterr",
        "description": "How fast is delivery when you buy Instagram followers from real people? The campaign starts quickly, grows every day and builds an audience for your Lives.",
        "h1": ("Buying Instagram followers with fast delivery? ", "Here's what fast means."),
        "intro": "Buying Instagram followers with fast delivery usually means one of two things: a counter that jumps in minutes, or a campaign that starts right away and keeps going. We only do the second. Your campaign starts quickly, real people arrive from the first days, and your dashboard shows what each day brought.",
        "hero": {"image": "instagram-creator-studio", "alt": "A creator getting ready to go live on Instagram from a desk setup"},
        "sections": [
            {
                "h2": "Fast where it counts, never instant",
                "p": [
                    "The fast part is the start. We set up your campaign soon after you order, and people begin seeing your profile from the first days. What we won't do is squeeze a month of real decisions into an hour, because the only way to do that is with accounts nobody runs.",
                    "So when you compare delivery times, look at when real growth begins and whether it keeps going, not at how quickly a number jumps.",
                ],
            },
            {
                "h2": "Followers for your Instagram Lives",
                "p": [
                    "Live followers are simply followers who show up when you go live. Instagram can let your followers know when a broadcast starts, so more people who chose to follow you means more people who might tap in.",
                    "We don't sell Live viewers, and nobody can promise a crowd at a set time: people join when they're interested and around. The followers you gain through the month are the ones most likely to.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Followers joining a creator's Instagram Live and commenting as it runs"},
            },
            {
                "h2": "Gradual delivery for likes, too",
                "p": [
                    "Likes keep the same rhythm. They come from the people who discover your profile, so they land on your posts slowly through the month, typically {pick_likes} with {pick_name}. There's no separate likes order to schedule and no burst to explain.",
                ],
            },
        ],
        "faqs": [
            ("How soon does delivery start?", "Quickly. Once your order is in, we set up the campaign and people start visiting your profile from the first days. Follows begin with those visits and continue all month."),
            ("Can I get instant delivery?", "No. Instant delivery only works with bots, because no person follows within seconds of a payment. We start fast and grow every day instead."),
            ("Will I have new followers before my Live tonight?", "Perhaps some, if your campaign is already running, but we can't time people to a broadcast. If a Live matters to you, start a few weeks ahead so your new followers have had time to get to know you."),
            ("Do you sell viewers for Instagram Live?", "No. Live viewers would have to be people watching at a given minute, which nobody can deliver honestly. The followers we bring may join your Lives on their own."),
            ("Where can I follow my delivery?", "In your dashboard, which counts the profile visits our campaign brought and the follows that came from them, day by day. Your account's own total also moves with your other growth and with unfollows."),
        ],
    },
    {
        "service": "followers",
        "modifier": "no-drop",
        "slug": "instagram/followers/no-drop",
        "label": "Instagram followers that stay",
        "title": "Permanent Instagram Followers? Why Real People Stay | Growsterr",
        "description": "Want to buy permanent Instagram followers that don't drop off? Bot accounts vanish in clean-ups. Real people stay, because following you was their own idea.",
        "h1": ("Permanent Instagram followers ", "start with real people."),
        "intro": "Anyone shopping to buy permanent Instagram followers has seen the other kind: a jump, then a slow leak back down. Followers fall off when they were never people to begin with. Ours are people who chose to follow you, so they stay the way any real audience stays, and when one leaves, it's for the reasons any follower leaves.",
        "hero": {"image": "instagram-followers", "alt": "An Instagram follower count holding steady and rising over several months"},
        "sections": [
            {
                "h2": "Why bought followers fall off",
                "p": [
                    "Instagram removes fake and spam accounts on a regular basis. When your followers are those accounts, every clean-up takes a bite out of your count. Refills top the number back up with more of the same, and the cycle starts again.",
                    "A person isn't removed in a clean-up. They only leave if they decide to unfollow, which happens far less often and is something your posts can influence.",
                ],
            },
            {
                "h2": "What keeps followers around",
                "ul": [
                    "They chose you, and a follow that starts with interest tends to last.",
                    "They come from where your audience lives, so your posts make sense to them.",
                    "They see your next posts, and each good one is a reason to stay.",
                    "Your rhythm matters more than anything we do: people stay for posts they look forward to.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Long-time followers still liking and commenting on a creator's newest post"},
            },
            {
                "h2": "No drop, honestly defined",
                "p": [
                    "We won't tell you nobody will ever unfollow, because that isn't how people work. We can tell you that you won't see the waves of losses fake accounts cause, and your dashboard shows the new followers our campaign brought, day by day, so you always know what came from us.",
                ],
            },
        ],
        "faqs": [
            ("Are your followers permanent?", "They're real people, so they stay as long as they want to. Nobody can promise a person will never unfollow; what we can say is that none of them is a fake account waiting to be deleted."),
            ("Do you offer refills if followers drop?", "No, because there's nothing to refill. Refills exist for followers who vanish in clean-ups. Ours are people, and the odd unfollow is part of any real audience."),
            ("Why do bought followers disappear?", "Usually they don't unfollow at all: the accounts get removed. Instagram deletes fake and spam profiles in waves, and the follower count drops with them."),
            ("What happens to my followers if I cancel?", "They stay. They followed because they wanted to, not because a subscription told them to. Cancelling only means we stop bringing new people once your paid month ends; the ones you've gained are still your followers."),
            ("How do I keep the followers I gain?", "Post regularly, answer comments, and give new followers a reason to come back in their first weeks. People stay for the same reasons they followed."),
        ],
    },
    {
        "service": "followers",
        "modifier": "organic",
        "slug": "instagram/followers/organic",
        "label": "Organic Instagram followers",
        "title": "Organic Instagram Followers: You Pay for Reach | Growsterr",
        "description": "Can you buy organic Instagram followers? You can pay to be seen by real people, every day, in the place you choose. Following stays their own decision.",
        "h1": ("Buy organic Instagram followers? ", "Pay for reach, let people choose."),
        "intro": "Strictly speaking, nobody can buy organic Instagram followers: a follow is organic because a person chose it. What you can buy is reach. Each day, real people in the place you pick come across your profile through our campaigns, and every follow that comes from it is a decision someone made on their own.",
        "hero": {"image": "instagram-real-people", "alt": "People coming across a creator's Instagram profile and choosing to follow"},
        "sections": [
            {
                "h2": "Where paid ends and organic begins",
                "p": [
                    "Our campaigns are promoted: we pay to put your profile in front of people in our partner network. That part is paid, and we say so. Everything after it isn't. Nobody is asked to follow, and nobody follows back as part of a trade.",
                    "It's the same deal as an ad or a feature on someone else's page: you pay for the introduction, and the audience decides.",
                ],
            },
            {
                "h2": "Organic followers, targeted to your audience",
                "p": [
                    "Organic growth works best when the people who see you are likely to care. Name the city, region or country where your audience lives, and that's where we show your profile first. A bakery in Lyon and a travel creator with readers across Europe need different people, and we aim accordingly.",
                ],
            },
            {
                "h2": "What organic rules out",
                "ul": [
                    "Follow-for-follow trades and engagement groups.",
                    "Bots and fake profiles, however slowly they're released.",
                    "Logins of any kind: your password stays with you.",
                    "Follower bursts faster than any real audience could manage.",
                ],
            },
        ],
        "faqs": [
            ("Are paid campaigns really organic?", "The reach is paid; the follow is not. Every new follower saw your profile and decided on their own, which is what makes a follower organic in the first place."),
            ("Will I get real Instagram followers every day?", "Yes. The campaign runs every day of the month and people follow as they discover you. Some days bring more than others; over the month it typically adds up to {pick_audience} with {pick_name}."),
            ("Is this the same as running Instagram ads myself?", "Similar in spirit, different in practice. We run the campaigns in our partner network, our team looks after them, and you see measured visits and new followers in a dashboard. You don't need an ad account or a budget to manage."),
            ("Does organic growth help my posts reach more people?", "More than bought numbers ever could, because organic followers actually see and react to what you post. How far a single post travels still depends on the post."),
            ("Is organic growth slower?", "It's steadier. A month of organic growth arrives day by day instead of in an hour, and it isn't followed by the drop that bot bursts bring."),
        ],
    },
    {
        "service": "followers",
        "modifier": "private-account",
        "slug": "instagram/followers/private-account",
        "label": "Instagram followers for a private account",
        "title": "Getting Instagram Followers on a Private Account | Growsterr",
        "description": "Can you buy Instagram followers on a private account? People can only send follow requests there, so we ask for a public profile while your campaign runs.",
        "h1": ("Followers on a private Instagram account? ", "Go public while you grow."),
        "intro": "If you want to buy or get Instagram followers on a private account, here's the honest catch: people can't follow a private account, they can only ask to. That's why we ask you to keep your profile public while your campaign runs. You still decide what's on it, and we never need your password.",
        "hero": {"image": "instagram-followers", "alt": "A private Instagram profile with a lock icon next to the same profile set to public"},
        "sections": [
            {
                "h2": "What a private account does to a campaign",
                "p": [
                    "When someone finds a private profile, they see a name, a bio and a lock. They can request to follow, but they can't see a single post, so most people move on. The few who do request then wait for you to approve them, one by one.",
                    "A campaign that sends people to that locked door wastes most of its reach. On a public profile, the same people can scroll your posts, make up their minds and follow straight away.",
                ],
            },
            {
                "h2": "If a service says private accounts are no problem",
                "p": [
                    "A follower count can only rise on a private account when requests are approved. If someone promises followers there without you approving anyone, they'd have to do the approving themselves, from inside your account. Handing over your password for that is the one thing you should never do.",
                ],
            },
            {
                "h2": "Going public without giving up control",
                "ul": [
                    "Switch to public for the campaign and back to private whenever you like.",
                    "Archive posts you'd rather keep to yourself; nothing is deleted.",
                    "Share personal stories with Close Friends instead of everyone.",
                    "Anyone who follows while you're public stays a follower if you go private again.",
                ],
            },
        ],
        "faqs": [
            ("Can you grow a private Instagram account?", "Only a little, so we don't try. People can request to follow, but they can't see your posts, so few do. Keep the account public while the campaign runs and it can do its job."),
            ("Will I lose followers if I go private again?", "No. People who already follow you stay when you switch to private. New visitors would have to send a request, so growth slows while the account is private."),
            ("Do I have to approve follow requests?", "Not while your account is public: people follow directly. If you switch to private mid-month, new requests wait for you, and the campaign brings far fewer followers."),
            ("Do you need access to my account to grow it?", "No. Your login stays yours; we only need your username, plus a public profile for the people we send to look at."),
            ("Do likes work on a private account?", "Only from people who already follow you, because nobody else can see the posts. One more reason the campaign needs the profile public."),
        ],
    },
    {
        "service": "followers",
        "modifier": "real",
        "slug": "instagram/followers/real",
        "label": "Active Instagram followers",
        "title": "Buy Active Instagram Followers Who Like and Comment | Growsterr",
        "description": "Active Instagram followers are people who like, comment and watch. Ours bring likes and comments from the same accounts: typically {pick_likes} likes a month.",
        "h1": ("Buy active Instagram followers ", "who actually interact."),
        "intro": "When people buy Instagram followers that are active, they mean followers who like, comment and watch, not a number that sits still. That only happens with real people, so that's all we bring: people who discover your profile, choose to follow, and react to the posts they enjoy.",
        "hero": {"image": "instagram-real-people", "alt": "New Instagram followers liking a post and starting a conversation in the comments"},
        "sections": [
            {
                "h2": "Looking real versus being real",
                "p": [
                    "Some followers are built to look real: a borrowed photo, a few posts, a plausible name. They pass a quick glance and fail everything else. They never like your new post, never watch a Reel to the end, never ask a question in the comments.",
                    "High quality, in the only sense that matters, means a person who might do those things. Profile pictures and bios are cosmetics; interaction is the test.",
                ],
            },
            {
                "h2": "Activity arrives with the followers",
                "p": [
                    "Because our followers are people, activity comes with them, from the same accounts. With {pick_name}, a typical month brings {pick_audience} new followers along with {pick_likes} likes and {pick_comments} comments.",
                ],
            },
            {
                "h2": "How to check whether followers are active",
                "ul": [
                    "Compare likes to followers on your last few posts: real growth moves both.",
                    "Read the comments: real ones mention the post, bot ones could sit under anything.",
                    "Open a handful of new followers' profiles: real people's are uneven and specific.",
                    "Watch the total over a few weeks: active followers don't vanish in waves.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "A creator comparing likes and comments across recent Instagram posts"},
            },
        ],
        "faqs": [
            ("What makes a follower active?", "A person who sees your posts and sometimes reacts: a like, a comment, a watched Reel, a share. Nobody reacts to every post, and that's normal."),
            ("Will my new followers like my posts?", "Many will. Likes come from the same people who follow, and with {pick_name} they typically add up to {pick_likes} a month. People like what they enjoy, so your best posts collect the most."),
            ("Are these good quality followers?", "They're people who decided to follow you, from the place you named. We don't grade followers by how polished their profiles look; we care that someone is behind each one."),
            ("Do the followers look real?", "They are real, so they look like ordinary Instagram users: their own photos, friends and habits. Some profiles are busy and some are quiet, as in any audience."),
            ("Is Growsterr a real website or a reseller?", "We're a growth agency, part of Sterr Agency (Sterr Technologies OÜ, Tallinn, Estonia), and a team runs every campaign. We bring people to your profile; we don't resell follower stock."),
        ],
    },
    {
        "service": "followers",
        "modifier": "safe",
        "slug": "instagram/followers/safe",
        "label": "Safe, legit Instagram followers",
        "title": "Buy Instagram Followers From a Legit Website | Growsterr",
        "description": "Looking for a legit website to buy Instagram followers? Who we are, how you pay, what we never ask for, and the checks to run on any growth service.",
        "h1": ("Buy Instagram followers from a legit website: ", "here's how to tell."),
        "intro": "Before you buy Instagram followers from a website that calls itself legit, it's fair to ask who's behind it and what could go wrong. Here's our side, plainly: who we are, how payment works, what we do with your account (nothing), and the checks we'd run on any growth service, us included.",
        "hero": {"image": "instagram-hub", "alt": "An Instagram creator looking over a growth service's details before signing up"},
        "sections": [
            {
                "h2": "Who you're paying",
                "p": [
                    "Growsterr is a product of Sterr Agency, run by Sterr Technologies OÜ, a company registered in Tallinn, Estonia, with headquarters in Turkey. You pay by card through Stripe's checkout, or with Apple Pay or Google Pay where your device supports them, and your card details go to Stripe, not to us.",
                    "It's a monthly subscription. You can cancel it yourself whenever you like, and the campaign carries on until the paid month is over.",
                ],
            },
            {
                "h2": "What we do with your account: nothing",
                "p": [
                    "We never log in, never post, never follow anyone in your name and never touch a setting. The campaign happens outside your account: people see your profile in our partner network and visit it the way they'd visit any profile someone recommended.",
                ],
            },
            {
                "h2": "Five checks for any growth service",
                "ul": [
                    "Does it ask for your password? A legitimate service never needs it.",
                    "Does it promise thousands of followers in minutes? That speed only comes from bots.",
                    "Are the numbers ranges or promises? People can't be counted in advance.",
                    "Can you cancel on your own, without writing to anyone?",
                    "Is there a company name and a country behind the website?",
                ],
            },
        ],
        "faqs": [
            ("Is Growsterr legitimate?", "Yes. We're a registered company, payment runs only through Stripe, and every campaign is run by a team and measured in your dashboard. You can stop any time from your account."),
            ("Is it safe for my Instagram account?", "We can't speak for Instagram, and nobody honest can promise how it treats an account. What we can say is that we don't do the things that put accounts at risk: no logins, no bots, no bursts of followers."),
            ("What do you need from me?", "Your Instagram username, where your new followers should be from, and a public profile. That's the whole list."),
            ("Can I trust the numbers you show?", "They're measured, not estimated: your dashboard shows the visits our campaign brought and the new followers among them, day by day. Before you order, we quote typical ranges, never promises, because people decide for themselves."),
            ("Will I be charged after cancelling?", "No. Cancelling stops the subscription from renewing. You keep the month you've paid for, and nothing is charged after it."),
        ],
    },
    {
        "service": "followers",
        "modifier": "targeted",
        "slug": "instagram/followers/targeted",
        "label": "Local, targeted Instagram followers",
        "title": "Buy Local Instagram Followers, Targeted by Place | Growsterr",
        "description": "Buy local Instagram followers from the city, region or country you name: real people who live where your customers do, every day of the month.",
        "h1": ("Buy local Instagram followers ", "from the place you name."),
        "intro": "A café in Manchester gains little from followers on the other side of the world. When you buy local Instagram followers, the place is the whole point, so it's the first thing we ask: which city, region or country should your new followers come from? Then we aim your campaign at the people who live there.",
        "hero": {"image": "instagram-followers", "alt": "New followers from the same city appearing on a local business's Instagram profile"},
        "sections": [
            {
                "h2": "Why local matters more than the total",
                "p": [
                    "For a shop, a studio, a restaurant or a creator who meets people in person, a follower who can actually visit is worth several who can't. Local followers can walk in, tell a friend and recognise the street you filmed on.",
                    "It also keeps your audience coherent. When most of your followers share a place and a language, more of them understand each post.",
                ],
            },
            {
                "h2": "How place targeting works",
                "ul": [
                    "You name a city, a region or a whole country when you order.",
                    "We show your profile to people there first, every day of the month.",
                    "If the matching audience there is small, some followers may come from nearby rather than from somewhere unrelated.",
                    "Your content does the rest: people follow when your posts speak to them.",
                ],
            },
            {
                "h2": "Followers from the country you serve",
                "p": [
                    "Followers from a country you never post for don't help you, wherever that country is. If your customers are in Canada, we look for people in Canada; if they're in Istanbul alone, say so, and we start there.",
                ],
            },
        ],
        "faqs": [
            ("Can I choose a city, not just a country?", "Yes. A city, a region or a whole country all work. A city gives the tightest audience; a region or a country gives the campaign more people to reach."),
            ("Can I avoid followers from India or another country I don't serve?", "Yes. You choose where your followers come from, and we target that place. There's nothing wrong with followers from any country; the question is whether they're your audience. If your customers are in Germany, we look for people in Germany."),
            ("Will every follower be from my city?", "We show your profile there first. When the closely matching audience is larger in the surrounding area, some followers may come from there, so think of it as aimed at your city rather than fenced in."),
            ("Does local targeting cost extra?", "No. Every package includes it, from {starter_name} at {starter_price} a month."),
            ("Can I target by age or interests?", "We target by place only. Within that place, your content decides who follows, because people follow what interests them."),
            ("Does local targeting suit an online business?", "Yes, if your audience lives somewhere in particular: a language area, a country, a market you're entering. If your buyers are spread across a whole country, name the country."),
        ],
    },
    {
        "service": "followers",
        "modifier": "viral",
        "slug": "instagram/followers/viral",
        "label": "Instagram followers for going viral",
        "title": "Viral Instagram Followers? What Actually Helps | Growsterr",
        "description": "Can you buy Instagram followers to go viral? Nobody can promise virality. Real followers give every post more people who might share it, month after month.",
        "h1": ("Buy Instagram followers to go viral? ", "Grow the people who share."),
        "intro": "Nobody can sell you a viral post, whatever their page says. What makes a post spread is people: they watch, send it to a friend, save it, and Instagram shows it to more people like them. If going viral is why you'd buy Instagram followers, buy the part that can help: more real people who see your next post first.",
        "hero": {"image": "instagram-followers-1000", "alt": "A creator's follower line jumping after a popular Reel, then holding steady"},
        "sections": [
            {
                "h2": "Why a big number doesn't make a post spread",
                "p": [
                    "A post travels when the people who see it first react to it. Thousands of followers who never react give it a worse start than a few hundred who do, because Instagram sees a post its first audience ignored.",
                ],
            },
            {
                "h2": "What real followers give a viral moment",
                "ul": [
                    "More first viewers for each post: the people who decide whether it travels.",
                    "Shares and saves, which only people can give.",
                    "A profile worth following when a post does take off, so the moment leaves something behind.",
                ],
                "image": {"image": "instagram-real-people", "alt": "People sharing a creator's Instagram post with friends in their messages"},
            },
            {
                "h2": "The honest odds",
                "p": [
                    "Most posts don't go viral, ours or anyone's. Steady growth makes the posts that could take off more likely to, and makes the ones that don't still worth posting. That's the trade we offer: no promise of a moment, a better starting position for every post.",
                ],
            },
        ],
        "faqs": [
            ("Can you make my post go viral?", "No, and be careful with anyone who says they can. Virality depends on the post, the timing and the choices of thousands of people. What we can do is bring fresh, real viewers to your profile daily, which gives each post a better start."),
            ("Do viral posts bring followers?", "Often, if the profile behind the post gives people a reason to stay. That's why we grow the profile rather than a single post: when something takes off, newcomers find an active audience and a body of work."),
            ("Does buying followers help the algorithm?", "Bought bots work against you there, because they make every post look ignored. Real followers who react help each post start better. Neither is a switch you can flip."),
            ("Which package suits a post I think could take off?", "{rising_name} or {pro_name}. Both let you name the posts that should get more eyes, so more real people see the one you believe in. {pro_name} adds priority placement."),
            ("How soon would I notice a difference?", "Your campaign starts quickly and new followers arrive from the first days. Whether a post takes off is never on a schedule; your growth is."),
        ],
    },
    # --- Likes ----------------------------------------------------------------------------
    {
        "service": "likes",
        "slug": "instagram/likes",
        "label": "Instagram likes",
        "title": "Instagram Likes on Your Posts, From Real People | Growsterr",
        "description": "Instagram likes from people who saw your post and enjoyed it, inside every monthly package: typically {starter_likes} a month with {starter_name}.",
        "h1": ("Instagram likes ", "from people who enjoyed the post."),
        "intro": "Want to buy Instagram likes for your posts? With us they're never sold by themselves. Each package sends real people to your profile, and they like the posts they enjoy: {starter_name} typically brings {starter_likes} likes a month, {pick_name} {pick_likes}, together with new followers and comments.",
        "hero": {"image": "instagram-hub", "alt": "Likes from real people gathering on a grid of Instagram posts"},
        "sections": [
            {
                "h2": "A like is where it starts",
                "p": [
                    "On Instagram, a like is often the first of several things a person does: they open your profile, look at a few more posts, follow, come back next week. Likes bought on their own stop at step one, and a post with plenty of likes and nothing else around it reads exactly that way.",
                    "Ours come from people who are on that path. That's why they arrive together with follows and comments instead of by themselves.",
                ],
                "image": {"image": "instagram-real-people", "alt": "A person liking an Instagram post, then opening the creator's profile"},
            },
            {
                "h2": "Likes on the posts you choose",
                "p": [
                    "With {starter_name}, likes land wherever people enjoy them most, usually your newest posts. {rising_name} and {pro_name} let you choose which posts get the attention, useful for a launch, a collaboration or a post you want seen.",
                ],
            },
            {
                "h2": "Choosing where to buy Instagram likes online in 2026",
                "ul": [
                    "No app to install and no login to share: a site that wants either is asking for the wrong kind of access.",
                    "Likes that arrive with views and follows, not ahead of them.",
                    "Typical ranges instead of exact counts, because people decide.",
                    "A company you can name and a checkout you recognise: ours is Sterr Technologies OÜ, taking cards through Stripe.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy likes for a single post?", "Not as a one-off order. Likes come inside a monthly package, from people who discover your profile. With {rising_name} or {pro_name} you can point that attention at the posts you choose."),
            ("Is there an app for Instagram likes?", "We don't have one, and you don't need one. You order on the website, pay through Stripe and follow your campaign from your account on any device. We never need your Instagram login."),
            ("How many likes does each package bring?", "Typically {starter_likes} a month with {starter_name}, {rising_likes} with {rising_name} and {pro_likes} with {pro_name}. Ranges, not counts: each like is a person's choice."),
            ("When do the likes start?", "As soon as your campaign is running and the first people reach your profile, usually within the first days. They keep coming through the month, never in one burst."),
            ("Do likes still matter now that counts can be hidden?", "Instagram lets people hide like counts, so the number on screen matters less than it once did. What still matters is that people engage with your posts, and that's what real likes reflect."),
        ],
    },
    {
        "service": "likes",
        "modifier": "comment-likes",
        "slug": "instagram/likes/comment-likes",
        "label": "Likes on Instagram comments",
        "title": "Buy Instagram Likes for Comments? Here's What Works | Growsterr",
        "description": "Want to buy Instagram likes for comments? We don't sell comment likes. People who reach your posts read the thread and like the replies they agree with.",
        "h1": ("Likes on Instagram comments ", "come from people reading the thread."),
        "intro": "People buy Instagram likes for comments for two reasons: to push a comment up someone else's post, or to make their own comment section look busier. We don't sell either. We bring real people to your profile, and the ones who read your comments can like the replies they agree with, on their own.",
        "hero": {"image": "instagram-real-people", "alt": "A busy comment thread under an Instagram post, with likes on the best replies"},
        "sections": [
            {
                "h2": "Comments on other people's posts",
                "p": [
                    "A well-liked comment near the top of a big account's post can send visitors your way, which is why people look for comment likes. We don't run campaigns on other people's posts. Our work happens on your own profile: we show it to real people, and they decide what to do there.",
                ],
            },
            {
                "h2": "Comment likes on your own posts",
                "p": [
                    "On your posts, comment likes happen naturally once there's a conversation. People who arrive through your campaign read the comments, reply to some and like the ones they agree with, yours included. We don't count those likes or forecast them, because nobody can predict which reply a person will like.",
                    "What we do count: with {pick_name}, a month typically brings {pick_likes} likes on your posts and {pick_comments} comments.",
                ],
            },
            {
                "h2": "Three ways to earn more likes on your replies",
                "ul": [
                    "Answer the first comments quickly, while people are still on the post.",
                    "Reply with something worth reading: a tip, a detail, a question back.",
                    "Pin a comment that starts the conversation you want.",
                ],
            },
        ],
        "faqs": [
            ("Do you sell likes on Instagram comments?", "No. Comment likes, like every other like, come only from people who choose to give them. Our packages bring those people to your posts; what they like in the thread is up to them."),
            ("Can you push my comment to the top of another account's post?", "No. We only grow your own profile, and we don't send likes to comments anywhere else."),
            ("Will my comment section get busier?", "Usually, because more people see your posts. Typically {pick_comments} comments a month come with {pick_name}, and comments tend to draw replies and likes of their own."),
            ("Are comment likes part of the package numbers?", "No. Our typical ranges count likes on your posts. Likes on individual comments come on top of that whenever people give them."),
            ("Will you log in to my account?", "No. Nobody on our side touches your account, and your password never leaves you. Everything that happens on your posts is done by people, from their own accounts."),
        ],
    },
    {
        "service": "likes",
        "modifier": "gradual",
        "slug": "instagram/likes/gradual",
        "label": "Slow, gradual Instagram likes",
        "title": "Slow Instagram Likes That Build Over Days | Growsterr",
        "description": "Want to buy Instagram likes slow, not in one spike? Ours come from real people finding your posts across the month, so likes build the way they naturally do.",
        "h1": ("Slow Instagram likes, ", "because people take their time."),
        "intro": "If you're looking to buy Instagram likes slow, you already know that hundreds of likes in two minutes looks wrong. Slow is right, but speed is only half of it. Our likes arrive gradually because they come from real people who find your posts over days and weeks, not from a queue set to a timer.",
        "hero": {"image": "instagram-followers-1000", "alt": "Likes on an Instagram post building gently over several days"},
        "sections": [
            {
                "h2": "How likes build on a real post",
                "p": [
                    "A post picks up likes in a curve: a first wave from people who see it soon after you share it, then a long tail as it's found on your profile, through a hashtag or in a friend's messages. That tail can go on for weeks.",
                    "Our campaigns add people to every part of that curve. They visit your profile across the month, scroll your posts and like what they enjoy, so older posts gain likes too, not just the newest one.",
                ],
            },
            {
                "h2": "Why a timer isn't the same as time",
                "p": [
                    "Slow-release likes from bots solve the wrong problem. The spike is gone, but the accounts behind the likes still never watch, follow or comment, and likes without the views, follows or comments around them look just as odd at a slow pace.",
                ],
            },
            {
                "h2": "When slow isn't what you want",
                "p": [
                    "If you need a wall of likes on a post within the hour, we're the wrong service, and we'd rather say so now. If you want every post to keep gathering likes from people who care, that's exactly what we're built for.",
                ],
            },
        ],
        "faqs": [
            ("How slowly do the likes arrive?", "At the speed people find your posts: some in the first days of your campaign, more across the weeks after. There's no timer and no batch, so no two days look the same."),
            ("Can I choose the speed of the likes?", "No, and that's deliberate. The pace comes from people visiting your profile. What you can choose, with {rising_name} or {pro_name}, is which posts get the attention."),
            ("Will older posts get likes too?", "Often, yes. People who discover your profile scroll back and like what they enjoy, so likes spread across your feed rather than piling onto one post."),
            ("Do slow likes look more natural?", "Slow only looks natural when people are behind it. Ours do because they are: each like comes with a person who may follow or comment as well."),
            ("How many likes come in a month?", "With {pick_name}, typically {pick_likes} over 30 days. That's a range, not a quota, because people like at their own pace."),
        ],
    },
    {
        "service": "likes",
        "modifier": "monthly",
        "slug": "instagram/likes/monthly",
        "label": "Monthly Instagram likes",
        "title": "Monthly Instagram Likes Without Ordering Per Post | Growsterr",
        "description": "Buy Instagram likes monthly instead of post by post: one subscription, real people, likes on your posts all month. Renews automatically, cancel any time.",
        "h1": ("Automatic monthly Instagram likes, ", "from people, not a script."),
        "intro": "If you want to buy automatic Instagram likes monthly, you probably want to stop thinking about likes one post at a time. That's what a package does. You subscribe once, we run your campaign every day, and real people like the posts they enjoy all month: typically {pick_likes} likes with {pick_name}. It renews monthly until you cancel.",
        "hero": {"image": "instagram-creator-studio", "alt": "A creator planning a month of Instagram posts on a wall calendar"},
        "sections": [
            {
                "h2": "Automatic, but not automated",
                "p": [
                    "Auto-likes usually means software that spots each new post and fires a set number of likes at it within minutes. It's automatic, and every one of those likes comes from an account nobody is using.",
                    "Ours are automatic in a different sense: you don't have to do anything per post. The campaign keeps running, people keep discovering your profile, and the likes they leave are their own.",
                ],
            },
            {
                "h2": "What a monthly package changes",
                "ul": [
                    "One price a month, {pick_price} for {pick_name}, instead of an order for every post.",
                    "No counts to set and no timing to schedule.",
                    "Likes on new and older posts alike, as people find them.",
                    "A month of likes is a month of feedback: you see which posts people actually enjoy.",
                    "You can stop whenever you like, with no notice period.",
                ],
            },
        ],
        "faqs": [
            ("Do new posts get likes automatically?", "People decide, so there's no fixed number per post. New posts are usually where people start, and with {rising_name} or {pro_name} you can tell us which posts should get the attention."),
            ("Does the subscription renew automatically?", "Yes. Stripe renews it each month on the payment method you chose. Cancelling takes a moment in your account, and the month you've paid for still runs to its end."),
            ("How many posts do I need?", "There's no minimum, but likes come from people browsing your profile, so a few recent posts give them something to enjoy. Posting through the month gives each new visitor more to like."),
            ("Can I change package from one month to the next?", "Yes. Start with the package that fits today and move up when your posts are ready for more people."),
            ("Is this the same as auto-likes software?", "No. Software that likes every post on a timer uses accounts with nobody behind them. Our likes come from people who visited your profile and enjoyed a post."),
        ],
    },
    {
        "service": "likes",
        "modifier": "no-drop",
        "slug": "instagram/likes/no-drop",
        "label": "Instagram likes that stay",
        "title": "Instagram Likes That Stay on Your Posts | Growsterr",
        "description": "Want to buy Instagram likes that stay? Likes vanish when the accounts behind them are removed. Ours come from real people, so they stay unless a person unlikes.",
        "h1": ("Instagram likes that stay, ", "because a person gave them."),
        "intro": "Likes disappear for one main reason: the accounts that gave them get removed. If you want to buy Instagram likes that stay, the lasting kind comes from people. Ours do, so a like on your post stays there unless the person who gave it changes their mind.",
        "hero": {"image": "instagram-hub", "alt": "An Instagram post whose likes hold steady weeks after it was shared"},
        "sections": [
            {
                "h2": "Where disappearing likes go",
                "p": [
                    "A like belongs to the account that gave it. When Instagram removes fake or spam accounts, every like they left goes with them, often weeks after the order. A post can lose a large share of its likes overnight, and anyone who looked before can see the gap.",
                ],
            },
            {
                "h2": "Why likes from people hold",
                "p": [
                    "A person's account isn't swept up in a clean-up. Their like stays on your post for as long as they leave it there, and people rarely go back to unlike something they enjoyed.",
                    "Real likes also keep coming. Older posts pick up new likes as more people find your profile, so a post's count can keep climbing long after you shared it.",
                ],
                "image": {"image": "instagram-real-people", "alt": "New visitors liking an older Instagram post weeks after it went up"},
            },
        ],
        "faqs": [
            ("Will the likes ever drop?", "Not the way bought likes do. Each like is from a person's own account, so one only goes if that person unlikes the post or closes their account, which is rare and happens one at a time."),
            ("Is there a refill period?", "There's no refill period because there's no expected drop. Refills fix a problem we don't create."),
            ("Do likes on Reels stay too?", "Yes. A like stays on any post, photo, carousel or Reel, as long as the account that gave it is still there."),
            ("How can I tell if earlier likes came from bots?", "Look for sudden drops after a clean-up, likes far above your views, and likers whose profiles have no posts of their own. Likes from people rarely show any of these."),
            ("How many likes does a package bring?", "{pick_name} typically brings {pick_likes} a month, spread over the posts people enjoy. They stay, and next month's likes add to them."),
        ],
    },
    {
        "service": "likes",
        "modifier": "organic",
        "slug": "instagram/likes/organic",
        "label": "Organic Instagram likes",
        "title": "Organic Instagram Likes From People Who Found You | Growsterr",
        "description": "Buy organic Instagram likes and get honest feedback: real people see your posts through our campaigns and like only what they enjoy, post by post.",
        "h1": ("Organic Instagram likes, ", "and what they tell you."),
        "intro": "When you buy Instagram likes that are organic, you get something bought likes can't give: honest feedback. Our campaigns put your posts in front of real people, and they like only what they enjoy. Some posts will gather far more than others, and that difference tells you what your audience wants.",
        "hero": {"image": "instagram-real-people", "alt": "People reacting differently to a row of Instagram posts, liking some more than others"},
        "sections": [
            {
                "h2": "Uneven likes are a good sign",
                "p": [
                    "Bought likes are suspiciously even: every post gets roughly the same number, whatever it is. Organic likes vary. A strong Reel pulls ahead, a quiet photo trails behind, and the pattern looks like an audience with opinions, because it is one.",
                ],
            },
            {
                "h2": "Using your likes to post better",
                "ul": [
                    "Compare your three best posts of the month: what do they share?",
                    "Notice which format people like most: Reels, carousels or photos.",
                    "Post more of what works, then see whether the likes follow.",
                    "With {rising_name} or {pro_name}, put extra attention on a post that tests a new idea.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "A creator sorting last month's Instagram posts by how many likes each received"},
            },
            {
                "h2": "How organic likes reach your posts",
                "p": [
                    "We show your profile to people in our partner network, in the city, region or country you choose. They browse, follow if they want to, and like the posts that catch them. Nobody is asked to like anything.",
                ],
            },
        ],
        "faqs": [
            ("Does paying for reach make the likes inorganic?", "No. Paying to be seen is how every ad and promoted post works. The like itself is still someone's own reaction to your post."),
            ("Will every post get likes?", "Most posts people enjoy will, but not equally, and that's the point. Your best posts will usually gather the most."),
            ("How many organic likes can I expect?", "A typical month with {pick_name} brings {pick_likes}. The total is a range; how it splits between posts is up to the people who see them."),
            ("Do organic likes come with followers?", "Yes. The people who like your posts often follow too: typically {pick_audience} new followers a month with {pick_name}, and some leave comments."),
            ("Why is that better than a fixed number per post?", "Because a fixed number tells you nothing. Organic likes rise and fall with each post, so they show you what's landing and what isn't."),
        ],
    },
    {
        "service": "likes",
        "modifier": "private-account",
        "slug": "instagram/likes/private-account",
        "label": "Instagram likes on a private account",
        "title": "Buy Instagram Likes on a Private Account? | Growsterr",
        "description": "Can you buy Instagram likes on a private account? Only approved followers can see its posts, so nobody new can like them. Here's what works instead.",
        "h1": ("Likes on a private Instagram account ", "can only come from followers."),
        "intro": "Before you buy Instagram likes for a private account, know the limit: on a private profile, only approved followers can see your posts, so only they can like them. Anyone a campaign brings to your profile would meet a lock. So while your campaign runs, the profile needs to be public, and there are good ways to stay private where it matters.",
        "hero": {"image": "instagram-hub", "alt": "An Instagram post that only approved followers can see and like"},
        "sections": [
            {
                "h2": "Who can like a post on a private account",
                "p": [
                    "Only the people you've approved. Everyone else sees your name, bio and follower count, but not a single post, so there's nothing for them to like. A service promising likes there would need its accounts approved as your followers first, by you or by someone logged in as you.",
                ],
            },
            {
                "h2": "Keeping things private, the practical way",
                "ul": [
                    "Run a second, public account for your work and keep your personal one private.",
                    "Hide the like count on any post if you'd rather the number stay out of view.",
                    "Turn off comments on posts you want to share without a conversation.",
                ],
            },
            {
                "h2": "What changes once the profile is public",
                "p": [
                    "People can see your posts and like the ones they enjoy; with {pick_name}, that's typically {pick_likes} likes over a month, together with new followers and comments. You still decide what you post and who you talk to.",
                ],
            },
        ],
        "faqs": [
            ("Can people who don't follow me like posts on a private account?", "No. Instagram only shows a private account's posts to approved followers, so nobody else can like them."),
            ("Do I have to stay public after the campaign?", "No, that's your choice, and likes already on your posts stay. While the account is private, though, new people can't see your posts, so a running campaign can't bring you likes."),
            ("Can I grow a separate public account instead?", "Yes. One public account for your work and one private account for friends works well. We'd grow the public one."),
            ("Will you need access to approve requests?", "No. Your password stays with you, and we never sign in to your account. On a public profile there's nothing to approve: people follow and like directly."),
            ("Can I hide my like counts and still grow?", "Yes. Hiding the count only changes what visitors see on that post. People can still like it, and you still see the number yourself."),
        ],
    },
    {
        "service": "likes",
        "modifier": "real",
        "slug": "instagram/likes/real",
        "label": "Real Instagram likes",
        "title": "Real Instagram Likes: Genuine People, No Bots | Growsterr",
        "description": "Real Instagram likes from genuine people with their own accounts, never bots. They arrive with followers and comments from the same people, in every package.",
        "h1": ("Real Instagram likes, ", "each one from a person who meant it."),
        "intro": "Want to buy real Instagram likes? A real like comes from someone who looked at your post and liked what they saw. That's the only kind we bring. Every package shows your profile to people, and the likes they leave sit alongside follows, comments and views from the same accounts, so your engagement looks realistic because it is.",
        "hero": {"image": "instagram-real-people", "alt": "Different people, each with their own profile, liking the same Instagram post"},
        "sections": [
            {
                "h2": "Premium likes, quality likes and real likes",
                "p": [
                    "Many sellers split likes into tiers: cheap ones from empty accounts, premium or high-quality ones from accounts with photos and posts. Both tiers are the same thing in different clothes: accounts that like on command. A better disguise doesn't make a like genuine.",
                    "Quality, for a like, means one thing: a person chose to give it. Everything else is presentation.",
                ],
            },
            {
                "h2": "Real likes that engage beyond the like",
                "p": [
                    "A real like comes from someone who might also follow, comment or watch your next Reel. That's why real likes increase the rest of your numbers instead of sitting beside them: they're one step in what a person does, not the whole transaction.",
                ],
            },
            {
                "h2": "How to spot likes that only look real",
                "ul": [
                    "Likes jump while views, follows and comments stay flat.",
                    "The likers' profiles have stock photos, few posts and thousands of accounts followed.",
                    "Hundreds arrive within minutes of posting, then nothing.",
                    "The count falls a few weeks later.",
                ],
            },
        ],
        "faqs": [
            ("Are your Instagram likes from real accounts?", "Yes. Every like comes from a person's own account: someone who discovered your profile through our campaign and enjoyed the post. No bots and no account farms."),
            ("Do you sell premium likes?", "We don't sell likes in tiers or on their own. Every like we bring is from a person, inside a monthly package; {starter_name}, the smallest, typically brings {starter_likes} a month."),
            ("Will real likes increase my reach?", "They help the way only real engagement can, because the people behind them can also follow, comment and share. Where a post ends up still depends on the post itself, so we never promise reach."),
            ("Why do some bought likes look real?", "Because they're made to: profile photos, a few posts, believable names. Look at what happens around them. Likes from people come with views and follows; disguised ones arrive alone."),
            ("Can I get real likes without new followers?", "No. Likes arrive as part of the package, from people who find your profile, and many of them follow as well. That's what keeps likes realistic."),
        ],
    },
    {
        "service": "likes",
        "modifier": "reels",
        "slug": "instagram/likes/reels",
        "label": "Instagram Reels likes",
        "title": "Buy Instagram Likes for Reels From Real Viewers | Growsterr",
        "description": "Buy Instagram likes for Reels the honest way: people watch your videos and like the ones they enjoy, so every like comes with a view behind it.",
        "h1": ("Likes on your Reels, ", "from people who actually watched."),
        "intro": "Before you buy Instagram likes for Reels, it helps to know what a like is worth on a Reel nobody watched: not much. Our likes on Reels come from real people who discovered your profile, watched your videos and liked the ones that held them, alongside new followers and comments.",
        "hero": {"image": "instagram-creator-studio", "alt": "A creator editing an Instagram Reel on a phone at a desk"},
        "sections": [
            {
                "h2": "On a Reel, watching comes before liking",
                "p": [
                    "Reels live on what viewers do: whether they watch to the end, replay, share, follow. A like is one signal among those, and it means most when it follows a real watch.",
                    "Video likes bought on their own usually arrive without plays to match. A Reel with more likes than views is easy to spot and says nothing good about how it got them.",
                ],
            },
            {
                "h2": "Getting more of your Reels seen",
                "ul": [
                    "People browse your profile and watch the Reels that catch them, not only the newest.",
                    "{rising_name} and {pro_name} let you put a particular Reel in front of more people.",
                    "Viewers come from the place you choose, so your language and references land.",
                ],
            },
            {
                "h2": "Make the first seconds count",
                "p": [
                    "We can bring people to your Reels; keeping them is the video's job. A clear hook in the first second or two, captions for people watching without sound, and an ending that makes a replay tempting all help turn a view into a like.",
                ],
                "image": {"image": "instagram-real-people", "alt": "Viewers watching an Instagram Reel to the end and tapping like"},
            },
        ],
        "faqs": [
            ("Can I point likes at a specific Reel?", "Yes, with {rising_name} or {pro_name}: you choose which posts and Reels get the attention, and people do the rest. With {starter_name}, viewers find the Reels they enjoy on their own."),
            ("Do Reels likes come with views?", "Yes. People watch before they like, so a view sits behind every like. We don't sell or count views separately, because each is a person choosing to watch."),
            ("Will this get my Reel onto Explore?", "No one can promise that, and we don't. Instagram decides what goes on Explore and in the Reels feed. Viewers who watch and react give a Reel a fair start; bought likes without views give it a strange one."),
            ("Does my account need to be public?", "Yes, while your campaign runs. People outside your followers can't watch Reels on a private account, so they couldn't like them either."),
            ("How many likes will my Reels get?", "With {pick_name}, typically {pick_likes} likes a month across your posts and Reels. How they split depends on what people enjoy most."),
        ],
    },
    {
        "service": "likes",
        "modifier": "safe",
        "slug": "instagram/likes/safe",
        "label": "Legit Instagram likes",
        "title": "Legit Instagram Likes: What Makes One Legitimate | Growsterr",
        "description": "Want to buy Instagram likes that are legit? A legit like comes from a person who saw your post. How to tell, and how our monthly packages bring them.",
        "h1": ("Legit Instagram likes ", "start with a person and a post."),
        "intro": "Looking to buy Instagram likes that are legit? A legit like has two parts: a real person, and a post they actually saw. Everything we do is built around both. We show your profile to people, and the ones who enjoy your posts like them, with no logins, no bots and no likes sold on their own.",
        "hero": {"image": "instagram-hub", "alt": "A person scrolling Instagram and stopping to like a post they enjoyed"},
        "sections": [
            {
                "h2": "Red flags in any likes offer",
                "ul": [
                    "A price per thousand likes: people can't be bought by the thousand.",
                    "Delivery in minutes, or a promise of exact numbers.",
                    "A request for your password, or a login through an app.",
                    "Likes sold without views, follows or comments to go with them.",
                ],
            },
            {
                "h2": "Why fake likes aren't legit, whoever sells them",
                "p": [
                    "Instagram's rules ask people not to collect likes artificially, and likes from accounts that like on command are exactly that. We can't say how Instagram treats any single account, and we won't guess. We just don't bring anything artificial to yours.",
                ],
            },
            {
                "h2": "Where our likes come from",
                "p": [
                    "From the people our campaigns bring to your profile: users in our partner network, in the place you choose, every day of the month. They like what they enjoy, typically {pick_likes} likes a month with {pick_name}, and many of them follow and comment too.",
                ],
            },
        ],
        "faqs": [
            ("Is it legit to buy Instagram likes?", "Buying likes from accounts that like on command goes against Instagram's rules on artificial engagement. What we sell is different: reach to real people, who decide for themselves whether to like."),
            ("Can I lose my account over bought likes?", "We can't speak for Instagram, and anyone who promises an outcome is guessing. What we control is that every like we bring comes from a person, and that we never touch your login."),
            ("How do I pay?", "With a card, Apple Pay or Google Pay, through Stripe's secure checkout. Billing is monthly and stops whenever you cancel."),
            ("Do you ask for my Instagram login?", "Never. We need your username to start the campaign. If any likes service asks for your password, walk away."),
            ("Why don't you sell likes per post?", "Because a set number of likes on a set post can only come from accounts that like on command. We bring people instead; likes are what they do when they enjoy a post."),
        ],
    },
    {
        "service": "likes",
        "modifier": "viral",
        "slug": "instagram/likes/viral",
        "label": "Instagram likes for going viral",
        "title": "Viral Instagram Likes: Can Likes Make a Post Spread? | Growsterr",
        "description": "Thinking of buying Instagram likes to go viral? Likes alone don't make a post spread; people who watch, share and save do. What real likes can and can't do.",
        "h1": ("Viral Instagram likes ", "are a result, not a starting gun."),
        "intro": "People often buy Instagram likes to make a post go viral, hoping a big number will convince Instagram, and everyone else, that it deserves more attention. It rarely works that way. Likes from people who watched and enjoyed a post are a sign of momentum; likes piled onto a quiet post are a sign of nothing. We bring the first kind, and we don't promise the viral part.",
        "hero": {"image": "instagram-followers-1000", "alt": "Likes, shares and saves rising together on an Instagram post that is starting to spread"},
        "sections": [
            {
                "h2": "Likes come after the spread, not before",
                "p": [
                    "When a post takes off, the likes are the visible trail of thousands of people watching it, sending it to friends and saving it for later. Copy the trail without the people and you get the number without the movement.",
                ],
            },
            {
                "h2": "What actually gives a post a chance",
                "ul": [
                    "A first audience that reacts: people who see the post early and like, comment or share it.",
                    "A hook that makes people stop, and a reason to send it to someone.",
                    "Posting where your audience is, in their language, when they're scrolling.",
                    "Focus: with {rising_name} or {pro_name}, more people see the post you think could travel.",
                ],
            },
            {
                "h2": "What we promise, and what we don't",
                "p": [
                    "We promise real people, every day, and a dashboard of what we measured. We don't promise views in the millions, a spot on Explore or a post that spreads. Anyone who does is selling the look of a viral post.",
                ],
            },
        ],
        "faqs": [
            ("Will buying likes make my post go viral?", "Not by itself. A like count is the result of people's attention, and bought likes add the count without the attention. Likes from people who watched give a post an honest start, which is the most anyone can offer."),
            ("How many likes does a viral post need?", "There's no magic number. A post with a modest count can travel if the people who see it share it, and a post with a big count can stall."),
            ("Do you send likes in the first hour after I post?", "We don't time likes to a post. People arrive through the month and like what they enjoy. If one post matters more, {rising_name} and {pro_name} let you choose which posts get the attention."),
            ("Are shares and saves included?", "We don't count or sell them, but they happen: the people who like your posts can also share and save them, which bots never do."),
            ("Does a high like count make others more likely to like?", "People do notice a busy post. But a big count with no comments or shares looks staged to exactly the people you want to impress."),
        ],
    },
]
