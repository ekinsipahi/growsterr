"""English payment answers: one page per way people ask to pay. Growsterr takes cards through
Stripe's checkout (Apple Pay and Google Pay where the device supports them), as a monthly
subscription. Every other method gets a plain no, what works instead, and why. Keys and
placeholders: docs/CONTENT.md; the brief: docs/keywords/WRITING.md ("Payment pages")."""

UPDATED = "2026-11-08"

ARTICLES = [
    # --- Methods we take --------------------------------------------------------------------
    {
        "article": "pay-with-apple-pay",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/apple-pay",
        "label": "Paying with Apple Pay",
        "title": "Buy Instagram Likes With Apple Pay | Growsterr",
        "description": "Yes, you can buy Instagram likes with Apple Pay. Stripe's checkout offers it on supported Apple devices for every package, TikTok and YouTube included.",
        "h1": ("Buy Instagram likes with Apple Pay? ", "Yes, it's built into our checkout."),
        "intro": "Yes. When you buy Instagram likes from us, Apple Pay is one of the ways to pay. Likes come inside a monthly package, together with new followers and comments from the same real people, and Stripe's secure checkout shows the Apple Pay button on iPhones, iPads and Macs that support it. A glance or a touch confirms it, and the package renews on that card each month until you cancel.",
        "hero": {"image": "instagram-hub", "alt": "An iPhone showing the Apple Pay sheet beside an Instagram profile that is about to grow"},
        "sections": [
            {
                "h2": "Paying with Apple Pay, step by step",
                "ul": [
                    "Pick {starter_name}, {rising_name} or {pro_name}, then give us your username and the place your audience should come from.",
                    "At Stripe's checkout, tap the Apple Pay button instead of typing a card number.",
                    "Confirm with Face ID, Touch ID or your passcode; your bank may ask for one more confirmation.",
                    "Your campaign starts, and the same card in your Wallet is charged once a month from then on.",
                ],
            },
            {
                "h2": "What the payment buys on each platform",
                "p": [
                    "On Instagram, likes never come by themselves. {starter_name} typically brings {starter_likes} likes a month, along with {starter_audience} new followers and {starter_comments} comments, all from people who discovered your profile.",
                    "TikTok works the same way: followers, likes and views arrive together, from the same viewers. On YouTube the package brings subscribers, and they watch your videos on their own, so views come with them rather than as a separate order.",
                ],
            },
            {
                "h2": "No Apple Pay button?",
                "p": [
                    "The button only shows when the device and browser support Apple Pay and a card is set up in Wallet. Safari on an iPhone, iPad or Mac is the usual way to see it. If it's missing, type the card in instead: same checkout, same monthly subscription.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy TikTok followers with Apple Pay?", "Yes. TikTok packages use the same Stripe checkout, so Apple Pay appears there too on a supported device. Your new followers also like and watch your videos, so TikTok likes and views come from the same people."),
            ("Can I pay for YouTube views with Apple Pay?", "Yes, Apple Pay works for YouTube packages. What you pay for is a month of new subscribers who then watch your videos, and you can name one video for new viewers to go to. We don't sell views by themselves or promise watch time."),
            ("Does Apple Pay renew every month?", "Yes. Stripe charges the card behind your Apple Pay on the same date each month until you cancel. Cancelling stops the next renewal, and the month you've paid for still runs to its end."),
            ("Do you see my card number?", "No. Apple Pay doesn't share your actual card number with us, and the payment itself is handled by Stripe."),
            ("Can I use Apple Pay on an Android phone or a Windows PC?", "Apple Pay belongs to Apple devices. On Android, Google Pay may appear at checkout instead, and on any device you can type in a credit or debit card."),
        ],
    },
    {
        "article": "pay-with-google-pay",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/google-pay",
        "label": "Paying with Google Pay",
        "title": "Buy YouTube Views With Google Pay | Growsterr",
        "description": "Can you buy YouTube views with Google Pay? Yes: Stripe's checkout offers Google Pay for every monthly package, TikTok followers and views included.",
        "h1": ("Buy YouTube views with Google Pay? ", "Yes, with a card saved in Google."),
        "intro": "Yes, you can buy YouTube views with Google Pay at our checkout, with one thing to know first. What you buy is a monthly package that brings real subscribers to your channel, and they watch your videos on their own. Tap the Google Pay button at Stripe's secure checkout, and the card saved in your Google account renews the package each month.",
        "hero": {"image": "youtube-hub", "alt": "A YouTube channel on an Android phone, with Google Pay open to confirm a monthly payment"},
        "sections": [
            {
                "h2": "Google Pay for YouTube: what you're paying for",
                "p": [
                    "Our YouTube packages bring subscribers: people who discover your channel through our campaigns and choose to subscribe. Views follow from them. If one video matters most, name it at checkout or afterwards in your account, and new viewers are sent there: they subscribe first, then watch.",
                    "We don't sell views on their own, and we don't promise watch time, likes or comments on any video. Every view is someone deciding to press play.",
                ],
            },
            {
                "h2": "When Google Pay shows up",
                "ul": [
                    "On Android phones and in Chrome, once a card is saved to your Google account.",
                    "You confirm the way your device asks, often with a fingerprint or your screen lock.",
                    "If the button doesn't appear, typing the same card into the checkout works just as well.",
                ],
            },
            {
                "h2": "Google Pay in India and UPI",
                "p": [
                    "In India, many people use the Google Pay app for UPI transfers. Those can't be used here: our checkout takes Google Pay only with a debit or credit card saved in it. If your Google Pay holds just a UPI-linked bank account, pay with a card instead.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy TikTok followers with Google Pay?", "Yes. TikTok packages go through the same checkout, so Google Pay is there whenever your device supports it. The people who follow you watch and like your videos too."),
            ("Does Google Pay work for TikTok views?", "Views are part of every TikTok package rather than a purchase of their own: the people who follow you watch your videos because they want to. You pay for the package with Google Pay, a card or Apple Pay."),
            ("Is Google Pay charged every month?", "Yes. The package is a monthly subscription, so Stripe charges the card in your Google Pay on each renewal date. Cancel from your account whenever you like; the paid month still runs to its end."),
            ("Can I pay through UPI in the Google Pay app?", "No. We don't take UPI. The Google Pay button at our checkout works with a debit or credit card saved in your Google account."),
            ("Which YouTube package should I start with?", "{starter_name}, at {starter_price} a month, is the smallest; {rising_name}, at {rising_price}, is the most popular. Both bring subscribers who then watch, and you can move up whenever your videos are ready for more people."),
        ],
    },
    {
        "article": "pay-with-credit-card",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/credit-card",
        "label": "Paying by credit card",
        "title": "Buy Instagram Followers With a Credit Card | Growsterr",
        "description": "Buy Instagram followers with a credit card through Stripe's secure checkout: one monthly charge in US dollars until you cancel. TikTok works the same way.",
        "h1": ("Buy Instagram followers with a credit card, ", "through Stripe's secure checkout."),
        "intro": "A credit card is the simplest way to buy Instagram followers from us. You choose a monthly package, enter your card at Stripe's secure checkout, and your campaign starts bringing real people to your profile. The card is charged once a month, in US dollars, until you cancel. TikTok packages work exactly the same way.",
        "hero": {"image": "instagram-followers", "alt": "A credit card beside a laptop showing an Instagram profile with a rising follower count"},
        "sections": [
            {
                "h2": "What happens when you pay by card",
                "ul": [
                    "You enter the card on Stripe's payment page; the full number goes to Stripe, never to us.",
                    "Your bank may ask you to approve the payment in its app or with a code, an extra check we request on every card that supports it.",
                    "The first month is charged when you subscribe, then the same amount on the same date each month.",
                    "Invoices, the card on file and cancelling all live in the billing section of your account.",
                ],
            },
            {
                "h2": "Why a card fits a monthly package",
                "p": [
                    "A package is a subscription: the campaign runs month after month, and so does the payment. A card lets Stripe renew it automatically with your permission, and lets you stop it yourself in a couple of clicks. You don't send anything each month, and you're never billed for months in advance.",
                ],
            },
            {
                "h2": "Paying from outside the US",
                "p": [
                    "Prices are in US dollars. If your card is in another currency, your bank converts the amount and may add a foreign transaction fee, so it's worth a look at your card's terms before you subscribe.",
                ],
            },
        ],
        "faqs": [
            ("Which credit cards do you accept?", "The major card networks Stripe's checkout accepts, such as Visa and Mastercard. A card that already works for online shopping abroad should work here."),
            ("Can I buy TikTok followers with a credit card?", "Yes. TikTok packages use the same checkout and the same monthly billing. The followers you gain also like, watch and comment on your videos."),
            ("Why did my bank ask me to confirm the payment?", "We ask Stripe to run your bank's extra security step, often a code or a tap in your banking app, whenever the card supports it. It protects you if someone else ever tries to use your card."),
            ("Can I switch to a different card?", "Yes. Open the billing section of your account, which takes you to Stripe's customer portal, and replace the card. The next renewal goes on the new one."),
            ("What happens if I cancel?", "No further charges. The campaign keeps running until the end of the month you've paid for, and the followers you've gained are still yours."),
        ],
    },
    {
        "article": "pay-with-debit-card",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/debit-card",
        "label": "Paying by debit card",
        "title": "Buy Instagram Followers With a Debit Card | Growsterr",
        "description": "No credit card? You can buy Instagram followers with a debit card at Stripe's checkout: one monthly payment from your bank account, the same for TikTok.",
        "h1": ("Buy Instagram followers with a debit card: ", "no credit card needed."),
        "intro": "You don't need a credit card to buy Instagram followers from us. A debit card works at Stripe's checkout just like one, and the monthly payment comes straight out of your bank account. The package renews on the same date each month, so the one thing to watch is that the money is there on renewal day. TikTok packages are paid the same way.",
        "hero": {"image": "instagram-creator-studio", "alt": "A creator at a desk paying for a monthly growth package with a debit card"},
        "sections": [
            {
                "h2": "Debit or credit: the same checkout",
                "p": [
                    "Stripe treats your debit card like any other card. Type it in, or use Apple Pay or Google Pay if the debit card is saved there, and confirm with your bank if it asks. Your campaign then starts as it would for anyone, with real people seeing your profile from the first days.",
                ],
            },
            {
                "h2": "Three things to check on a debit card",
                "ul": [
                    "Online payments are switched on; some banks turn them off by default.",
                    "International payments are allowed too, because the charge is in US dollars and may count as one.",
                    "There's enough in the account on each renewal date, or the bank can decline the renewal.",
                ],
            },
            {
                "h2": "Prepaid and virtual debit cards",
                "p": [
                    "Many prepaid and virtual cards from banks and money apps work as well, as long as they allow repeat payments online. A card topped up for a single purchase can pay the first month and then fail at renewal, so keep it funded if you use one.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy TikTok followers with a debit card?", "Yes, in exactly the same way: TikTok packages go through the same Stripe checkout. New followers arrive every day, and the same people like and watch your videos."),
            ("Is it safe to use my debit card?", "You enter it on Stripe's payment page and it stays with Stripe. We never see the full number, and your bank can ask you to confirm the payment before it goes through."),
            ("What if my debit card is declined?", "Usually the bank is blocking online or international payments, or the balance is short. Check both in your banking app and try again, or use another card, Apple Pay or Google Pay."),
            ("Will I be charged before each month starts?", "You're charged on the day you subscribe, then on that same date each month. Nothing is taken beyond the month that's starting."),
            ("How do I stop the monthly payments?", "Cancel in your account. The renewal stops, the current month runs to its end, and your debit card isn't charged again."),
        ],
    },
    # --- Methods we don't take --------------------------------------------------------------
    {
        "article": "pay-with-paypal",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/paypal",
        "label": "Paying with PayPal",
        "title": "Buy Instagram Followers With PayPal? How to Pay | Growsterr",
        "description": "We don't take PayPal. For Instagram followers, TikTok followers or YouTube subscribers, pay by card, Apple Pay or Google Pay through Stripe, billed monthly.",
        "h1": ("Buy Instagram followers with PayPal? ", "We take cards instead."),
        "intro": "If you came to buy Instagram followers with PayPal, here's the straight answer: we don't take PayPal. Every package is paid by card through Stripe's secure checkout, or with Apple Pay or Google Pay where your device has them, as a monthly subscription you can cancel whenever you like. If a card funds your PayPal account, that same card works here directly.",
        "hero": {"image": "instagram-followers-1000", "alt": "A checkout offering card, Apple Pay and Google Pay for an Instagram growth package"},
        "sections": [
            {
                "h2": "Why there's no PayPal button",
                "p": [
                    "Every payment runs through one checkout, Stripe, and it takes cards and the phone wallets built on them. A package renews each month, and a single payment route means a single place to see invoices, swap cards and cancel, for us and for you.",
                    "It also keeps things simple if something goes wrong: your bank's card protections cover every payment, and your full card number stays with Stripe.",
                ],
            },
            {
                "h2": "Paying for TikTok and YouTube without PayPal",
                "ul": [
                    "TikTok followers, likes and views come together in one package, paid by card, Apple Pay or Google Pay.",
                    "YouTube packages bring subscribers, and the views come from those same people; the ways to pay are identical.",
                    "Instagram likes come inside every package as well, so there's no separate likes payment to make.",
                ],
            },
            {
                "h2": "If PayPal was about privacy",
                "p": [
                    "Some people prefer PayPal so that a shop never holds their card. Here, nobody at Growsterr does either: the card is entered on Stripe's page and stays with Stripe. What we keep is what a campaign needs: your email, your username and where your audience should come from.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy TikTok followers with PayPal?", "No. TikTok packages are paid like everything else: card, Apple Pay or Google Pay through Stripe, renewing monthly until you cancel."),
            ("Can I buy YouTube subscribers using PayPal?", "No, but a card works for YouTube packages, and so do Apple Pay and Google Pay. The package brings real subscribers, and they watch your videos on their own."),
            ("Can I pay for Instagram likes with PayPal?", "No. Likes also aren't sold on their own: they come inside a monthly package, from the people who follow you, typically {starter_likes} a month with {starter_name}."),
            ("Will you accept PayPal in future?", "We can't promise that. For now, card, Apple Pay and Google Pay are the only ways to pay, and they cover every package on every platform."),
            ("Can I use the card linked to my PayPal?", "Yes. Your PayPal account can't be used, but the debit or credit card behind it can, entered directly at Stripe's checkout."),
        ],
    },
    {
        "article": "pay-with-crypto",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/crypto",
        "label": "Paying with crypto",
        "title": "Buy Instagram Followers With Crypto? Here's Why Not | Growsterr",
        "description": "We don't take crypto for Instagram, TikTok or YouTube packages. Pay by card, Apple Pay or Google Pay through Stripe, on a monthly plan you can cancel any time.",
        "h1": ("Buy Instagram followers with crypto? ", "No, and here's why."),
        "intro": "We don't accept crypto, so you can't buy Instagram followers from us with Bitcoin, USDT or any other coin. Every package is a monthly subscription paid by card through Stripe, or with Apple Pay or Google Pay, and that holds for TikTok and YouTube too. Here's why we chose it, and what it means if you were hoping to stay private.",
        "hero": {"image": "tiktok-hub", "alt": "A creator's phone showing a monthly card payment next to a growing social profile"},
        "sections": [
            {
                "h2": "A subscription needs a payment that can renew",
                "p": [
                    "A crypto transfer is something you push yourself, once, and it can't be reversed. A package is a subscription that renews each month until you stop it. Card payments through Stripe fit that: the renewal happens without you sending anything, you can cancel on your own, and if a charge ever looks wrong, your bank can step in.",
                ],
            },
            {
                "h2": "Privacy: what we actually need from you",
                "ul": [
                    "An email address, to set up your account and reach you.",
                    "Your Instagram, TikTok or YouTube username, never the password.",
                    "The place your audience should come from.",
                    "A card, Apple Pay or Google Pay, handled by Stripe so the card number never reaches us.",
                ],
            },
            {
                "h2": "Crypto-funded cards",
                "p": [
                    "Some crypto services issue debit cards that spend your balance in ordinary currency. If yours works for online payments in US dollars, it can be used at our checkout like any other card, and each monthly renewal is charged to it. Keep it topped up before every renewal date.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy YouTube subscribers with crypto?", "No. YouTube packages are paid by card, Apple Pay or Google Pay like the rest. They bring real subscribers who choose your channel, and views come from the same people."),
            ("Can I buy TikTok views with crypto?", "No. Views also aren't a separate purchase: they come with every TikTok package, from the people who discover and follow you. You pay for the package by card or phone wallet."),
            ("Do you take Bitcoin or USDT?", "Neither, nor any other coin or token. We don't take crypto in any form."),
            ("Can I buy Instagram likes with crypto?", "No. And likes come inside a package rather than on their own: typically {starter_likes} a month with {starter_name}, from the same people who follow you."),
            ("Is paying by card worse for my privacy?", "Your card goes into Stripe's payment page and stays with Stripe, so we never see the full number. We also never need your social media password, which is the detail that matters most to keep to yourself."),
        ],
    },
    {
        "article": "pay-with-klarna",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/klarna",
        "label": "Paying with Klarna",
        "title": "Buy Instagram Followers With Klarna? Pay Monthly | Growsterr",
        "description": "We don't take Klarna, but there's nothing to split: every package is already paid month by month by card, Apple Pay or Google Pay, and you can cancel any time.",
        "h1": ("Buy Instagram followers with Klarna? ", "Our packages are already monthly."),
        "intro": "We don't take Klarna, so it isn't a way to buy Instagram followers from us. The good news is that you won't miss it. Pay-later services split one big purchase into smaller payments, and our packages are never one big purchase: you pay one month at a time, by card, Apple Pay or Google Pay through Stripe, and you can stop whenever you like.",
        "hero": {"image": "instagram-followers", "alt": "An Instagram profile gaining followers month by month on a simple monthly plan"},
        "sections": [
            {
                "h2": "Splitting a payment versus paying monthly",
                "p": [
                    "With instalments, you commit to a total and pay it off over weeks or months. With a subscription, there's no total to pay off. Each month is paid when it starts, the campaign runs for that month, and if you cancel, nothing more is owed.",
                    "So the most you're ever committed to is one month: {starter_price} for {starter_name}, and the next payment only happens if you keep going.",
                ],
            },
            {
                "h2": "How to pay instead",
                "ul": [
                    "A credit or debit card, typed in at Stripe's secure checkout.",
                    "Apple Pay on a supported iPhone, iPad or Mac.",
                    "Google Pay on Android or in Chrome, with a card saved to your Google account.",
                ],
            },
            {
                "h2": "The same rhythm for TikTok",
                "p": [
                    "TikTok packages are paid the same way, on the same monthly rhythm. If you grow both accounts, each package is its own subscription, so you can keep one and stop the other.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy TikTok followers with Klarna?", "No. TikTok packages are paid by card, Apple Pay or Google Pay, monthly, just like Instagram ones."),
            ("Can I pay for three months at once?", "No. Packages are billed one month at a time, and that's deliberate: you can see a month's results in your dashboard before deciding on the next."),
            ("Is there interest or a credit check?", "No. It's a plain monthly card payment through Stripe with nothing borrowed, so there's nothing to check and no interest from us. Your card's own terms still apply."),
            ("What if I want to stop after one month?", "Cancel in your account any time during that month. The campaign runs to the end of it, and no further payment is taken."),
            ("Which package costs least per month?", "{starter_name}, at {starter_price} a month, typically bringing {starter_audience} new followers. {rising_name} and {pro_name} bring more people for {rising_price} and {pro_price}."),
        ],
    },
    {
        "article": "pay-with-upi",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/upi",
        "label": "Paying with UPI",
        "title": "Buy Instagram Followers With UPI? What Works | Growsterr",
        "description": "We don't take UPI payments. From India you can buy Instagram followers with a debit or credit card, or Apple Pay or Google Pay with a card, through Stripe.",
        "h1": ("Buy Instagram followers with UPI? ", "Use a card at our checkout."),
        "intro": "We don't take UPI, so a UPI payment can't be used to buy Instagram followers from us. What works from India is a debit or credit card at Stripe's secure checkout, typed in or saved in Google Pay or Apple Pay. Your package is a monthly subscription in US dollars that renews on that card until you cancel, and your audience can come from the Indian city or state you choose.",
        "hero": {"image": "instagram-real-people", "alt": "An Instagram creator in India paying for a monthly growth package by card on a phone"},
        "sections": [
            {
                "h2": "Why UPI isn't an option here",
                "p": [
                    "Our checkout runs on Stripe and takes cards, plus the phone wallets that hold them. Each package renews monthly on the card you subscribed with, and you can cancel or change that card from your account. Keeping one route for every payment is what lets this work the same for everyone.",
                ],
            },
            {
                "h2": "Getting an Indian card ready",
                "ul": [
                    "Turn on international online transactions for the card; many banks let you do it in their app.",
                    "Expect an OTP or an in-app approval from your bank before the first payment goes through.",
                    "The price is in US dollars: your bank converts it to rupees and may add a currency conversion fee.",
                    "Some banks also ask you to approve the monthly renewal; if one is declined, update the card from your account.",
                ],
            },
            {
                "h2": "Aiming at an Indian audience",
                "p": [
                    "Paying by card doesn't change who sees your profile. Name Mumbai, Delhi, Bengaluru, a state or all of India, and your campaign shows your profile to people there first, every day of the month.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy TikTok followers with UPI?", "No. Every package, TikTok included, is paid by card, Apple Pay or Google Pay through Stripe, never by UPI."),
            ("Does Google Pay at checkout mean UPI?", "No. In India the Google Pay app is often used for UPI, but our checkout accepts Google Pay only with a card saved in it."),
            ("Why was my Indian card declined?", "Most often, international online payments are switched off for the card, or the OTP step wasn't completed. Turn them on in your bank's app and try again, or use a different card."),
            ("Do I pay in rupees?", "No. Packages are priced in US dollars, starting at {from_price} a month. Your bank converts the amount, so the rupee figure on your statement depends on its exchange rate and fees."),
            ("Can I cancel the subscription myself?", "Yes, from your account at any time. The paid month runs to its end and the card isn't charged again."),
        ],
    },
    {
        "article": "pay-with-paytm",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/paytm",
        "label": "Paying with Paytm",
        "title": "Buy Instagram Followers With Paytm? Pay by Card | Growsterr",
        "description": "Paytm isn't accepted here. From India you can still buy Instagram followers, with likes included, by debit or credit card through Stripe, renewing monthly.",
        "h1": ("Buy Instagram followers with Paytm? ", "Not by wallet, but by card."),
        "intro": "Paytm wallet and Paytm UPI payments aren't accepted, so you can't buy Instagram followers or likes from us with Paytm. You can pay with a debit or credit card through Stripe's secure checkout, including a card from an Indian bank, or with Apple Pay or Google Pay using a saved card. It's a monthly subscription, and nothing renews once you cancel.",
        "hero": {"image": "instagram-hub", "alt": "Followers in India liking and commenting on a creator's latest Instagram posts"},
        "sections": [
            {
                "h2": "Wallets top up, subscriptions renew",
                "p": [
                    "A wallet is handy for paying a shop once. A growth package is different: it continues month after month until you stop it. Our checkout charges a card for that, the same card each month, so your campaign carries on without you sending a payment every time.",
                ],
            },
            {
                "h2": "Instagram likes come with the package",
                "p": [
                    "If you were hoping to pay for Instagram likes through Paytm, there's a second difference: we don't sell likes by themselves. Every package brings new followers, and the same people like and comment on the posts they enjoy, typically {starter_likes} likes and {starter_comments} comments a month with {starter_name}.",
                ],
            },
            {
                "h2": "Before you pay with an Indian card",
                "ul": [
                    "Check that the card allows online payments to merchants outside India.",
                    "Keep your phone close for the OTP or approval your bank sends.",
                    "Remember the charge is in US dollars, converted by your bank.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy TikTok followers with Paytm?", "No. TikTok packages use the same card checkout, so Paytm can't be used for them either."),
            ("Can I use a card I've saved in Paytm?", "Not through Paytm itself. If you have that card to hand, enter it directly at our checkout instead."),
            ("Is there a lower price for India?", "No. Prices are the same everywhere, in US dollars, starting with {starter_name} at {starter_price} a month."),
            ("Can I target followers in my own city?", "Yes. Tell us the city, state or country your audience should come from, such as Jaipur, Kerala or all of India, and your profile is shown to people there first."),
            ("Will you ask for my Instagram password?", "No, never. We need your username, a public profile and the place your followers should come from."),
        ],
    },
    {
        "article": "pay-with-gcash",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/gcash",
        "label": "Paying with GCash",
        "title": "Buy Instagram Followers With GCash? Use a Card | Growsterr",
        "description": "We don't take GCash. From the Philippines you can buy Instagram or TikTok followers and likes with a card, Apple Pay or Google Pay through Stripe, monthly.",
        "h1": ("Buy Instagram followers with GCash? ", "Here's what works from the Philippines."),
        "intro": "GCash isn't accepted at our checkout, so you can't buy Instagram followers or likes from us with GCash. From the Philippines, you can pay with a debit or credit card through Stripe, or with Apple Pay or Google Pay where your phone has them. The package bills monthly in US dollars, and your new followers can come from Metro Manila, Cebu, Davao or anywhere you name.",
        "hero": {"image": "tiktok-likes", "alt": "A Filipino creator checking new followers and likes on TikTok and Instagram"},
        "sections": [
            {
                "h2": "Why we don't take e-wallet transfers",
                "p": [
                    "Every Growsterr package is a subscription that renews itself each month on a card, through Stripe. An e-wallet transfer is sent by hand each time, so it doesn't fit that model, and we keep a single checkout for every country rather than one per wallet.",
                ],
            },
            {
                "h2": "If your money lives in an e-wallet",
                "p": [
                    "Some e-wallets and digital banks give you a Visa or Mastercard card, physical or virtual, linked to your balance. If yours does and it's enabled for online payments abroad, you can use it at our checkout like any other card. Keep enough on it for each monthly renewal.",
                ],
            },
            {
                "h2": "Followers and likes on Instagram and TikTok",
                "ul": [
                    "On Instagram, followers, likes and comments come from the same real people, every day of the month.",
                    "On TikTok, the people who follow you also watch and like your videos.",
                    "Neither platform has a likes-only order: likes arrive with the package.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy TikTok followers with GCash?", "No, TikTok packages are paid the same way as Instagram ones: card, Apple Pay or Google Pay through Stripe."),
            ("Can I pay for TikTok likes with GCash?", "No. TikTok likes come inside a package rather than as a purchase of their own, and the package is paid by card or phone wallet."),
            ("How much is it in pesos?", "We price in US dollars only, from {from_price} a month. Your bank or card provider converts it at its own rate."),
            ("Can I target followers in the Philippines only?", "Yes. Name the country, a region or a city such as Quezon City, and we show your profile to people there first."),
            ("Is it safe to pay by card?", "Your card details go to Stripe's secure checkout, not to us, and your bank may ask you to confirm the payment. You can cancel from your account at any time."),
        ],
    },
    {
        "article": "pay-with-m-pesa",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/m-pesa",
        "label": "Paying with M-Pesa",
        "title": "Buy Instagram Followers With M-Pesa? Use Your Card | Growsterr",
        "description": "M-Pesa isn't accepted. From Kenya you can buy Instagram or TikTok followers with a Visa or Mastercard, Apple Pay or Google Pay through Stripe, billed monthly.",
        "h1": ("Buy Instagram followers with M-Pesa? ", "Pay by card instead."),
        "intro": "We don't take M-Pesa, so you can't buy Instagram followers from us with M-Pesa. From Kenya or anywhere else, packages are paid by card through Stripe's secure checkout, or with Apple Pay or Google Pay on supported phones. You pay one month at a time, in US dollars, and you can cancel whenever you like. TikTok packages work the same.",
        "hero": {"image": "instagram-followers-1000", "alt": "A Kenyan creator's Instagram follower count climbing week by week"},
        "sections": [
            {
                "h2": "Why M-Pesa doesn't fit our subscription",
                "p": [
                    "A Growsterr package renews on the same card each month through Stripe, with no new payment for you to send. M-Pesa isn't part of that checkout, and we use one way of paying in every country, so subscriptions, invoices and cancelling work identically for everyone.",
                ],
            },
            {
                "h2": "Ways Kenyan creators can pay",
                "ul": [
                    "A Visa or Mastercard debit card from your bank, enabled for online payments.",
                    "A credit card, typed into the checkout.",
                    "Apple Pay or Google Pay, if a card is saved on your phone.",
                    "A virtual card linked to your mobile money, if your provider offers one that allows payments abroad.",
                ],
            },
            {
                "h2": "Followers from Nairobi, Mombasa or the whole country",
                "p": [
                    "Whatever you pay with, you choose where your audience comes from. Name Nairobi, Mombasa, Kisumu or all of Kenya, and real people there see your profile first, every day of your campaign.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy TikTok followers with M-Pesa?", "No. TikTok packages go through the same card checkout, so M-Pesa can't be used there either."),
            ("Do you have a till or paybill number?", "No. We don't take M-Pesa in any form, so there's no till, paybill or phone number to send money to. If someone asks you to send M-Pesa in our name, it isn't us."),
            ("What will I pay in shillings?", "Our prices are in US dollars, from {from_price} a month. Your card's bank converts the amount to shillings and may charge a fee for doing so."),
            ("Will the payment repeat automatically?", "Yes, once a month on the card you used, until you cancel in your account. After cancelling, the month you've paid for runs to its end."),
            ("Do I need to give you my Instagram login?", "No. Your username and a public profile are enough. Nobody from Growsterr ever signs in to your account."),
        ],
    },
    {
        "article": "pay-with-mobile-money",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/mobile-money",
        "label": "Paying with mobile money",
        "title": "Buy Instagram Followers With Mobile Money? | Growsterr",
        "description": "Mobile money isn't accepted at our checkout. You can buy Instagram or TikTok followers by card, Apple Pay or Google Pay through Stripe, one month at a time.",
        "h1": ("Buy Instagram followers with mobile money? ", "Here's how to pay instead."),
        "intro": "Mobile money isn't one of our payment options, so you can't buy Instagram followers from us with a mobile money wallet. Packages are paid by card through Stripe's secure checkout, or with Apple Pay or Google Pay where your phone supports them. The subscription renews monthly on that card until you cancel, and the same goes for TikTok.",
        "hero": {"image": "tiktok-creator", "alt": "A creator filming a short video on a phone mounted on a tripod in a sunny room"},
        "sections": [
            {
                "h2": "Why cards, when mobile money is everywhere",
                "p": [
                    "Mobile money is how many people pay for almost everything, so we understand the question. Our packages are monthly subscriptions, though, and the only checkout we use, Stripe, renews them on a card. One way of paying for every customer keeps billing, invoices and cancelling the same wherever you are.",
                ],
            },
            {
                "h2": "Turning a wallet balance into a card payment",
                "ul": [
                    "Ask your mobile money provider or bank whether it offers a virtual Visa or Mastercard card linked to your wallet.",
                    "Check that the card allows online payments in US dollars to companies abroad.",
                    "Keep the card funded for each renewal date, since the package renews monthly.",
                ],
            },
            {
                "h2": "Choosing where your followers live",
                "p": [
                    "You name the place: Accra, Kampala, Lagos, Nairobi, a whole country or a wider region. Our campaign shows your profile to real people there every day, and those who like what they see follow you.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy TikTok followers with mobile money?", "No. Every TikTok package is paid like an Instagram one: by card, Apple Pay or Google Pay through Stripe."),
            ("Do you accept bank transfer?", "No. Bank transfers aren't accepted either; payment happens only at Stripe's checkout, by card or phone wallet."),
            ("Why do you charge in US dollars?", "One currency keeps prices the same for everyone. Your bank converts the amount when you pay, at its own rate."),
            ("Can I pay for one month and stop?", "Yes. Cancel in your account whenever you like; the month you've paid for runs to its end and nothing more is charged."),
            ("What does a first month bring?", "With {starter_name}, typically {starter_audience} new followers, {starter_likes} likes and {starter_comments} comments, spread across the month. They're ranges rather than promises, because each follower is a person's choice."),
        ],
    },
    {
        "article": "pay-with-momo",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/momo",
        "label": "Paying with MoMo",
        "title": "Buy Instagram Followers With MoMo? Cards Work Here | Growsterr",
        "description": "We don't take MoMo, in Africa or in Vietnam. You can buy Instagram or TikTok followers by card, Apple Pay or Google Pay through Stripe, on a monthly plan.",
        "h1": ("Buy Instagram followers with MoMo? ", "Not here, but a card works."),
        "intro": "Whether your MoMo is a mobile money wallet in Ghana, Uganda or Cameroon, or the MoMo e-wallet in Vietnam, we can't take it, so it isn't a way to buy Instagram followers from us. Packages are paid by card through Stripe's secure checkout, or with Apple Pay or Google Pay. They renew monthly and stop whenever you cancel, for TikTok as well as Instagram.",
        "hero": {"image": "tiktok-hub", "alt": "Likes and new follows appearing on a TikTok video as people discover the creator"},
        "sections": [
            {
                "h2": "Approving each payment versus a renewal",
                "p": [
                    "MoMo payments are usually approved one at a time on your phone. A Growsterr package works differently: it's a subscription that Stripe renews on your card each month, without you having to send anything. That's the only way we take payment, in every country, which is why MoMo isn't on the list.",
                ],
            },
            {
                "h2": "Paying from Ghana, Uganda or Vietnam",
                "ul": [
                    "A bank debit or credit card works once online payments abroad are turned on.",
                    "Apple Pay and Google Pay appear at checkout when your phone has a card saved.",
                    "A virtual card from your bank or wallet provider can work too, if it's enabled for payments in US dollars.",
                ],
            },
            {
                "h2": "Your audience, in your country",
                "p": [
                    "Paying by card has no effect on targeting. Ask for followers from Accra, Kampala, Ho Chi Minh City, Hanoi or a whole country, and that's where we show your profile first.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy TikTok followers with MoMo?", "No. TikTok packages use the same card checkout as Instagram ones."),
            ("Is there a MoMo number I can send money to?", "No. We never take payment by MoMo, so treat any request to send money to a number in our name as a scam. Payment only happens at Stripe's checkout."),
            ("Will my card be charged in cedis or dong?", "No, in US dollars. Your bank converts the amount and shows it in your currency, at its own rate."),
            ("How long does each payment cover?", "One month. Your campaign runs every day of that month, and the next month is charged only if you haven't cancelled."),
            ("Do the followers interact, or just follow?", "Many interact. The same people who follow you like and comment on posts they enjoy: with {starter_name}, typically {starter_likes} likes and {starter_comments} comments a month."),
        ],
    },
    {
        "article": "pay-with-coins-app",
        "kind": "payment",
        "platform": "instagram",
        "slug": "payments/coins-app",
        "label": "Paying with a coins app",
        "title": "Buy Instagram Followers With a Coins App? | Growsterr",
        "description": "Coins apps don't work here, whether you earn coins by following others or pay from a coins wallet. Packages are paid by card, Apple Pay or Google Pay, monthly.",
        "h1": ("Buy Instagram followers with a coins app? ", "Coins don't work here."),
        "intro": "People mean two things by buying Instagram followers with a coins app: earning coins by following other accounts and spending them on followers, or paying from a wallet app that holds coins. We don't take either. Growsterr packages are paid by card through Stripe's secure checkout, or with Apple Pay or Google Pay, as a monthly subscription. The same applies to TikTok followers.",
        "hero": {"image": "instagram-followers", "alt": "An Instagram profile gaining followers from people who chose to follow, not from coin trades"},
        "sections": [
            {
                "h2": "Earning coins by following others",
                "p": [
                    "In a follow-for-coins app, you follow strangers to earn coins, then spend the coins so strangers follow you. Nobody is choosing you for your posts; they're collecting coins too. Many of these apps ask you to sign in with your Instagram account, which means handing over your password, and the follows tend to disappear when people unfollow to earn their next coins.",
                ],
            },
            {
                "h2": "Paying from a coins wallet",
                "p": [
                    "If you meant a wallet app holding coins or crypto, we don't take that either. Every package is a subscription that renews monthly on a card through Stripe, so you can cancel it yourself and your bank's protections apply to each payment.",
                ],
            },
            {
                "h2": "What a package brings instead",
                "ul": [
                    "Real people who found your profile and chose to follow, every day of the month.",
                    "Likes and comments from those same people, inside the package.",
                    "Your password stays with you; your username is all we ask for.",
                    "A dashboard of what our campaign measured, day by day.",
                ],
            },
        ],
        "faqs": [
            ("Can I buy TikTok followers with coins?", "No. Neither coins earned by following nor coins in a wallet app can pay for a TikTok package. Pay by card, Apple Pay or Google Pay instead."),
            ("Do follow-for-coins followers stay?", "Often not. People in those apps follow to earn coins, not out of interest, and unfollow when it suits them. Real followers stay as long as your posts give them a reason to."),
            ("Is a coins app safe for my account?", "We can't speak for any particular app. Be wary of anything that wants your Instagram login: we never ask for it, and you shouldn't give it to anyone."),
            ("So how does paying work here?", "Choose a package, enter your username and where your audience should come from, then pay at Stripe's checkout by card, Apple Pay or Google Pay. The subscription then renews each month until you cancel it."),
            ("Is there a cheaper way to try it?", "The smallest package is {starter_name}, at {starter_price} for a month, and you can cancel straight away so it doesn't renew. There's no trial, and no coins."),
        ],
    },
]
