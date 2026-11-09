"""English YouTube country pages: subscribers and views, aimed at the audience of one country.
Keys and placeholders: docs/CONTENT.md. Brief: docs/keywords/WRITING.md ("Countries").
Targeting by place is real: the customer names the country, region or city. Prices stay in
USD placeholders; payment is card, Apple Pay or Google Pay through Stripe. No local office, team,
payment method or law is ever claimed, and monetization or watch hours are never promised."""

UPDATED = "2026-11-08"

PAGES = [
    # --- Subscribers ---------------------------------------------------------------------
    {
        "service": "subscribers",
        "country": "us",
        "slug": "youtube/subscribers/united-states",
        "label": "YouTube subscribers in the United States",
        "title": "Buy YouTube Subscribers in the USA, State by State | Growsterr",
        "description": "Buy YouTube subscribers in the USA: real people in the city, state or region you pick, who found your channel and chose it. Monthly, from {from_price}.",
        "h1": ("Buy YouTube subscribers in the USA, ", "from the states your channel speaks to."),
        "intro": "Want to buy YouTube subscribers in the USA? Tell us where your American audience lives, from a single city to all fifty states, and we put your channel in front of real people there daily. Those who like your videos subscribe: typically {pick_audience} a month with {pick_name}, measured day by day on your dashboard.",
        "hero": {"image": "youtube-subscribers", "alt": "An American creator's YouTube channel gaining subscribers from viewers in several US states"},
        "sections": [
            {
                "h2": "A country this big needs a target",
                "p": [
                    "A cooking channel from New Orleans, a car channel from Detroit and a personal finance channel for the whole country are looking for different people. In a country of fifty states, 'American viewers' is a starting point, not an audience.",
                    "Local channels gain the most from a narrow aim: a Chicago food guide wants Chicagoans, a Texas barbecue channel wants Texans. Nationwide topics like tech reviews or budgeting can take the whole country.",
                ],
            },
            {
                "h2": "Spanish-language channels in the States",
                "p": [
                    "Targeting follows geography, not language. So for a Spanish-language channel made for American viewers, choose a city where Spanish is widely spoken at home, such as Miami, San Antonio, El Paso or Los Angeles. The viewers who understand you are the ones who subscribe.",
                ],
                "image": {"image": "youtube-channel", "alt": "A bilingual creator in Miami recording a Spanish-language YouTube video at home"},
            },
            {
                "h2": "Living abroad, creating for Americans",
                "p": [
                    "You don't need a US address to choose the United States as your audience. Plenty of creators in other countries make English-language commentary, tutorials or gaming videos for Americans. Name the US when you order, and the campaign aims there wherever you upload from.",
                ],
            },
        ],
        "faqs": [
            ("Can I get subscribers from one state only?", "Yes. Name a state, a metro area such as Atlanta or Phoenix, or a single city. A small town has a small pool of people, so a campaign aimed there may also reach the surrounding counties."),
            ("Are the subscribers actually in the United States?", "Your channel is shown first to people in the place you named; if a larger audience that suits you lives close by, some may come from there. YouTube Studio's audience reports list the countries your viewers are in, so you can check."),
            ("Which package suits a new American channel?", "{starter_name}, at {starter_price} a month, typically brings {starter_audience} subscribers. Channels that upload often can pick {rising_name} or {pro_name}, which show your channel to more people each day."),
            ("Will I be dealing with a US company?", "No. Growsterr belongs to Sterr Agency, registered in Tallinn, Estonia, and we work with American creators online. What's local is your audience: the campaign runs where you tell us."),
            ("How do American subscribers arrive?", "A few every day across the month, never in a batch. Each one is someone who visited your channel through the campaign and decided it was worth subscribing to."),
            ("What do you need from me before the campaign begins?", "We need your channel handle and the part of the US your audience should come from, and the channel has to be public. Never your Google password."),
        ],
    },
    {
        "service": "subscribers",
        "country": "gb",
        "slug": "youtube/subscribers/united-kingdom",
        "label": "YouTube subscribers in the UK",
        "title": "Buy Real YouTube Subscribers in the UK | Growsterr",
        "description": "Buy real YouTube subscribers in the UK: British viewers from London to Glasgow who found your channel and chose it, a few each day. From {from_price} a month.",
        "h1": ("Buy real YouTube subscribers in the UK, ", "from viewers who get your references."),
        "intro": "Wanting to buy real YouTube subscribers in the UK means wanting British viewers: people who get the jokes, know the places and are awake when you post. Tell us whether that's London, Manchester, Scotland or the whole country, and that's where your channel is shown to real people, day after day. Those who enjoy it subscribe.",
        "hero": {"image": "youtube-subscribers", "alt": "A British creator filming a YouTube video on a rainy city street for viewers across the UK"},
        "sections": [
            {
                "h2": "Four nations, four audiences",
                "p": [
                    "The UK is four nations with their own accents, teams and in-jokes. A Glasgow comedy channel, a Welsh-language music channel and a London property channel each need a different audience, so name the nation, region or city that fits yours.",
                ],
                "ul": [
                    "A city channel: name the city, whether that's Leeds, Bristol or Birmingham.",
                    "A Welsh-language channel: name Wales, where most Welsh speakers live.",
                    "A Scottish football or comedy channel: name Scotland.",
                    "A channel for everyone in Britain: name the UK as a whole.",
                ],
            },
            {
                "h2": "Real subscribers, not British-sounding profiles",
                "p": [
                    "A list of profiles with British names proves nothing about who's behind them. What shows a subscriber is real is what they do: they visit your channel first, they watch, and some leave a comment in their own words.",
                    "That's also how you can check us. Each day's measured channel visits and new subscribers sit on your dashboard, and YouTube Studio shows which countries your viewers watch from.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Friends in a London flat watching a British creator's YouTube video on the TV"},
            },
            {
                "h2": "Paying from the UK",
                "p": [
                    "Every package carries a US dollar price, paid by card, Apple Pay or Google Pay at Stripe's checkout. Your bank turns each monthly dollar charge into pounds at its own rate, so the sterling amount can differ slightly between months.",
                ],
            },
        ],
        "faqs": [
            ("Can I target viewers in Scotland or Wales only?", "Yes. Name a nation, a region or a city. The smaller the place, the fewer people live there, so a campaign aimed at a small town may also reach the area around it."),
            ("Will UK subscribers be around when I upload?", "They share your clock, so an evening upload arrives in their evening. Whether they watch each new video is up to them, as it is with any audience."),
            ("Will British subscribers comment?", "Some will, in their own words and their own slang. Over a month, {pick_name} usually brings {pick_comments} comments from the people who subscribed."),
            ("What does a month cost?", "{starter_name} is {starter_price}, {rising_name} {rising_price} and {pro_name} {pro_price}, monthly and in US dollars. Stop it in your account at any point, and the month you've paid keeps going until its last day."),
            ("Can I buy a set number of UK subscribers?", "No. A fixed batch of British subscribers delivered on day one can only be fake accounts. Our packages bring real people across the month: typically {pick_audience} with {pick_name}."),
        ],
    },
    {
        "service": "subscribers",
        "country": "au",
        "slug": "youtube/subscribers/australia",
        "label": "YouTube subscribers in Australia",
        "title": "Buy YouTube Subscribers Australia: Aussie Viewers | Growsterr",
        "description": "Buy YouTube subscribers in Australia: real viewers in Sydney, Melbourne, Brisbane, Perth or wherever you choose, a few each day. From {from_price} a month.",
        "h1": ("Buy YouTube subscribers in Australia ", "who watch in your time zone."),
        "intro": "If you want to buy YouTube subscribers in Australia, you probably want viewers who are awake when you upload and know the places you film. Pick a city, a state or all of Australia, and we introduce your channel to people there each day. Those who enjoy your videos subscribe at their own pace.",
        "hero": {"image": "youtube-subscribers", "alt": "An Australian creator filming a YouTube video on a beach at sunrise"},
        "sections": [
            {
                "h2": "Why aim at Australia, not just English speakers",
                "p": [
                    "An English-language channel easily drifts toward viewers overseas, simply because there are more of them. For some topics that's fine. For a Gold Coast surf report, a tour of Adelaide's wineries or a Melbourne café guide, viewers in Australia are the ones who'll care, comment and come back.",
                ],
            },
            {
                "h2": "From Perth to Brisbane: time zones and uploads",
                "p": [
                    "Perth sits two or three hours behind Sydney, depending on the time of year, and that gap matters for a channel that posts in the evening. If most of your viewers are on the east coast, aim there; if you film the west, name Western Australia.",
                ],
                "image": {"image": "youtube-channel", "alt": "A Perth creator scheduling an evening YouTube upload for viewers on the west coast"},
            },
            {
                "h2": "Starting a new Australian channel",
                "p": [
                    "A channel with a handful of videos doesn't need the biggest package. {starter_name} at {starter_price} a month typically brings {starter_audience} subscribers, enough to give every new upload real Australians to meet it. Move up when you're publishing often enough to welcome more.",
                ],
            },
        ],
        "faqs": [
            ("Can I target just Sydney or Melbourne?", "Yes, either one on its own. Large cities have plenty of viewers, so a city-only aim suits them well."),
            ("Could some subscribers come from New Zealand?", "Possibly, if your channel suits viewers across the Tasman too. We show it in the place you named first, and YouTube Studio tells you which countries your viewers are in."),
            ("Is the price in Australian dollars?", "No, in US dollars. Your bank converts each monthly charge to Australian dollars when it reaches your statement."),
            ("Will all the subscribers arrive at once?", "No. They come a few at a time across the month, typically {pick_audience} with {pick_name}. Thousands overnight is what fake accounts look like."),
            ("Can I target a regional area instead of a city?", "Yes, a region like the Sunshine Coast or the Hunter Valley works. Where the local pool is small, some viewers may come from the wider state."),
            ("Will you ask for my Google sign-in?", "No. We work from your public channel handle and the place you chose. Keep your password to yourself, with us and with anyone else."),
        ],
    },
    {
        "service": "subscribers",
        "country": "in",
        "plan": "starter",
        "slug": "youtube/subscribers/india",
        "label": "YouTube subscribers in India",
        "title": "Buy 1,000 YouTube Subscribers in India? About a Month | Growsterr",
        "description": "Buy 1,000 YouTube subscribers in India the real way: {starter_name} typically brings {starter_audience} a month from the state or city you pick. Priced in USD.",
        "h1": ("Buy 1,000 YouTube subscribers in India? ", "Real ones usually arrive within the first month."),
        "intro": "Looking to buy 1,000 YouTube subscribers in India? Here's the honest version: we don't sell a pack of 1,000. We show your channel to real people in the Indian state or city you choose, and the ones who like it subscribe. {starter_name} typically brings {starter_audience} a month, so 1,000 usually comes within the first month.",
        "hero": {"image": "youtube-subscribers", "alt": "An Indian creator in a home studio watching a YouTube channel pass its first 1,000 subscribers"},
        "sections": [
            {
                "h2": "Why 1,000 subscribers for a few rupees is a trap",
                "p": [
                    "Sites that sell 1,000 subscribers for the price of a cup of chai deliver accounts that never watch. YouTube clears spam accounts out of subscriber counts, so those numbers tend to fall, and while they last they make your videos look ignored.",
                    "Real subscribers cost more because a person has to see your channel and decide. That decision is what makes them worth having: it's why they show up for your next upload.",
                ],
            },
            {
                "h2": "Choose the state that speaks your channel's language",
                "p": [
                    "India's YouTube audience is many audiences. A Tamil cooking channel, a Telugu tech channel and a Hindi comedy channel each need viewers who understand them, so aim where your language is spoken.",
                ],
                "ul": [
                    "Hindi: much of the north, from Delhi to Lucknow, Jaipur and Patna.",
                    "Tamil: Tamil Nadu, home to Chennai, Coimbatore and Madurai.",
                    "Telugu: Telangana and Andhra Pradesh, with Hyderabad and Visakhapatnam.",
                    "Kannada: Karnataka, with Bengaluru and Mysuru.",
                    "Malayalam: Kerala, with Kochi and Thiruvananthapuram.",
                    "Bengali: West Bengal, with Kolkata.",
                    "Marathi: Maharashtra, with Pune and Mumbai.",
                ],
                "image": {"image": "youtube-channel", "alt": "A Tamil cooking channel's creator filming a recipe in a Chennai kitchen"},
            },
            {
                "h2": "Paying in rupees, INR or USD",
                "p": [
                    "Our prices are set in US dollars, starting at {from_price} a month, with no separate rupee price list. Pay with an Indian debit or credit card that's open to international online payments, or with Apple Pay or Google Pay where a card is saved. Your bank turns the dollar charge into rupees, so the INR figure on your statement follows its exchange rate.",
                ],
            },
        ],
        "faqs": [
            ("Can I pay in Indian rupees?", "Not directly: every package is priced in US dollars. Your card pays the dollar amount and your bank converts it to INR, at its rate and with any fee it adds."),
            ("Can I pay with UPI?", "No. Checkout runs on Stripe and accepts cards, plus Apple Pay and Google Pay with a card saved in them. UPI apps aren't part of it."),
            ("Is 1,000 subscribers enough to be monetized?", "We never promise monetization or watch hours. Subscribers are only one part of YouTube's Partner Program, which also looks at watch time and reviews the channel itself. The decision is YouTube's alone."),
            ("Can I get subscribers from India if I live abroad?", "Yes. Plenty of creators outside India make videos for viewers back home. Name India, or the state your audience lives in, and the campaign runs there, wherever you happen to upload from."),
            ("Can I aim at a single city like Bengaluru?", "Yes. A single city is ideal for food guides, property tours and city news. For a language channel, a whole state usually reaches more of the right people."),
            ("How can I check they're real Indian subscribers?", "Look for what bought accounts never do: a visit to your channel before each subscription, views on your next upload, comments in Hindi, Tamil or whatever you speak. The dashboard logs each day's measured visits and subscribers alongside."),
        ],
    },
    {
        "service": "subscribers",
        "country": "pk",
        "slug": "youtube/subscribers/pakistan",
        "label": "YouTube subscribers in Pakistan",
        "title": "Buy YouTube Subscribers in Pakistan, Priced in USD | Growsterr",
        "description": "Buy YouTube subscribers in Pakistan from real viewers in Karachi, Lahore, Islamabad or anywhere you choose. Priced in USD rather than PKR, from {from_price} a month.",
        "h1": ("Buy YouTube subscribers in Pakistan ", "who watch in Urdu, Punjabi or Pashto."),
        "intro": "Planning to buy YouTube subscribers in Pakistan? Tell us where your viewers are: a city like Lahore, a province like Khyber Pakhtunkhwa, or the whole country. Each day, real people there come across your channel through our campaign, and the ones who enjoy your videos subscribe on their own. With {pick_name}, that's typically {pick_audience} a month.",
        "hero": {"image": "youtube-subscribers", "alt": "A Pakistani creator recording an Urdu cooking video for YouTube in a Lahore kitchen"},
        "sections": [
            {
                "h2": "Aim where your language is spoken",
                "p": [
                    "Urdu reaches viewers right across Pakistan. Punjabi, Pashto and Sindhi channels do best in the provinces where those languages are part of daily life.",
                ],
                "ul": [
                    "Urdu cooking, drama reviews or tech: name Pakistan, or a big city like Karachi.",
                    "Punjabi comedy or music: name Punjab, from Lahore to Faisalabad.",
                    "Pashto content: name Khyber Pakhtunkhwa, with Peshawar.",
                    "Sindhi content: name Sindh, with Hyderabad and Sukkur.",
                ],
            },
            {
                "h2": "Viewers at home, or Pakistanis abroad",
                "p": [
                    "Some Pakistani creators want the audience at home; others make videos for families in the UK, the Gulf or North America. Both work, because you choose the place. Name Pakistan for viewers at home, or the country abroad where your audience lives, and the people there who understand your videos are the ones who subscribe.",
                ],
                "image": {"image": "youtube-viewers", "alt": "A family in Karachi watching an Urdu YouTube video together on a phone"},
            },
            {
                "h2": "Paying from Pakistan: USD, not PKR",
                "p": [
                    "Each package has a single price in US dollars. A Pakistani debit or credit card that's cleared for payments abroad can pay it, and so can a card stored in Apple Pay or Google Pay. The rupee amount is your bank's conversion, which is why it can shift a little from month to month.",
                ],
            },
        ],
        "faqs": [
            ("Is there a PKR price?", "Prices exist only in US dollars. Your Pakistani card pays that amount and your bank works out the rupee figure."),
            ("Do you accept JazzCash or Easypaisa?", "No. Stripe's checkout takes cards, and Apple Pay or Google Pay where your phone offers them. Wallet apps can't be used directly."),
            ("Can subscribers come from one city, like Lahore?", "Yes. City targeting works well for local channels: Lahore food walks, Karachi street news, Islamabad property tours. For a regional language, naming the province usually reaches more of the right people."),
            ("Will the subscribers understand Urdu?", "The place you choose does that work. Aim an Urdu channel at Pakistan and it's shown to people who, for the most part, understand Urdu."),
            ("How quickly do they arrive?", "A few each day from the start of your campaign, never in one batch. Over the month that's typically {pick_audience} with {pick_name}, or {starter_audience} with {starter_name}."),
        ],
    },
    {
        "service": "subscribers",
        "country": "bd",
        "slug": "youtube/subscribers/bangladesh",
        "label": "YouTube subscribers in Bangladesh",
        "title": "Buy YouTube Subscribers in Bangladesh: Real Viewers | Growsterr",
        "description": "Buy YouTube subscribers in Bangladesh: real Bangla-speaking viewers in Dhaka, Chattogram, Sylhet or across BD, a few each day. Monthly, from {from_price}.",
        "h1": ("Buy YouTube subscribers in Bangladesh, ", "from viewers who watch in Bangla."),
        "intro": "Want to buy YouTube subscribers in Bangladesh? Whether it's Dhaka or all of BD, you name the place and our campaign shows your channel to people there daily. The ones who enjoy your natok, recipes or tutorials subscribe because they want more, and your dashboard shows the visits and new subscribers as they come.",
        "hero": {"image": "youtube-subscribers", "alt": "A creator in Dhaka filming a Bangla cooking video for YouTube"},
        "sections": [
            {
                "h2": "A Bangla channel needs Bangla viewers",
                "p": [
                    "Most YouTube channels in Bangladesh speak Bangla, and their best subscribers understand every line. Aiming at Bangladesh puts your channel in front of exactly those people.",
                    "Bangla is spoken across the border in West Bengal too, so a few viewers from there may find your channel as well. YouTube Studio shows how your audience splits between countries.",
                ],
            },
            {
                "h2": "Dhaka, Chattogram, Sylhet: when a city fits better",
                "p": [
                    "A Dhaka food review channel or a Chattogram travel vlog has a home city, and naming it keeps the audience local. Sylhet has a large community in Britain, so a Sylheti channel might want viewers in the UK as much as at home: name whichever place your videos are for.",
                ],
                "image": {"image": "youtube-channel", "alt": "A travel vlogger filming the hills outside Chattogram for a Bangla YouTube channel"},
            },
            {
                "h2": "Paying from Bangladesh",
                "p": [
                    "Every package is billed in US dollars through Stripe, to a card, Apple Pay or Google Pay. bKash and Nagad aren't accepted. If your card works for online payments in dollars, the monthly charge shows up on your statement in taka.",
                ],
            },
        ],
        "faqs": [
            ("Can I aim at all of BD, not one city?", "Yes. Name Bangladesh and the campaign covers the country. Choose a single city only when your channel is about that city."),
            ("Will bKash or Nagad work at checkout?", "No. We take cards, and Apple Pay or Google Pay on phones that support them, all through Stripe's checkout. Mobile wallets aren't part of it."),
            ("Is the price shown in taka?", "No, in US dollars, starting at {starter_price} a month for {starter_name}. Your bank converts it when it charges your card."),
            ("Will Bangladeshi subscribers comment in Bangla?", "Those who comment write whatever they like, usually in the language of your videos. {pick_name} typically adds {pick_comments} comments a month across your videos, every one written by hand."),
            ("How are subscribers spread over the month?", "A handful each day from the first days of your campaign. Thousands in an hour points to fake accounts, never to people."),
        ],
    },
    {
        "service": "subscribers",
        "country": "np",
        "slug": "youtube/subscribers/nepal",
        "label": "YouTube subscribers in Nepal",
        "title": "Buy YouTube Subscribers in Nepal: Real Nepali Viewers | Growsterr",
        "description": "Buy YouTube subscribers in Nepal: real viewers in Kathmandu, Pokhara and beyond, or Nepalis abroad, who chose your channel. Monthly, from {from_price}.",
        "h1": ("Buy YouTube subscribers in Nepal, ", "at home or wherever Nepalis watch."),
        "intro": "Thinking about how to buy YouTube subscribers in Nepal? Start with who you want watching. Your channel is introduced to real people in the place you name, whether that's the Kathmandu Valley, Pokhara or the whole country, and the ones who enjoy your songs, vlogs or podcasts subscribe on their own.",
        "hero": {"image": "youtube-subscribers", "alt": "A Nepali creator recording a podcast for YouTube in a small Kathmandu studio"},
        "sections": [
            {
                "h2": "Nepali channels and who they're for",
                "p": [
                    "Nepali YouTube runs on music, vlogs, podcasts, comedy and travel. A new song or a trekking film speaks most to viewers who know the language and the trails, which makes Nepal the natural place to aim.",
                ],
            },
            {
                "h2": "Nepalis abroad are an audience too",
                "p": [
                    "A great many Nepali families have someone working or studying abroad, in the Gulf, Malaysia, Japan, South Korea or Australia. If your videos are made for them, name the country where they live. Your channel is then shown to people there, and it's the viewers who understand Nepali who'll subscribe.",
                ],
                "image": {"image": "youtube-viewers", "alt": "A Nepali worker abroad watching a YouTube vlog from home on a phone during a break"},
            },
            {
                "h2": "Kathmandu, Pokhara or the Terai",
                "ul": [
                    "A city channel: name Kathmandu, Pokhara, Biratnagar or Butwal.",
                    "A channel for one part of the country: name the province, such as Gandaki or Madhesh.",
                    "A channel for everyone: name Nepal.",
                ],
            },
        ],
        "faqs": [
            ("Can I pay with eSewa or Khalti?", "No. You pay by card, or with Apple Pay or Google Pay if your phone has a card in it. A card that can pay online in US dollars can be used."),
            ("Is the price in Nepali rupees?", "No. Packages are priced in US dollars, from {from_price} a month, and your card's bank handles the conversion."),
            ("Can I target Nepali viewers in Qatar or Japan?", "Yes: name that country and your channel is shown to people there. Those who understand Nepali are the ones likely to subscribe, so it suits countries with large Nepali communities."),
            ("Will a Nepali music channel gain subscribers?", "If listeners like what they hear, yes. Nobody can promise how one release does, but a growing base of listeners gives each new song more people to meet it."),
            ("What's a typical month for a Nepali channel?", "Typically {starter_audience} with {starter_name} and {pick_audience} with {pick_name}. It's a range because every subscriber is a person choosing."),
        ],
    },
    {
        "service": "subscribers",
        "country": "lk",
        "slug": "youtube/subscribers/sri-lanka",
        "label": "YouTube subscribers in Sri Lanka",
        "title": "Buy YouTube Subscribers Sri Lanka: Sinhala and Tamil | Growsterr",
        "description": "Buy YouTube subscribers in Sri Lanka from real Sinhala- and Tamil-speaking viewers in Colombo, Kandy, Jaffna or island-wide. From {from_price} a month.",
        "h1": ("Buy YouTube subscribers in Sri Lanka, ", "in Sinhala, Tamil or English."),
        "intro": "To buy YouTube subscribers in Sri Lanka that last, start with real viewers. Name Colombo, a province or the whole island, and your channel is shown to people across it daily. Those who enjoy your cooking, travel, cricket or music videos subscribe on their own: typically {pick_audience} a month with {pick_name}.",
        "hero": {"image": "youtube-subscribers", "alt": "A Sri Lankan creator filming a village cooking video for YouTube outdoors"},
        "sections": [
            {
                "h2": "Sinhala, Tamil and English channels",
                "p": [
                    "Sri Lankan creators work in three languages, and each has its heartland. Sinhala channels find most of their viewers in the south and west, Tamil channels in the north and east around Jaffna, Trincomalee and Batticaloa, and English channels across the cities.",
                ],
                "ul": [
                    "Sinhala: name the Western or Southern Province, or the whole country.",
                    "Tamil: name the Northern Province, or Jaffna itself.",
                    "English or a mix: name Colombo, or Sri Lanka as a whole.",
                ],
            },
            {
                "h2": "Viewers on the island and abroad",
                "p": [
                    "Plenty of Sri Lankans abroad, in the Middle East, Italy, Australia, Canada or the UK, follow channels from home. A food or travel channel made for them can name that country instead of Sri Lanka.",
                ],
                "image": {"image": "youtube-viewers", "alt": "A Sri Lankan family abroad watching a cooking video from home on a laptop"},
            },
            {
                "h2": "What a month brings",
                "ul": [
                    "New subscribers: typically {pick_audience} with {pick_name}, a few each day.",
                    "Likes: typically {pick_likes}, from the same people.",
                    "Comments: typically {pick_comments}, in Sinhala, Tamil or English, as people choose.",
                    "Views: not counted in advance, because each one is someone deciding to watch.",
                ],
            },
        ],
        "faqs": [
            ("How do I reach viewers who speak Tamil?", "Name the place where they live: the Northern Province or Jaffna for a Tamil channel. People there understand your videos, which is why they subscribe."),
            ("Is pricing in Sri Lankan rupees?", "No, only US dollars, starting at {from_price}. Whatever currency your card uses, your bank converts the monthly charge."),
            ("Might some subscribers come from India?", "For a Tamil channel, possibly: Tamil Nadu is next door and speaks the same language. Your campaign starts in the place you named, and YouTube Studio shows the split between countries."),
            ("How can I tell the subscribers are real?", "Watch what they do. Real subscribers show up as views on your next uploads and as comments in their own words, and the dashboard records every campaign visit that came before."),
            ("Do I have to commit to several months?", "No. You can stop after the first month or any month after it, from your account. Nothing more is charged, and the month you've paid for continues to its last day."),
        ],
    },
    {
        "service": "subscribers",
        "country": "ph",
        "slug": "youtube/subscribers/philippines",
        "label": "YouTube subscribers in the Philippines",
        "title": "Buy YouTube Subscribers in the Philippines, Real Ones | Growsterr",
        "description": "Buy YouTube subscribers in the Philippines from real Filipino viewers in Metro Manila, Cebu, Davao or nationwide, a few each day. From {from_price} a month.",
        "h1": ("Buy YouTube subscribers in the Philippines ", "who get your Taglish."),
        "intro": "If you'd like to buy YouTube subscribers in the Philippines, begin with where your viewers are: Metro Manila, Cebu, Davao, a region or the whole country. Every day, real people in that place see your channel, and the ones who enjoy your vlogs, song covers or gaming videos subscribe because they want the next one.",
        "hero": {"image": "youtube-subscribers", "alt": "A Filipino vlogger in Manila filming a family YouTube vlog on a phone"},
        "sections": [
            {
                "h2": "Tagalog, Bisaya or Taglish: aim where it's spoken",
                "p": [
                    "A Tagalog or Taglish channel speaks to viewers across Luzon and the whole country. A Bisaya channel does best in the Visayas and Mindanao, around Cebu and Davao, and Ilocano content has its home in northern Luzon. Pick the place that matches how you talk on camera.",
                ],
            },
            {
                "h2": "Vlogs, covers and OFW audiences",
                "p": [
                    "Family vlogs, song covers, mukbang and mobile gaming are part of everyday Filipino YouTube, and so are channels made for OFWs abroad. If your viewers are Filipinos working in the Middle East, Hong Kong or elsewhere, name that country instead of the Philippines.",
                ],
                "image": {"image": "youtube-viewers", "alt": "An overseas Filipino worker watching a Tagalog vlog from home on a phone"},
            },
            {
                "h2": "Paying from the Philippines",
                "p": [
                    "GCash and Maya can't be used at our checkout. Packages bill in US dollars through Stripe, by card or by Apple Pay and Google Pay, and your bank converts each monthly charge into pesos.",
                ],
            },
        ],
        "faqs": [
            ("Can I target only Cebu or Davao?", "Yes. Name the city, or the region around it, and the campaign starts there. A smaller place has fewer people, so some viewers may come from neighboring provinces."),
            ("Which payment methods work from the Philippines?", "Debit and credit cards, plus Apple Pay and Google Pay where your phone has a card saved. Everything runs through Stripe's checkout."),
            ("Are the subscribers real Filipinos?", "They're real people in the place you chose, who saw your channel and decided to subscribe. Comments in Tagalog or Bisaya under your next upload are often the clearest sign."),
            ("Will they join my live streams?", "Some may, when it suits them. Nobody can promise who turns up at a set time, but each new subscriber is one more person who might."),
            ("How much growth is typical?", "With {pick_name}, typically {pick_audience} subscribers, {pick_likes} likes and {pick_comments} comments over a month, all from the same people."),
        ],
    },
    {
        "service": "subscribers",
        "country": "ng",
        "slug": "youtube/subscribers/nigeria",
        "label": "YouTube subscribers in Nigeria",
        "title": "Buy YouTube Subscribers in Nigeria, Lagos to Kano | Growsterr",
        "description": "Buy YouTube subscribers in Nigeria: real viewers in Lagos, Abuja, Port Harcourt or Kano who chose your channel. Priced in USD, from {from_price} a month.",
        "h1": ("Buy YouTube subscribers in Nigeria, ", "in English, Pidgin, Yoruba, Igbo or Hausa."),
        "intro": "If you want to buy YouTube subscribers in Nigeria, you want people who understand your channel: the skits, the music, the Pidgin. Tell us where they live, from Lagos to Kano or the whole country, and your channel reaches real people there day after day. Those who enjoy it subscribe, typically {pick_audience} a month with {pick_name}.",
        "hero": {"image": "youtube-subscribers", "alt": "A Nigerian comedy creator filming a skit for YouTube on a Lagos street"},
        "sections": [
            {
                "h2": "Skits, music and Nollywood on YouTube",
                "p": [
                    "Nigerian YouTube is full of comedy skits, Afrobeats videos, Nollywood films and lifestyle vlogs. Each has a home audience that catches every reference, and that audience is the natural place for a growing channel to start.",
                ],
            },
            {
                "h2": "Match the place to the language",
                "ul": [
                    "English or Pidgin: name Nigeria, or a big city like Lagos or Port Harcourt.",
                    "Yoruba: name Lagos, Ibadan or the south-west.",
                    "Igbo: name the south-east, with Enugu, Onitsha and Owerri.",
                    "Hausa: name the north, around Kano and Kaduna.",
                ],
                "image": {"image": "youtube-channel", "alt": "A musician in Abuja recording an Afrobeats performance for a YouTube channel"},
            },
            {
                "h2": "Paying from Nigeria: dollars, not naira",
                "p": [
                    "Each package costs a fixed amount in US dollars, paid by card through Stripe or with Apple Pay or Google Pay. There's no bank transfer option. You need a card that can make online payments in dollars; whether yours can is up to your bank or card issuer.",
                ],
            },
        ],
        "faqs": [
            ("Do you bill in naira?", "No. Dollars are the only currency we charge in. A card that pays online in dollars works, and the naira amount depends on your bank's rate."),
            ("Why can't I pay by bank transfer?", "Because a monthly subscription renews by itself. That needs a card, Apple Pay or Google Pay on file with Stripe, so transfers aren't an option."),
            ("Can I grow a Nigerian audience while living abroad?", "Yes. Plenty of Nigerian creators in the UK, the US or Canada make videos for viewers at home. Name Nigeria, or a city there, and that's where we show your channel first."),
            ("Will Nigerian subscribers comment?", "Some will, in their own words; across a month, {pick_name} tends to bring {pick_comments}. Pidgin replies under a skit are a good sign the right people found you."),
            ("Can I visit you in Lagos?", "We don't have an office there or anywhere in Nigeria. Growsterr is a product of Sterr Agency, and we work with Nigerian creators online; your audience is the only local part."),
        ],
    },
    {
        "service": "subscribers",
        "country": "gh",
        "slug": "youtube/subscribers/ghana",
        "label": "YouTube subscribers in Ghana",
        "title": "Buy YouTube Subscribers in Ghana: Accra to Kumasi | Growsterr",
        "description": "Buy YouTube subscribers in Ghana from real viewers in Accra, Kumasi, Tamale or Takoradi who chose your channel. Monthly packages in USD from {from_price}.",
        "h1": ("Buy YouTube subscribers in Ghana, ", "from people who speak your language."),
        "intro": "Before you buy YouTube subscribers in Ghana, decide where your viewers should be: Accra, Kumasi, a region or the whole country. Your channel then goes in front of real people there every day. The ones who enjoy your music, comedy or vlogs subscribe at their own pace, and you can follow it on your dashboard.",
        "hero": {"image": "youtube-subscribers", "alt": "A Ghanaian music creator filming a performance video for YouTube in Kumasi"},
        "sections": [
            {
                "h2": "Music, comedy and Kumawood",
                "p": [
                    "Ghanaian YouTube carries highlife, hiplife, Afrobeats and drill videos, comedy skits and Kumawood films, much of it in Twi as well as English. An audience in Ghana understands all of it, the jokes included.",
                ],
            },
            {
                "h2": "Choosing between Accra, Kumasi and the north",
                "ul": [
                    "A Twi channel: name the Ashanti Region, with Kumasi.",
                    "A Ga channel: name Greater Accra.",
                    "An Ewe channel: name the Volta Region.",
                    "A Dagbani or northern channel: name the Northern Region, with Tamale.",
                    "English for everyone: name Ghana.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Viewers in an Accra café watching a Ghanaian comedy skit on YouTube"},
            },
            {
                "h2": "What the first month looks like",
                "p": [
                    "Your campaign starts in the first days, and the first visitors arrive soon after. From then on, new subscribers come a few at a time, with likes and comments from the same people. By the end of the month, {pick_name} typically adds {pick_audience}.",
                ],
            },
        ],
        "faqs": [
            ("Is MoMo accepted?", "No. Checkout accepts cards, Apple Pay and Google Pay, all processed by Stripe, and mobile money wallets aren't among them."),
            ("Is the price in cedis?", "No, in US dollars: {starter_price} a month for {starter_name}. Your bank converts the charge into cedis on your statement."),
            ("Can I reach Ghanaians living in the UK?", "Yes: name the UK, or a city like London, and your channel is shown to people there. Whoever connects with your videos, Ghanaian or not, is who'll subscribe."),
            ("Will all my subscribers be in Ghana?", "The campaign begins with the place you chose. If a larger matching audience lives close by, a share may come from neighboring countries. YouTube Studio lists the countries your viewers come from."),
            ("Will you ever need my YouTube password?", "Never. All we need is your public channel handle and the place your audience lives."),
        ],
    },
    {
        "service": "subscribers",
        "country": "ke",
        "slug": "youtube/subscribers/kenya",
        "label": "YouTube subscribers in Kenya",
        "title": "Buy YouTube Subscribers in Kenya: Nairobi and Beyond | Growsterr",
        "description": "Buy YouTube subscribers in Kenya: real viewers in Nairobi, Mombasa, Kisumu or countrywide who chose your channel. Paid by card, from {from_price} a month.",
        "h1": ("Buy YouTube subscribers in Kenya, ", "in Swahili, English or Sheng."),
        "intro": "Hoping to buy YouTube subscribers in Kenya? Tell us where your viewers are, from Nairobi to Mombasa or the whole country, and real people there discover your channel daily through our campaign. Those who enjoy your comedy, music or vlogs subscribe on their own, a few each day, and like and comment along the way.",
        "hero": {"image": "youtube-subscribers", "alt": "A Kenyan creator in Nairobi filming a Swahili comedy sketch for YouTube"},
        "sections": [
            {
                "h2": "Swahili, English and Sheng",
                "p": [
                    "Kenyan creators switch between Swahili, English and Sheng, sometimes within a sentence. Viewers in Kenya follow all three without thinking twice, which is why aiming at Kenya beats aiming at the widest English-speaking audience you can find.",
                ],
            },
            {
                "h2": "Nairobi, the coast or the whole country",
                "ul": [
                    "Nairobi: city comedy, nightlife, tech and business channels.",
                    "Mombasa and the coast: food, travel and coastal life.",
                    "Kisumu, Nakuru or Eldoret: local news, music and farming channels.",
                    "Kenya as a whole: gospel, music and topics for everyone.",
                ],
                "image": {"image": "youtube-viewers", "alt": "Friends in Mombasa watching a Kenyan travel vlog on YouTube"},
            },
            {
                "h2": "M-Pesa and paying in dollars",
                "p": [
                    "Plenty of Kenyans pay for almost everything with M-Pesa, but our checkout doesn't take it. Packages are billed monthly in US dollars, by card through Stripe or with Apple Pay and Google Pay; your bank turns each charge into shillings.",
                ],
            },
        ],
        "faqs": [
            ("Can I target Mombasa only?", "Yes. Name Mombasa, or any other Kenyan city, and the campaign starts there. In a smaller town the pool is thinner, and the surrounding county may supply some viewers."),
            ("What does a month cost in shillings?", "We only price in US dollars: {starter_price}, {rising_price} or {pro_price} a month, depending on the package. The shilling amount is your bank's conversion."),
            ("Are the subscribers people in Kenya?", "Yes, real people in the place you named, who saw your channel through our campaign and chose to subscribe. YouTube Studio lets you check the countries your viewers are in."),
            ("Will Kenyan subscribers watch my music videos?", "Listeners who subscribe after hearing your music are the likeliest to play your next release, but each person picks what to watch. We never promise views on a particular video."),
            ("What happens to my subscribers when I stop?", "Nobody is removed when you stop. They're people who chose your channel, and they stay as long as it interests them."),
        ],
    },
    {
        "service": "subscribers",
        "country": "tr",
        "slug": "youtube/subscribers/turkey",
        "label": "YouTube subscribers in Turkey",
        "title": "Buy YouTube Subscribers in Turkey, Istanbul to İzmir | Growsterr",
        "description": "Buy YouTube subscribers in Turkey (Türkiye): real viewers in Istanbul, Ankara, İzmir or nationwide who watch in Turkish. Monthly, in USD, from {from_price}.",
        "h1": ("Buy YouTube subscribers in Turkey, ", "from viewers who watch in Turkish."),
        "intro": "If you're looking to buy YouTube subscribers in Turkey, the language matters most: Turkish viewers want Turkish videos. Name Istanbul, Ankara, İzmir, a region or the whole country, and we bring your channel to real viewers there every day. The ones who enjoy your gaming, vlogs or recipes subscribe of their own accord.",
        "hero": {"image": "youtube-subscribers", "alt": "A Turkish gaming creator recording a video from a home setup in Istanbul"},
        "sections": [
            {
                "h2": "A Turkish channel, a Turkish audience",
                "p": [
                    "Gaming, vlogs, cooking, football talk and tech reviews in Turkish all have a large audience at home. Aiming at Turkey puts your channel in front of people who catch every joke and reference, and those are the people who stay subscribed.",
                ],
            },
            {
                "h2": "Istanbul, Anatolia or Turkish speakers in Europe",
                "p": [
                    "A city channel can name Istanbul, Ankara, İzmir, Antalya or Bursa, and a national channel names Turkey. If your videos are for Turkish speakers in Germany or the Netherlands, name that country instead: the people there who understand Turkish are the ones who'll subscribe.",
                ],
                "image": {"image": "youtube-viewers", "alt": "A Turkish family in Germany watching a Turkish-language cooking channel on YouTube"},
            },
            {
                "h2": "Paying from Turkey",
                "p": [
                    "Packages are priced in US dollars and renew each month on the card you pay with, or through Apple Pay or Google Pay. There are no installments: each month is a single charge, which your bank shows in lira at its own rate.",
                ],
            },
        ],
        "faqs": [
            ("Is the price in Turkish lira?", "No. Lira isn't offered: packages start at {from_price} a month in US dollars, and your bank does the conversion."),
            ("Can I pay in installments?", "There's nothing to split: you pay one month at a time, and you can stop whenever you like from your account."),
            ("Can I aim at one city, such as Antalya?", "Yes. For a channel about one place, naming that city keeps the audience close to it."),
            ("How do I know they're really in Turkey?", "Your channel is shown to people in the place you named, and only those who like it subscribe. Turkish comments under your next videos are usually the first sign."),
            ("What can a Turkish channel expect in a month?", "With {pick_name}, around {pick_audience} new subscribers and {pick_likes} likes, spread across the month and coming from the same people."),
        ],
    },
    # --- Views ---------------------------------------------------------------------------
    {
        "service": "views",
        "country": "us",
        "slug": "youtube/views/united-states",
        "label": "YouTube views from the United States",
        "title": "Buy Real YouTube Views in the USA, Coast to Coast | Growsterr",
        "description": "Buy real YouTube views from the US: Americans who choose to watch, from one city to the whole United States, inside a monthly package from {from_price}.",
        "h1": ("Buy real YouTube views in the USA, ", "from Americans who chose to press play."),
        "intro": "Want to buy real YouTube views in the USA? Then each view should be an American who picked your video. Every day, our campaign puts your channel before real people in whichever city, state or region you name. From there they choose their own videos, and plenty leave a like, a comment or a subscription behind. Views come inside the package, never as a counted batch.",
        "hero": {"image": "youtube-viewers", "alt": "Viewers across the United States pressing play on the same YouTube video at different times of day"},
        "sections": [
            {
                "h2": "Views from the United States, checked in YouTube Studio",
                "p": [
                    "'From the US' only means something if you can see it. YouTube Studio breaks your audience down by country, so that's where to look while your campaign runs: new American viewers appear there along with the subscribers and comments they leave.",
                ],
            },
            {
                "h2": "Four time zones, one upload",
                "p": [
                    "When it's 6 p.m. in New York, it's 3 p.m. in Los Angeles. A national channel publishes when both coasts are awake; a local one names its city and posts for that city's evening. A Seattle channel and a Miami channel live on different clocks.",
                ],
                "image": {"image": "youtube-channel", "alt": "A creator in Los Angeles scheduling a YouTube upload for East Coast evening viewers"},
            },
            {
                "h2": "When one video matters most",
                "p": [
                    "Launching a trailer, a song or the first episode of a series? Name that video when you order, or later in your account, and new viewers are pointed to it. They land on it, subscribe, and then watch. What we won't do is promise its view count, since each view still depends on someone choosing it.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy views from the US if I live somewhere else?", "Yes. Where you live doesn't matter; where your audience lives does. Name the United States, or part of it, and that's where we show your channel first."),
            ("Can you tell me how many American views to expect?", "We don't forecast views. What we quote are typical monthly ranges for what viewers do next: with {pick_name}, {pick_audience} subscribers and {pick_likes} likes."),
            ("Could my views come from a single state?", "Yes, or from a single city. For a Texas real estate channel or a Boston sports show, a narrow aim brings viewers who care about the topic."),
            ("Is an American view different from any other?", "A view is a person watching, wherever they are. What changes is who's watching: aim at the place your videos are made for, and viewers are more likely to understand your references and stay."),
            ("Do I pay in dollars from the US?", "Yes. Packages are priced in US dollars, {starter_price} a month for {starter_name}, so there's no currency to convert, whether you pay by card, Apple Pay or Google Pay."),
        ],
    },
    {
        "service": "views",
        "country": "gb",
        "slug": "youtube/views/united-kingdom",
        "label": "YouTube views from the UK",
        "title": "Buy YouTube Views in the UK From British Viewers | Growsterr",
        "description": "Buy YouTube views in the UK from British viewers who choose to watch: London, Manchester, Glasgow or nationwide, with subscribers too. From {from_price} a month.",
        "h1": ("Buy YouTube views in the UK, ", "watched by people who live there."),
        "intro": "If you want to buy YouTube views in the UK, they should come from people in Britain who chose to watch. Our campaign introduces your channel to real people in the city, nation or region you name. They watch what catches them, and plenty go on to subscribe and comment. There are no view bundles here: views arrive with the package, from the people it brings.",
        "hero": {"image": "youtube-viewers", "alt": "A viewer in Manchester watching a British YouTube channel on a phone on the bus"},
        "sections": [
            {
                "h2": "English is everywhere. British viewers aren't.",
                "p": [
                    "An English-language video can be watched anywhere, which is exactly how a UK channel ends up with viewers who miss half of what it says. Naming the UK, or part of it, means the people watching know the places, the teams and the slang.",
                ],
            },
            {
                "h2": "Match-day reactions and other timely videos",
                "p": [
                    "Plenty of British channels live on timing: a reaction after the final whistle, a review on release day, a take on last night's telly. Nobody honest can deliver viewers at a set minute. What helps is a growing base of UK subscribers who may see your upload in their feed while it's fresh.",
                ],
                "image": {"image": "youtube-channel", "alt": "A football fan filming a post-match reaction video for a UK YouTube channel"},
            },
            {
                "h2": "London, or the rest of Britain",
                "p": [
                    "London is the obvious choice for a big-city channel, but most of the UK lives well outside it. A channel about Yorkshire walks, Cornish surf or the Scottish islands does better naming that region, where viewers recognize the landscapes on screen.",
                ],
            },
        ],
        "faqs": [
            ("Can views come from London only?", "Yes. London is big enough that a London-only aim works well."),
            ("Do you sell 1,000 UK views?", "No. A thousand views made to order are generated plays, and YouTube removes plays it judges artificial. Ours come from British viewers who chose to watch, inside a monthly package."),
            ("Will British viewers subscribe too?", "Many do, when they like what they watch. With {pick_name}, typically {pick_audience} new subscribers a month, along with {pick_likes} likes."),
            ("Is it priced in pounds?", "It's priced in dollars, not pounds: {from_price} a month for the smallest package, converted by your bank."),
            ("Can I target Northern Ireland?", "Yes. Name Northern Ireland or Belfast. With the Republic of Ireland next door, a few viewers may come from across the border."),
        ],
    },
    {
        "service": "views",
        "country": "au",
        "slug": "youtube/views/australia",
        "label": "YouTube views from Australia",
        "title": "Buy YouTube Views Australia: Viewers Who Live There | Growsterr",
        "description": "Buy YouTube views in Australia from real people in Sydney, Melbourne, Brisbane, Perth or regional towns who chose to watch. Monthly packages from {from_price}.",
        "h1": ("Buy YouTube views in Australia ", "from people who know the places you film."),
        "intro": "To buy YouTube views in Australia that mean something, the viewers have to be real Australians who picked your video. Your channel is shown every day to people in the state, city or region you name. Whatever grabs them, they watch; those who enjoy it go on to like, comment and subscribe. Views come inside the package and aren't counted ahead of time.",
        "hero": {"image": "youtube-viewers", "alt": "A viewer in a Brisbane backyard watching an Australian outdoors channel on a tablet"},
        "sections": [
            {
                "h2": "Four-wheel drives, fishing spots and footy",
                "p": [
                    "Australian channels about 4WD tracks, fishing spots, AFL and NRL, renovations and road trips are local by nature. Viewers in Australia know the beaches and the tracks you film, so they're the ones most likely to watch to the end and add tips of their own.",
                ],
            },
            {
                "h2": "Regional towns and the outback",
                "p": [
                    "You can name a region or a town, from the Sunshine Coast to Broken Hill. Small places have small audiences, so the campaign may reach out across the surrounding area to find enough people.",
                ],
                "image": {"image": "youtube-channel", "alt": "A creator filming a YouTube video beside a four-wheel drive on an outback track"},
            },
            {
                "h2": "For businesses: viewers near your customers",
                "p": [
                    "A Gold Coast surf school, a Perth builder or an Adelaide café can use YouTube too, and views from the other side of the world do little for them. Name the city where your customers live, so the people watching could one day walk through your door. What they do next is theirs to decide, but they're the right people to reach.",
                ],
            },
        ],
        "faqs": [
            ("Can I get views from Perth only?", "Yes. Name Perth, or Western Australia, and the campaign starts there."),
            ("Do Australian viewers subscribe as well?", "They do, and the same people bring both. {pick_name} usually means {pick_audience} new subscribers in a month, plus {pick_likes} likes."),
            ("How is the package priced?", "Monthly, in US dollars: {starter_name} {starter_price}, {rising_name} {rising_price}, {pro_name} {pro_price}. Australian dollars only appear once your bank converts the charge."),
            ("Why not buy a fixed number of Aussie views?", "Because a fixed number made to order can only be generated plays. Real Australians choose what to watch, so we bring people and let the views follow."),
            ("Can I see that viewers are in Australia?", "Yes, in YouTube Studio, whose audience reports list viewers' countries. Your Growsterr dashboard adds the channel visits and subscribers we measured."),
        ],
    },
    {
        "service": "views",
        "country": "ca",
        "slug": "youtube/views/canada",
        "label": "YouTube views from Canada",
        "title": "Buy YouTube Views in Canada, in English or French | Growsterr",
        "description": "Buy YouTube views in Canada from real viewers in Toronto, Vancouver, Montreal or nationwide, in English or French. Monthly packages from {from_price}.",
        "h1": ("Buy YouTube views in Canada, ", "in English or en français."),
        "intro": "To buy YouTube views in Canada that fit your channel, first decide which Canada: English-speaking Toronto and Vancouver, French-speaking Montreal and Quebec City, or the whole country. Our campaign shows your channel to real people in the place you name; they watch what appeals to them, and many subscribe. Views come with every package rather than as a number on a menu.",
        "hero": {"image": "youtube-viewers", "alt": "A creator in Montreal filming a French-language YouTube video in a café"},
        "sections": [
            {
                "h2": "French-language channels: aim at Quebec",
                "p": [
                    "Targeting works by place, so a French-language channel does best aimed at Quebec, where French is the everyday language, from Montreal to Quebec City and Sherbrooke. New Brunswick has a large French-speaking community too.",
                ],
            },
            {
                "h2": "Next door to a bigger audience",
                "p": [
                    "Canada shares a border, a language and plenty of tastes with the United States. We start your campaign in the Canadian place you named; if a bigger matching audience sits just south, some viewers may come from across the border. YouTube Studio shows the split, so you'll know.",
                ],
                "image": {"image": "youtube-channel", "alt": "A Toronto creator checking which countries a video's viewers come from"},
            },
            {
                "h2": "From St. John's to Vancouver",
                "p": [
                    "Canada spans six time zones, and St. John's runs four and a half hours ahead of Vancouver. A national channel posts when Ontario and British Columbia are both awake; a Halifax channel posts for Atlantic evenings. Name the region whose evening matters most to you.",
                ],
            },
        ],
        "faqs": [
            ("Do you take payment in Canadian dollars?", "No. Every package is priced in US dollars, the smallest at {from_price} a month, and your bank converts the charge into Canadian dollars."),
            ("Could the views be just from Toronto?", "Yes. Name Toronto, the Greater Toronto Area or Ontario, depending on how local your channel is."),
            ("Will French-speaking viewers subscribe?", "If your videos are in French and aimed at Quebec, the people seeing them understand every word, and those who enjoy them subscribe like any other viewer."),
            ("Can I order Canadian views on their own?", "No. Views come from the same people who subscribe, like and comment, so they're only part of a package."),
            ("Can I check that the viewers are Canadian?", "Check YouTube Studio: its audience reports break viewers down by country, Canada and the US included. Your dashboard adds the channel visits and subscribers our campaign measured."),
        ],
    },
    {
        "service": "views",
        "country": "in",
        "slug": "youtube/views/india",
        "label": "YouTube views from India",
        "title": "Buy YouTube Views From India: Real Indian Viewers | Growsterr",
        "description": "Buy YouTube views from India: real viewers in the state or city you choose, watching in Hindi, Tamil, Telugu or English, with subscribers. From {from_price}.",
        "h1": ("Buy YouTube views from India, ", "from viewers who understand every line."),
        "intro": "Whether you want to buy YouTube views from India or you're a creator in India looking for viewers, it works the same way. You name the state or city, and real people there come across your channel every day. Each picks the videos that interest them, and plenty go on to like, comment and subscribe. Views come inside the package; nobody here counts them in advance.",
        "hero": {"image": "youtube-viewers", "alt": "Commuters in India watching a regional-language YouTube video on their phones on a train"},
        "sections": [
            {
                "h2": "Songs, Shorts, cricket and exam prep",
                "p": [
                    "Indian YouTube is film songs and devotional music, cricket talk, tech reviews, exam preparation and Shorts watched on the move. Whatever your channel does, viewers who share its language are the ones who keep watching, so aim at where they live.",
                ],
            },
            {
                "h2": "Festival uploads and the regions they belong to",
                "p": [
                    "Diwali recipes, Onam sadya, Pongal kolam, Durga Puja pandal tours: a lot of Indian content follows the festival calendar, and each festival has its region. A Pongal video aimed at Tamil Nadu reaches the people celebrating it.",
                    "If one upload matters most, name it at checkout, or afterwards from your account. New viewers go there first: they subscribe, then press play. How many views it ends up with is never something we promise.",
                ],
                "image": {"image": "youtube-channel", "alt": "A creator filming a festival recipe video for YouTube in a Kerala kitchen"},
            },
            {
                "h2": "Beyond Mumbai and Delhi",
                "p": [
                    "The biggest cities aren't the only ones worth naming. A channel about Jaipur's food, Indore's streets or Kochi's cafés can aim at that city directly, and local viewers are the ones who comment that they've been there.",
                ],
            },
        ],
        "faqs": [
            ("Do my Shorts get views from the campaign too?", "They can. Viewers who reach your channel see your Shorts beside your longer videos and pick whichever they like. We don't count either kind in advance."),
            ("Is there a price per 1,000 views in rupees?", "No per-view price exists here, in rupees or dollars. Packages are monthly, in US dollars, from {from_price}, and views come with them."),
            ("Does Google Pay work from India?", "Only with a card saved in it: our checkout takes Google Pay as a card payment through Stripe, not as UPI."),
            ("Are views from India safe for my channel?", "Views from people who chose to watch are ordinary audience behavior. What YouTube acts against are artificial plays from bots and scripts, which we never use."),
            ("Can I aim at one state?", "Yes. Name the state where your language or topic lives, from Punjab to Kerala, and the campaign starts there."),
        ],
    },
    {
        "service": "views",
        "country": "pk",
        "slug": "youtube/views/pakistan",
        "label": "YouTube views from Pakistan",
        "title": "Buy YouTube Views in Pakistan From People Who Watch | Growsterr",
        "description": "Buy YouTube views in Pakistan from real viewers in Lahore, Karachi, Islamabad or Peshawar who choose to watch, inside a monthly package from {from_price}.",
        "h1": ("Buy YouTube views in Pakistan, ", "from people who chose your video."),
        "intro": "Ready to buy YouTube views in Pakistan? Here's what we do instead of selling a count. Day by day, our campaign brings your channel to people in whichever city or province you name. They watch whatever catches their interest, and the ones who enjoy it subscribe, like and comment. Views come with the package, because nobody can honestly sell you a number.",
        "hero": {"image": "youtube-viewers", "alt": "Cricket fans in Lahore watching a match analysis video on YouTube"},
        "sections": [
            {
                "h2": "Cricket nights, drama OSTs and Ramadan recipes",
                "p": [
                    "Pakistani viewers come for cricket analysis, drama soundtracks and episode reviews, cooking that gets busy around Ramadan and Eid, tech reviews in Urdu, and comedy. All of it lands best with people who share the language and the moment.",
                ],
            },
            {
                "h2": "Why cheap view packages fall apart",
                "p": [
                    "Views sold by the thousand for pocket change are plays, not people. YouTube removes views it judges artificial, so those counts tend to drop, and a video with views but no likes or comments looks emptier than one with fewer, real viewers.",
                ],
                "image": {"image": "youtube-channel", "alt": "A creator in Karachi comparing a video's views with its likes and comments"},
            },
            {
                "h2": "Karachi, Lahore, Islamabad: local channels",
                "p": [
                    "A Karachi street food channel, a tour of Lahore's old city or a guide to Islamabad's hiking trails has a home audience. Name that city and the viewers are people who know the places on screen; name Pakistan when your topic is national.",
                ],
            },
        ],
        "faqs": [
            ("Do you charge in rupees?", "No, only in dollars. The smallest package is {from_price} a month; rupees appear only on your bank statement."),
            ("Is this a route to monetization?", "Monetization and watch hours are never part of what we promise. Real viewers' watching is genuine, but whether a channel is monetized is decided by YouTube alone."),
            ("Can I target Peshawar for a Pashto channel?", "Yes. Name Peshawar or Khyber Pakhtunkhwa, and your channel is shown to people there, where Pashto is spoken every day."),
            ("Do views arrive the moment I pay?", "No. The campaign starts in the first days and real viewers arrive daily from then on. Thousands of views within an hour are generated, not watched."),
            ("How do I check the viewers are in Pakistan?", "YouTube Studio's audience reports show viewers' countries, and your Growsterr dashboard lists the channel visits and subscribers we measured."),
        ],
    },
    {
        "service": "views",
        "country": "bd",
        "slug": "youtube/views/bangladesh",
        "label": "YouTube views from Bangladesh",
        "title": "Buy YouTube Views BD: Real Viewers in Bangladesh | Growsterr",
        "description": "Buy YouTube views in BD from real Bangladeshi viewers who choose your natok, songs or recipes, with subscribers from the same people. From {from_price} a month.",
        "h1": ("Buy YouTube views BD? ", "Bring viewers in Bangladesh who choose to watch."),
        "intro": "Want to buy YouTube views in BD? A straight answer first: views aren't sold in bundles here. Our campaign shows your channel every day to real people in Bangladesh, or in the city you name. They open the videos that catch their eye, and the ones who stay to enjoy them like, comment and subscribe. Every view has a person behind it.",
        "hero": {"image": "youtube-viewers", "alt": "A family in Dhaka watching an Eid natok on YouTube on the living room TV"},
        "sections": [
            {
                "h2": "Eid natok, music videos and recipes",
                "p": [
                    "Bangladeshi YouTube gets busiest around Eid, when new natok and telefilms come out, while music videos, cooking and tech tutorials run all year. Viewers in Bangladesh understand every line of dialogue, so they're the ones likely to finish an episode and look for the next.",
                ],
            },
            {
                "h2": "Dhaka or the divisions",
                "p": [
                    "A Dhaka channel names Dhaka. A channel about village life, farming or a regional dialect does better naming Bangladesh as a whole, or a division such as Rajshahi, Khulna or Rangpur.",
                ],
                "image": {"image": "youtube-channel", "alt": "A creator filming rice fields in Rajshahi for a Bangla village-life YouTube channel"},
            },
            {
                "h2": "Bangladeshis in the Gulf, Malaysia or Italy",
                "p": [
                    "Millions of Bangladeshis work or study abroad, and plenty of them watch channels from home on their breaks. Made your videos for them? Then name their country, not Bangladesh. People there who understand Bangla are the ones who'll press play.",
                ],
            },
        ],
        "faqs": [
            ("Can I pay for views in taka?", "No. Packages carry dollar prices only, and you pay by card, Apple Pay or Google Pay; the taka figure comes from your bank."),
            ("Will Bangladeshi viewers also subscribe?", "Those who like your channel do. With {pick_name}, typically {pick_audience} subscribers a month, from the same people who watch."),
            ("Can views come from Sylhet or Chattogram only?", "Yes, either city works as a target. Smaller places may bring in viewers from the surrounding area too."),
            ("Why no bulk view packs?", "Because views made to order are plays, not viewers. YouTube removes views it judges artificial, so bulk packs tend to shrink and never bring subscribers."),
            ("Do you need my channel login?", "No. Just your public channel handle and where your viewers should be."),
        ],
    },
    {
        "service": "views",
        "country": "np",
        "slug": "youtube/views/nepal",
        "label": "YouTube views from Nepal",
        "title": "Buy YouTube Views Nepal: Real Listeners and Viewers | Growsterr",
        "description": "Buy YouTube views in Nepal from real viewers in Kathmandu, Pokhara and the Terai who choose your songs, vlogs or podcasts. Monthly packages from {from_price}.",
        "h1": ("Buy YouTube views in Nepal ", "for the songs, vlogs and podcasts people choose."),
        "intro": "Want to buy YouTube views in Nepal for a new song, a vlog or a podcast? We bring the people instead of a number. Your channel is shown to real viewers in Nepal, or the city or province you name, every day. They press play on what interests them, and the ones who enjoy it subscribe so they catch the next one.",
        "hero": {"image": "youtube-viewers", "alt": "Young people in Pokhara listening to a new Nepali song on YouTube"},
        "sections": [
            {
                "h2": "Teej songs, Dashain releases and lok dohori",
                "p": [
                    "Nepali music has its seasons: Teej songs, releases timed for Dashain and Tihar, and lok dohori all year round. Viewers in Nepal know these moments, so they're the audience most likely to come back for your next release.",
                ],
            },
            {
                "h2": "The Terai and its languages",
                "p": [
                    "The Terai has languages of its own, Maithili and Bhojpuri among them. Name a Terai city such as Janakpur or Birgunj for a channel in either, and some viewers may come from just across the border in Bihar, where the same languages are spoken.",
                ],
                "image": {"image": "youtube-channel", "alt": "A Maithili singer recording a music video in Janakpur for YouTube"},
            },
            {
                "h2": "Point new viewers at your latest release",
                "p": [
                    "Name the song or video that matters most at checkout, or add it afterwards in your account. New listeners are directed to it: subscribing comes first, the watching after. How it does from there is up to the people listening, so we don't put a number on its views.",
                ],
            },
        ],
        "faqs": [
            ("Will only my newest song get played?", "No. Listeners who reach your channel browse, so older songs often get played too, alongside the one you named. Which ones is up to them."),
            ("Can views come from Nepalis in the Gulf?", "Yes. Name that country instead of Nepal, and people living there see your channel; those who understand Nepali are the ones who'll watch."),
            ("Do I pay in Nepali rupees?", "No, there's only a dollar price. Your card, Apple Pay or Google Pay is charged in USD, and your bank shows the rupee amount."),
            ("Can the views come from Pokhara alone?", "Pokhara can be your target, yes. As it's a smaller city, some viewers may come from the wider Gandaki Province."),
            ("Are real views safer than cheap ones?", "Yes. Cheap views are usually generated plays, which YouTube can remove. Views from people who chose to watch are simply an audience."),
        ],
    },
    {
        "service": "views",
        "country": "ng",
        "slug": "youtube/views/nigeria",
        "label": "YouTube views from Nigeria",
        "title": "Buy YouTube Views in Naira? How Pricing Works | Growsterr",
        "description": "Wondering how to buy YouTube views in naira? Packages are priced in USD and paid by card. Here's how it works, and how real Nigerian viewers find your channel.",
        "h1": ("Buy YouTube views in naira? ", "Here's how paying from Nigeria works."),
        "intro": "Before you buy YouTube views in naira, know this: we charge in US dollars, never naira, and payment goes through Stripe by card, Apple Pay or Google Pay. What you get is real viewers in Nigeria, in Lagos, Abuja or wherever you name. Nobody tells them what to watch, and those who enjoy your videos like, comment and subscribe of their own accord.",
        "hero": {"image": "youtube-viewers", "alt": "Friends in Abuja watching a Nollywood film on YouTube on a laptop"},
        "sections": [
            {
                "h2": "Paying from Nigeria, step by step",
                "ul": [
                    "Choose a package: the smallest costs {from_price} a month.",
                    "Pay with a card that works for online payments in US dollars, or through Apple Pay or Google Pay when a card is saved there.",
                    "Your bank works out the naira amount; we don't see or set the rate.",
                    "The same card is charged each month until you cancel from your account.",
                ],
            },
            {
                "h2": "Nollywood, skits and Afrobeats premieres",
                "p": [
                    "Whole Nollywood films go up on YouTube, skit makers post several times a week, and Afrobeats artists release videos there. All of it travels furthest with viewers at home who understand the Pidgin, the Yoruba or the Igbo.",
                    "If one video matters most, a new film or single, you can name it while ordering or from your account later. Newcomers are pointed to it and subscribe before they watch; what happens on the video after that is their call.",
                ],
                "image": {"image": "youtube-channel", "alt": "A Nigerian creator in Lagos uploading a new music video to YouTube"},
            },
            {
                "h2": "What cheap naira view packs really are",
                "p": [
                    "Thousands of views for a small naira sum can only be plays from bots or scripts. YouTube strips out views it considers artificial, so those numbers tend to fall back, and they never bring a single subscriber.",
                ],
            },
        ],
        "faqs": [
            ("Can I use a dollar card?", "If it can make online payments in US dollars, yes: it works at our checkout like any other card."),
            ("Can I get views from Lagos only?", "Yes, Lagos on its own works. For a Hausa channel, Kano or the north is the better choice."),
            ("How many Nigerian views should I expect?", "Views aren't forecast, because each is somebody's choice. The package quotes typical ranges for what viewers do next: {pick_audience} subscribers and {pick_likes} likes a month with {pick_name}."),
            ("Is the price ever shown in naira?", "No. It's always in US dollars; the naira figure only appears on your bank statement."),
            ("Can I aim at Nigerians abroad?", "Yes: name the country they live in, such as the UK. The viewers there who connect with your videos are the ones who'll watch."),
        ],
    },
    {
        "service": "views",
        "country": "ke",
        "slug": "youtube/views/kenya",
        "label": "YouTube views from Kenya",
        "title": "Buy YouTube Views Kenya: People Who Press Play | Growsterr",
        "description": "Buy YouTube views in Kenya from real people in Nairobi, Mombasa, Kisumu or Eldoret who choose your music, comedy or vlogs. Monthly packages from {from_price}.",
        "h1": ("Buy YouTube views in Kenya ", "from viewers who hit play on their own."),
        "intro": "To buy YouTube views in Kenya that hold up, start with real viewers. Each day your channel appears in front of people in Kenya, or the city you name, and they decide what to watch. Whoever enjoys your music, comedy or vlogs can like, comment and subscribe. Views arrive inside every package rather than in a block of a thousand.",
        "hero": {"image": "youtube-viewers", "alt": "A viewer in Nairobi watching a Kenyan music video on YouTube on a phone at a matatu stage"},
        "sections": [
            {
                "h2": "New music, gospel and comedy",
                "p": [
                    "Gengetone and gospel releases, comedy skits, podcasts and Swahili vlogs fill Kenyan YouTube. Each finds its first fans at home, among viewers who get the Sheng and the inside jokes.",
                ],
            },
            {
                "h2": "Watched on phones, on data",
                "p": [
                    "Many Kenyans watch YouTube on their phones, often on data bundles, so a video has to earn its megabytes. A strong thumbnail, a quick start and Shorts that lead to your longer videos help viewers decide your channel is worth the data.",
                ],
                "image": {"image": "youtube-channel", "alt": "A Kenyan creator editing a short vertical video on a phone for YouTube Shorts"},
            },
            {
                "h2": "Kenya's neighbors watch too",
                "p": [
                    "Swahili is spoken across East Africa, so a Swahili channel aimed at Kenya may also pick up viewers in Tanzania or Uganda. Your campaign starts in Kenya, or the city you named, and YouTube Studio shows which countries the views come from.",
                ],
            },
        ],
        "faqs": [
            ("Is a package worth it for a new Kenyan artist?", "A new artist with a few songs can start with {starter_name} at {starter_price} a month, which typically brings {starter_audience} subscribers. Each release then has more listeners waiting for it, though nobody can promise how a song does."),
            ("Does checkout take M-Pesa?", "No. It takes cards, plus Apple Pay and Google Pay where your phone supports them, with prices in US dollars."),
            ("Can I target Kisumu or Eldoret?", "Yes, either one. Since they're smaller than Nairobi, some viewers may come from the surrounding counties."),
            ("Are bought views risky for a Kenyan channel?", "Generated views are, anywhere: YouTube removes plays it judges artificial. Views from people who chose to watch aren't bought plays; they're an audience."),
            ("Will you need access to my channel?", "No. We work from the public handle of your channel and a target location, nothing more."),
        ],
    },
]
