"""English Instagram country pages: followers, likes and comments for people who name a country
("buy instagram followers usa", "buy instagram likes india"). The customer names the country, region
or city and the campaign aims there. Prices stay in US dollars (placeholders from apps/growth/plan.py);
payment is card, Apple Pay or Google Pay through Stripe. Keys and placeholders: docs/CONTENT.md."""

UPDATED = "2026-11-08"

PAGES = [
    # --- Comments -------------------------------------------------------------------------
    {
        "service": "comments",
        "country": "in",
        "plan": "starter",
        "slug": "instagram/comments/india",
        "label": "Instagram comments from India",
        "title": "Buy Comments on Instagram Posts in Rupees? | Growsterr",
        "description": "Instagram comments from real people across India, in Hinglish, Tamil, English or whatever they speak. Billed in US dollars, inside every monthly package.",
        "h1": ("Buy comments on Instagram posts in rupees? ", "Real Indian voices, billed in dollars."),
        "intro": "Planning to buy comments on an Instagram post in rupees? Two straight answers first. We bill in US dollars, and an Indian card that works for international online payments covers it; your bank shows the rupee amount. And comments never come alone: real people across India discover your profile, follow, and write in their own words: on {starter_name}, usually {starter_comments} comments over a month.",
        "hero": {"image": "instagram-real-people", "alt": "Replies in Hinglish, English and emoji under an Indian creator's Instagram post"},
        "sections": [
            {
                "h2": "The language follows the place you choose",
                "p": [
                    "Indian comment sections switch languages without warning: Hinglish from Delhi, Tamil from Chennai, Malayalam from Kochi, and English almost everywhere. We don't assign a language to anyone. We aim your campaign at the city or state you name, and people there comment the way they already talk.",
                    "So a Telugu food page gains more from naming Hyderabad than from any instruction we could give. If you post in English for the whole country, name India and let the mix arrive on its own.",
                ],
            },
            {
                "h2": "Paying from India, step by step",
                "ul": [
                    "Every package has a US dollar price: {starter_price} a month for {starter_name}, {rising_price} for {rising_name}.",
                    "Stripe runs the checkout: pay by card, or through Apple Pay or Google Pay using a card stored there.",
                    "UPI, wallets and bank transfers aren't accepted.",
                    "Your bank converts the charge into rupees at its own rate and may add a foreign-exchange fee.",
                    "If a payment is declined, check in your banking app that international online use is switched on for the card.",
                ],
            },
            {
                "h2": "Choosing which posts get the attention",
                "p": [
                    "On {rising_name} and {pro_name} you pick the posts our campaign puts in front of people: a festive collection before Diwali, a fresh wedding shoot, the Reel you're proudest of. How many visitors comment on that particular post is their decision, so we never quote a number for a single post.",
                ],
                "image": {"image": "instagram-creator-studio", "alt": "An Indian creator choosing which Instagram posts should get more attention this month"},
            },
        ],
        "faqs": [
            ("Can I pay for Instagram comments in rupees?", "Not directly in rupees. Stripe charges the package in US dollars, and your bank converts it at its own rate. What you agree to at checkout is the dollar price: {starter_price} a month for {starter_name}."),
            ("Will the comments come from Indian accounts?", "They're written by real people in whichever place you pick. Name India, a state such as Kerala or Punjab, or a single city like Pune, and your profile is shown there first. If the closest match for your niche is next door, a few may come from a neighbouring area."),
            ("Can I write the comments myself, or send a list?", "No. Nobody on our side writes comments and nobody is handed a script. Comment sections built that way read like conversation, which is the whole reason to want comments in the first place."),
            ("Can I buy comments for one Instagram post only?", "Only as part of a package. Comments grow out of the monthly campaign, from people who follow and engage. On {rising_name} or {pro_name} you name the posts that deserve the spotlight, but what people write there, and how many of them do, stays with them."),
            ("Is this worth it next to cheap comment packs?", "Work it out per person. {starter_price} a month typically brings {starter_audience} new followers, {starter_likes} likes and {starter_comments} comments, all from the same real people. Spread across that, each person costs a few US cents, and none of them vanishes when Instagram sweeps away fake accounts."),
        ],
    },
    {
        "service": "comments",
        "country": "ng",
        "slug": "instagram/comments/nigeria",
        "label": "Instagram comments from Nigeria",
        "title": "Buy Instagram Comments in Nigeria From Real People | Growsterr",
        "description": "Buy Instagram comments in Nigeria the honest way: real people in Lagos, Abuja or the city you name write in their own words, inside a monthly package.",
        "h1": ("Buy Instagram comments in Nigeria ", "from people who actually reply."),
        "intro": "If you want to buy Instagram comments in Nigeria, you know how empty a vendor page or a skit looks with nobody talking under it. We fill that silence the real way: people in Lagos, Abuja, Port Harcourt or the city you name discover your profile, follow, and comment in English, Pidgin or whatever comes naturally. With {pick_name}, that usually adds up to {pick_comments} comments a month.",
        "hero": {"image": "instagram-real-people", "alt": "Lively replies in English and Pidgin under a Nigerian creator's Instagram post"},
        "sections": [
            {
                "h2": "Why a Nigerian comment section is hard to fake",
                "p": [
                    "A real one has texture. Someone asks 'how much?', someone tags a friend to come and see, someone answers in Pidgin with three laughing emoji. Copied praise from accounts with no posts sticks out to exactly the people you're trying to sell to.",
                    "The comments that grow out of our campaigns are written by people who found your page and had something to say, so they carry that same texture.",
                ],
            },
            {
                "h2": "For vendors who sell through the DMs",
                "ul": [
                    "A commenter near you is someone who can actually order and receive the delivery.",
                    "Questions under a post are often the first step to a sale, so answer them where others can read the reply.",
                    "Name Lagos alone if that's the only place you deliver.",
                    "With {rising_name} or {pro_name}, choose the posts that show your newest stock.",
                ],
            },
            {
                "h2": "What we won't do",
                "p": [
                    "We don't sell packs of comments, we don't write them, and nobody here ever logs in to your account to post or reply. If someone offers fifty comments on one post by tonight, a script is doing the typing.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy Instagram comments for a single post in Nigeria?", "Not on its own. Comments come bundled in the monthly package, written by people who found your profile through the campaign. On {rising_name} or {pro_name} you decide which posts are put in front of them; how many comments a given post collects is up to its readers."),
            ("Will people comment in Pidgin?", "Some will, if that's how they talk. We target places, not languages, and Nigerians comment in English, Pidgin, Yoruba, Igbo, Hausa or a mix of them. Your captions set the tone: write in Pidgin and you'll often hear Pidgin back."),
            ("How do I pay from Nigeria?", "Stripe handles payment: a card, or Apple Pay and Google Pay on phones that offer them. Because the price is in US dollars, a dollar card works, and so does a naira card your bank allows for foreign online payments."),
            ("How many comments does {starter_name} bring?", "Typically {starter_comments} a month, together with {starter_audience} new followers and {starter_likes} likes from the same people. {rising_name} and {pro_name} bring proportionally more."),
            ("Can I choose Abuja instead of Lagos?", "Yes. Write any Nigerian city, a state, or the whole country when you order. A single city keeps the conversation local; the whole country widens the pool of people the campaign can reach."),
        ],
    },
    {
        "service": "comments",
        "country": "pk",
        "slug": "instagram/comments/pakistan",
        "label": "Instagram comments from Pakistan",
        "title": "Buy Instagram Comments in Pakistan, Written by People | Growsterr",
        "description": "Buy Instagram comments in Pakistan from real people in Karachi, Lahore or Islamabad, in Urdu, Roman Urdu or English. Included in every monthly package.",
        "h1": ("Buy Instagram comments in Pakistan, ", "in Urdu, English and everything between."),
        "intro": "To buy Instagram comments in Pakistan that sound like Pakistan, they have to come from people who live there. Every day, our campaign puts your profile in front of real people in Karachi, Lahore, Islamabad or the city you choose, and the ones who connect with your posts comment as they always do: Roman Urdu, English, Punjabi, a quick MashaAllah, a question about the price.",
        "hero": {"image": "instagram-real-people", "alt": "Comments in Roman Urdu and English under a Pakistani clothing brand's Instagram post"},
        "sections": [
            {
                "h2": "Comment sections that sell bridal, lawn and food",
                "p": [
                    "Plenty of Pakistani accounts run on comments. A bridal designer is asked about delivery dates, a lawn brand about restocks, a home baker whether they deliver to DHA. Those questions are what make a page look open for business.",
                    "When real people from your city find your profile, questions like these start appearing by themselves, because the people asking actually want to know.",
                ],
            },
            {
                "h2": "Seasons that fill a comment section",
                "ul": [
                    "Before Eid, people browse outfits, gifts and recipes, and ask about the ones they plan to buy.",
                    "In Ramadan, the hours after iftar tend to be busy on Instagram.",
                    "Wedding season fills feeds with mehndi and baraat looks, and with questions about them.",
                    "On {rising_name} or {pro_name}, you choose which posts get the attention as each season starts.",
                ],
            },
            {
                "h2": "How the comments stay real",
                "p": [
                    "Nobody writes a comment for us, and we don't hand out scripts or lists of phrases. We bring people; they decide whether a post deserves a reply. That's also why we can't sell a set number of comments on a set post.",
                ],
            },
        ],
        "faqs": [
            ("Will the comments be in Urdu?", "Comments come in whatever language people choose, and in Pakistan that's often Urdu, Roman Urdu or English. Captions in Urdu tend to invite replies in Urdu."),
            ("Can I target Lahore only?", "Yes. Name a city, a province or the whole of Pakistan. Lahore alone gives a tight local audience; the whole country gives the campaign more room to find people."),
            ("Are the commenters real Pakistani accounts?", "They're real people in the place you chose, on their own accounts. No one is asked to comment, and we don't run a single account ourselves."),
            ("How much do Instagram comments cost in Pakistan?", "We don't price comments one by one. {starter_name} is {starter_price} a month, billed in US dollars, and typically brings {starter_comments} comments along with {starter_audience} new followers. Your bank converts the charge into Pakistani rupees."),
            ("Can I pay with JazzCash or Easypaisa?", "No. Payment is by card through Stripe, and Apple Pay or Google Pay also work if your phone has them. A debit card enabled for international online payments is usually the simplest route from Pakistan."),
        ],
    },
    # --- Followers ------------------------------------------------------------------------
    {
        "service": "followers",
        "country": "ae",
        "slug": "instagram/followers/united-arab-emirates",
        "label": "Instagram followers in Dubai and the UAE",
        "title": "Buy Instagram Followers in Dubai Who Live in the UAE | Growsterr",
        "description": "Buy Instagram followers in Dubai, Abu Dhabi or anywhere in the UAE: real people there discover your profile and choose to follow. Billed monthly.",
        "h1": ("Buy Instagram followers in Dubai, ", "from people who could walk through your door."),
        "intro": "When you buy Instagram followers in Dubai, the people behind them should be people who could visit your salon, book your table or view your listing. That's who we bring. Name Dubai, Abu Dhabi, Sharjah or the whole UAE, and our campaign shows your profile to real people there every day. With {pick_name}, a typical month brings {pick_audience} of them.",
        "hero": {"image": "instagram-followers", "alt": "A Dubai café's Instagram profile gaining followers from across the city"},
        "sections": [
            {
                "h2": "One city, many languages",
                "p": [
                    "A Dubai audience scrolls in Arabic and English, and often in Hindi, Urdu, Malayalam, Tagalog or Russian as well. We aim at the place, not at a community, so your followers come from whichever of those groups your posts speak to.",
                    "That makes captions worth a thought. Arabic and English side by side speak to more of the city than either alone, and a line in a third language can win over a community you'd like as customers.",
                ],
            },
            {
                "h2": "Who gains most from a UAE audience",
                "ul": [
                    "Restaurants and cafés, from Jumeirah to Al Barsha.",
                    "Salons, spas and fitness studios that live on bookings.",
                    "Property agents who want followers living in the city.",
                    "Creators covering food, events or family life in the Emirates.",
                ],
            },
            {
                "h2": "Dubai only, or the whole country?",
                "p": [
                    "Name Dubai for the tightest audience, or the UAE for more people to reach. You can also write two cities, say Dubai and Abu Dhabi, and we aim at those first. When the matching audience for your niche is small, some followers may come from the emirates next door.",
                ],
            },
        ],
        "faqs": [
            ("Can I get followers from Dubai only?", "Mostly, yes. Name Dubai and people there see your profile first. For a narrow niche, some may come from neighbouring emirates."),
            ("Will my followers be Emirati, expat or both?", "Both, because we target where people are, not who they are. Your new followers will look like Dubai itself: Emiratis, long-time residents and newer arrivals, drawn by whatever your posts offer."),
            ("How do I pay from the UAE?", "Stripe takes your card, Apple Pay or Google Pay. The price is set in US dollars; if your card is in dirhams, your bank converts the charge."),
            ("Does anything change during Ramadan?", "Your campaign keeps running every day. People's Instagram hours often shift later into the evening then, so it pays to post when your audience is actually awake."),
            ("When do followers from Dubai start arriving?", "Within the first days of the campaign, then a few more every day of the month. Your dashboard shows each day's profile visits and the follows they turned into, so you can watch it build."),
        ],
    },
    {
        "service": "followers",
        "country": "bd",
        "plan": "starter",
        "slug": "instagram/followers/bangladesh",
        "label": "Instagram followers in Bangladesh",
        "title": "Buy Instagram Followers in Bangladesh: Real People | Growsterr",
        "description": "Buy Instagram followers in Bangladesh from real people in Dhaka, Chattogram, Sylhet or the city you choose. Priced in US dollars, paid by card, cancel any time.",
        "h1": ("Buy Instagram followers in Bangladesh, ", "from Dhaka to Sylhet."),
        "intro": "If you're looking to buy Instagram followers in Bangladesh, you probably want people who can order from your boutique, book your shoot or taste your home kitchen's kacchi. We show your profile to real people in Dhaka, Chattogram, Sylhet or the place you name, and the ones who like your posts follow. {starter_name} usually brings {starter_audience} a month.",
        "hero": {"image": "instagram-followers-1000", "alt": "A Dhaka boutique's Instagram follower count rising steadily over a month"},
        "sections": [
            {
                "h2": "From a Facebook page to an Instagram audience",
                "p": [
                    "Many shops in Bangladesh started on Facebook and now want the same customers on Instagram, where photos and Reels do the selling. Growing there from zero is slow while nobody local knows the account exists.",
                    "That's the gap our campaign fills. People in your city see your profile, the ones who like your style follow, and your next post meets an audience that's already interested.",
                ],
            },
            {
                "h2": "Bangla, English or both",
                "p": [
                    "We target places, not languages, so your followers read whatever people in your city read. In Dhaka that's often a mix of Bangla and English; in Sylhet or Rajshahi, Bangla carries more of the conversation. Captions in the language your customers use tend to turn more visits into follows.",
                ],
            },
            {
                "h2": "What each follower costs",
                "p": [
                    "At {starter_price} a month, {starter_name} usually adds {starter_audience} followers, along with likes and comments from the same people. Divided out, each real follower costs a few US cents, and they're people who chose you, so they don't vanish in a clean-up.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy Instagram followers in Bangladesh with bKash or Nagad?", "No. Payment runs through Stripe, by card, or with Apple Pay or Google Pay on a phone that supports them. A dual-currency or international debit card is a common way to pay a dollar price from Bangladesh."),
            ("Are the followers really from Bangladesh?", "Yes: real people living where you point the campaign. Write Dhaka, a division such as Chattogram, or the whole country; we aim there first, and if your niche is small there, some may come from nearby."),
            ("Can I target only Gulshan or Dhanmondi?", "Write the neighbourhood if you like, but think of it as the centre of the target rather than a fence. A whole city usually gives the campaign enough people to work with, and your posts decide who follows."),
            ("Do I get likes too?", "They come with it. The people who follow also like and comment: {starter_name} months usually see {starter_likes} likes and {starter_comments} comments, and neither is ever sold separately."),
            ("Is there a minimum contract?", "No. Cancel in your account at any point; the month you paid for still runs to its end, and the followers you gained stay yours."),
        ],
    },
    {
        "service": "followers",
        "country": "ca",
        "slug": "instagram/followers/canada",
        "label": "Instagram followers in Canada",
        "title": "Buy Instagram Followers in Canada, Coast to Coast | Growsterr",
        "description": "Buy Instagram followers in Canada from real people in Toronto, Vancouver, Montreal or wherever your audience lives. English, French, or both. Monthly packages.",
        "h1": ("Buy Instagram followers in Canada, ", "in English, French or both."),
        "intro": "Canadian accounts can easily end up with a mostly American audience, simply because the US is next door and louder. If you want to buy Instagram followers in Canada and keep them Canadian, tell us where: Toronto, Vancouver, Montreal, Calgary or the whole country. Real people there come across your profile daily, and those who like it hit follow. {pick_name} usually brings {pick_audience} a month.",
        "hero": {"image": "instagram-hub", "alt": "A Canadian creator's Instagram profile with new followers from Toronto and Montreal"},
        "sections": [
            {
                "h2": "English Canada, French Canada",
                "p": [
                    "Name Montreal or Quebec City and a large share of the people who see your profile will scroll in French; name Calgary or Halifax and English leads. Neither is better. What matters is that your captions match, or at least nod to, the people you're asking to follow.",
                    "Bilingual brands often caption in both languages. If you'd rather keep two audiences apart, two accounts can make more sense than one.",
                ],
            },
            {
                "h2": "Who does well with a Canadian audience",
                "ul": [
                    "Shops that only ship within Canada.",
                    "Cafés, studios and salons that need people within driving distance.",
                    "Creators whose posts lean on Canadian life: the winters, the hockey, the long weekends.",
                    "Brands testing a launch in one province before the rest.",
                ],
            },
            {
                "h2": "Seasons change the feed",
                "p": [
                    "Canadian Instagram has a rhythm: patios and lake weekends in summer, ski hills and cozy indoor content once the snow arrives. Your campaign runs all year, but posts that follow the season give new followers a reason to stay.",
                ],
            },
        ],
        "faqs": [
            ("Can I target one province?", "Yes. Name a province such as Ontario or British Columbia, a single city, or all of Canada. That's where the campaign aims first; for a narrow niche, part of the audience may come from nearby."),
            ("Will some followers be from the US?", "We aim at the place you name, so most come from there. When the closest match for a niche sits just across the border, a share may come from there, which is why naming a city with a big audience in your niche helps."),
            ("Do you charge in Canadian dollars?", "No, prices are in US dollars. Your card issuer converts the charge into Canadian dollars at its own exchange rate, sometimes with a fee."),
            ("Can my French-language account grow with you?", "Yes. Name Quebec or a French-speaking city, and the people who discover your profile will mostly be French speakers. They'll follow, like and comment in French because that's what they speak."),
            ("How many followers come in a month?", "Expect roughly {starter_audience} on {starter_name}, {rising_audience} on {rising_name} and {pro_audience} on {pro_name}. A smaller city may sit at the lower end of a range; a whole province gives the campaign more room."),
        ],
    },
    {
        "service": "followers",
        "country": "de",
        "slug": "instagram/followers/germany",
        "label": "Instagram followers in Germany",
        "title": "Buy Instagram Followers in Germany, Berlin to Munich | Growsterr",
        "description": "Buy Instagram followers in Germany: real people in Berlin, Hamburg, Munich or your own city find your profile and follow by choice. Billed monthly.",
        "h1": ("Buy Instagram followers in Germany, ", "from people who scroll in German."),
        "intro": "To buy Instagram followers in Germany worth having, aim for people who live there, speak the language and chose to follow you. That's all we bring. Real people in Berlin, Hamburg, Munich, Cologne or the region you name come across your profile every day; those who like your posts follow, usually {pick_audience} a month on {pick_name}.",
        "hero": {"image": "instagram-creator-studio", "alt": "A creator in Germany writing an Instagram caption in German at a desk"},
        "sections": [
            {
                "h2": "Du or Sie: write for the people you want",
                "p": [
                    "Most German creators address their followers as du, and many brands now do too, while some shops and professions keep the formal Sie. Pick one and stick with it: a campaign brings people to your profile, but the tone of your captions decides whether they feel spoken to.",
                    "If you post in English, you'll still reach people in Germany, especially in Berlin, Hamburg and Munich, where English is common on Instagram. German captions tend to land better outside the biggest cities.",
                ],
            },
            {
                "h2": "City, state or the whole country",
                "ul": [
                    "A café in Leipzig or a studio in Stuttgart: name the city.",
                    "A brand rooted in Bavaria or the Ruhr: name the region.",
                    "An online shop shipping across Germany: name the country.",
                    "A trade in a smaller town: name the nearest city, so the campaign has enough people to reach.",
                ],
            },
            {
                "h2": "Paying the way it works here",
                "p": [
                    "Plenty of people in Germany reach for PayPal, Klarna or an invoice when they buy online. We don't offer any of those. What we do take is a card, Apple Pay or Google Pay through Stripe; the subscription is billed monthly in US dollars, which your bank converts into euros.",
                ],
            },
        ],
        "faqs": [
            ("Will my followers write in German?", "If they comment, most will, because they're people living in Germany and that's what most of them speak day to day. Some will write in English or another language they're at home in."),
            ("Can I pay with PayPal or Klarna?", "No. Stripe takes the payment, by card, Apple Pay or Google Pay, as a monthly subscription you can cancel yourself from your account at any point."),
            ("Do you offer prices in euros?", "We bill in US dollars only: {starter_price} a month for {starter_name}, {pro_price} for {pro_name}. Your bank statement shows the euro amount."),
            ("Can I target Munich and the area around it?", "Yes. Name Munich, or Upper Bavaria if you also want the towns around it. We aim at the place you write; when the closest match for your niche is just outside it, a few followers may come from there."),
            ("Do you ever sign in to my Instagram account?", "No. We never sign in, never post and never change a setting. All we need is your username and a public profile people can look at."),
        ],
    },
    {
        "service": "followers",
        "country": "gr",
        "slug": "instagram/followers/greece",
        "label": "Instagram followers in Greece",
        "title": "Buy Instagram Followers in Greece: Real, Local People | Growsterr",
        "description": "Buy Instagram followers in Greece from real people in Athens, Thessaloniki or the islands, or from the countries your summer guests come from.",
        "h1": ("Buy Instagram followers in Greece, ", "or from wherever your guests live."),
        "intro": "Not every account that wants to buy Instagram followers in Greece needs Greek followers. A taverna in Thessaloniki does; a villa on Santorini may need people in London or Munich who are planning their summer. Tell us which, and we show your profile every day to real people in the place you name. On {pick_name}, a month usually brings {pick_audience} new followers.",
        "hero": {"image": "instagram-hub", "alt": "An island hotel's Instagram profile gaining followers ahead of the summer season"},
        "sections": [
            {
                "h2": "Two kinds of Greek accounts",
                "p": [
                    "Accounts that serve people living in Greece, such as cafés in Athens, shops in Patras or gyms in Heraklion, grow best with a local audience that scrolls in Greek and can walk in any week of the year.",
                    "Accounts that serve visitors work the other way round. Your future guests live abroad, so name the country they come from, and save Greece for the months when locals are your customers too.",
                ],
            },
            {
                "h2": "Planning around the season",
                "ul": [
                    "Start a few months before your season, so new followers have time to get to know you before they book.",
                    "Keep posting in winter: a silent off-season feed is where many island accounts lose people.",
                    "With {rising_name} or {pro_name}, put attention on the posts that show what you're opening this year.",
                    "If your guests and your locals are different people, decide which group this month is for.",
                ],
            },
            {
                "h2": "Greek captions, English captions",
                "p": [
                    "Locals scroll in Greek and appreciate being addressed in it; visitors mostly read English. Many hospitality accounts write both, Greek first or English first depending on who they want to reach.",
                    "Name days, Easter and the August holidays are moments Greek followers expect a local account to mark. A short post on the day says you're part of the place, not just passing through it.",
                ],
            },
        ],
        "faqs": [
            ("Can I target the island I'm on?", "You can name it, but a single island is a small audience for a month-long campaign. Naming the region, or all of Greece, gives us more people to reach, and your posts decide who follows."),
            ("Can my followers come from abroad instead of Greece?", "Yes. You choose the place: Greece, a city there, or the country your visitors come from. We aim at that place first."),
            ("Do you charge in euros?", "No. The price is in US dollars, charged through Stripe to your card, Apple Pay or Google Pay; your bank converts it into euros."),
            ("Is it worth running a campaign in winter?", "If your customers are local, your season is the whole year. If they're summer visitors, starting a few months ahead gives new followers time to plan a trip around you."),
            ("Will my Greek followers like and comment?", "Many will, from the same accounts that follow you. With {pick_name}, a typical month brings {pick_likes} likes and {pick_comments} comments along with the followers."),
        ],
    },
    {
        "service": "followers",
        "country": "in",
        "plan": "starter",
        "slug": "instagram/followers/india",
        "label": "Instagram followers in India",
        "title": "Buy Instagram Followers Cheap in India, Real People | Growsterr",
        "description": "Buy Instagram followers cheap in India without buying bots: {starter_name} brings {starter_audience} real followers a month for {starter_price}, billed in USD.",
        "h1": ("Buy Instagram followers cheap in India, ", "and pay for people, not numbers."),
        "intro": "Wanting to buy Instagram followers cheap in India makes sense: budgets are real, and a creator in Jaipur or a café in Kochi shouldn't overspend on growth. The question is what the money buys. For {starter_price} a month, {starter_name} typically brings {starter_audience} new followers, real people in India who decided to follow, plus likes and comments from those same accounts.",
        "hero": {"image": "instagram-followers", "alt": "An Indian creator's Instagram follower count rising with real people from Mumbai and Jaipur"},
        "sections": [
            {
                "h2": "What the cheapest rate in India really gets you",
                "p": [
                    "Packs that promise followers, likes and views at the cheapest rate in India all work the same way: accounts made by software, released onto your profile in a batch. They're priced at almost nothing because there's no one there to pay, and they leave in the next clean-up.",
                    "Real people cost more than that, though not by much once you divide it out. Each follower {starter_name} brings costs a few US cents, and the likes and views they give your posts come at no extra charge.",
                ],
            },
            {
                "h2": "Paying in rupees, UPI and Indian cards",
                "ul": [
                    "Prices are set in US dollars; we don't show or charge amounts in INR.",
                    "Your bank turns the dollar charge into Indian rupees at its own rate.",
                    "UPI isn't accepted, nor are wallets or net banking.",
                    "A debit or credit card that allows international online payments works, as does a card saved in Apple Pay or Google Pay.",
                ],
            },
            {
                "h2": "Real Indian followers, city by city",
                "ul": [
                    "Mumbai: a fast English-and-Hindi audience for fashion, food, fitness and film.",
                    "Jaipur: a natural fit for jewellery, block prints, heritage stays and wedding shoots.",
                    "Kerala: Malayalam captions, Kochi and Thiruvananthapuram, and the travel and food people there care about.",
                    "All of India: for creators who post in English or Hindi for the whole country.",
                ],
                "image": {"image": "instagram-real-people", "alt": "New followers from Mumbai, Jaipur and Kochi reacting to an Instagram Reel"},
            },
        ],
        "faqs": [
            ("Can I buy Instagram followers in Indian rupees?", "You pay the dollar price, and your bank does the conversion: {starter_name} is {starter_price} a month, and your statement shows what that came to in rupees. We don't run separate INR prices."),
            ("Do you accept UPI?", "No. Payment goes through Stripe by card, Apple Pay or Google Pay. Google Pay at our checkout means a card saved in your Google account, not a UPI ID."),
            ("Are these real Indian followers?", "Yes: people in the place you name, India or any city or state in it, each on their own account. Each one saw your profile and chose to follow; none is a profile made to fill a number."),
            ("Do likes and views come with the followers?", "They do, and from the same people. On {starter_name} that's usually {starter_likes} likes and {starter_comments} comments in a month, plus views on the posts and Reels they watch. Views aren't counted ahead of time: each is someone choosing to watch."),
            ("Why a monthly package instead of a one-time cheap pack?", "A pack lands once and then shrinks as fake accounts are removed. A package keeps bringing real people every day, and you can stop it whenever you like."),
            ("Can I target Kerala and get Malayalam-speaking followers?", "Name Kerala, or a city such as Kochi, and people there see your profile. Whether they follow depends on your posts, so Malayalam captions help if that's the audience you want."),
        ],
    },
    {
        "service": "followers",
        "country": "ke",
        "slug": "instagram/followers/kenya",
        "label": "Instagram followers in Kenya",
        "title": "Buy Instagram Followers in Kenya With Real People | Growsterr",
        "description": "Buy Instagram followers in Kenya from real people in Nairobi, Mombasa, Kisumu or the town you choose. Paid by card in US dollars; no M-Pesa, no login needed.",
        "h1": ("Buy Instagram followers in Kenya, ", "from Nairobi to the coast."),
        "intro": "If you're about to buy Instagram followers in Kenya, picture who they should be: people in Nairobi, Mombasa or Kisumu who might buy your designs, come to your event or share your skits. That's exactly who our campaign reaches. Each day our campaign puts your profile before real people in the place you name, and whoever enjoys it follows. On {pick_name}, that's typically {pick_audience} new followers a month.",
        "hero": {"image": "instagram-followers-1000", "alt": "A Nairobi fashion label's Instagram profile gaining followers day by day"},
        "sections": [
            {
                "h2": "English, Swahili and Sheng",
                "p": [
                    "Kenyan Instagram moves between English, Swahili and Sheng, often inside one caption. We don't target languages, we target places, so your new followers speak whatever people around them speak. Name Nairobi and you'll likely see Sheng in the replies; name Mombasa and Swahili comes through stronger.",
                ],
            },
            {
                "h2": "Who grows well in Kenya",
                "ul": [
                    "Fashion and beauty brands that sell on Instagram and deliver across Nairobi.",
                    "Comedians and skit makers building an audience before taking it to YouTube or the stage.",
                    "Restaurants, cafés and rooftop spots in Westlands and Kilimani.",
                    "Safari camps and coastal hotels, which often aim at the countries their guests come from instead.",
                ],
            },
            {
                "h2": "Paying from Kenya",
                "p": [
                    "We don't take M-Pesa. You pay through Stripe instead, with a card, Apple Pay or Google Pay, and the subscription renews monthly in US dollars. A Visa or Mastercard debit card that allows online payments abroad usually works, and your bank converts the charge into shillings.",
                ],
            },
        ],
        "faqs": [
            ("Can I pay for Instagram followers with M-Pesa?", "No. Payment is card, Apple Pay or Google Pay, handled by Stripe. A monthly subscription needs a payment method Stripe can renew, and M-Pesa isn't one we accept."),
            ("Can I target Nairobi only?", "Yes. Name Nairobi, a county, or the whole of Kenya. We aim at the place you name first; for a narrow niche, a share of followers may come from nearby towns."),
            ("Will my followers be real Kenyans?", "They'll be real people in the place you named, on their own accounts. We target where people are, so a Nairobi campaign brings people who live in or around Nairobi, whatever their background."),
            ("How quickly will I see results?", "Your campaign starts soon after you order, and new followers come in from the first days. It builds a little every day; nothing lands in one burst."),
            ("Do likes and comments come too?", "Yes, from the same people who follow: around {pick_likes} likes and {pick_comments} comments in a typical {pick_name} month."),
        ],
    },
    {
        "service": "followers",
        "country": "kw",
        "slug": "instagram/followers/kuwait",
        "label": "Instagram followers in Kuwait",
        "title": "Buy Instagram Followers in Kuwait, Real and Local | Growsterr",
        "description": "Buy Instagram followers in Kuwait from real people in Kuwait City, Salmiya, Hawalli or wherever your customers are. Arabic and English audiences, monthly.",
        "h1": ("Buy Instagram followers in Kuwait ", "for the shop that lives on Instagram."),
        "intro": "In Kuwait, a lot of business starts on Instagram: home bakers, perfume blends, abaya designers, cafés found through a friend's story. So when you buy Instagram followers in Kuwait, make them people who can order from you. Real people in Kuwait City, Salmiya, Hawalli or the area you name see your profile every day. Expect around {pick_audience} new followers in a typical {pick_name} month.",
        "hero": {"image": "instagram-creator-studio", "alt": "A Kuwaiti home bakery photographing its desserts for an Instagram post"},
        "sections": [
            {
                "h2": "A small country, a close audience",
                "p": [
                    "Kuwait is compact, so a campaign aimed at the whole country still reaches people who could drive to you in an evening. That makes the country itself a good choice for most accounts; naming a single area only makes sense when your customers really are concentrated there.",
                    "Word travels quickly in a close audience, too. When real people follow and talk about your page, their friends notice.",
                ],
            },
            {
                "h2": "Arabic, English, or both",
                "p": [
                    "Your followers will read Arabic, English or both, depending on who your posts speak to. Captions in Kuwaiti Arabic feel personal to local customers; English reaches the many residents who don't read Arabic. Plenty of shops write both and let the reader choose.",
                ],
            },
            {
                "h2": "Busy seasons on Kuwaiti Instagram",
                "ul": [
                    "Ramadan and the two Eids, when orders for sweets, gifts and outfits pick up.",
                    "National Day and Liberation Day in February, when feeds fill with green, white, red and black.",
                    "The cooler months, when cafés, terraces and outdoor events draw people out again.",
                    "On {rising_name} or {pro_name}, pick the posts that should get attention before each season.",
                ],
            },
        ],
        "faqs": [
            ("Can I target the whole of Kuwait?", "Yes, and for most accounts it's the best choice: the country is small enough that followers anywhere in it can reach you. Name an area like Salmiya only if your customers really do cluster there."),
            ("Do you charge in Kuwaiti dinar?", "No. Prices are in US dollars, and the Stripe checkout accepts debit and credit cards along with Apple Pay and Google Pay. Your card issuer handles the exchange into dinar."),
            ("Will my followers be Kuwaiti or expats?", "Both, depending on who your posts appeal to. We aim at the place, and Kuwait's Instagram audience includes Kuwaitis and the many residents who've made a home there."),
            ("Can a home business use this?", "Yes. You need a public Instagram profile and your username; we never ask for your password and never sign in."),
            ("How many likes come with the followers?", "With {pick_name}, typically {pick_likes} a month from the same people, plus {pick_comments} comments. They arrive as people discover your posts, never all at once."),
        ],
    },
    {
        "service": "followers",
        "country": "ng",
        "plan": "starter",
        "slug": "instagram/followers/nigeria",
        "label": "Instagram followers in Nigeria",
        "title": "Buy Instagram Followers in Nigeria: No App, No Login | Growsterr",
        "description": "Looking for an app to buy Instagram followers in Nigeria? You don't need one. Real people in Lagos, Abuja and beyond, paid by card in dollars, not naira.",
        "h1": ("An app to buy Instagram followers in Nigeria? ", "You only need your username."),
        "intro": "Plenty of apps that promise followers in Nigeria ask you to log in with your Instagram account first. Don't. If you came looking for an app to buy Instagram followers in Nigeria, here's the simpler route: order on this site from any phone, give us your username, and real people in Lagos, Ibadan, Kano or wherever you choose start discovering your profile. Over a month, {starter_name} typically adds {starter_audience}.",
        "hero": {"image": "instagram-followers", "alt": "A Lagos creator checking new Instagram followers in a phone browser"},
        "sections": [
            {
                "h2": "Why follower apps want your login",
                "p": [
                    "An app that hands out followers usually needs your account to do it: it signs in as you and follows other people, or lets them follow you as part of a trade. That puts your password in a stranger's hands and fills your profile with accounts that only came for the swap.",
                    "We work from the outside. Your profile is shown to people through promoted campaigns in our partner network, and each of them decides alone whether to follow.",
                ],
            },
            {
                "h2": "Naira, dollars and your card",
                "ul": [
                    "Packages carry a dollar price, not a naira one: {starter_price} a month gets you {starter_name}.",
                    "Many people in Nigeria pay foreign subscriptions with a dollar card, virtual or physical, and that works here too.",
                    "If you use a naira card, check its limit for foreign spending before you order.",
                    "Apple Pay and Google Pay appear at checkout on phones that support them.",
                ],
            },
            {
                "h2": "Lagos, Abuja or the whole country",
                "p": [
                    "A fashion vendor in Lekki, a caterer in Abuja and a comedian with fans everywhere need different audiences. Name the city when your customers are local, and the country when your posts travel; the people we reach decide whether your page is worth following.",
                ],
            },
        ],
        "faqs": [
            ("Do I need to download a Growsterr app?", "No. Everything runs on the website: you order, pay and follow your campaign from your account in any phone browser. Nothing to install, and nothing that asks for your Instagram login."),
            ("Can I pay in naira?", "Not in naira. Stripe charges the package in US dollars; if you pay with a naira card, your bank sets the exchange rate and its own limits apply."),
            ("Will the followers be Nigerian?", "They'll live where you aim the campaign: Nigeria, a state, or a city such as Ibadan or Enugu. Every one of them looked at your page before deciding to follow."),
            ("What do I need to give you?", "Your Instagram username, the place your followers should come from, and a public profile. Never a password: if any app or site asks for it, close the tab."),
            ("Do I get likes along with the followers?", "Yes. The people who follow you like the posts they enjoy, typically {starter_likes} likes a month on {starter_name}, and some leave comments as well."),
        ],
    },
    {
        "service": "followers",
        "country": "np",
        "plan": "starter",
        "slug": "instagram/followers/nepal",
        "label": "Instagram followers in Nepal",
        "title": "Buy Real Instagram Followers in Nepal | Growsterr",
        "description": "Buy real Instagram followers in Nepal: people in Kathmandu, Pokhara or Lalitpur who decide to follow you, not accounts made to fill a number. Monthly.",
        "h1": ("Buy real Instagram followers in Nepal ", "who live where you post."),
        "intro": "When you buy Instagram followers in Nepal, real is the part that matters. A trekking company in Thamel, a momo spot in Patan or a photographer in Pokhara needs people who live there and care, not accounts with no one behind them. Every day your profile reaches real people in the area you choose, and those who like it follow: usually {starter_audience} a month on {starter_name}.",
        "hero": {"image": "instagram-real-people", "alt": "People in Kathmandu discovering a local photographer's Instagram profile"},
        "sections": [
            {
                "h2": "Real means people in Nepal, not people from Nepal",
                "p": [
                    "We target where people are, not where they're from. Name Nepal or a city in it, and everyone who sees your profile is there right now.",
                    "If your audience is Nepalis working in Doha, Kuala Lumpur or Sydney, name that city instead. You'll reach people in that city, Nepali or not, and captions in Nepali decide who stays.",
                ],
            },
            {
                "h2": "Nepali captions bring Nepali followers",
                "p": [
                    "Many Nepali creators post in English for reach. That's fine, but if your customers are local, a caption in Nepali, even a single line, tells them the account is for them.",
                    "Dashain, Tihar and the new year in April are when local feeds fill with greetings, offers and family photos. A local account that joins in feels like a neighbour.",
                ],
            },
            {
                "h2": "What a month costs, per person",
                "ul": [
                    "{starter_name} is {starter_price} a month, priced in US dollars.",
                    "It typically brings {starter_audience} new followers, which works out to a few US cents each.",
                    "Likes and comments from the same people come inside that price.",
                    "Your statement shows the amount in Nepali rupees, at your bank's rate.",
                ],
            },
        ],
        "faqs": [
            ("How do I know these followers are real people?", "Open a few of their profiles: real people have their own photos, friends and uneven posting habits. Then watch your likes and comments move along with your follower count; with fake accounts, they don't."),
            ("Can I pay from Nepal?", "Yes, with a card that allows international online payments, or Apple Pay or Google Pay on a device that offers them, all processed by Stripe. We don't take eSewa, Khalti or bank transfers."),
            ("Can I target Pokhara only?", "Yes, name Pokhara. It's a smaller audience than Kathmandu, so think of it as the centre of your target: if the best match for your niche is nearby, some followers may come from there."),
            ("Do you target Nepalis living abroad?", "We target places, not nationalities. Name the city where that community lives and we'll reach people there; captions in Nepali will draw the ones you're looking for."),
            ("How long until I see the first followers?", "Usually within the first days after your campaign starts, then a few more every day. Your dashboard shows the visits and new followers it measured, one day at a time."),
        ],
    },
    {
        "service": "followers",
        "country": "ph",
        "slug": "instagram/followers/philippines",
        "label": "Instagram followers in the Philippines",
        "title": "Buy Instagram Followers in the Philippines | Growsterr",
        "description": "Buy Instagram followers in the Philippines from real people in Metro Manila, Cebu, Davao or your own city. Taglish welcome; paid by card, cancel any time.",
        "h1": ("Buy Instagram followers in the Philippines ", "who scroll in Taglish."),
        "intro": "Anyone looking to buy Instagram followers in the Philippines wants the people who'll actually show up: at your shop in Quezon City, at your food stall in Cebu, in the comments of your next Reel. We bring real people from Metro Manila, Cebu, Davao or wherever you name, every day of the month, and those who enjoy your posts follow. A month on {pick_name} typically adds {pick_audience}.",
        "hero": {"image": "instagram-followers-1000", "alt": "A Cebu food business's Instagram followers growing through the month"},
        "sections": [
            {
                "h2": "Filipino, English, Taglish, Bisaya",
                "p": [
                    "Instagram captions in the Philippines switch languages as easily as their writers do. Tagalog and Taglish carry Metro Manila; Cebuano is everywhere in Cebu and much of Mindanao. Your followers come from the place you name, so match your captions to it and follows tend to come easier.",
                ],
            },
            {
                "h2": "The calendar Filipino followers live by",
                "ul": [
                    "The ber months: from September, Christmas content starts early, and so do gift orders.",
                    "Payday weekends, when more people browse shops and food spots.",
                    "Summer from March to May, for travel, resorts and beach content.",
                    "With {rising_name} or {pro_name}, choose which posts get the attention ahead of each season.",
                ],
            },
            {
                "h2": "Paying from the Philippines",
                "p": [
                    "We don't take GCash or Maya. Pay at the Stripe checkout with a card; Apple Pay and Google Pay appear there on devices that support them. The price is in US dollars, and a debit card enabled for online purchases abroad is usually enough.",
                ],
            },
        ],
        "faqs": [
            ("Can I pay with GCash?", "No. Because the package renews every month, it needs a card Stripe can charge each time, or Apple Pay or Google Pay with a card behind it. Your bank shows the charge in pesos."),
            ("Can I target Cebu only?", "Yes. Name Cebu City, the province, or the whole of the Visayas. A wider area gives the campaign more people; a single city keeps your followers close."),
            ("Will my followers be Filipino?", "We aim at a location, not a nationality, so a campaign for Makati reaches people living in and around Makati, whoever they are."),
            ("Do they like and comment too?", "Many do, from the same accounts that follow: {pick_likes} likes and {pick_comments} comments is a typical month on {pick_name}."),
            ("Will Christmas season change my growth?", "The campaign itself runs evenly, every day. What changes is what people want to see: posts that fit the season give new visitors more reason to follow."),
        ],
    },
    {
        "service": "followers",
        "country": "pk",
        "plan": "starter",
        "slug": "instagram/followers/pakistan",
        "label": "Instagram followers in Pakistan",
        "title": "Buy Real Instagram Followers in Pakistan | Growsterr",
        "description": "Buy real Instagram followers in Pakistan and skip the bulk packs: people in Karachi, Lahore or Islamabad find your profile and follow by choice. Monthly.",
        "h1": ("Buy real Instagram followers in Pakistan, ", "not a number that disappears."),
        "intro": "Plenty of offers to buy Instagram followers in Pakistan promise thousands for almost nothing, and many of those followers are gone after the next clean-up. Real ones cost more and stay. Every day, people in Karachi, Lahore, Islamabad or your own city see your profile, and whoever likes what they find follows. The usual range on {starter_name} is {starter_audience} new followers a month.",
        "hero": {"image": "instagram-followers", "alt": "A Lahore fashion brand's Instagram profile with followers from across Pakistan"},
        "sections": [
            {
                "h2": "Real Pakistani followers, city by city",
                "ul": [
                    "Karachi: the biggest audience, for food, fashion, business and comedy.",
                    "Lahore: weddings, design, food and a big creative scene.",
                    "Islamabad and Rawalpindi: cafés, fitness, education and family brands.",
                    "Faisalabad, Multan, Peshawar: name them directly if your customers are there.",
                ],
            },
            {
                "h2": "Signs you're looking at real followers",
                "p": [
                    "Real followers from Pakistan look like the people you know: their own photos, a cousin's wedding, cricket, food. They don't all follow in the same minute, and some of them like and comment on what you post next.",
                    "Bulk followers look different: empty grids, names that don't match the photos, and a count that falls whenever Instagram removes fake accounts.",
                ],
            },
            {
                "h2": "Paying from Pakistan",
                "p": [
                    "Packages are billed in US dollars. You can pay with any major card, or tap Apple Pay or Google Pay at the Stripe checkout. We don't take wallets or bank transfers, so use a debit or credit card cleared for international online payments.",
                ],
            },
        ],
        "faqs": [
            ("What makes a follower real?", "A person behind the account who saw your profile and decided to follow. Real followers come and go at their own pace, react to some posts and ignore others, the way any audience does."),
            ("Can I target Karachi only?", "Yes. Name Karachi, a province such as Sindh, or the whole country. The place you name is where the campaign aims, and your posts decide who follows."),
            ("How much do real followers cost in Pakistan?", "{starter_name} is {starter_price} a month for typically {starter_audience} new followers, with {starter_likes} likes and {starter_comments} comments from the same people. That's a few US cents per real person."),
            ("Will my followers drop later?", "Not in the waves bulk followers do, because there's no fake account to remove. A real person may unfollow now and then, as in any audience."),
            ("Do you ask for my password?", "Never. We need your username and a public profile. Any service that wants your login can do things in your name, and you should never allow that."),
        ],
    },
    {
        "service": "followers",
        "country": "tr",
        "slug": "instagram/followers/turkey",
        "label": "Instagram followers in Turkey",
        "title": "Buy Instagram Followers in Turkey, Aimed by City | Growsterr",
        "description": "Buy Instagram followers in Turkey from real people in Istanbul, Ankara, İzmir or Antalya, for brands and creators reaching a Turkish-speaking audience.",
        "h1": ("Buy Instagram followers in Turkey, ", "city by city."),
        "intro": "Reading this in English? You might be a foreign brand opening in Istanbul, a hotel in Antalya or a creator whose captions aren't in Turkish yet. Whatever brought you to buy Instagram followers in Turkey, the people behind them should live there. Our campaign introduces your profile to people in Istanbul, Ankara, İzmir or any city you choose, daily. Typical growth on {pick_name}: {pick_audience} followers a month.",
        "hero": {"image": "instagram-hub", "alt": "An Istanbul café's Instagram grid with new followers from Kadıköy and Beşiktaş"},
        "sections": [
            {
                "h2": "Writing for a Turkish audience",
                "p": [
                    "People in Turkey scroll mostly in Turkish. A Turkish caption tells a local visitor the account is for them; English alone tends to reach the cities' international crowd and few others.",
                    "If you don't write Turkish yet, start with short bilingual captions and let your audience show you which they prefer.",
                ],
            },
            {
                "h2": "Choosing the city",
                "ul": [
                    "Istanbul: the biggest audience, from Kadıköy cafés to Nişantaşı boutiques.",
                    "Ankara: students, families and a steady local crowd.",
                    "İzmir: the Aegean, food and an easygoing coastal life.",
                    "Antalya and Bodrum: for hospitality, though your guests may live abroad, so consider naming their country instead.",
                ],
            },
            {
                "h2": "Holidays and seasons",
                "p": [
                    "Ramazan and Kurban Bayramı, New Year's shopping and the long summer on the coast all change what people want to see. Your campaign doesn't change with the calendar; your posts should.",
                ],
            },
        ],
        "faqs": [
            ("Can I pay in Turkish lira?", "No. The price is set in dollars, and Stripe processes every payment, whether by card or by Apple Pay or Google Pay; the lira amount is worked out by your bank at its own rate."),
            ("Can I target Istanbul only?", "Yes. Name Istanbul, or a district if your customers are concentrated there, though a whole city gives the campaign more people to reach."),
            ("Will my followers be Turkish?", "Your followers will be whoever lives in the city you choose. In Istanbul or Antalya that includes plenty of residents from elsewhere, so your audience will look like the city."),
            ("Does this suit a foreign brand entering Turkey?", "It suits it well: name the city you're opening in, and people there discover your profile before your doors open. Bigger launches with influencer campaigns start with a conversation on WhatsApp or by email."),
            ("Do comments come in Turkish?", "If people comment, they write in their own language, which in Turkey is mostly Turkish. With {pick_name}, a typical month brings {pick_comments} comments and {pick_likes} likes from the same people."),
        ],
    },
    {
        "service": "followers",
        "country": "ug",
        "plan": "starter",
        "slug": "instagram/followers/uganda",
        "label": "Instagram followers in Uganda",
        "title": "Buy Instagram Followers in Uganda: Kampala and Beyond | Growsterr",
        "description": "Buy Instagram followers in Uganda from real people in Kampala, Entebbe, Jinja or your own town. Billed in US dollars by card; no mobile money, no login.",
        "h1": ("Buy Instagram followers in Uganda, ", "starting with Kampala."),
        "intro": "To buy Instagram followers in Uganda that are worth having, start with the people who'd actually come to your show, eat at your restaurant or buy from your boutique. Every day, real people in Kampala, Entebbe, Jinja, Mbarara or the place you name come across your profile, and the ones who like it follow. {starter_audience} new followers is a typical month on {starter_name}, with likes and comments from them too.",
        "hero": {"image": "instagram-followers", "alt": "A Kampala musician's Instagram profile gaining new followers through the month"},
        "sections": [
            {
                "h2": "Kampala is the start, not the limit",
                "p": [
                    "Many Ugandan accounts begin with Kampala, where the audience is largest and English, Luganda and Swahili mix freely in the comments. If your customers are in Gulu, Mbarara or Mbale, name that town; the audience is smaller, so treat it as the centre rather than a fence.",
                    "Tourism accounts, such as lodges near the gorillas or rafting outfits on the Nile at Jinja, usually do better aiming at the countries their visitors come from.",
                ],
            },
            {
                "h2": "No mobile money, and why",
                "p": [
                    "We don't take MTN MoMo, Airtel Money or other mobile money. The package is a monthly subscription that Stripe renews automatically, which needs a card, or Apple Pay or Google Pay where your phone has them. Prices are in US dollars, and your statement shows the amount in shillings.",
                ],
            },
            {
                "h2": "What one month brings",
                "ul": [
                    "Typically {starter_audience} new followers with {starter_name}, at {starter_price} a month.",
                    "Around {starter_likes} likes and {starter_comments} comments from those same people.",
                    "Views on your Reels from people who choose to watch them.",
                    "No contract: stop whenever you like and keep the followers you gained.",
                ],
            },
        ],
        "faqs": [
            ("Can I pay for followers with mobile money in Uganda?", "No. Cards, Apple Pay and Google Pay are the only options, all through Stripe. A Visa or Mastercard debit card that works online abroad is the usual way to pay from Uganda."),
            ("Are the followers real Ugandans?", "Yes, real people around the place you choose, each using an account of their own; a Kampala campaign reaches people in and around Kampala."),
            ("Can I grow a music or events page?", "Yes. People who enjoy your posts follow, and they're the ones most likely to come to a show. We can't promise a crowd on a given night, but we can grow the audience you announce it to."),
            ("How long before I see followers?", "From the first days of your campaign, a few at a time, then more each week. Nothing arrives in a single batch."),
            ("Can I cancel after a month?", "Yes, from your account, any time. You keep the rest of the month you paid for, and nothing renews after it."),
        ],
    },
    {
        "service": "followers",
        "country": "us",
        "slug": "instagram/followers/united-states",
        "label": "Instagram followers in the USA",
        "title": "Buy IG Followers in the USA: Real People, Any City | Growsterr",
        "description": "Buy IG followers in the USA from real people in New York, Los Angeles, Houston or the state you name: real US followers who chose you, from {from_price} monthly.",
        "h1": ("Buy IG followers in the USA, ", "one city or coast to coast."),
        "intro": "To buy IG followers in the USA that are real, the targeting has to be as specific as your audience. A barber in Atlanta, a Brooklyn bakery and a fitness coach selling online nationwide need very different people. Name a city, a state or the whole country, and your profile starts appearing to real people there every day. {pick_name} typically brings {pick_audience} new followers a month.",
        "hero": {"image": "instagram-followers-1000", "alt": "A creator's Instagram follower line climbing with real people from across the United States"},
        "sections": [
            {
                "h2": "Four time zones, one audience",
                "p": [
                    "An audience spread across the US is awake at different hours: when it's 9 p.m. in New York, Los Angeles is still at dinner. If your followers are nationwide, test your posting times; if they're in one city, post for that city's evening.",
                ],
            },
            {
                "h2": "Real US followers, and how to tell",
                "ul": [
                    "They follow over days and weeks, not in a single afternoon.",
                    "Their profiles are lived-in: friends, vacations, their own posts.",
                    "Some of them like, comment and share what you post next.",
                    "Your count doesn't fall back when Instagram removes fake accounts.",
                ],
            },
            {
                "h2": "English, Spanish, or both",
                "p": [
                    "In Miami, Los Angeles, San Antonio and much of Texas, Instagram is often bilingual. We aim at places, so naming those cities brings Spanish speakers along with everyone else, and a caption in both languages welcomes them.",
                ],
                "image": {"image": "instagram-real-people", "alt": "New US followers commenting in English and Spanish on a creator's Instagram post"},
            },
        ],
        "faqs": [
            ("Can I target one state, like Texas or California?", "Yes. Name a state, a city or the whole US. A state gives the campaign plenty of people to reach; a single city keeps your followers local."),
            ("Are the followers real Americans?", "Yes: people physically in the US, each with their own account. Targeting is by location, so a US campaign brings people who live there, not profiles dressed up to look American."),
            ("How do I pay from the US?", "Stripe takes cards, plus Apple Pay and Google Pay on supported devices. Prices are in US dollars, so there's no conversion: {pick_name} is {pick_price} a month."),
            ("Is IG growth this way safe for my account?", "We never sign in, never ask for your password and never act in your name. People see your profile and decide for themselves. What Instagram does with any account is Instagram's call, and nobody honest can promise more."),
            ("Do you work with US small businesses?", "Yes. Shops, studios, restaurants and service businesses use the same packages as creators. Name the city you serve, and the people who see your profile are people who could become customers."),
        ],
    },
    {
        "service": "followers",
        "country": "vn",
        "slug": "instagram/followers/vietnam",
        "label": "Instagram followers in Vietnam",
        "title": "Buy Instagram Followers in Vietnam, Hanoi to Saigon | Growsterr",
        "description": "Buy Instagram followers in Vietnam from real people in Ho Chi Minh City, Hanoi or Da Nang who choose to follow. Vietnamese audiences, priced in USD, monthly.",
        "h1": ("Buy Instagram followers in Vietnam ", "who know your street."),
        "intro": "In Vietnam, Instagram is where cafés, fashion labels and young creators show their best side, while much of everyday chat happens elsewhere. That's the audience to reach when you buy Instagram followers in Vietnam: people in Ho Chi Minh City, Hanoi or Da Nang who scroll for style, food and places to go. {pick_name} usually turns daily visits from them into {pick_audience} new followers a month.",
        "hero": {"image": "instagram-creator-studio", "alt": "A Saigon café photographing its iced coffee for an Instagram post"},
        "sections": [
            {
                "h2": "Saigon, Hanoi, Da Nang: different feeds",
                "ul": [
                    "Ho Chi Minh City: the biggest audience, quick to try new cafés, brands and food spots.",
                    "Hanoi: old-quarter charm, coffee culture and a strong local fashion scene.",
                    "Da Nang and Hoi An: beaches, travel and hospitality, often aimed at visitors too.",
                    "The whole country: for brands that ship nationwide or post for everyone.",
                ],
            },
            {
                "h2": "Write in Vietnamese, with the accents",
                "p": [
                    "Captions in Vietnamese, with proper diacritics, read as local and careful. English works for travel and for younger city audiences, but it can make a neighbourhood café feel like it's talking to tourists. Since your followers come from wherever you aim the campaign, write for the people there.",
                ],
            },
            {
                "h2": "Tết and the year's rhythm",
                "p": [
                    "The weeks before Tết are when people shop for gifts, outfits and food, and when local brands post their most important campaigns. Start your package a month or two before, so new followers already know you when the season arrives.",
                ],
            },
        ],
        "faqs": [
            ("Do you charge in đồng?", "No. Everything is priced in US dollars, and the đồng amount depends on your bank's rate that day."),
            ("Can I pay with MoMo or a bank transfer?", "No. We accept cards and the Apple Pay or Google Pay wallets, processed by Stripe, because the package renews monthly. An international debit or credit card is the simplest way to pay from Vietnam."),
            ("Can I target Da Nang only?", "Yes. Name Da Nang, or Da Nang and Hoi An together, and the campaign aims there first. A smaller city has a smaller audience, so some followers may come from nearby provinces."),
            ("Will my followers be Vietnamese?", "Mostly, yes: they'll be people living in the place you name. Tourist areas can add visitors and expats to the mix."),
            ("Do my new followers also engage?", "Many do. A typical month on {pick_name} brings {pick_likes} likes and {pick_comments} comments, from the same accounts that follow."),
        ],
    },
    {
        "service": "followers",
        "country": "za",
        "slug": "instagram/followers/south-africa",
        "label": "Instagram followers in South Africa",
        "title": "Buy Instagram Followers in South Africa | Growsterr",
        "description": "Buy Instagram followers in South Africa from real people in Johannesburg, Cape Town, Durban or Pretoria. Aim at one city or the whole country, month by month.",
        "h1": ("Buy Instagram followers in South Africa: ", "Joburg, Cape Town or Durban."),
        "intro": "Joburg and Cape Town can feel like different countries on Instagram, and Durban is different again. So before you buy Instagram followers in South Africa, decide which South Africa you're talking to. Name the city or province, or the whole country, and that's where real people meet your profile each day; those who like your posts follow, typically {pick_audience} a month on {pick_name}.",
        "hero": {"image": "instagram-real-people", "alt": "People in South Africa discovering a Cape Town creator's Instagram profile and following"},
        "sections": [
            {
                "h2": "Many languages, one feed",
                "p": [
                    "South African Instagram runs mostly in English, with isiZulu, isiXhosa, Afrikaans, Sesotho and Setswana woven through captions and comments. A line in the language of your city's biggest audience goes a long way: isiZulu in Durban, Afrikaans in parts of the Western Cape.",
                ],
            },
            {
                "h2": "Who grows with a South African audience",
                "ul": [
                    "Fashion and beauty brands selling online across the country.",
                    "Restaurants, markets and weekend spots around Cape Town.",
                    "Musicians and DJs building a following in the amapiano scene.",
                    "Coaches and creators in Joburg and Pretoria selling services online.",
                ],
            },
            {
                "h2": "Paying from South Africa",
                "p": [
                    "Your package is billed monthly in US dollars. Cards work, and so do Apple Pay and Google Pay, all through Stripe. Your bank converts the charge into rand, sometimes with a foreign transaction fee, so the amount on your statement can move a little with the exchange rate.",
                ],
            },
        ],
        "faqs": [
            ("Can I target Cape Town only?", "Yes. Name Cape Town, the Western Cape, or all of South Africa. The campaign aims at the place you name; when the closest match for your niche sits just outside it, some followers may come from there."),
            ("Will my followers be South African?", "They'll be people who live in the area you choose. A Johannesburg campaign reaches people in and around Johannesburg, whoever they are and wherever they grew up."),
            ("Is it worth targeting the whole country?", "If you sell online or post for everyone, yes: it gives the campaign the most people to reach. If your customers need to visit you, a city or province brings more followers who can."),
            ("Do I keep the followers if I stop?", "Yes. They followed because they wanted to. Cancelling only means no new people are brought in after your paid month ends."),
            ("Do you need my Instagram login?", "No. Your username and a public profile are all we need. Nobody on our side signs in or acts on your account."),
        ],
    },
    # --- Likes ----------------------------------------------------------------------------
    {
        "service": "likes",
        "country": "au",
        "slug": "instagram/likes/australia",
        "label": "Instagram likes from Australia",
        "title": "Buy Instagram Likes in Australia on Aussie Time | Growsterr",
        "description": "Buy Instagram likes in Australia from real people in Sydney, Melbourne, Brisbane or Perth, who like your posts in their own time zone. Inside every package.",
        "h1": ("Buy Instagram likes in Australia ", "from people awake when you post."),
        "intro": "Likes from the other side of the world arrive while Australia sleeps, and it shows. To buy Instagram likes in Australia that look right, they should come from people in Sydney, Melbourne, Brisbane, Perth or Adelaide, scrolling on Australian time. Our packages bring those people to your profile, where they follow and like whatever catches them. {pick_name} usually adds up to {pick_likes} likes a month.",
        "hero": {"image": "instagram-hub", "alt": "Likes from people in Sydney and Melbourne landing on an Instagram post in the evening"},
        "sections": [
            {
                "h2": "Likes come with the follow",
                "p": [
                    "Likes are never a product of their own here. Each package puts your profile in front of people in the place you choose; the ones who enjoy it follow, then like what they see, today and on the posts you share next month. That's why Australian likes from us arrive with Australian followers and comments, from the same accounts.",
                ],
            },
            {
                "h2": "Perth is not Sydney",
                "p": [
                    "Australia spans three main time zones, and five once daylight saving starts in some states and not others. If your audience is national, post when the east coast is scrolling; if it's Perth, post for Perth's evening. People like posts when they see them, so timing matters more than any number.",
                ],
            },
            {
                "h2": "Summer at Christmas, and other local cues",
                "ul": [
                    "Christmas lands in summer: beach and barbecue posts beat snow.",
                    "Footy finals, the Melbourne Cup and long weekends shape what people want to see.",
                    "Australian spelling and slang in captions make a profile feel local.",
                    "{rising_name} and {pro_name} add one thing: you pick the posts that get shown.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy likes for just one post?", "No single-post orders. Likes arrive inside a monthly package, from people who discover your profile. If you're on {rising_name} or {pro_name}, tell us which posts matter most and they get the attention; the likes each one collects come down to who sees it."),
            ("Will the likes come from Australians?", "They're from whichever place you set: Australia, a state, or a city such as Brisbane or Adelaide. The campaign aims there first; for a narrow niche, a few may come from nearby."),
            ("Do you charge in Australian dollars?", "No. Prices are in US dollars, {pick_price} a month for {pick_name}, and the Australian dollar amount on your statement is your bank's conversion."),
            ("How many likes can an Australian account expect?", "Expect {pick_likes} on {pick_name} in a typical month; the smallest package, {starter_name}, brings {starter_likes}. Followers and comments come alongside them."),
            ("Do likes help a post reach more Australians?", "Likes from people who actually saw the post are part of what helps it travel, alongside comments, shares and watch time. We can't promise reach to anyone; we can make sure every like is a person."),
        ],
    },
    {
        "service": "likes",
        "country": "bd",
        "plan": "starter",
        "slug": "instagram/likes/bangladesh",
        "label": "Instagram likes from Bangladesh",
        "title": "Buy Instagram Likes in BD: Real People in Bangladesh | Growsterr",
        "description": "Buy Instagram likes in BD from real people in Dhaka, Chattogram or Sylhet who see your posts and enjoy them. Included with followers in every monthly package.",
        "h1": ("Buy Instagram likes in BD ", "from people who'd buy from you."),
        "intro": "If you're searching to buy Instagram likes in BD, chances are you sell something: a saree collection, cakes from your home kitchen, a photography package. Likes help when they come from people in Bangladesh who might buy. Ours do: people in Dhaka, Chattogram, Sylhet or wherever you sell find your profile, follow, and tap like on what they enjoy: typically {starter_likes} a month on {starter_name}.",
        "hero": {"image": "instagram-real-people", "alt": "People in Dhaka liking a boutique's new saree collection on Instagram"},
        "sections": [
            {
                "h2": "Why likes from abroad don't sell sarees",
                "p": [
                    "Anyone can tap a like count and see who liked a post. A Dhaka shopper who finds a list of strangers from other continents learns nothing good about your shop.",
                    "Likes from people in their own city tell them the shop is real and local. That's the kind we bring, because the campaign is aimed at the place you name.",
                ],
            },
            {
                "h2": "Eid, Pohela Boishakh and sale seasons",
                "ul": [
                    "Before Eid, new collections go up and people browse more; it's a good moment to have {rising_name} or {pro_name} point attention at your new posts.",
                    "Pohela Boishakh brings red and white everywhere, and a natural reason to post.",
                    "Winter wedding season fills feeds with jewellery, outfits and photographers.",
                    "Whatever the season, post when your customers are online: likes come from people who see your posts.",
                ],
            },
            {
                "h2": "One price covers likes, followers and comments",
                "p": [
                    "Likes aren't a separate order. {starter_name} costs {starter_price} a month, priced in US dollars, and typically brings {starter_audience} new followers, who between them give those {starter_likes} likes and {starter_comments} comments. Your bank turns the dollar charge into taka.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy likes on one post only?", "Not as a separate purchase. {rising_name} and {pro_name} let you steer the campaign toward chosen posts, but the likes each post gets depend on who enjoys it."),
            ("Will the likes be from Bangladeshi accounts?", "From real people where you aim the campaign, each liking from their own account. Name Bangladesh or a city, and the campaign starts there."),
            ("Do Reels get likes too?", "Yes. Reels show up on your profile alongside photos, and visitors like whichever they enjoy. A Reel shot in your shop or kitchen can feel more personal than a product photo."),
            ("How soon do likes start showing up?", "In the first days of your campaign, as the first people reach your profile. They keep arriving across the month, a few at a time."),
            ("Why do your likes cost more than BD likes packages?", "Because a person is behind every one, and most come with a follower. Cheap packs are cheap because nobody is there: those accounts can't buy from you, and they can disappear when fake profiles are removed."),
        ],
    },
    {
        "service": "likes",
        "country": "gb",
        "slug": "instagram/likes/united-kingdom",
        "label": "Instagram likes from the UK",
        "title": "Buy Instagram Likes in the UK, London to Glasgow | Growsterr",
        "description": "Buy Instagram likes in the UK from real people in London, Manchester, Birmingham or Glasgow. They follow, like and comment, inside every monthly package.",
        "h1": ("Buy Instagram likes in the UK ", "from people who'd actually pop in."),
        "intro": "A like from someone in Leeds means more to a Leeds bakery than a hundred from abroad. To buy Instagram likes in the UK that count, start with people: real people in London, Manchester, Birmingham, Glasgow or your own town discover your profile, follow if they like it, and like the posts they enjoy. On {pick_name}, that's typically {pick_likes} likes a month, together with followers and comments.",
        "hero": {"image": "instagram-followers", "alt": "A Leeds bakery's Instagram post collecting likes from people nearby"},
        "sections": [
            {
                "h2": "Four nations, one campaign",
                "p": [
                    "You can aim at the whole UK, one nation such as Scotland or Wales, a region like the North West, or a single city. A national brand gets the widest audience; a pub in Cardiff gets people who could be there by Friday.",
                ],
            },
            {
                "h2": "British feeds have their own rhythm",
                "ul": [
                    "The weather shapes the week: a sunny Saturday post lands differently from a rainy one.",
                    "Bank holidays, Bonfire Night and the run-up to Christmas give people reasons to browse.",
                    "British spelling and a dry caption suit the audience better than borrowed American hype.",
                    "On {rising_name} or {pro_name}, you pick the posts that get the attention.",
                ],
            },
            {
                "h2": "Why likes aren't sold on their own",
                "p": [
                    "A post with hundreds of likes, a handful of followers and no comments reads as bought to anyone who looks. Ours come from people who follow and sometimes comment too, so the numbers sit together naturally.",
                ],
            },
        ],
        "faqs": [
            ("Do you charge in pounds?", "No. Prices are in US dollars, paid at a Stripe checkout by card, Apple Pay or Google Pay, and your bank shows the sterling amount."),
            ("Can I target just London?", "Yes. Name London, or a part of it such as Hackney if your customers really are that local; the wider the area, the more people the campaign can reach."),
            ("Will the likes come from British accounts?", "They'll come from people in whichever part of the UK you name, each liking from their own account."),
            ("Can I get likes on a launch post?", "With {rising_name} or {pro_name}, you can tell us which posts should get the attention, a launch included. How many likes it gets is up to the people who see it, so we don't put a number on any one post."),
            ("How quickly do likes appear?", "From the first days of the campaign, as people find your profile, and then steadily through the month. Never hundreds in a minute, which is how fake likes give themselves away."),
        ],
    },
    {
        "service": "likes",
        "country": "in",
        "plan": "starter",
        "slug": "instagram/likes/india",
        "label": "Instagram likes from India",
        "title": "Buy Instagram Likes Cheap in India Without Bots | Growsterr",
        "description": "Buy Instagram likes cheap in India, from real people: {starter_name} typically brings {starter_likes} likes a month on posts and Reels for {starter_price}, billed in USD.",
        "h1": ("Buy Instagram likes cheap in India, ", "from people who watched the Reel."),
        "intro": "Wanting to buy Instagram likes cheap in India is reasonable: likes help, and nobody wants to overpay. But a like is only worth something if a person gave it. {starter_name}, at {starter_price} a month, usually brings {starter_likes} likes on your posts and Reels, from real people in India who discovered your profile and enjoyed what they saw, plus the new followers among them.",
        "hero": {"image": "instagram-creator-studio", "alt": "An Indian creator editing a Reel that will collect likes from viewers in India"},
        "sections": [
            {
                "h2": "Reel likes in India start with a watch",
                "p": [
                    "Reels are where many Indian creators put their energy, and a Reel with likes but no views gives the game away. Our likes come from people who watched first, so the views are there too. With {rising_name} or {pro_name} you can choose which Reels and posts are shown to more people.",
                ],
            },
            {
                "h2": "The price, in plain numbers",
                "ul": [
                    "{starter_name}: {starter_price} a month for typically {starter_likes} likes, {starter_audience} followers and {starter_comments} comments.",
                    "Per like, that's a few US cents or less, and every one has a person behind it.",
                    "You're charged in US dollars, and your bank statement shows the INR amount.",
                    "No UPI or wallets: card, Apple Pay or Google Pay at a Stripe checkout.",
                ],
            },
            {
                "h2": "Buying Instagram likes online in India, safely",
                "p": [
                    "Many likes services ask for a login or an app. You should never need either. We work from your username alone, and nobody on our side ever signs in to your account.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy Instagram likes in rupees?", "You pay in US dollars, and your bank converts the charge into rupees. There's no separate price in Indian currency; {starter_price} a month for {starter_name} is what Stripe charges."),
            ("Can I buy post likes for a single post in India?", "Single-post likes aren't something we sell. Likes come inside a monthly package from people who find your profile. {rising_name} and {pro_name} let you pick the posts that get attention; how many likes each receives is the viewers' choice."),
            ("Are these Indian likes?", "They come from people in the place you name: India, a state, or a city such as Bengaluru or Ahmedabad. Each like is from a person's own account."),
            ("Why not a much cheaper likes pack?", "Because at that price there's no person on the other end. Those likes sit on one post, never reach your next one, and drop when fake accounts are removed. Real likes keep coming as people follow you."),
            ("Do views come with the likes?", "Yes. Nobody likes a Reel they didn't play, so a view sits behind every Reel like. We just don't sell or forecast views: they're people's choices."),
        ],
    },
    {
        "service": "likes",
        "country": "ke",
        "slug": "instagram/likes/kenya",
        "label": "Instagram likes from Kenya",
        "title": "Buy Instagram Likes in Kenya From Nairobi and Beyond | Growsterr",
        "description": "Buy Instagram likes in Kenya from real people who see your posts in Nairobi, Mombasa or Nakuru. Likes come with followers and comments, never as a pack.",
        "h1": ("Buy Instagram likes in Kenya ", "that come with a follower attached."),
        "intro": "Likes are the quickest signal on Instagram, which is why people look to buy Instagram likes in Kenya before a launch or a gig. We do it the long way round, because it's the way that holds: real people in Nairobi, Mombasa, Nakuru or the town you name discover your profile, many follow, and they like the posts they enjoy. A typical {pick_name} month brings {pick_likes} likes.",
        "hero": {"image": "instagram-real-people", "alt": "Friends in Nairobi liking and sharing a Kenyan creator's Instagram post"},
        "sections": [
            {
                "h2": "Likes that travel beyond Instagram",
                "p": [
                    "On Kenyan Instagram, a good skit or a new song doesn't stay put: it gets forwarded to WhatsApp groups and talked about. Likes from people who'll do that are worth far more than likes from accounts that never leave the app.",
                ],
            },
            {
                "h2": "Likes for skits, music and small brands",
                "ul": [
                    "Comedy and skit creators: people who laugh tend to like, and the ones who follow see the next skit.",
                    "Musicians: likes on a snippet from people in your city, who might come to the show.",
                    "Small brands in Nairobi: likes from people who can order and receive delivery the same week.",
                    "Your chosen posts lead the campaign on {rising_name} or {pro_name}.",
                ],
            },
            {
                "h2": "What it costs",
                "p": [
                    "Packages are priced in US dollars, starting at {starter_price} a month for {starter_name}, which typically brings {starter_likes} likes. Checkout is a Stripe page that accepts cards, plus Apple Pay or Google Pay when your device offers them.",
                ],
            },
        ],
        "faqs": [
            ("Can I point likes at my new single?", "Yes, on {rising_name} or {pro_name}: mark the single as a post to feature and the campaign leads with it. The number of likes it collects is up to the people who hear it."),
            ("Can I pay with a Kenyan bank card?", "Yes, if it's a Visa or Mastercard that allows online payments in US dollars. The amount is converted into shillings by your bank."),
            ("Will the likes be from Kenyans?", "From people around the place you set, using their own accounts: Kenya, a county, or a town such as Eldoret or Kisumu."),
            ("Do likes come before followers?", "Usually together. People who find your profile often like a post first, then follow, or follow and like later. Both come from the same accounts."),
            ("Will likes drop after a while?", "Not in the way bought likes vanish. Each is a person's own tap, and it stays unless that person changes their mind."),
        ],
    },
    {
        "service": "likes",
        "country": "ng",
        "slug": "instagram/likes/nigeria",
        "label": "Instagram likes from Nigeria",
        "title": "Buy Instagram Likes in Nigeria, Lagos to Kano | Growsterr",
        "description": "Buy Instagram likes in Nigeria from real people who scroll in Lagos, Abuja and beyond. Likes on your posts and Reels come with followers, inside every package.",
        "h1": ("Buy Instagram likes in Nigeria ", "from people who'll actually DM you."),
        "intro": "For a Nigerian vendor, a like is often the step before a DM asking for the price. That's why, when you buy Instagram likes in Nigeria, they should come from people who could become customers. Ours do: real people in Lagos, Abuja, Kano or another city you pick come across your profile, follow, and like the posts they enjoy, typically {pick_likes} a month on {pick_name}.",
        "hero": {"image": "instagram-followers-1000", "alt": "Likes building on a Lagos vendor's Instagram product posts through the month"},
        "sections": [
            {
                "h2": "From a like to a sale",
                "p": [
                    "Likes from people near you do quiet work: they tell the next visitor that others have looked and liked what they saw. Some of those likers send a DM, some tag a friend, some come back at month end. Likes from accounts that can never buy do none of that.",
                ],
            },
            {
                "h2": "Skits, Afrobeats and owambe season",
                "ul": [
                    "Skit makers: real likes come from people who laughed, and they're the ones who share.",
                    "Afrobeats artists: likes from listeners in your city on the teaser before release day.",
                    "Fashion and aso ebi vendors: likes on new styles from people who'll be at the next owambe.",
                    "Featured posts are yours to choose on {rising_name} and {pro_name}.",
                ],
            },
            {
                "h2": "Why we don't sell likes by the thousand",
                "p": [
                    "A thousand likes on one post, from accounts that can't place an order, is a number with nothing behind it. We'd rather bring people who follow and come back, and let the likes add up across everything you post.",
                ],
            },
        ],
        "faqs": [
            ("What does it cost in naira?", "We don't set naira prices. Packages are billed in US dollars, from {starter_price} a month, and what that comes to in naira is up to your bank's exchange rate."),
            ("Do the likes come from Nigerian accounts?", "Yes, if Nigeria is where you aim: the country, a state such as Rivers or Oyo, or a single city."),
            ("Can I get likes on a giveaway post?", "With {rising_name} or {pro_name}, you can name the posts that should get attention, a giveaway included. People decide whether to like it, so we never quote a number for one post."),
            ("Will my likes disappear?", "No mass drops, because there's no fake account behind them to delete. An odd unlike can happen, the way it does with any audience."),
            ("Can I target Port Harcourt?", "Yes. Name Port Harcourt, Rivers State, or all of Nigeria when you order, and the campaign starts there."),
        ],
    },
    {
        "service": "likes",
        "country": "ph",
        "slug": "instagram/likes/philippines",
        "label": "Instagram likes from the Philippines",
        "title": "Buy Instagram Likes in the Philippines | Growsterr",
        "description": "Buy Instagram likes in the Philippines from real people in Manila, Cebu or Davao. Likes on posts and Reels come with followers and comments, monthly.",
        "h1": ("Buy Instagram likes in the Philippines ", "from people who share with their barkada."),
        "intro": "In the Philippines, a liked post rarely stays put: it gets sent to group chats, tagged under a friend's name, saved for later. That's what you want when you buy Instagram likes in the Philippines, and it only happens with real people. We bring them from Metro Manila, Cebu, Davao or the city you name; they follow, and they like what they enjoy. {pick_name} usually means {pick_likes} likes a month.",
        "hero": {"image": "instagram-real-people", "alt": "Friends in Manila tagging each other under an Instagram post they liked"},
        "sections": [
            {
                "h2": "Likes from your own province",
                "p": [
                    "A food business in Iloilo gains more from likes in Iloilo than from likes in Manila, let alone abroad. Name the city or province where your customers are, and that's where the campaign aims. If you sell nationwide, name the whole country and let your posts find their audience.",
                ],
            },
            {
                "h2": "Ideas that suit a Filipino feed",
                "ul": [
                    "Food, especially something new to try nearby.",
                    "Travel spots, from Siargao to Batanes, with honest tips.",
                    "Family moments, humour and anything that feels like home.",
                    "On {rising_name} or {pro_name}, the posts you pick get extra attention.",
                ],
            },
            {
                "h2": "Likes that look like real interest",
                "p": [
                    "A post with thousands of likes and no comments looks odd on Filipino Instagram, where people comment and tag all the time. Because our likes come from people, comments and follows arrive with them, and the numbers match.",
                ],
            },
        ],
        "faqs": [
            ("Can I pay with a Philippine debit card?", "Yes, if it's enabled for online payments abroad. The charge is in US dollars; your bank shows it in pesos."),
            ("Do Reels get likes as well?", "They do. A like on a Reel comes from someone who watched it, so views arrive with the likes."),
            ("Can I target Davao only?", "Yes. Name Davao City, the region, or all of Mindanao, and the campaign aims there first."),
            ("Are the likes from accounts in the Philippines?", "Yes, from real people in the place you name, each on their own account. Name the Philippines, a region or a city, and that's the campaign's starting point."),
            ("What does each package bring in likes?", "{starter_name} typically brings {starter_likes} a month, {rising_name} {rising_likes} and {pro_name} {pro_likes}, with followers and comments from the same people."),
        ],
    },
    {
        "service": "likes",
        "country": "pk",
        "plan": "starter",
        "slug": "instagram/likes/pakistan",
        "label": "Instagram likes from Pakistan",
        "title": "Buy Instagram Likes in Pakistan, From Real Accounts | Growsterr",
        "description": "Buy Instagram likes in Pakistan from people scrolling in Karachi, Lahore and Islamabad. Likes arrive with followers and comments from the same accounts.",
        "h1": ("Buy Instagram likes in Pakistan ", "for the posts people actually stop on."),
        "intro": "If you want to buy Instagram likes in Pakistan, think about who taps the heart. Likes from people in Karachi, Lahore or Islamabad tell your customers the page is alive and local. Those are the people our campaign finds for you: they come across your profile in the place you name and like the posts and Reels they enjoy, usually {starter_likes} a month on {starter_name}, along with new followers.",
        "hero": {"image": "instagram-hub", "alt": "Likes from Karachi and Lahore gathering on a Pakistani food page's Instagram grid"},
        "sections": [
            {
                "h2": "Likes during lawn season, Eid and the cricket",
                "p": [
                    "Pakistani feeds have peaks: new lawn collections in spring, Eid outfits and recipes, wedding season, and every big cricket match. Your campaign runs every day, and on {rising_name} or {pro_name} you can point it at the posts that matter when one of those moments comes.",
                ],
            },
            {
                "h2": "Likes from people, not from a panel",
                "ul": [
                    "Each like comes from a person who saw your post in their own feed or on your profile.",
                    "Those people can follow, comment and come back; a panel's likes can't.",
                    "Likes spread across what people enjoy, so your strongest posts lead.",
                    "Nothing arrives in a burst, and nothing needs your password.",
                ],
            },
            {
                "h2": "What it costs from Pakistan",
                "p": [
                    "{starter_name} costs {starter_price} a month in US dollars and usually brings {starter_likes} likes, {starter_audience} new followers and {starter_comments} comments. Spread over everything it brings, that's a small amount per real person.",
                ],
            },
        ],
        "faqs": [
            ("Will the likes come from Pakistani accounts?", "They come from the area you set: Pakistan, a province like Punjab or Khyber Pakhtunkhwa, or a single city."),
            ("Can I target Islamabad and Rawalpindi together?", "Yes. Write both when you order, and the campaign aims at the twin cities first. For a narrow niche, some likes may come from nearby."),
            ("Can I choose which post gets likes?", "Yes, on {rising_name} or {pro_name}, which let you pick the posts the campaign features. People still decide what to like, so there's never a set number per post."),
            ("How do I pay from Pakistan?", "You pay by card at a Stripe checkout, or use Apple Pay or Google Pay if your phone is set up for them. The bank converts the dollar charge into rupees."),
            ("Will my likes stay?", "Yes, unless someone changes their mind, because each like comes from a person's own account rather than one that gets removed later."),
        ],
    },
    {
        "service": "likes",
        "country": "tr",
        "slug": "instagram/likes/turkey",
        "label": "Instagram likes from Turkey",
        "title": "Buy Instagram Likes in Turkey, Liked by Locals | Growsterr",
        "description": "Buy Instagram likes in Turkey from real people in Istanbul, İzmir or Antalya who see your posts and enjoy them. Part of every package, never a bulk pack.",
        "h1": ("Buy Instagram likes in Turkey ", "from people who know the neighbourhood."),
        "intro": "If you'd like to buy Instagram likes in Turkey, the ones that help most come from people near you: a Moda café gets more from likes in Kadıköy than from anywhere abroad. We bring real people from Istanbul, İzmir, Ankara, Antalya or the city you name to your profile, and they like the posts they enjoy. Around {pick_likes} likes is a typical {pick_name} month, alongside new followers.",
        "hero": {"image": "instagram-followers", "alt": "An Istanbul café's Instagram posts collecting likes from people in Kadıköy"},
        "sections": [
            {
                "h2": "Likes for tourism, or likes from locals?",
                "p": [
                    "A boutique hotel in Kaş or Cappadocia has two audiences: guests abroad who book, and people in Turkey who visit at weekends and holidays. Name the one you want this month. Likes from the right side help with bookings; likes from the wrong side only add a number.",
                ],
            },
            {
                "h2": "Timing your posts for Turkish feeds",
                "ul": [
                    "Evenings and weekends tend to be when people scroll at leisure.",
                    "Ramazan evenings after iftar and the long Bayram holidays change daily habits.",
                    "Summer moves much of the audience to the coast; post accordingly.",
                    "On {rising_name} or {pro_name}, choose the posts the campaign shows first.",
                ],
            },
            {
                "h2": "Likes, never on their own",
                "p": [
                    "We don't sell likes by the hundred. They come from the people your package brings, so a post's likes sit next to new follows and comments, and the whole picture adds up.",
                ],
            },
        ],
        "faqs": [
            ("Can I target İzmir only?", "Yes. Name İzmir, the Aegean coast, or the whole of Turkey. A wider area simply means more people for the campaign to reach."),
            ("Do likes come from Turkish accounts?", "From people who live where you aim the campaign, every one with an account of their own."),
            ("What does it cost in lira?", "Our prices are dollar prices: {starter_name} costs {starter_price} a month. Your bank converts it into lira, so the lira figure can change from month to month."),
            ("Can I get likes on a Reel I made for a launch?", "Pick it as a featured post on {rising_name} or {pro_name}, and the campaign puts it forward. People decide whether to like it, so no single post has a set number."),
            ("Do I need to share my password?", "No. Your username is all we work from; your login never leaves you."),
        ],
    },
    {
        "service": "likes",
        "country": "us",
        "slug": "instagram/likes/united-states",
        "label": "Instagram likes from the US",
        "title": "Buy American Instagram Likes From People in the US | Growsterr",
        "description": "Buy American Instagram likes from real people in the US who see your posts and enjoy them. Likes come with followers and comments, billed in US dollars.",
        "h1": ("Buy American Instagram likes ", "from people scrolling in the US."),
        "intro": "When people buy American Instagram likes, they usually want proof that their posts land with a US audience. A like only proves that if someone in the US actually saw the post. So we start with people: real people in New York, Chicago, Dallas or wherever you name discover your profile and like the posts they enjoy. Expect {pick_likes} likes in a typical {pick_name} month, alongside new followers.",
        "hero": {"image": "instagram-creator-studio", "alt": "A US creator reviewing which Instagram posts drew the most likes from American viewers"},
        "sections": [
            {
                "h2": "Likes from the US, or likes from US-looking accounts?",
                "p": [
                    "A like is American because the person who gave it is in the US, not because a profile says so. Bulk sellers can dress an account in an American name and a stock photo; they can't give it a life in Ohio. We target people by where they are, so US likes from us come from people in the US.",
                ],
            },
            {
                "h2": "Brand deals look at more than likes",
                "p": [
                    "Brands checking whether you reach US consumers often look at your audience, your comments and how your likes compare with your views and followers. Likes from people who also follow and comment pass that look; likes from nowhere don't.",
                ],
            },
            {
                "h2": "Choosing your US audience",
                "ul": [
                    "The whole US, for creators and online brands with national reach.",
                    "One state, such as Florida or New York, for regional brands.",
                    "One metro, such as Phoenix or Seattle, for local businesses.",
                    "{rising_name} and {pro_name} let you put chosen posts first.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy US likes for a single post?", "Not as a standalone order. Likes come with the monthly package, from people who land on your profile; on {rising_name} or {pro_name} you can pick which posts get the attention, with no set number on any of them."),
            ("Are the likes from real American accounts?", "Yes: every like is a person tapping from their own account, in the US or the part of it you name."),
            ("How many likes will I get each month?", "Around {pick_likes} on {pick_name}, {starter_likes} on {starter_name} and {pro_likes} on {pro_name}. Each is a range, because people choose what to like."),
            ("Will likes arrive right after I post?", "No, we don't line likes up with the moment you post. People reach your profile across the month and like what they enjoy, so new and older posts both collect likes."),
            ("Do I have to log in anywhere?", "Only to your Growsterr account, to manage the subscription. Your Instagram login stays with you, and your username is all we need."),
        ],
    },
]
