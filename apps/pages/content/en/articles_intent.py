"""English intent articles: TikTok shares, saves, reposts, music promotion and Shop followers,
and growth by country on each platform. Things people ask for that sit outside the platform x
service grid; each page answers honestly and leads to the monthly package. Keys and
placeholders: docs/CONTENT.md; angles: docs/keywords/WRITING.md."""

UPDATED = "2026-11-08"

ARTICLES = [
    # --- TikTok: what viewers do that nobody can sell -------------------------------------
    {
        "article": "tiktok-shares",
        "kind": "intent",
        "platform": "tiktok",
        "slug": "tiktok/shares",
        "label": "TikTok shares",
        "title": "Buy TikTok Shares? Why Real Ones Come From Viewers | Growsterr",
        "description": "Want to buy TikTok shares? We don't sell shares. A share is a viewer sending your video to someone, and only real viewers inside our packages do that.",
        "h1": ("Buy TikTok shares? ", "A share needs someone to send it to."),
        "intro": "If you want to buy TikTok shares, think about what a share does: a viewer sends your video to a friend, a group chat or another app, and a new person watches. Bought shares send it nowhere. We don't sell shares on their own and never will. They come from the real people our packages bring to your profile, when a video is good enough to pass on.",
        "hero": {"image": "tiktok-watch-time", "alt": "A viewer sending a TikTok video to a friend in a private message"},
        "sections": [
            {
                "h2": "Why shares matter so much on TikTok",
                "p": [
                    "A like says 'I enjoyed this'. A share says 'you should see this', and it brings a new viewer along. That's why creators care about shares: each one is a small recommendation from one person to another, and the video's reach grows by exactly the people it was sent to.",
                ],
            },
            {
                "h2": "What bought TikTok video shares do",
                "ul": [
                    "The share counter goes up, but the video goes to no one, or to accounts that never open it.",
                    "No new viewers arrive, so nothing else on the video moves.",
                    "The order lands on one video, at one moment, in a round number: the pattern of a purchase.",
                    "Cheap shares are cheap because there's no person and no recipient anywhere in the chain.",
                ],
            },
            {
                "h2": "Real TikTok shares, from real viewers",
                "p": [
                    "We put your profile in front of real people daily through our campaigns. Some of them watch a video and send it on, the way people share anything they enjoy. We don't count or forecast shares, and we can't steer them to a particular video, because sharing is the most personal choice a viewer makes. What we do measure is in your dashboard: daily profile visits and the follows they turned into.",
                ],
                "image": {"image": "tiktok-likes", "alt": "A TikTok video passed between friends after one of them discovered it"},
            },
        ],
        "faqs": [
            ("Can I buy shares on TikTok from Growsterr?", "No. We don't sell shares, alone or as an add-on. Shares happen when the real people our packages bring decide a video is worth passing on."),
            ("Can you tell me how many shares to expect?", "We can't say, and we don't promise any. Shares depend on the video: useful, funny or surprising videos get shared, and others don't, whoever watches them."),
            ("Are real TikTok shares worth more than likes?", "They do something a like can't: bring someone new to the video. That's why the videos that get shared are often made with a particular person in mind, the 'send this to a friend who…' kind."),
            ("Are cheap TikTok shares risky?", "They come from accounts acting on command, which TikTok's rules count as fake engagement. They also achieve nothing, because nobody receives them: money spent on a number only you will look at."),
            ("What do the packages include, then?", "Real people who follow, like and comment: on {starter_name} ({starter_price} a month) that's typically {starter_audience} followers. Shares, saves and reposts happen on top, whenever people choose."),
        ],
    },
    {
        "article": "tiktok-saves",
        "kind": "intent",
        "platform": "tiktok",
        "slug": "tiktok/saves",
        "label": "TikTok saves and favorites",
        "title": "Buy TikTok Saves? What a Real Save Means | Growsterr",
        "description": "Thinking of buying TikTok saves or favorites? A save means someone plans to come back. Bought saves never return; real viewers from our packages might.",
        "h1": ("Buy TikTok saves? ", "Make videos people want to keep."),
        "intro": "A save on TikTok, the bookmark that adds a video to someone's Favorites, is a promise to come back: to the recipe, the workout, the tutorial step they'll need later. If you want to buy TikTok saves, know that bought ones keep no promise; the accounts behind them never return. We don't sell saves. They come from the real people our packages bring, when your video is worth keeping.",
        "hero": {"image": "tiktok-creator", "alt": "A creator filming a step-by-step TikTok recipe that viewers save for later"},
        "sections": [
            {
                "h2": "What a save tells you",
                "p": [
                    "Likes measure enjoyment in the moment. Saves measure usefulness over time: the viewer expects to need this again. That's why saves cluster on certain videos, such as how-tos, recipes, lists, places to visit and product picks, and why a high save count is one of the clearest signs a video gave people something.",
                ],
            },
            {
                "h2": "Buying TikTok favorites: what you'd get",
                "ul": [
                    "A save counter that rises while nobody's Favorites list holds your video for a reason.",
                    "No return visits: the second view that gives a save its meaning never happens.",
                    "Saves with no likes, comments or follows beside them, a mismatch anyone can see on the video.",
                    "Cheap saves in round numbers, all on the one video they were ordered for.",
                ],
            },
            {
                "h2": "How to earn more saves",
                "ul": [
                    "Pack the video with something people will need later: steps, amounts, names, places.",
                    "Say why it's worth keeping: 'for your next trip' gives people a reason to tap the bookmark.",
                    "Make series, so saving one video means coming back for the next.",
                    "Put the useful part on screen as text, so a returning viewer finds it fast.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "A viewer reopening a saved TikTok tutorial from their Favorites"},
            },
        ],
        "faqs": [
            ("Do you sell TikTok saves or favorites?", "No. Saves aren't sold on their own or added to packages. The real people our packages bring save whatever they want to keep, by themselves."),
            ("Are saves and favorites the same thing on TikTok?", "Yes. Tapping the bookmark icon saves a video to the viewer's Favorites, so people use both words for the same action."),
            ("Will my videos get saves from your package?", "Some will, if they're worth keeping. We can't count saves in advance or direct them to a video; people choose what to save. What we bring is the people, {starter_audience} new followers in a typical {starter_name} month."),
            ("Are cheap TikTok saves worth it?", "No. A save is valuable because a person intends to come back. A bought save has no person behind it, so it adds a number without anything the number is supposed to mean."),
            ("Which videos get saved most?", "Ones with lasting value: tutorials, recipes, recommendations, workouts, travel tips, and anything with more information than people can remember in one go."),
        ],
    },
    {
        "article": "tiktok-reposts",
        "kind": "intent",
        "platform": "tiktok",
        "slug": "tiktok/reposts",
        "label": "TikTok reposts",
        "title": "Buy TikTok Reposts? How Real Reposts Spread | Growsterr",
        "description": "Want to buy TikTok reposts? A repost shows your video to the reposter's own followers. Bought reposts reach empty audiences; real ones come from real viewers.",
        "h1": ("Buy TikTok reposts? ", "A repost is only as good as its audience."),
        "intro": "A repost on TikTok passes your video to the people who follow whoever reposted it. That's the whole value, and it's why buying TikTok reposts makes little sense: an account made to repost on command has no real audience to pass your video to. We don't sell reposts. They come, now and then, from the real people our packages bring to your profile.",
        "hero": {"image": "tiktok-hub", "alt": "A TikTok video marked as reposted, appearing for the reposter's friends"},
        "sections": [
            {
                "h2": "How a repost works",
                "p": [
                    "When someone taps Repost, your video can show up for their friends and followers, marked as reposted by them. The reposter is vouching for it in front of people who know them. It's word of mouth built into the app, and it works because the reposter has an audience that trusts their taste.",
                ],
            },
            {
                "h2": "Why buying reposts on TikTok falls flat",
                "ul": [
                    "The reposting accounts have no real followers, so your video is passed to nobody.",
                    "The repost count rises with no new views behind it.",
                    "They're ordered for one video in one batch, which is how they're spotted.",
                    "They're the kind of activity TikTok sweeps away when it clears out fake engagement.",
                ],
            },
            {
                "h2": "Earning reposts from real people",
                "p": [
                    "People repost what says something for them: a joke they wish they'd made, an opinion they share, a tip their friends need. Make videos people want to be associated with, and the real viewers our campaigns bring will sometimes do the passing on. We don't count reposts or promise them, and we can't send them to a chosen video; what we measure is visits and new followers.",
                ],
                "image": {"image": "tiktok-creator", "alt": "A creator recording an opinion video that viewers want to pass on"},
            },
        ],
        "faqs": [
            ("Can I buy reposts on TikTok from you?", "No. Reposts aren't for sale, separately or in a package. They happen when a real viewer decides your video belongs in front of their own followers."),
            ("Is a repost the same as a share?", "Not quite. A share sends the video to particular people or to another app; a repost puts it in front of the reposter's followers on TikTok itself. Both start with a viewer who liked it enough to pass it on."),
            ("Do reposts bring followers?", "They can, when the people who see a repost like your video enough to visit your profile. That only happens when the reposter has a real audience."),
            ("Why can't you promise reposts?", "Because a repost is a person putting their name next to your video. Nobody can decide that for them, and a service that says it can is using accounts with no one behind them."),
            ("How do your packages help with reposts?", "Indirectly: more real people see your videos, and each of them could repost one. With {pick_name} that typically means {pick_audience} new followers a month, plus the visitors who watched without following."),
        ],
    },
    {
        "article": "tiktok-sound-promotion",
        "kind": "intent",
        "platform": "tiktok",
        "slug": "tiktok/music-promotion",
        "label": "TikTok music promotion",
        "title": "TikTok Music Promotion: What We Do and Don't | Growsterr",
        "description": "Looking for TikTok music promotion? We don't run sound campaigns or pay creators to use your song. We grow your artist account with real people who hear it.",
        "h1": ("TikTok music promotion, honestly: ", "we grow the artist, not the sound."),
        "intro": "Most TikTok music promotion means paying creators to use a song in their videos. We don't do that, and we don't run sound campaigns. What we do is grow your own TikTok account: every day, real people in the place you choose discover your profile, watch your videos and hear your music there. Some follow, and some may use your sound. That part is up to them.",
        "hero": {"image": "tiktok-creator", "alt": "A musician filming a TikTok video of a new song in a home studio"},
        "sections": [
            {
                "h2": "What we don't do",
                "ul": [
                    "Pay or brief creators to use your track.",
                    "Promise sound uses, a trend, a dance or a chart position.",
                    "Push one song or one video in particular: the campaign promotes your profile.",
                    "Touch your account: we never need your password.",
                ],
            },
            {
                "h2": "How to promote a song on TikTok yourself",
                "p": [
                    "Songs spread on TikTok when people want to make something with them. Post the track in several kinds of video: performing it, the story behind it, a snippet with the lyrics on screen, a moment people can copy. Use the official sound your distributor delivers, so every video made with it links back to the song.",
                    "Above all, keep posting. A song rarely takes off from one video; it takes off from an artist people have started to follow.",
                ],
            },
            {
                "h2": "Where our packages fit",
                "p": [
                    "If you're an artist, your account is where your music lives on TikTok, and an audience there hears every release first. Our campaigns send real people there every day: {starter_name} typically adds {starter_audience} followers a month, and those same listeners like and comment. Name the city or country where you want listeners, such as your home scene or the place your language is spoken, and we aim there.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Listeners discovering an artist's TikTok profile and playing a song video"},
            },
        ],
        "faqs": [
            ("Do you promote songs on TikTok?", "Not as sound campaigns. We grow the TikTok account of the artist or creator, so more real people discover your videos and the music in them. We don't buy sound uses or pay creators to feature a track."),
            ("Can you make my song go viral on TikTok?", "No, and nobody can honestly promise that. A song spreads when many people choose to make videos with it. A growing audience gives each release more people who might."),
            ("Will people use my sound?", "Some may, but we don't count sound uses or promise any. Every use is a person deciding your song fits their video."),
            ("Can I find listeners in a specific country?", "Yes. Write the city, region or country on the order form, and the campaign puts your profile in front of people there. For many artists that's their home scene or the countries where their language is spoken."),
            ("Does this work for labels or managers?", "We grow one TikTok account per package, so a label or manager orders for the artist's own account. We don't run label-wide or per-track campaigns."),
        ],
    },
    {
        "article": "tiktok-shop-growth",
        "kind": "intent",
        "platform": "tiktok",
        "slug": "tiktok/shop-followers",
        "label": "TikTok Shop followers",
        "title": "Buy TikTok Shop Followers Who Can Actually Buy | Growsterr",
        "description": "Want to buy TikTok Shop followers? Real people from the country your shop sells in, every day of the month. No bots, no Seller Center access, no password.",
        "h1": ("Buy TikTok Shop followers ", "who live where you ship."),
        "intro": "If you want to buy TikTok Shop followers, start with one question: where do your buyers live? A TikTok Shop sells in particular countries, so a follower anywhere else can watch but usually can't check out. Our packages bring real people from the city, region or country you name to your shop's TikTok account, every day of the month, without touching your account or Seller Center.",
        "hero": {"image": "tiktok-hub", "alt": "A small brand's TikTok Shop profile gaining followers from its home country"},
        "sections": [
            {
                "h2": "Why TikTok Shop followers have to be real",
                "p": [
                    "A shop account's followers are its first customers: they see new product videos, can be told when you go live and come back when they're ready to buy. Bot followers do none of that. They raise the number on your profile and lower everything a seller cares about: views per video, taps on products, viewers in a live.",
                ],
            },
            {
                "h2": "TikTok Shop followers from your country",
                "ul": [
                    "Name the country your shop sells in, or the cities where your best customers live.",
                    "Every day of the month, people there are the first to see your shop's profile.",
                    "The ones who like your products and videos follow, and many like and comment too.",
                    "Each day the dashboard logs visits and follows, and splits the visits by country.",
                ],
                "image": {"image": "tiktok-likes", "alt": "Local shoppers liking a product video on a TikTok Shop account"},
            },
            {
                "h2": "What we can't promise a shop",
                "p": [
                    "We don't promise sales, clicks or orders: people decide whether to buy, as they decide whether to follow. Follower requirements for some TikTok Shop features differ by country and change over time, so check TikTok's current rules rather than counting on a number. What we bring is real reach to the people who could become customers.",
                ],
            },
        ],
        "faqs": [
            ("Do you need access to my TikTok Shop or Seller Center?", "No. All we need is your shop's TikTok username and the country or city its buyers live in. We never ask for a password or a Seller Center login."),
            ("Will followers from your campaigns buy my products?", "Some might, if your products and videos win them over, but we can't promise sales. What we can say is that every follower is a real person in the place you chose, which is the only kind who could buy."),
            ("Can I grow my shop account and my creator account?", "Yes, with a package for each. A package grows one TikTok account."),
            ("Do shop followers help when I go live?", "A larger real audience means more people who might join a live, since followers can be notified when you start. Nobody can promise viewers at a given time, and we don't."),
            ("Which package suits a shop?", "{rising_name} is the most popular: typically {rising_audience} new followers a month for {rising_price}. A new shop can start with {starter_name} at {starter_price} and move up as its videos find their footing."),
        ],
    },
    # --- Growth by country ----------------------------------------------------------------
    {
        "article": "instagram-growth-by-country",
        "kind": "intent",
        "platform": "instagram",
        "slug": "instagram/by-country",
        "label": "Instagram growth by country",
        "title": "Buy Instagram Likes by Country, From Real People | Growsterr",
        "description": "Want to buy Instagram likes by country? Name a country, region or city, and real people there discover your profile and like the posts they enjoy, every day.",
        "h1": ("Buy Instagram likes by country: ", "you pick the place, people pick the posts."),
        "intro": "To buy Instagram likes by country is really to choose whose attention you want. With us, you name a country, region or city when you order, and every day our campaigns show your profile to real people there. Whoever enjoys a post likes it, and plenty also follow or comment: typically {pick_likes} likes a month with {pick_name}, mostly from the place you picked.",
        "hero": {"image": "instagram-real-people", "alt": "People in one country liking a creator's Instagram posts"},
        "sections": [
            {
                "h2": "Why the country behind a like matters",
                "p": [
                    "A like from someone who can read your caption, visit your shop or recognise your street is worth more to you than one from anywhere. Likes from the wrong country also skew your audience: Instagram's insights will say your audience lives somewhere you never post for, and so will the insights you share with a brand.",
                ],
            },
            {
                "h2": "How country targeting works for Instagram likes",
                "ul": [
                    "One line on the order form names the place: a country, a region or one city.",
                    "Our campaigns show your profile to people there first, every day for 30 days.",
                    "Likes land on the posts people choose; we don't promise them on one post.",
                    "Where the matching audience is thin, some people may come from nearby.",
                    "Your dashboard lists profile visits by country, so you can watch the targeting work.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "A creator checking which countries their Instagram profile visits came from"},
            },
            {
                "h2": "Choosing the right country",
                "p": [
                    "Pick the place your audience already is, or the one you're trying to reach: the country your customers live in, the city you work in, the region where your language is spoken. If you're unsure, Instagram's insights show where your current followers are, and growing there first strengthens what's already working.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy Instagram likes from one country only?", "You can aim your campaign at one country, and most people who see your profile will be there. Think of it as aimed rather than fenced: when the matching audience next door is larger, a share may come from there."),
            ("Which countries can I choose?", "Any country, region or city. Larger places give the campaign more people to reach; a single city gives you the most local audience."),
            ("Are likes sold separately by country?", "No. Every package includes likes, and they come from the people who also follow you. The place you choose applies to all of it: followers, likes and comments."),
            ("Do prices differ between countries?", "No. Packages cost the same wherever your audience is, and you can name any place when you order."),
            ("Will followers in Spain comment in Spanish?", "Mostly, yes. People write in the language they speak, so a campaign aimed at Spain brings comments largely in Spanish."),
        ],
    },
    {
        "article": "tiktok-growth-by-country",
        "kind": "intent",
        "platform": "tiktok",
        "slug": "tiktok/by-country",
        "label": "TikTok growth by country",
        "title": "Buy TikTok Followers by Country: Choose the Place | Growsterr",
        "description": "Buy TikTok followers by country: name a country, region or city and real people there discover your videos daily. Views and likes arrive with each of them.",
        "h1": ("Buy TikTok followers by country, ", "from people who share your language."),
        "intro": "When you buy TikTok followers by country, the point is an audience that understands you: your language, your humour, your references. We ask where your followers should come from when you order, then show your profile to real people in that country, region or city every day. Their views, likes and comments come with them, and on {pick_name} the followers alone typically number {pick_audience} a month.",
        "hero": {"image": "tiktok-hub", "alt": "A TikTok creator's new followers arriving from one country"},
        "sections": [
            {
                "h2": "Why TikTok growth is local",
                "p": [
                    "TikTok has said that language and country settings are among the things it considers when suggesting videos. So the place your followers come from shapes who your videos reach next. Followers who understand you watch longer and react more, and that's what a video needs from its first viewers.",
                ],
            },
            {
                "h2": "Buy TikTok views by country? Here's how views come",
                "p": [
                    "We don't sell views by country, or on their own at all. Views come from the same people our campaign brings: real users in the place you chose, watching the videos on your profile that catch them. We don't count views in advance or promise them on one video, but the views the campaign brings come from people in or around the place you named.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Viewers in one city watching a local creator's TikTok videos"},
            },
            {
                "h2": "Picking a country for TikTok",
                "ul": [
                    "Follow your language: a creator speaking Portuguese might pick Brazil or Portugal, depending on accent and references.",
                    "Follow your customers: a shop or service picks the country it sells to.",
                    "Pick your city if you're a local business, or a creator who films where you live.",
                    "Check TikTok's analytics: your followers' top locations show where you're already landing.",
                ],
            },
        ],
        "faqs": [
            ("Can I choose any country?", "Yes. Name a country, a region or a city on the order form. We show your profile to people there first, and the dashboard shows visits by country."),
            ("Will all my followers come from that country?", "Most will. The campaign is aimed at the place you name; where the best-matching audience is larger just across a border, some people may come from there."),
            ("Can I target two countries?", "Write the area on the order form, such as 'Germany and Austria' or 'the Nordics', and we aim the campaign there. One clear place usually gives the most coherent audience."),
            ("Does a smaller country grow more slowly?", "It can. A small country or a single city has fewer people to reach, so monthly numbers may sit lower in the typical range. Naming a wider region gives the campaign more room."),
            ("Do you need my login to target a country?", "No. The place is set in our campaigns, outside your account; all we need is your username and the location."),
        ],
    },
    {
        "article": "youtube-growth-by-country",
        "kind": "intent",
        "platform": "youtube",
        "slug": "youtube/by-country",
        "label": "YouTube growth by country",
        "title": "Buy YouTube Views by Country? Grow Viewers There | Growsterr",
        "description": "Want to buy YouTube views by country? We don't sell views. Name a country or city, and people there find your channel, subscribe and watch.",
        "h1": ("Buy YouTube views by country? ", "Grow an audience there instead."),
        "intro": "If you want to buy YouTube views by country, you probably want viewers who understand your videos: your language, your market, your city. We don't sell views, by country or otherwise. We grow your channel: every day, real people in the place you name discover it, and the ones who like it subscribe and watch. A typical month on {pick_name} adds {pick_audience} subscribers.",
        "hero": {"image": "youtube-viewers", "alt": "Viewers in one country watching a YouTube channel's latest videos"},
        "sections": [
            {
                "h2": "Why viewers' country matters on YouTube",
                "p": [
                    "YouTube Studio breaks your audience down by geography, and brands and partners who look at your channel often ask to see it. A channel about Turkish cooking with most of its views from elsewhere tells a confusing story. Viewers from the place you make videos for are more likely to watch to the end, comment in your language and return for the next upload.",
                ],
            },
            {
                "h2": "Views by country, without buying views",
                "ul": [
                    "On the order form, you write the country, region or city.",
                    "We show your channel to real people there every day for 30 days.",
                    "Those who like it subscribe, and many watch, like and comment on the videos they choose.",
                    "We don't count views in advance or promise watch hours, though you can name one video in your account for new viewers to land on.",
                    "Your dashboard shows visits and new subscribers day by day, and which countries the visits came from.",
                ],
                "image": {"image": "youtube-channel", "alt": "A YouTube channel page gaining subscribers from the country its creator targets"},
            },
            {
                "h2": "What we won't promise",
                "p": [
                    "Bought views from a chosen country are still bought views, and YouTube discounts views it doesn't consider genuine. We don't promise view counts, watch hours or monetization, and nobody should. What we bring is people, from the place you choose, who decided your channel was worth subscribing to.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy YouTube views from a specific country?", "No. We don't sell views at all. We grow your channel with real people from the country you choose, and their views come with subscribes, likes and comments."),
            ("Will these viewers show up in YouTube Studio's geography report?", "The people we bring watch like any other viewers, so their views appear wherever YouTube reports views, geography included. Studio also counts views from everywhere else your videos travel."),
            ("Do you promise watch hours for monetization?", "No. We never promise watch hours, views or monetization. Bought views don't help with any of it, and YouTube's rules don't allow them. Real subscribers who watch are the only growth that counts there."),
            ("Can I aim at one city, like a local business?", "Yes. If your channel serves a city, name it. Fewer people live there than in a whole country, so the numbers may sit lower in the typical range, but they'll be people you can actually serve."),
            ("Which package suits a channel?", "A channel starting out can begin with {starter_name} ({starter_price}, typically {starter_audience} new subscribers a month); {pro_name} reaches the most people, typically {pro_audience}. Every package includes place targeting."),
        ],
    },
]
