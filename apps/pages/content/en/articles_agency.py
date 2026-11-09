"""English agency pages: Growsterr for brands and creators (influencer agency, TikTok agency,
Instagram growth agency, influencer marketing by platform, AI, pricing, niches, the creator side)
and four guides on how influencer agencies and influencer marketing work. Kind "agency" uses the
money-page layout; kind "guide" reads first. What we may and may not claim on these pages:
docs/keywords/WRITING.md, "Agency pages". Package numbers come from apps/growth/plan.py through
the placeholders; anything beyond the packages is "talk to us on WhatsApp or by email"."""

UPDATED = "2026-11-08"

ARTICLES = [
    # --- The core page: our own positioning --------------------------------------------
    {
        "article": "instagram-growth-agency",
        "kind": "agency",
        "platform": "instagram",
        "slug": "instagram-growth-agency",
        "label": "Instagram growth agency",
        "title": "The Best Instagram Growth Agency Isn't Instant | Growsterr",
        "description": "Looking for the best Instagram growth agency? We run a monthly campaign that shows your profile to real people every day. A team behind it, never instant.",
        "h1": ("The best Instagram growth agency ", "is a growth agency, not an instant service."),
        "intro": "If you're weighing up who to trust as the best Instagram growth agency, you'll find two kinds of offer: services that drop a number on your account within the hour, and agencies that run a campaign and let people decide. Growsterr is the second kind. A team runs your campaign every day, real people in the place you choose discover your profile, and the ones who like it follow.",
        "hero": {"image": "instagram-hub", "alt": "An Instagram profile being discovered by new people over the course of a month"},
        "sections": [
            {
                "h2": "What a growth agency does that an instant service can't",
                "p": [
                    "An instant service sells an outcome it can produce on demand: a count, delivered by accounts that do as they're told. A growth agency sells something slower and far more useful: attention from people who hadn't heard of you yesterday. That can't be produced on demand. It has to be earned day after day, which is why our work takes the shape of a monthly campaign rather than an order.",
                    "It also changes what your money buys. You aren't paying for followers by the thousand. You're paying a team to put your profile in front of the right people, month after month, and to show you honestly what came of it. Call it an IG growth agency, a followers agency, a promotion agency or simply someone to increase your Instagram followers; the test is the same: are there people at the end of it?",
                ],
            },
            {
                "h2": "How we run an Instagram growth campaign",
                "ul": [
                    "You give us your username and the city, region or country your audience lives in; at no point do we need your password.",
                    "We set up a promoted campaign in our partner network, aimed at that place, and it runs every day for 30 days.",
                    "People there come across your profile, look through your posts and make up their own minds about following.",
                    "Many of the same people like, watch and comment, so your engagement grows from the same accounts as your following.",
                    "Your dashboard records the visits the campaign brought and the follows that came from them, one day at a time.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "A creator reviewing a month-long Instagram growth campaign on a laptop at a desk"},
            },
            {
                "h2": "The team behind your campaign",
                "p": [
                    "Growsterr is a brand of Sterr Technologies OÜ, the company behind Sterr Agency, registered in Tallinn, Estonia, with headquarters in Turkey. Growsterr brings Sterr Agency's way of working to creators and personal brands: a team behind every campaign, and numbers you can check for yourself.",
                    "On {pro_name}, you also get priority placement and a direct WhatsApp line to that team. On any package, when something needs a human answer, you can reach us on WhatsApp or by email.",
                ],
            },
            {
                "h2": "How to judge any Instagram growth agency, us included",
                "ul": [
                    "It can explain where your new followers come from in a sentence you could repeat to a friend.",
                    "It needs your username and nothing more from your account.",
                    "Its numbers are ranges for a month, never an exact count by tomorrow.",
                    "It shows you what it measured on your own profile, not screenshots of someone else's.",
                    "You can stop it yourself, from your account, without having to ask anyone.",
                ],
            },
        ],
        "compare": [
            ("What you pay for", "A count delivered to your account", "A month of campaigns that show your profile to real people"),
            ("Who's behind it", "Usually a checkout and nothing else", "A team that sets up and watches every campaign"),
            ("Where followers come from", "Accounts that follow on command", "People in the city, region or country you name"),
            ("Timing", "Most of it in the first hour", "Every day for 30 days"),
            ("Likes and comments", "Extra orders, from more of the same accounts", "From the people who followed, inside the same package"),
            ("What you see afterwards", "A number, until the next clean-up", "A dashboard of the visits and follows we measured"),
        ],
        "faqs": [
            ("What does an Instagram growth agency actually do?", "It puts your profile in front of people who are likely to care, steadily, and reports what happened. Ours does that with promoted campaigns in our partner network, aimed at the place you choose, every day of the month. What people do once they see you is up to them, and to your posts."),
            ("Is Growsterr an Instagram followers agency or an engagement agency?", "Both words describe part of the job. The campaign is built around new followers, and likes, comments and views come from the same people inside the package: with {pick_name}, typically {pick_audience} followers, {pick_likes} likes and {pick_comments} comments a month. We never sell engagement on its own."),
            ("How is this different from boosting a post myself?", "Boosting from your own account puts one post in front of people for as long as you keep paying. Our campaigns run outside your account, introduce your whole profile for the month, and come with a team and a dashboard. There's no ad account for you to set up and no login to share with us."),
            ("How many followers can a growth agency get me?", "Nobody honest can name an exact figure, because each follow is a person's decision. Our packages come with typical monthly ranges instead: {starter_audience} with {starter_name}, {rising_audience} with {rising_name} and {pro_audience} with {pro_name}. Strong posts and a well-chosen place tend to help a month along."),
            ("Will I have my own Instagram growth agent?", "A team runs every campaign rather than a single assigned agent, so nothing stalls when one person is away. On {pro_name} you get a direct WhatsApp line to that team, and on any package you can write to us on WhatsApp or by email."),
            ("Can I stop if it isn't right for me?", "Yes. You can cancel at any point from your own account. Cancelling stops the next payment, the month you've paid for runs to its end, and every follower you gained stays yours."),
        ],
    },
    # --- Influencer agency, TikTok agency, Instagram agencies ----------------------------
    {
        "article": "influencer-agency",
        "kind": "agency",
        "platform": "instagram",
        "slug": "influencer-agency",
        "plan": "pro",
        "label": "Influencer agency for brands and creators",
        "title": "Influencer Agency for Brands and Creators | Growsterr",
        "description": "An influencer agency that grows the audience itself: monthly campaigns bring real people to your brand or creator profile, worldwide, with a team behind them.",
        "h1": ("An influencer agency ", "that starts with your own audience."),
        "intro": "People looking for an influencer agency usually want one of two things: creators talking about their brand, or a bigger audience of their own. Growsterr does the second, every month, for brands, personal brands and creators on Instagram, TikTok and YouTube. If creator campaigns are also on your mind, those start with a conversation.",
        "hero": {"image": "instagram-followers", "alt": "A brand's Instagram profile gaining followers from real people across a month"},
        "sections": [
            {
                "h2": "Influencer marketing for brands starts at home",
                "p": [
                    "When a creator mentions your brand, their followers come to look at you. What they find decides what happens next: an active profile with real people in the comments, or a quiet one that gives them no reason to stay. Growing your own audience first means every mention, collaboration and campaign lands on something worth following.",
                    "That's the part we run as a package. Your brand's profile is shown to real people through promoted campaigns in our partner network, every day, in the place you choose. Those who like what they see follow, and your dashboard shows what the campaign measured.",
                ],
            },
            {
                "h2": "What we do, and what starts with a conversation",
                "ul": [
                    "Monthly growth packages for brand, business and creator profiles, from {starter_price} a month.",
                    "Audience targeting by city, region or country, included in every package.",
                    "A team behind each campaign, and a dashboard of measured visits and new followers.",
                    "Campaigns with creators, or anything larger than a package: talk to us on WhatsApp or by email, and we'll tell you honestly what we can take on.",
                ],
            },
            {
                "h2": "A worldwide influencer agency, run remotely",
                "p": [
                    "We work online with brands and creators wherever they are, from a company registered in Tallinn, Estonia, with headquarters in Turkey. There's no local office to drop by. Wanting an agency near you usually means wanting an audience near you, and that we can aim for from anywhere: name a city and the campaign is pointed there.",
                ],
            },
        ],
        "faqs": [
            ("Do you work with brands, or only with creators?", "Both. Any public Instagram, TikTok or YouTube account can run a package: a creator, a personal brand, a shop, a restaurant or a company. The campaign works the same way for each; only the people you want to reach change."),
            ("Can you connect my brand with influencers?", "Not as a package. Creator campaigns depend on the brand, the creators and the budget, so they begin with a conversation: talk to us on WhatsApp or by email and tell us what you have in mind. We won't promise creators, posts or results before we've talked."),
            ("Do you work with brands globally?", "Yes. We work remotely, and your campaign can be aimed at whichever city, region or country you choose. Prices are in US dollars, and payment runs through Stripe."),
            ("What does an influencer agency usually cost?", "It depends on what's included, because creator fees, production and management are priced very differently. Our side is simple: three monthly packages from {starter_price} to {pro_price}, with nothing to sign and no minimum term."),
            ("Is digital influencer marketing the same as advertising?", "Not quite. An ad speaks for the brand; influencer marketing borrows the trust between a creator and their audience. Our campaigns sit between the two: the introduction is paid for, and people decide on their own whether your profile is worth following."),
            ("Who runs my campaign?", "A team at Growsterr, a brand of the company behind Sterr Agency. You never hand over your login: all we ask for is your username, a public profile and where your audience lives."),
        ],
    },
    {
        "article": "tiktok-agency",
        "kind": "agency",
        "platform": "tiktok",
        "slug": "tiktok-agency",
        "label": "TikTok agency",
        "title": "TikTok Agency for Growth With Real People | Growsterr",
        "description": "A TikTok agency that grows your profile month by month: real people discover your videos, follow and engage, from the place you choose. No bots, no login.",
        "h1": ("A TikTok agency ", "that brings real people to your videos."),
        "intro": "A TikTok agency can mean a production studio, a LIVE agency, an ads team or a growth partner. We're the last of those. Each month we show your TikTok profile to real people in the place you choose; the ones who enjoy your videos follow, like and comment on their own, and your dashboard shows what we measured.",
        "hero": {"image": "tiktok-hub", "alt": "A TikTok creator's profile grid with new viewers arriving through the month"},
        "sections": [
            {
                "h2": "Which kind of TikTok agency do you need?",
                "ul": [
                    "Content studios script, film and edit videos for you. We don't: your videos stay yours to make.",
                    "LIVE agencies sign hosts through TikTok's own agency programme. We aren't one, and we don't recruit hosts.",
                    "Ads teams run campaigns from your TikTok ad account. We never work from your account.",
                    "Growth agencies bring people to your profile. That's us: a monthly campaign, real people and a measured dashboard.",
                ],
            },
            {
                "h2": "Why TikTok growth needs people, not numbers",
                "p": [
                    "TikTok decides how far a video travels by watching what viewers do with it: whether they stay, rewatch, share or follow. A following made of accounts that never watch gives each new video a weaker start, because the first people to see it do nothing at all.",
                    "The people our campaigns bring watch because they chose to. With {pick_name}, a month typically brings {pick_audience} new followers, along with {pick_likes} likes and {pick_comments} comments from those same people.",
                ],
                "image": {"image": "tiktok-creator", "alt": "A TikTok creator filming a short video on a phone propped on a desk"},
            },
            {
                "h2": "What we won't promise on TikTok",
                "p": [
                    "A spot on the For You feed, a video that takes off, a crowd for a LIVE at a set time: none of these can be delivered honestly, by us or by anyone else. What we can deliver is steady attention from real people, aimed where you want it, every day of the month.",
                ],
            },
        ],
        "faqs": [
            ("Is Growsterr a TikTok marketing agency?", "We're a growth agency that works on TikTok, Instagram and YouTube. We don't make videos or manage ad accounts; we run the campaign that brings people to your profile, and a team looks after it."),
            ("Can you choose which TikTok videos people see?", "With {rising_name} or {pro_name}, yes: you tell us which videos should get the attention. With {starter_name}, people find the videos they like by themselves. Either way, we never promise views or likes on any single video."),
            ("Do you need my TikTok login?", "No. Your username, a public profile and the place your audience lives are all we need. Nobody on our side ever signs in to your TikTok."),
            ("Are you a TikTok LIVE agency?", "No. We don't sign creators to TikTok's LIVE programme or take a share of gifts. The followers your campaign brings may drop in when you go live, but we never sell LIVE viewers."),
            ("How much does a TikTok agency cost with you?", "There are three monthly packages: {starter_name} at {starter_price}, {rising_name} at {rising_price} and {pro_name} at {pro_price}. Each one is a subscription you can cancel from your account."),
            ("Can brands work with you on TikTok?", "Yes. A brand profile runs the same packages as a creator's. For anything beyond them, such as campaigns with TikTok creators, talk to us on WhatsApp or by email first."),
        ],
    },
    {
        "article": "tiktok-ugc-agency",
        "kind": "agency",
        "platform": "tiktok",
        "slug": "tiktok-ugc-agency",
        "label": "TikTok UGC agency",
        "title": "TikTok UGC Agency: Where a Growth Agency Fits In | Growsterr",
        "description": "Looking for a TikTok UGC agency? We don't produce UGC videos. We grow TikTok profiles with real people, and bigger brand projects start with a conversation.",
        "h1": ("Looking for a TikTok UGC agency? ", "Here's where we fit, and where we don't."),
        "intro": "A TikTok UGC agency hires creators to film videos in the style of ordinary users, which a brand then posts or runs as ads. We don't produce UGC, and we'd rather say so in the first lines. What we do sits right next to it: we grow the TikTok profile those videos point to, with real people, every month.",
        "hero": {"image": "tiktok-creator", "alt": "A creator filming a product demonstration video for TikTok at a kitchen table"},
        "sections": [
            {
                "h2": "What UGC is, and what it isn't",
                "p": [
                    "User-generated content, in agency terms, usually means paid content made to feel unpaid: a creator unboxing, reviewing or demonstrating a product on camera, delivered to the brand as files. The creator may never post it on their own account. That's different from influencer marketing, where the value lies in the creator's own audience.",
                    "Both have their place. Neither replaces a brand profile people want to follow, because that's where viewers go when a video makes them curious.",
                ],
            },
            {
                "h2": "Questions to ask any UGC agency",
                "ul": [
                    "Who owns the videos, for how long, and on which platforms may you use them?",
                    "Can the videos run as ads from the creator's handle, and is that priced separately?",
                    "How many rounds of revisions are included, and who writes the brief?",
                    "How will the paid relationship be disclosed when a video is posted?",
                ],
            },
            {
                "h2": "Where Growsterr comes in",
                "p": [
                    "Once your videos are live on your own TikTok, we can show your profile to real people in the place you choose, every day of the month. The ones who like what they see follow, like and comment; with {pick_name}, a typical month brings {pick_audience} new followers.",
                    "For a larger brand project, talk to us on WhatsApp or by email, and we'll tell you plainly what we can and can't do.",
                ],
            },
        ],
        "faqs": [
            ("Do you make UGC videos for brands?", "No. We don't film, script or edit videos, and we don't hire creators to make them. We grow the account those videos live on."),
            ("Can you grow a brand's TikTok while we run UGC ads?", "Yes. Your ads run wherever you run them, and our campaign brings people to your profile every day alongside them. Your dashboard shows only what our campaign measured, which keeps the two easy to tell apart."),
            ("Can a UGC creator use your packages for their own account?", "Yes. If you post for yourself as well, a package works on any public TikTok profile, and a real audience of your own makes your portfolio easier to show."),
            ("Can you recommend UGC creators?", "We don't keep a roster of UGC creators to recommend. If you're planning something bigger, tell us about it on WhatsApp or by email and we'll be straight with you about whether we can help."),
            ("Do comments on my videos come from real people?", "Yes. Comments come inside every package from people who discovered your videos, written in their own words: typically {starter_comments} a month with {starter_name}. None of them follows a script."),
        ],
    },
    {
        "article": "instagram-marketing-agency",
        "kind": "agency",
        "platform": "instagram",
        "slug": "instagram-marketing-agency",
        "label": "Instagram marketing agency",
        "title": "Instagram Marketing Agency That Never Logs In | Growsterr",
        "description": "Need an Instagram marketing agency? We run the growth part: real people discover your profile every month. We never manage your account or ask for your login.",
        "h1": ("An Instagram marketing agency ", "that never needs your login."),
        "intro": "An Instagram marketing agency usually takes over the whole account: content, posting, replies, ads. We do one part of that, and we do it without ever signing in. You keep making and posting your content; we run the campaign that brings real people to your profile every day, in the place you choose.",
        "hero": {"image": "instagram-creator-studio", "alt": "A small business owner posting to Instagram from a phone while the account grows"},
        "sections": [
            {
                "h2": "Instagram management agency or growth agency?",
                "p": [
                    "A management or handling agency works inside your account. That means sharing access, approving posts and trusting someone else to speak in your voice, which suits businesses that would rather not run Instagram at all.",
                    "A growth agency works outside it. Your account stays entirely yours, and the work is getting people to look at it. If you already have content you're proud of and simply need more of the right people to see it, the second kind is what you're after.",
                ],
            },
            {
                "h2": "What's in an Instagram marketing package with us",
                "ul": [
                    "A campaign that shows your profile to real people every day for 30 days.",
                    "New followers, with likes and comments from the same people: with {pick_name}, typically {pick_audience}, {pick_likes} and {pick_comments} a month.",
                    "Targeting by the city, region or country your customers live in.",
                    "A dashboard of what was measured, and a team you can reach on WhatsApp or by email.",
                ],
            },
            {
                "h2": "What we leave to you, or to someone else",
                "ul": [
                    "Making and posting your content, captions and Stories.",
                    "Replying to comments and direct messages.",
                    "Running ads from your own ad account.",
                    "Anything that needs a login: we never ask for one.",
                ],
            },
        ],
        "faqs": [
            ("Will you post on my Instagram for me?", "No. We never sign in, post, reply or change anything on your account. If you need someone to run your account day to day, a management agency is the better fit; we'd focus on the audience."),
            ("Is there an Instagram marketing agency near me?", "We work remotely, so distance doesn't matter much; what matters is where your audience is. Name your city and the campaign shows your profile to people there first."),
            ("What kinds of accounts do you work with?", "Creators, personal brands and businesses, as long as the profile is public. A local shop and a travel creator run the same packages, aimed at very different places."),
            ("How do I know the marketing is working?", "Your dashboard shows the profile visits our campaign brought and the new followers among them, day by day, plus where those visitors came from. You'll notice it in your likes and comments too, because they come from the same people."),
            ("Do you offer custom Instagram marketing plans?", "Our packages are the same for everyone, which keeps them clear. If you need something beyond them, talk to us on WhatsApp or by email and we'll say honestly whether it's work we can do."),
        ],
    },
    {
        "article": "instagram-ads-agency",
        "kind": "agency",
        "platform": "instagram",
        "slug": "instagram-ads-agency",
        "label": "Instagram ads agency",
        "title": "Instagram Ads Agency or Growth Agency? How to Choose | Growsterr",
        "description": "Looking for an Instagram ads agency? We don't manage ad accounts; we run monthly campaigns that bring real people to your profile, with a team behind them.",
        "h1": ("Looking for an Instagram ads agency? ", "First decide what the ads are for."),
        "intro": "An Instagram ads agency runs paid campaigns from your ad account: it writes the ads, sets the budget, picks the audience and reports on clicks or sales. We don't manage ad accounts, and we never work from yours. If the goal behind your ads is a bigger, real audience on your profile, that's exactly what our monthly campaigns are built for.",
        "hero": {"image": "instagram-followers", "alt": "An Instagram business profile with new followers arriving from its own city"},
        "sections": [
            {
                "h2": "When an Instagram advertising agency is the right call",
                "p": [
                    "If you sell online and want ads that send people straight to a product page, an agency that manages ad accounts is the right partner. Its work is measured in clicks, sign-ups and sales, and it needs access to your ad account and your budget.",
                    "If what you really want is more people following your profile, liking your posts and coming back, an ads agency is a roundabout route to it. That's the job we do directly.",
                ],
            },
            {
                "h2": "How our campaigns differ from ads you'd run yourself",
                "ul": [
                    "They run as promoted campaigns in our partner network, aimed at the place you choose.",
                    "Nothing runs from your account, and we never need access to it.",
                    "There's no ad budget to manage: one monthly price, starting at {starter_price}.",
                    "The goal is your profile, not a click: people visit, look through your posts and decide whether to follow.",
                    "A team sets up and watches the campaign, and your dashboard shows what it measured.",
                ],
            },
            {
                "h2": "An advertising agency near me, or an audience near me?",
                "p": [
                    "Local businesses often look for an agency nearby so they can meet in person. We work remotely, but the campaign itself can be as local as you like: name a city and your profile is shown to people there first. A café, a clinic or a studio gains followers who can actually walk through the door.",
                ],
            },
        ],
        "faqs": [
            ("Do you run Instagram ads for clients?", "We don't manage ad accounts or run ads from your account. Our campaigns are promoted in our partner network, point people to your profile, and come as monthly packages."),
            ("Can I use your packages alongside my own ads?", "Yes. You can keep running your own ads for sales and use a package for audience growth at the same time. Our dashboard counts only the visits and followers our campaign brought, so the figures never blur together."),
            ("What do you need from me to get going?", "Your Instagram username, a public profile and the place your audience should come from. No ad account, no budget, no password."),
            ("How is your price different from an ad budget?", "An ad budget is spent as people see or click the ad, and it stops working when the money does. Our packages are a fixed monthly price, {starter_price} to {pro_price}, and the followers you gain stay after the month ends."),
            ("Can you handle a larger advertising project?", "Anything beyond the monthly packages starts with a conversation. Talk to us on WhatsApp or by email, tell us what you have in mind, and we'll be honest about whether we're the right people for it."),
        ],
    },
    {
        "article": "instagram-content-agency",
        "kind": "agency",
        "platform": "instagram",
        "slug": "instagram-content-agency",
        "label": "Instagram content and branding agency",
        "title": "Instagram Branding Agency or Growth Partner? | Growsterr",
        "description": "Looking for an Instagram branding or content agency? We don't design feeds or edit Reels. We bring real people to the brand you've built, all month long.",
        "h1": ("An Instagram branding agency builds the look. ", "We bring the people."),
        "intro": "An Instagram branding agency, a content studio or a creative team will shape how your profile looks and sounds: the feed, the Reels, the design, the voice. That isn't our work. Ours starts once the content exists: we show your profile to real people in the place you choose, and the ones who like your brand follow it.",
        "hero": {"image": "instagram-creator-studio", "alt": "A designer and a creator laying out an Instagram feed on a large screen"},
        "sections": [
            {
                "h2": "What we don't make",
                "p": [
                    "We don't design feeds, edit Reels, clip long videos, write captions, handle DMs or run PR, and we don't build websites. Agencies that do those things well are worth their fee, and we'd rather tell you that than pretend to be one of them.",
                ],
            },
            {
                "h2": "Why content and growth need each other",
                "p": [
                    "Beautiful content with nobody watching is a portfolio. A growing audience with nothing to watch is a leaky bucket: people arrive, find little and drift away. The accounts that grow well have both, and each makes the other worth more.",
                    "If you've invested in your content or your personal brand, a monthly campaign is how you put it in front of people who don't know you yet. With {pick_name} that typically means {pick_audience} new followers a month, plus likes and comments from the same people.",
                ],
                "image": {"image": "instagram-real-people", "alt": "People pausing on a well-designed Instagram post and opening the profile behind it"},
            },
            {
                "h2": "Personal branding on Instagram, with real people",
                "p": [
                    "A personal brand is a promise about who you are, and an audience of bots quietly breaks it. Coaches, consultants, artists and founders can run the same packages as creators, aimed at the city, region or country where their clients or readers live. Nothing is posted in your name and nobody signs in to your account.",
                ],
            },
        ],
        "faqs": [
            ("Do you create Instagram content or Reels?", "No. We don't film, design, edit or clip. You make the content; we bring real people to see it, and with {rising_name} or {pro_name} you can choose which posts and Reels get the attention."),
            ("Can you help with Instagram Live?", "Not with the broadcast itself, and we never sell Live viewers. What we add is a larger audience of people who chose to follow, and they're the ones who hear about it when you go live."),
            ("Will you manage my DMs or comments?", "No. Replies are the part people value most from you, and they need access we never ask for. The comments your campaign brings are written by real people and deserve your own answers."),
            ("Do you do Instagram PR?", "No. We don't pitch media or run PR campaigns. If you're planning something bigger than a package, talk to us on WhatsApp or by email and we'll tell you honestly what's within our reach."),
            ("Are you a digital agency for my whole online presence?", "No, our focus is narrow on purpose: audience growth on Instagram, TikTok and YouTube. Your website, ads and design are best left to specialists in each."),
        ],
    },
    # --- Influencer marketing, platform by platform ------------------------------------
    {
        "article": "influencer-marketing-instagram",
        "kind": "agency",
        "platform": "instagram",
        "slug": "influencer-marketing/instagram",
        "label": "Influencer marketing on Instagram",
        "title": "Influencer Marketing on Instagram: Both Sides of It | Growsterr",
        "description": "How influencer marketing on Instagram works for brands and creators, what makes a partnership pay off, and where real audience growth fits in. Plain answers.",
        "h1": ("Influencer marketing on Instagram ", "only works with a real audience."),
        "intro": "Influencer marketing on Instagram rests on one thing: a creator's followers trust what that creator shows them. Everything else, from the fee to the format, follows from how real that audience is. Here's how it works for brands and for creators, and the part an Instagram influencer agency like ours plays in it.",
        "hero": {"image": "instagram-real-people", "alt": "A creator's Instagram post featuring a product, with followers asking about it in the comments"},
        "sections": [
            {
                "h2": "How a brand partnership works on Instagram",
                "p": [
                    "A brand pays or gifts a creator to feature a product in a Reel, a carousel, a Story or a collaborative post that appears on both profiles. The post carries Instagram's paid partnership label, and the brand looks at reach, saves, profile visits and sales afterwards.",
                    "What the brand is really buying is the attention of the creator's followers. That's why careful brands look past the follower count to the comments, the likes on recent posts and where the audience lives.",
                ],
            },
            {
                "h2": "For creators: the audience comes first",
                "p": [
                    "A brand that knows what it's doing checks a creator's audience before paying: whether likes and comments keep pace with followers, whether the followers live where the brand sells, whether the count ever drops in waves. Bought bots fail every one of those checks.",
                    "Our packages build the kind of audience that passes them. Real people in the place you choose discover your profile, follow, and like and comment on their own: with {pick_name}, typically {pick_audience} new followers, {pick_likes} likes and {pick_comments} comments a month.",
                ],
                "image": {"image": "instagram-followers", "alt": "An Instagram creator's audience growing steadily, with likes keeping pace with new followers"},
            },
            {
                "h2": "For brands: a profile worth landing on",
                "p": [
                    "Every creator mention sends curious people to your brand's profile. If that profile is active, with real people following and talking, more of them stay. Our packages work for a brand's own Instagram exactly as they do for a creator's. For anything larger, such as campaigns with creators, talk to us on WhatsApp or by email.",
                ],
            },
        ],
        "faqs": [
            ("Do you run influencer campaigns on Instagram?", "Not as a set product. Our packages grow your own profile with real people. Campaigns with creators depend on too many things to price on a page, so they start with a conversation on WhatsApp or by email."),
            ("How many followers does an Instagram influencer need for brand deals?", "There's no fixed line. Brands often care more about engagement and where the audience lives than about size, and a smaller creator with an attentive local following can be exactly what a brand needs."),
            ("Does a paid partnership label hurt a post?", "Instagram asks creators to label paid partnerships, and advertising rules in many countries require it. A post people enjoy can still do well with the label; hiding a partnership is what damages trust."),
            ("Can growing my audience with you help me get sponsorships?", "It can make you easier to say yes to, because brands look for real, engaged followers. We can't promise deals: those depend on your niche, your content and the brands you approach."),
            ("Do brands check whether followers are bought?", "Careful ones do, by looking at engagement and audience data or with tools built for the purpose. Followers from our campaigns are people, so there's nothing for those checks to find."),
        ],
    },
    {
        "article": "influencer-marketing-tiktok",
        "kind": "agency",
        "platform": "tiktok",
        "slug": "influencer-marketing/tiktok",
        "label": "Influencer marketing on TikTok",
        "title": "Influencer Agency for TikTok: How Creator Deals Work | Growsterr",
        "description": "Looking for an influencer agency for TikTok? How influencer marketing on TikTok differs from other platforms, and how real audience growth fits into it.",
        "h1": ("An influencer agency for TikTok ", "starts with what viewers do."),
        "intro": "If you want an influencer agency for TikTok, it helps to know how differently the platform treats creators. A video can travel far beyond a creator's followers there, so brands judge creators by how their videos perform, not only by headcount. Here's how influencer marketing on TikTok works, and where our monthly growth packages fit.",
        "hero": {"image": "tiktok-hub", "alt": "Several TikTok videos from different creators featuring the same product"},
        "sections": [
            {
                "h2": "Why TikTok is different for brands",
                "p": [
                    "On most platforms, a creator's reach stays close to the size of their following. On TikTok, the For You feed shows videos to people who don't follow the creator at all, so a small creator can reach a big audience with the right video, and a big one can be passed over with the wrong one.",
                    "For brands, that makes a TikTok partnership a bet on content as much as on a creator. For creators, followers matter for a different reason: they're the people who see your next video first and give it its start.",
                ],
            },
            {
                "h2": "What a TikTok creator deal usually includes",
                "ul": [
                    "One or more videos made in the creator's own style, with TikTok's disclosure setting switched on.",
                    "Sometimes the right for the brand to run a video as an ad from the creator's handle.",
                    "Agreed dates, a brief that leaves room for the creator's voice, and a short report afterwards.",
                ],
            },
            {
                "h2": "Where our TikTok packages come in",
                "p": [
                    "We grow TikTok profiles, a creator's or a brand's, with real people in the place you choose. They watch, follow, like and comment on their own, and {pick_name} typically brings {pick_audience} new followers in a month. Creator campaigns for brands start with a conversation on WhatsApp or by email.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "A viewer watching a TikTok creator's video all the way through"},
            },
        ],
        "faqs": [
            ("Are you a TikTok influencer agency?", "We're a growth agency that works on TikTok. We don't represent creators or broker brand deals; we grow accounts. Larger brand projects begin with a talk on WhatsApp or by email."),
            ("Do TikTok followers still matter if videos can reach anyone?", "Yes. Followers are among the first to see a new video, and how they react helps decide where it goes next. Real followers who watch give each video a better start than a big number that never does."),
            ("Can you get my brand onto the For You feed?", "No, and anyone who promises it is guessing. TikTok decides what reaches the For You feed. We bring real viewers to your profile every day, which is the honest part we can do."),
            ("Do you work with TikTok Shop sellers?", "Any public TikTok profile can run a package, a shop's included. We grow the audience; we don't manage product listings, affiliates or sales."),
            ("Will my TikTok audience come from the right country?", "You name the city, region or country, and that's where your profile is shown first. When the matching audience just outside it is larger, some viewers may come from the surrounding area."),
        ],
    },
    {
        "article": "influencer-marketing-youtube",
        "kind": "agency",
        "platform": "youtube",
        "slug": "influencer-marketing/youtube",
        "label": "Influencer marketing on YouTube",
        "title": "Influencer Agency for YouTube Channels and Brands | Growsterr",
        "description": "Looking for an influencer agency for YouTube? How sponsorships work there, why subscribers still matter, and how we grow channels with real people each month.",
        "h1": ("Influencer marketing on YouTube ", "rewards channels people come back to."),
        "intro": "YouTube is where influencer marketing has the longest memory: a sponsored segment can keep being watched years after it went up. If you're looking for an influencer agency for YouTube, that's the thing to plan around. Here's how YouTube sponsorships work, and how we grow channels with real subscribers month by month.",
        "hero": {"image": "youtube-hub", "alt": "A YouTube creator recording a sponsored segment in a home studio"},
        "sections": [
            {
                "h2": "How YouTube sponsorships work",
                "p": [
                    "YouTube deals usually take one of two shapes: an integration, where a creator talks about a product for part of a video, or a dedicated video built around it. Shorts add a third, quicker option. Videos with paid promotion carry a disclosure that YouTube shows to viewers.",
                    "Because people keep finding videos long after upload, a sponsorship on YouTube works for as long as the video does. That's why sponsors pay attention to how a channel's older videos are still watched, not only to its subscriber count.",
                ],
            },
            {
                "h2": "Subscribers are a channel's first audience",
                "p": [
                    "When a channel uploads, its subscribers are among the first to hear about it. Real ones watch and give the video its start; bought ones never press play, and a channel full of them looks to YouTube like one nobody watches.",
                    "Our campaigns bring real people to your channel in the place you choose. You can also name one video, at checkout or later in your account: new viewers are sent to it, subscribe first, then watch. We don't promise views or watch hours on it, only real people.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Viewers subscribing to a YouTube channel and then watching its newest video"},
            },
            {
                "h2": "Brands and creators, on one channel",
                "p": [
                    "A creator can run a package to grow the channel sponsors look at; a brand can run the same package on its own channel. Campaigns with YouTube creators are a bigger conversation, and that one happens on WhatsApp or by email.",
                ],
            },
        ],
        "faqs": [
            ("Do you broker YouTube sponsorships?", "No. We don't represent creators or negotiate deals. We grow channels with real subscribers, and anything larger starts with a conversation on WhatsApp or by email."),
            ("How many subscribers does a channel need for sponsors?", "No single threshold applies to every brand. Sponsors tend to look at how many people watch recent videos, who those viewers are and how they react, so a smaller channel with an engaged audience can be a good fit."),
            ("Will your subscribers watch my videos?", "They're people who chose to subscribe, so many will watch whatever interests them. We count subscribers, not views, and never promise watch time."),
            ("Can you help my channel get monetized?", "We don't promise monetization or watch hours, and nobody honest can. Real subscribers who watch help a channel in ways bought ones never will; whether it reaches YouTube's thresholds depends on your videos."),
            ("What does each package bring in subscribers?", "With {starter_name}, typically {starter_audience} a month; with {rising_name}, {rising_audience}; with {pro_name}, {pro_audience}. They're ranges because each subscriber decides for themselves."),
        ],
    },
    {
        "article": "influencer-marketing-facebook-linkedin",
        "kind": "agency",
        "platform": "instagram",
        "slug": "influencer-marketing/facebook-linkedin",
        "label": "Influencer marketing on Facebook and LinkedIn",
        "title": "Influencer Marketing on Facebook and LinkedIn? | Growsterr",
        "description": "Planning influencer marketing on Facebook or LinkedIn? We work on Instagram, TikTok and YouTube only. What works on each, and where we can actually help.",
        "h1": ("Influencer marketing on Facebook or LinkedIn? ", "We work on Instagram, TikTok and YouTube."),
        "intro": "We'll say it first: we don't run campaigns on Facebook or LinkedIn. Our growth packages cover Instagram, TikTok and YouTube. If influencer marketing on Facebook or LinkedIn is your plan, here's what tends to work on each, and when one of our three platforms is the better home for your audience.",
        "hero": {"image": "instagram-hub", "alt": "A brand planning its social channels, with Instagram, TikTok and YouTube circled"},
        "sections": [
            {
                "h2": "Influencer marketing on LinkedIn",
                "p": [
                    "Influence on LinkedIn belongs mostly to people, not company pages: founders, specialists and employees who post about their work under their own names. B2B brands work with them through sponsored posts, co-hosted events and employee advocacy, and they measure success in conversations and leads rather than likes.",
                    "We don't grow LinkedIn profiles. If your expertise travels well on video, a YouTube channel or an Instagram profile can reach the same professionals, and those we can grow.",
                ],
            },
            {
                "h2": "Influencer marketing on Facebook",
                "p": [
                    "On Facebook, influence often lives in groups and community pages more than in personal profiles. Partnerships there tend to mean a trusted group admin or page owner recommending a product to people who already gather around a topic.",
                    "Instagram belongs to the same company, Meta, so brands often plan the two together. We work on the Instagram side only.",
                ],
            },
            {
                "h2": "Where we can help",
                "ul": [
                    "Growing your Instagram, TikTok or YouTube with real people, from {starter_price} a month.",
                    "Aiming that growth at the city, region or country where your customers or clients live.",
                    "Talking through anything larger on WhatsApp or by email, with no promise we can't keep.",
                ],
            },
        ],
        "faqs": [
            ("Do you offer influencer marketing on LinkedIn?", "No. We don't work on LinkedIn at all, for creators or for brands. Our packages are for Instagram, TikTok and YouTube."),
            ("Can you grow a Facebook page?", "No. We don't run campaigns for Facebook pages, profiles or groups. If your audience also uses Instagram, we can grow your profile there."),
            ("Is there an influencer agency for LinkedIn?", "Some agencies specialise in B2B creators on LinkedIn, and if that's your channel, one of them is the right call. We'd rather tell you that than stretch our packages to a platform we don't cover."),
            ("Which platform suits B2B influencer marketing best?", "It depends where your buyers spend their attention. LinkedIn is strong for direct professional reach; YouTube suits explainers and demos that people look up when they're deciding. We can only help with the second."),
            ("Can one campaign cover Facebook and Instagram?", "Each subscription grows one Instagram, TikTok or YouTube account. Nothing we do appears on your Facebook page, and we never need access to either account."),
        ],
    },
    {
        "article": "influencer-marketing-platform",
        "kind": "agency",
        "platform": "instagram",
        "slug": "influencer-marketing-platform",
        "label": "Influencer marketing platform or agency",
        "title": "Influencer Marketing Platform or Agency? What We Are | Growsterr",
        "description": "Comparing influencer marketing platforms? Growsterr isn't software or a creator database. We're an agency with a website, a team and a measured dashboard.",
        "h1": ("Looking for an influencer marketing platform? ", "Here's what we are instead."),
        "intro": "An influencer marketing platform is usually software: a searchable database of creators, outreach tools, contracts and reporting, sold as a monthly licence. Growsterr isn't that. We're an agency with a website where you order a monthly growth package, a team that runs the campaign, and a dashboard that shows what it measured.",
        "hero": {"image": "instagram-creator-studio", "alt": "A person comparing an influencer software tool with a growth agency's dashboard on two screens"},
        "sections": [
            {
                "h2": "Platform, marketplace or agency",
                "ul": [
                    "Software platforms give your team tools to find, contact and manage creators yourselves.",
                    "Marketplaces list creators and their rates, and you book them directly.",
                    "Agencies do the work for you. We're an agency, and the work we do is growing your own audience.",
                ],
            },
            {
                "h2": "What our website and dashboard do",
                "p": [
                    "On our website you pick a platform and a package, give your username and the place your audience lives, and pay by card, Apple Pay or Google Pay through Stripe. That's the whole order: there's no app to install and no creator database to browse.",
                    "Your dashboard then shows, day by day, the profile visits our campaign brought and the new {audience} that came from them, where visitors came from, and an outlook for the next 30 days that's clearly marked as an estimate.",
                ],
                "image": {"image": "instagram-followers-1000", "alt": "A growth dashboard showing profile visits and new followers for each day of the month"},
            },
            {
                "h2": "When a platform is the better choice",
                "p": [
                    "If your team wants to run creator campaigns in-house, searching, contacting and paying creators yourselves, a software platform is built for exactly that, and we'd point you that way. If you'd rather a team grew your audience for you, at a price you know in advance, that's us.",
                ],
            },
        ],
        "faqs": [
            ("Do you have an influencer marketing app?", "No. Everything works in the browser on your phone or computer: ordering, your dashboard and cancelling. You never install anything or connect your Instagram login."),
            ("Is there an influencer marketing API?", "Not from us. We don't keep a database of creators to query, and your campaign's numbers live in your dashboard."),
            ("Can I find influencers through Growsterr?", "No. We don't list creators or match brands with them. If you're planning a campaign with creators, talk to us on WhatsApp or by email and we'll tell you plainly what we can take on."),
            ("What does your dashboard measure?", "The profile visits our campaign brought, the new {audience} among those visitors day by day, and visits by country. It counts only what came from us, so your account's own total can differ because of other growth and unfollows."),
            ("How does your pricing compare with a platform licence?", "We don't charge for software. You pay a monthly package price, from {starter_price}, and the campaign, the team and the dashboard are all part of it. Cancel whenever you like from your account."),
        ],
    },
    {
        "article": "influencer-campaigns",
        "kind": "agency",
        "platform": "instagram",
        "slug": "influencer-campaigns",
        "plan": "pro",
        "label": "Influencer outreach and campaigns",
        "title": "Influencer Marketing Outreach: Our Honest Answer | Growsterr",
        "description": "Looking for influencer marketing outreach, seeding or gifting? We don't sell those as packages. We grow your audience monthly; bigger plans start with a talk.",
        "h1": ("Influencer marketing outreach? ", "Let's start with what we actually do."),
        "intro": "Influencer marketing outreach means finding creators, contacting them, sending products, agreeing terms and following up, often with dozens of creators at once. We don't sell outreach, seeding or gifting as packaged services. We grow your own audience with real people every month, and if you're planning a creator campaign, we'd like to hear about it before anyone promises anything.",
        "hero": {"image": "instagram-real-people", "alt": "A brand team planning a creator campaign around a table covered in product samples"},
        "sections": [
            {
                "h2": "What a creator campaign involves",
                "ul": [
                    "Choosing creators whose audience matches yours in place, language and interest.",
                    "Outreach that reads like a person wrote it, and a fair offer: a fee, a product, or both.",
                    "A brief that says what matters and leaves the rest to the creator.",
                    "Clear disclosure on every paid or gifted post.",
                    "A way to measure the result that both sides agreed on beforehand.",
                ],
            },
            {
                "h2": "Seeding, gifting and PR: honest answers",
                "p": [
                    "Seeding and gifting send products to creators in the hope they'll post about them. PR and media agencies place stories with journalists and creators. Each can work, and each depends on relationships and logistics that we don't offer as a set service.",
                    "What we do offer is the part that helps all of those efforts land: a brand profile with a real, growing audience, so the people a creator sends your way find something worth following.",
                ],
            },
            {
                "h2": "Starting the conversation",
                "p": [
                    "If you have a campaign in mind, talk to us on WhatsApp or by email. Tell us the brand, the platforms, where your audience lives and what you'd like to happen. We'll tell you straight what we can take on, and we won't quote deliverables we can't stand behind.",
                ],
            },
        ],
        "faqs": [
            ("Do you do influencer outreach or partnerships for brands?", "Not as a packaged service. Outreach and partnerships depend on the brand, the budget and the creators, so they start with a conversation on WhatsApp or by email. Our set offer is the monthly growth package."),
            ("Do you run influencer gifting or seeding campaigns?", "No. We don't ship products to creators or manage gifting lists. We grow the brand profile those creators send people to."),
            ("Are you an influencer PR, media or relations agency?", "No. We don't pitch media or manage creator relationships on behalf of brands. Our work is audience growth on Instagram, TikTok and YouTube."),
            ("Can a package support a campaign I'm already running?", "Yes. While creators talk about you, a package keeps real people discovering your profile every day, in the place you choose. The dashboard separates what our campaign brought from everything else, so you can see each effort on its own."),
            ("What should I send when I get in touch?", "The brand and its profiles, where your audience lives, the platforms you have in mind, a rough timeline and what success would look like. The clearer the picture, the more useful our answer can be."),
        ],
    },
    # --- AI ------------------------------------------------------------------------------
    {
        "article": "ai-influencer-marketing",
        "kind": "agency",
        "platform": "instagram",
        "slug": "ai-influencer-marketing",
        "label": "Influencer marketing and AI",
        "title": "Influencer Marketing AI: What It Can and Can't Do | Growsterr",
        "description": "Influencer marketing AI can sort data and draft briefs, but it can't be the audience. Where AI helps, and why a team runs our campaigns for real people.",
        "h1": ("Influencer marketing AI ", "can't stand in for the audience."),
        "intro": "Influencer marketing AI is everywhere in 2026: tools that sort creators, draft outreach, flag suspicious followers and even generate whole virtual influencers. Some of it is genuinely useful. None of it changes the core of the job, which is real people paying attention to someone they trust. We don't sell an AI product; a team and a partner network run our campaigns.",
        "hero": {"image": "instagram-real-people", "alt": "Real people reading and replying to a creator's Instagram post on their phones"},
        "sections": [
            {
                "h2": "Where AI genuinely helps",
                "ul": [
                    "Sorting long lists of creators by topic, language and place.",
                    "Spotting follower counts that jump in ways people don't, and comments that repeat.",
                    "Drafting briefs, captions and first versions of outreach for a person to rewrite.",
                    "Summarising campaign results so the people involved can decide faster.",
                ],
            },
            {
                "h2": "Where it can't stand in",
                "p": [
                    "An algorithm can pick a creator; it can't make their audience trust a recommendation. A tool can write a comment; it can't be the person who meant it. And an AI influencer agency promising engagement from generated accounts is selling the same bots as before, with better grammar.",
                    "That's the line we hold. The followers, likes and comments our packages bring come from people who decided to give them.",
                ],
            },
            {
                "h2": "How our campaigns are run",
                "p": [
                    "A team at Growsterr sets up each campaign and looks after it. Your profile is shown to real people through promoted campaigns in our partner network, in the city, region or country you choose, every day for 30 days. Your dashboard records the visits and new followers that came of it.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "A small team reviewing a creator's growth campaign together on a laptop"},
            },
        ],
        "faqs": [
            ("Is Growsterr an AI influencer agency?", "No. We don't sell AI tools, AI-generated engagement or virtual influencers. A team runs every campaign, and the audience is made of real people."),
            ("Do you use AI to find creators for brands?", "We don't run a creator search service, with AI or without it. Brand campaigns with creators start with a conversation on WhatsApp or by email."),
            ("Can AI-written comments help an account?", "Comments written by software tend to read that way, and the people you want to reach notice. Ours come from people who saw your posts, in their own words, inside every package."),
            ("Will AI replace influencers?", "Virtual influencers exist, and some brands experiment with them. But influence rests on trust in a person's taste and judgement, which is hard to generate. We think creators with real audiences will keep the advantage."),
            ("Can AI tell whether an influencer's followers are real?", "Tools can flag patterns, such as sudden jumps, weak engagement or followers from unlikely places, but a person should still look before deciding. The surest sign is engagement that keeps pace with the audience over months."),
        ],
    },
    {
        "article": "ai-instagram-growth",
        "kind": "agency",
        "platform": "instagram",
        "slug": "ai-instagram-growth",
        "label": "AI agents for Instagram growth",
        "title": "Instagram AI Agent for Growth? What Actually Works | Growsterr",
        "description": "Thinking of an Instagram AI agent to grow your account? Agents that follow, like and DM for you need your login. What works in 2026, and how we grow accounts.",
        "h1": ("Want an Instagram AI agent to grow you? ", "Read this before you hand over a login."),
        "intro": "An Instagram AI agent promises to grow your account while you sleep: following, liking, commenting and messaging on your behalf. To do that it needs your login, and it automates the kind of activity Instagram's rules restrict. We're not an Instagram AI agency. A team runs our campaigns, and the people who follow you are people.",
        "hero": {"image": "instagram-followers", "alt": "A phone showing an Instagram login screen next to a warning not to share the password"},
        "sections": [
            {
                "h2": "What growth agents actually do",
                "p": [
                    "Growth agents, AI or not, tend to run the same playbook: follow lots of accounts in your niche, like their posts, leave short comments, then unfollow anyone who doesn't follow back. Some add automated DMs. It's the old follow-unfollow routine with a language model writing the comments.",
                    "The followers it brings followed because you followed them first, and many leave once you unfollow. Meanwhile your account performs hundreds of actions a day that no person would, from a login that now sits on someone else's server.",
                ],
            },
            {
                "h2": "Where AI is useful on Instagram",
                "ul": [
                    "Brainstorming ideas, hooks and series you could post.",
                    "Tidying captions and alt text you've written yourself.",
                    "Reading your own insights and asking better questions of them.",
                    "Planning a posting rhythm you can actually keep.",
                ],
            },
            {
                "h2": "How we grow accounts instead",
                "p": [
                    "We don't act inside your account at all. Your profile is shown to real people through promoted campaigns in our partner network, aimed at the place you choose, and a team watches over each campaign. People who like what they see follow, like and comment on their own; over a month, {pick_name} typically adds {pick_audience} followers.",
                ],
                "image": {"image": "instagram-real-people", "alt": "New followers who found a creator's profile on their own, commenting on a recent post"},
            },
        ],
        "faqs": [
            ("Is there an Instagram AI agent that grows followers safely?", "Any agent that follows, likes or comments for you has to act inside your account, which means handing over your login and automating actions Instagram's rules restrict. We can't speak for how Instagram treats any account, but we won't ask for your login, and we'd advise against giving it to any tool."),
            ("Do you use AI to run my campaign?", "Our campaigns are set up and looked after by a team, and they work through people seeing your profile, not through software acting as you. Nothing is posted, liked or sent from your account."),
            ("Can I try an AI agent without paying?", "Some tools offer a trial, but the real cost is the login you hand over. We don't offer trials; we offer a monthly package you can cancel whenever you like."),
            ("Will AI-written DMs bring me followers?", "Automated messages to strangers read like spam to most people, and some will block or report them. Followers who arrive because they liked your posts are worth far more than replies to a script."),
            ("What should I use AI for instead?", "Making better content faster: ideas, edits, captions you then make your own. Leave the audience to real people, which is where we come in."),
        ],
    },
    # --- Pricing and niches ----------------------------------------------------------------
    {
        "article": "agency-pricing",
        "kind": "agency",
        "platform": "instagram",
        "slug": "influencer-agency/pricing",
        "label": "Influencer agency pricing",
        "title": "Instagram Marketing Agency Pricing, Explained | Growsterr",
        "description": "How Instagram marketing agency pricing usually works, what drives TikTok agency cost, and our three monthly packages from {starter_price}, with nothing hidden.",
        "h1": ("Instagram marketing agency pricing, ", "laid out plainly."),
        "intro": "Instagram marketing agency pricing is hard to compare: retainers, setup fees, creator fees and percentages, often only after a call. Ours fits on one line. Three monthly packages, {starter_name} at {starter_price}, {rising_name} at {rising_price} and {pro_name} at {pro_price}, the same on Instagram, TikTok and YouTube.",
        "hero": {"image": "instagram-followers-1000", "alt": "Three monthly growth packages laid out side by side with their prices"},
        "sections": [
            {
                "h2": "How agencies usually charge",
                "ul": [
                    "A monthly retainer for ongoing management, often with a minimum term.",
                    "A project fee for a single campaign, quoted after a brief.",
                    "Creator fees passed through, sometimes with a management percentage on top.",
                    "Media budgets for ads, separate from the agency's own fee.",
                ],
                "p": [
                    "None of these is wrong. They just make two quotes hard to compare unless you ask what each line actually buys.",
                ],
            },
            {
                "h2": "What a TikTok agency costs with us",
                "p": [
                    "The same as on Instagram or YouTube: one package price a month, with no setup fee, no minimum term and no media budget on top. {starter_name} typically brings {starter_audience} new followers a month, {rising_name} {rising_audience} and {pro_name} {pro_audience}, each with likes and comments from the same people.",
                ],
            },
            {
                "h2": "What the price includes",
                "ul": [
                    "A campaign every day for 30 days, aimed at the city, region or country you choose.",
                    "New followers, likes, comments and views from the same real people.",
                    "A team behind the campaign, and a dashboard of what it measured.",
                    "On {rising_name} and {pro_name}, the choice of which posts get the attention; on {pro_name}, priority placement and a direct WhatsApp line too.",
                ],
            },
        ],
        "faqs": [
            ("Why don't you need a call before quoting?", "Because our packages are the same for everyone, there's nothing to quote. Calls make sense for custom work; for anything beyond the packages, talk to us on WhatsApp or by email."),
            ("Are there extra fees?", "No. The package price is what you pay each month, charged in US dollars by card, Apple Pay or Google Pay through Stripe."),
            ("Can I pay for just one month?", "In effect, yes: subscribe, then cancel from your account whenever you like. The month you paid for runs to its end and nothing more is charged."),
            ("Do you offer discounts for longer commitments?", "No. There are no annual plans or long-term discounts; every package is billed monthly and can be stopped at any time."),
            ("What would a custom campaign cost?", "That depends entirely on what it involves, so we won't put a number on a page. Tell us what you have in mind on WhatsApp or by email and we'll answer honestly, including when the answer is that it isn't something we do."),
            ("Is a cheaper agency a better deal?", "Only if it brings the same thing. A price per thousand followers is a price for accounts, not people. Compare what arrives, how it's measured and how easily you can stop."),
        ],
    },
    {
        "article": "influencer-agency-gaming",
        "kind": "agency",
        "platform": "instagram",
        "slug": "influencer-agency/gaming",
        "label": "Influencer agency for gaming",
        "title": "Influencer Agency for Gaming Creators and Studios | Growsterr",
        "description": "An influencer agency for gaming? We grow gaming creators and studios on YouTube, TikTok and Instagram with real people. No live viewers, no bots.",
        "h1": ("An influencer agency for gaming, ", "built around real players."),
        "intro": "Gaming audiences can tell a bot from a player with one look at the comments. That's why we think an influencer agency for gaming has to start with real people. Our packages work for gaming creators, streamers who post clips and game studios on YouTube, TikTok and Instagram, aimed at the region where your players are.",
        "hero": {"image": "youtube-channel", "alt": "A gaming creator's desk with a controller, a microphone and a channel page on screen"},
        "sections": [
            {
                "h2": "Where gaming audiences grow",
                "p": [
                    "Gaming lives across platforms: long videos and guides on YouTube, clips and moments on TikTok, art, updates and community on Instagram. Live streaming is the one part we don't touch: we don't work on Twitch, and we don't sell live viewers anywhere.",
                    "If you stream, the clips and highlights you post on YouTube, TikTok or Instagram are where we can help. Real people who enjoy them follow, and some of them will go looking for your streams.",
                ],
            },
            {
                "h2": "For game studios and gaming brands",
                "p": [
                    "A studio's own channels are where players go after a trailer, a creator's video or a launch. Growing them with real people, aimed at the regions you launch in, means each announcement reaches more people who might play. Campaigns with gaming creators are a separate conversation: talk to us on WhatsApp or by email.",
                ],
                "image": {"image": "tiktok-creator", "alt": "A gaming creator cutting a highlight clip into a short vertical video"},
            },
            {
                "h2": "What we don't do in gaming",
                "ul": [
                    "Distribute game keys or run giveaways.",
                    "Sponsor esports teams or events.",
                    "Sell live viewers, chat activity or followers on streaming platforms.",
                    "Promise that a video or clip reaches a particular number of people.",
                ],
            },
        ],
        "faqs": [
            ("Can you grow a gaming YouTube channel?", "Yes. Real people in the place you choose discover your channel and subscribe if they like it. You can also name one video as the landing point: new viewers subscribe first and then watch it."),
            ("Do you work with Twitch streamers?", "Not on Twitch itself. If you post clips or highlights on YouTube, TikTok or Instagram, we can grow those accounts, and some of that audience may follow you to your streams."),
            ("Can you target gamers in a particular region?", "You can target a city, region or country. We don't target by interest, so your content decides whether gamers follow: post what players in that place care about."),
            ("Can game studios use your packages?", "Yes. A studio's Instagram, TikTok or YouTube runs the same packages as a creator's, from {starter_price} a month. Creator campaigns for a game launch start with a conversation on WhatsApp or by email."),
            ("Will I get comments from real players?", "Comments come from the people who discover your content, in their own words: typically {pick_comments} a month with {pick_name}. Gaming comment sections are blunt, and real ones are worth more than any script."),
        ],
    },
    {
        "article": "influencer-agency-fashion",
        "kind": "agency",
        "platform": "instagram",
        "slug": "influencer-agency/fashion",
        "label": "Influencer agency for fashion",
        "title": "Influencer Agency for Fashion Brands and Creators | Growsterr",
        "description": "An influencer agency for fashion that grows the audience itself: real people discover your label or style profile, from the cities you choose, every day.",
        "h1": ("An influencer agency for fashion, ", "measured in real followers."),
        "intro": "Fashion lives on Instagram and TikTok, and so does fake engagement. If you're looking for an influencer agency for fashion, you'll want one that grows an audience of people who actually dress, shop and comment. That's what our packages do for fashion creators, stylists, boutiques and labels: real people, from the cities you choose, every month.",
        "hero": {"image": "instagram-followers", "alt": "A boutique's Instagram profile with outfit posts and new followers from its city"},
        "sections": [
            {
                "h2": "Why place matters so much in fashion",
                "p": [
                    "Fashion is local in ways that count: climate, sizes, price points, the shops people can reach. A boutique in Milan needs followers who can visit; a label shipping across a country needs people in that country. Name the city, region or country and that's where your profile is shown first.",
                ],
            },
            {
                "h2": "Drops, lookbooks and the posts that count",
                "p": [
                    "In fashion, some posts matter more than others: a new collection, a lookbook, a collaboration. With {rising_name} or {pro_name}, you choose which posts get the attention, so more people see the one that matters. We don't promise likes or views on any single post; people decide what they like.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "A fashion creator arranging outfit photos for a new Instagram lookbook"},
            },
            {
                "h2": "What we leave to fashion PR and gifting agencies",
                "p": [
                    "We don't send products to creators, run seeding lists, book shoots or place your brand with editors. Those are real crafts with their own agencies. If you're planning a creator campaign around a collection, talk to us on WhatsApp or by email and we'll tell you honestly what we can take on.",
                ],
            },
        ],
        "faqs": [
            ("Do you work with fashion brands or fashion creators?", "Both. Labels, boutiques, stylists and fashion creators can run the same packages, aimed at the people they want to reach. Any public Instagram, TikTok or YouTube profile can start."),
            ("Can you get my brand in front of fashion influencers?", "Not as part of a package. We grow your own audience; partnerships with creators start with a conversation on WhatsApp or by email."),
            ("Will followers suit my style?", "You choose the place; your posts choose the people. Those who like your style follow and those who don't move on, which keeps your audience coherent."),
            ("How much can a fashion account grow in a month?", "A typical month brings {starter_audience} new followers on {starter_name}, {rising_audience} on {rising_name} and {pro_audience} on {pro_name}, along with likes and comments from the same people. Ranges, never promises."),
            ("Do you need access to my shop or my account?", "No. We need your username, a public profile and the place your audience lives. Your shop, your account and your login stay yours."),
        ],
    },
    # --- The creator side ------------------------------------------------------------------
    {
        "article": "creators",
        "kind": "agency",
        "platform": "instagram",
        "slug": "creators",
        "label": "For creators: grow or work with us",
        "title": "Influencer Talent Agency? What We Offer Creators | Growsterr",
        "description": "Looking for an influencer talent agency? We don't sign creators or take a cut of their deals. We grow audiences with real people, and we're open to ideas.",
        "h1": ("Looking for an influencer talent agency? ", "Here's what we offer creators."),
        "intro": "An influencer talent agency signs creators to a roster, finds them brand deals and takes a percentage. We're not that. Growsterr is a growth agency for creators: we grow your audience with real people every month, and if you'd like to work with us in other ways, you can write to us. No roster, no commission, nothing to sign.",
        "hero": {"image": "instagram-creator-studio", "alt": "A creator at a desk planning content with a phone, a notebook and a ring light"},
        "sections": [
            {
                "h2": "Talent management, booking and casting: what they do",
                "p": [
                    "Talent and management agencies represent creators: they negotiate brand deals, handle contracts and invoices, and often shape a creator's career, in return for a share of what they bring in. Booking and casting agencies match creators to specific campaigns, sometimes for a single shoot or post.",
                    "If you want representation, those are the people to talk to. We don't keep a roster, book creators or broker deals, and we'd rather you heard that from us now.",
                ],
            },
            {
                "h2": "What we do for creators of every size",
                "p": [
                    "We grow the audience brands look at. Your profile is shown to real people in the place you choose, every day; those who like your work follow, like and comment. It works the same for a micro creator with a few hundred followers as for an established one with a large following.",
                ],
                "ul": [
                    "{starter_name}, for new and small accounts: typically {starter_audience} new followers a month for {starter_price}.",
                    "{rising_name}, for creators ready to grow faster: typically {rising_audience}, and you pick the posts that get the attention.",
                    "{pro_name}, for established creators: typically {pro_audience}, with priority placement and a direct WhatsApp line.",
                ],
            },
            {
                "h2": "Want to work with us?",
                "p": [
                    "If you're a creator with an idea for working together beyond a package, you can apply by writing to us on WhatsApp or by email. It's a message, not a form, and it commits you to nothing.",
                ],
            },
        ],
        "faqs": [
            ("Will you represent me or find me brand deals?", "No. We don't manage creators or negotiate deals, and we don't take a share of your earnings. We grow your audience, which is what brands look at when they decide who to work with."),
            ("Do you work with small and micro creators?", "Yes. {starter_name} was designed with new and small accounts in mind. Small creators often have the most to gain from real people, because every new follower shows up in the engagement."),
            ("Is there a roster I can join?", "No, we don't keep one. If you'd like to work with us beyond a package, write to us on WhatsApp or by email and tell us who you are and what you have in mind."),
            ("Do you work with KOLs and creators outside Europe?", "Yes. We work remotely with creators wherever they are, and your campaign can target the city, region or country where your audience lives. Prices are in US dollars, paid through Stripe."),
            ("Are you an Instagram creator agency or a handling agency?", "We're a growth agency for creators on Instagram, TikTok and YouTube. We don't handle accounts, post for you or manage your inbox; we bring real people to your profile and leave the rest to you."),
            ("Do I keep control of my account?", "Completely. We never sign in, post or change anything; all we need is your username and a public profile. Everything about your content stays your decision."),
        ],
    },
    {
        "article": "creators-apply",
        "kind": "agency",
        "platform": "instagram",
        "slug": "creators/apply",
        "plan": "starter",
        "label": "Apply to work with Growsterr",
        "title": "Want to Apply to an Influencer Agency? Start Here | Growsterr",
        "description": "Want to apply to an influencer agency? With us, applying means writing to us on WhatsApp or by email. What to include, what we can offer, and what we can't.",
        "h1": ("Applying to an influencer agency? ", "With us, it starts with a message."),
        "intro": "Agency applications often mean a long form and a longer wait. With us, applying is simpler: you write to us on WhatsApp or by email, tell us who you are and what you'd like to do together, and we take it from there. Before you write, here's what we can offer creators, and what we honestly can't.",
        "hero": {"image": "instagram-real-people", "alt": "A creator typing a message on a phone to introduce their work"},
        "sections": [
            {
                "h2": "What to put in your message",
                "ul": [
                    "Your name and the platform you create on: Instagram, TikTok or YouTube.",
                    "Your username or channel handle, so we can look at your work.",
                    "Where most of your audience lives, and the language you post in.",
                    "What you have in mind: growing with us, working with us, or simply a question.",
                ],
            },
            {
                "h2": "What we can and can't offer",
                "p": [
                    "We can grow your audience with real people through our monthly packages, and we're happy to talk through any idea for working together.",
                    "We can't promise paid work, brand deals or a place on a roster, because we don't keep one. We don't post gigs, recruit creators in bulk or charge anyone to apply. If someone asks you for money to join an influencer agency, be careful.",
                ],
            },
            {
                "h2": "Influencer marketing gigs: a word of caution",
                "p": [
                    "Offers of paid gigs that arrive by DM, ask for an upfront fee or want your login to 'manage' your account are among the oldest tricks aimed at creators. A real brand or agency tells you who they are, puts the terms in writing and never asks for your password.",
                ],
            },
        ],
        "faqs": [
            ("How do I apply to work with Growsterr?", "Write to us on WhatsApp or by email with your handle, your platform, where your audience is and what you'd like to do. That message is the whole application."),
            ("Do you pay creators?", "We don't offer paid gigs or a creator programme with set fees. If an idea for working together involves payment, we'll discuss it openly before anything is agreed."),
            ("Is there a follower minimum to apply?", "No. You can write to us at any size. Our packages start with {starter_name}, made for new and small accounts."),
            ("Does applying cost anything?", "No. Writing to us costs nothing and commits you to nothing. The only thing we ever charge for is a monthly growth package, and only if you choose one."),
            ("Are you an influencer recruitment agency?", "No. We don't recruit creators for brands or fill campaign slots. We're a growth agency, and we're open to hearing from creators who'd like to work with us."),
        ],
    },
    # --- Guides ----------------------------------------------------------------------------
    {
        "article": "best-influencer-agencies",
        "kind": "guide",
        "platform": "instagram",
        "slug": "guides/best-influencer-agencies",
        "label": "How to choose an influencer agency",
        "title": "Best Influencer Agency? How to Judge the Top Ones | Growsterr",
        "description": "Looking for the best influencer agency or a list of top agencies? How to read lists and reviews, the questions to ask, and the warning signs to walk away from.",
        "h1": ("The best influencer agency ", "is the one that fits your goal."),
        "intro": "Every list of the best influencer agencies orders them differently, because each is answering a different question. A top agency for a global launch is the wrong one for a local café, and the other way round. Rather than another list, this guide covers how to read the lists and reviews you'll find, what to ask before signing, and where a growth agency like ours fits.",
        "hero": {"image": "instagram-hub", "alt": "A marketer comparing several influencer agency websites in open browser tabs"},
        "sections": [
            {
                "h2": "Why influencer agency lists disagree",
                "p": [
                    "Lists are often written by publishers who earn a fee when a reader contacts an agency, or by agencies placing themselves near the top. Even honest lists compare very different businesses: talent managers, full-service agencies, software platforms and growth agencies all end up on the same page.",
                    "Reviews help with the details, not the verdict. Look for how long the reviewer worked with the agency, what was promised at the start, and how reporting and leaving went.",
                ],
            },
            {
                "h2": "Questions to ask any influencer agency",
                "ul": [
                    "What exactly will you do each month, and what will I see as a result?",
                    "Where do the people who see my brand or profile come from?",
                    "Do you need access to my accounts, and why?",
                    "How do you check that creators' audiences are real?",
                    "What are the fees, what's the minimum term, and how do I stop?",
                    "Can I speak to the people who will actually do the work?",
                ],
            },
            {
                "h2": "Warning signs worth walking away from",
                "ul": [
                    "Exact follower or view numbers promised in advance.",
                    "A request for your password.",
                    "Results that appear overnight.",
                    "Case studies with no names, dates or way to check them.",
                    "Long contracts with no clear way out.",
                ],
            },
            {
                "h2": "Where Growsterr fits",
                "p": [
                    "We're a growth agency, not a full-service influencer agency. We run monthly campaigns that show your profile to real people in the place you choose, a team looks after each one, and your dashboard shows what was measured. We don't manage creators or broker deals; for anything beyond our packages, talk to us on WhatsApp or by email.",
                ],
            },
        ],
        "faqs": [
            ("Which is the best influencer agency?", "We won't name one, partly because we're an agency ourselves and partly because the answer depends on your goal, budget and platform. Use the questions above with any agency you're considering, us included."),
            ("Can I trust influencer agency reviews?", "Some of them. Reviews written after months of working together tell you far more than ones written after a first call. Be wary of a page full of glowing quotes with no way to check who wrote them."),
            ("What's the difference between a top agency and a small one?", "Large agencies bring scale, creator networks and experience with big brands; small ones often bring attention and flexibility. Neither is better in general: ask who will work on your account and how much of their time you get."),
            ("Do I need an influencer agency at all?", "Not always. If you want to grow your own profile, a monthly growth package may be all you need. If you want campaigns with many creators, an agency or a platform saves a great deal of work."),
            ("Why doesn't this guide include a list of agencies?", "Because we'd be judging competitors, and we don't think that's ours to do fairly. The checks in this guide work on any list you come across."),
        ],
    },
    {
        "article": "how-influencer-agencies-work",
        "kind": "guide",
        "platform": "instagram",
        "slug": "guides/how-influencer-agencies-work",
        "label": "How influencer agencies make money",
        "title": "Influencer Agency Revenue: How Agencies Make Money | Growsterr",
        "description": "How influencer agencies earn their revenue: retainers, project fees, creator commissions and margins. What each model means for you, and how Growsterr is paid.",
        "h1": ("Influencer agency revenue: ", "who pays, and for what."),
        "intro": "Knowing where an influencer agency's revenue comes from tells you whose side it's on. Some are paid by brands, some by creators, some by both, and some earn a margin you never see. Here are the common models, what each means for the person signing, and the one we use: a monthly package with its price on the page.",
        "hero": {"image": "instagram-creator-studio", "alt": "A creator reading through an agency contract at a desk with a laptop open"},
        "sections": [
            {
                "h2": "The common ways influencer agencies earn",
                "ul": [
                    "Retainers: a monthly fee from a brand for ongoing work, often with a minimum term.",
                    "Campaign fees: a price per project, quoted after a brief.",
                    "Margins on creator fees: the agency pays the creator one price and bills the brand another.",
                    "Commission from creators: talent agencies keep a share of the deals they negotiate.",
                    "Software subscriptions: platforms charge for access to their tools and creator data.",
                ],
            },
            {
                "h2": "What each model means for you",
                "p": [
                    "Whoever pays the agency is the client it answers to. A talent agency negotiating for a creator wants the highest fee; an agency billing a brand wants the campaign to look good in the report. Margins and markups aren't wrong, but it's fair to ask whether there are any, and how large.",
                    "For creators, the question to put to any agency is simple: what share of my income do you take, and what do you do for it?",
                ],
            },
            {
                "h2": "How Growsterr is paid",
                "p": [
                    "One way only: the monthly package you choose, from {starter_price} to {pro_price}, paid through Stripe. We don't take commission from creators or mark up anyone's fees. The price on the page is the whole of what we earn from you.",
                ],
            },
        ],
        "faqs": [
            ("How do influencer agencies make money?", "Usually through brand retainers and campaign fees, margins on what they pay creators, commission from the creators they represent, or software subscriptions. Many combine more than one."),
            ("Do influencer agencies take a percentage from creators?", "Talent and management agencies usually do, in return for finding and negotiating deals. Agencies that work for brands are typically paid by the brand instead."),
            ("Is a percentage or a flat fee better?", "A flat fee is easier to compare and budget for; a percentage ties the agency's income to results. Whichever you choose, get it in writing, along with what happens when you want to stop."),
            ("Does Growsterr take a share of my brand deals?", "No. We aren't involved in your deals at all. You pay for a monthly growth package, and anything you earn from your audience is yours."),
            ("Why do some agencies only quote after a call?", "Because custom work really does vary. It's still reasonable to ask for a written breakdown afterwards, so you can compare what each part costs."),
        ],
    },
    {
        "article": "influencer-marketing-report-2026",
        "kind": "guide",
        "platform": "instagram",
        "slug": "guides/influencer-marketing-report-2026",
        "label": "Influencer marketing in 2026",
        "title": "Influencer Marketing News and Trends for 2026 | Growsterr",
        "description": "Influencer marketing news for 2026 without made-up figures: the trends that matter, how to read the reports, and what will likely still hold in 2027 and beyond.",
        "h1": ("Influencer marketing news for 2026, ", "minus the made-up numbers."),
        "intro": "Influencer marketing news in 2026 comes with no shortage of reports, forecasts and market figures. We don't publish market data, and we won't repeat numbers we can't check. What we can offer is a plain reading of the trends that matter to creators and brands this year, and a guide to judging the reports you'll come across.",
        "hero": {"image": "instagram-followers-1000", "alt": "A creator reading industry reports on a tablet beside a growth chart"},
        "sections": [
            {
                "h2": "Trends worth paying attention to in 2026",
                "ul": [
                    "Short video is the default format on Instagram, TikTok and YouTube alike, and creators plan for all three at once.",
                    "Brands look harder at whether an audience is real, using engagement, audience location and growth history.",
                    "Smaller creators with close audiences get more serious attention, especially from local and niche brands.",
                    "Disclosure is stricter: platforms build paid partnership labels into posting, and regulators in several countries have tightened their guidance.",
                    "Platforms now label some AI-generated content, and audiences are quicker to ask what's real.",
                    "Longer partnerships with fewer creators are becoming a common alternative to one-off posts.",
                ],
            },
            {
                "h2": "How to read an influencer marketing report",
                "ul": [
                    "Who made it? Reports from platforms and agencies often reflect their own customers.",
                    "Is it a survey or measured data? Surveys tell you what people say, not what they do.",
                    "How big and how local is the sample? A global average can hide everything that matters in your country.",
                    "Does a forecast for 2027 or 2030 explain its method, or just extend a line?",
                ],
            },
            {
                "h2": "What will probably still hold in 2027 and beyond",
                "p": [
                    "Formats and platforms will keep changing. What has held through every change so far is that attention from real people is the scarce thing, and that audiences reward creators they trust. Any strategy that fakes either one tends to stop working the moment it's noticed.",
                ],
            },
            {
                "h2": "Where this leaves creators and brands",
                "p": [
                    "For creators: build an audience that would survive any brand's audit. For brands: grow your own profile so creator traffic lands somewhere worth staying. Our monthly packages do the growing with real people, from {starter_price} a month, and for anything larger you can talk to us on WhatsApp or by email.",
                ],
            },
        ],
        "faqs": [
            ("Is there a PDF of this report?", "No. This page is all of it, and we update it when something important changes. Nothing is locked behind a form or an email address."),
            ("How big is the influencer marketing industry in 2026?", "Estimates vary widely depending on who counts what, and we don't produce our own. If you need a figure, take it from a source that explains its method, and compare two or three before relying on one."),
            ("What changed between 2024, 2025 and 2026?", "Mostly a shift in emphasis: from follower counts towards engagement and audience quality, from single posts towards longer partnerships, and towards clearer labels for paid and AI-generated content."),
            ("Where can I follow influencer marketing updates?", "The platforms' own creator and business blogs announce changes first, and advertising regulators publish their disclosure rules. Those are better sources than secondhand summaries, ours included."),
            ("What's the most useful benchmark for my own account?", "Your own history. Compare engagement, follower growth and where your audience lives month by month; that tells you more than any industry average."),
        ],
    },
    {
        "article": "what-is-influencer-marketing",
        "kind": "guide",
        "platform": "instagram",
        "slug": "guides/what-is-influencer-marketing",
        "label": "What is influencer marketing?",
        "title": "Influencer Marketing Examples, Meaning and Strategy | Growsterr",
        "description": "What influencer marketing means, with everyday examples, a simple strategy, the funnel and the KPIs worth tracking. A plain guide for brands and creators.",
        "h1": ("Influencer marketing examples, ", "meaning and a strategy that works."),
        "intro": "Influencer marketing means working with people whose audiences trust them, so that a recommendation reaches people who'll actually listen. The meaning is simple; doing it well isn't. Here's a plain definition, influencer marketing examples you'll recognise from your own feed, a strategy you can follow, and the KPIs worth tracking.",
        "hero": {"image": "instagram-real-people", "alt": "A creator recommending a product to followers who reply with questions"},
        "sections": [
            {
                "h2": "Influencer marketing, defined",
                "p": [
                    "A brand works with a creator, and the creator presents the brand to their audience in their own way: a review, a tutorial, a day-in-the-life video, a discount code. The audience listens because they already follow the creator for a reason. That borrowed trust is the whole value, and it's why fake audiences make influencer marketing worthless.",
                ],
            },
            {
                "h2": "Influencer marketing examples from everyday feeds",
                "ul": [
                    "A local bakery invites a food creator from the same city to film the morning bake.",
                    "A skincare brand sends products to several small creators who each post an honest routine.",
                    "A software company sponsors a segment of a YouTube tutorial its users already watch.",
                    "A fitness creator launches a programme and partners with an apparel label for a joint post.",
                    "A travel creator makes a series about a region, paid for by its tourism board.",
                ],
            },
            {
                "h2": "A simple influencer marketing strategy",
                "ul": [
                    "Start with one goal: awareness, followers, sign-ups or sales.",
                    "Pick creators whose audience matches yours in place, language and interest.",
                    "Make sure your own profile is ready for the visitors a creator will send.",
                    "Agree on disclosure, timing and what you'll measure before anything is posted.",
                    "Judge results over weeks, not hours, and keep working with the creators who perform.",
                ],
            },
            {
                "h2": "The funnel, and the KPIs worth tracking",
                "p": [
                    "At the top of the funnel, influencer marketing creates awareness: reach, views and profile visits. In the middle it builds consideration: follows, saves, comments and clicks. At the bottom it drives action: sign-ups, codes used and sales. Track the KPIs for the stage you're aiming at, and don't judge an awareness campaign by its sales.",
                    "Growth packages like ours work in the middle of that funnel: real people visit your profile and choose to follow. With {pick_name}, that's typically {pick_audience} new followers a month, with likes and comments from the same people.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "A marketer sketching an awareness, consideration and action funnel on a notepad"},
            },
        ],
        "faqs": [
            ("What is influencer marketing in simple words?", "A brand asks a trusted creator to show or recommend something to their audience. It works because people listen to creators they chose to follow."),
            ("Is influencer marketing effective?", "It can be, when the creator's audience is real and matches the brand. It fails when the audience is bought, the fit is poor or the brief smothers the creator's voice."),
            ("What do influencer marketing 2.0 and 3.0 mean?", "They're loose labels, not standards. People use them for the move from one-off sponsored posts to longer partnerships and, more recently, to creators acting as businesses and media in their own right."),
            ("Do I need an agency for influencer marketing?", "Not to start. A small brand can contact a few local creators itself. Agencies help when you work with many creators at once; growth agencies like ours help with the audience on your own profile."),
            ("Which influencer marketing KPIs matter most?", "The ones tied to your goal. For awareness, reach and views; for an audience, profile visits and new followers; for sales, tracked links and codes. Our dashboard covers the audience part: visits and new followers, day by day."),
        ],
    },
]
