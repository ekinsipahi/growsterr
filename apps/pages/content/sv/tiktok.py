"""Swedish TikTok pages: the hub and likes (mirrors en/tiktok.py)."""

UPDATED = "2026-11-08"

PAGES = [
    {
        "slug": "tiktok",
        "label": "TikTok",
        "title": "TikTok-tillväxtpaket för kreatörer | Growsterr",
        "description": "Väx på TikTok med riktiga människor: månadspaket ger nya följare, likes och kommentarer från människor som själva valt att följa. Från {from_price} i månaden.",
        "h1": ("Få ditt TikTok att växa ", "med riktiga människor."),
        "intro": "Tillväxtpaket per månad för kreatörer och influencers. Riktiga människor hittar din profil, tittar på dina videor och följer dig när de gillar det de ser. Din översikt visar vad vi har mätt, dag för dag.",
        "hero": {"image": "tiktok-hub", "alt": "En TikTok-kreatörs profil där nya följare och likes kommer in"},
        "sections": [
            {
                "h2": "På TikTok är uppmärksamhet allt",
                "p": [
                    "TikTok visar en video för fler när de första tittarna tittar, gillar, kommenterar och följer. Siffror utan människor bakom påverkar inget av det.",
                    "Våra paket för riktiga människor till din profil varje dag. De tittar, de bestämmer, och de som gillar dina videor följer och gillar. Det är den sortens uppmärksamhet som hjälper en video att spridas.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Riktiga tittare som ser en kreatörs TikTok-videor"},
            },
            {
                "h2": "För kreatörer som har något att säga",
                "p": [
                    "Komedi, matlagning, mode eller tutorials: om du publicerar regelbundet ger riktiga tittare varje ny video en bättre start. Börja med {starter_name} och gå upp ett steg när du är redo.",
                ],
                "ul": [
                    "Du berättar vilken stad, region eller vilket land din publik ska komma ifrån.",
                    "Följare, likes och kommentarer kommer tillsammans, från samma människor.",
                    "Ditt konto förblir ditt: vi ber aldrig om ditt lösenord.",
                ],
                "image": {"image": "tiktok-creator", "alt": "En kreatör som filmar en TikTok-video med mobilen på ett stativ"},
            },
        ],
        "faqs": [
            ("Är följarna riktiga människor?", "Ja. Varje följare är en riktig människa som har sett din profil och valt att följa dig. Vi använder aldrig bottar, falska konton eller direktleverans."),
            ("Hur många följare ger ett paket?", "Oftast {starter_audience} nya följare i månaden med {starter_name}, {rising_audience} med {rising_name} och {pro_audience} med {pro_name}. Typiska intervall, inget fast antal: riktiga människor bestämmer själva."),
            ("Behöver ni mitt TikTok-lösenord?", "Aldrig. Vi behöver bara ditt användarnamn. Håll kontot offentligt så att de som hittar det kan följa dig."),
            ("Kan jag köpa visningar eller likes separat?", "Nej. Visningar, likes och kommentarer ingår i varje paket, från samma riktiga människor som följer dig."),
            ("Kan jag säga upp när jag vill?", "Ja. Paketen förnyas varje månad och du kan säga upp dem från ditt konto. Månaden du har betalat för löper till sitt slut."),
        ],
    },
    {
        "service": "likes",
        "slug": "tiktok/likes",
        "label": "TikTok-likes",
        "title": "TikTok-likes från riktiga människor, i varje paket",
        "description": "TikTok-likes från riktiga människor som tittar på dina videor, aldrig bottar. Likes ingår i varje månadspaket, med följare och kommentarer. Från {from_price}/mån.",
        "h1": ("TikTok-likes från riktiga människor. ", "I varje paket."),
        "intro": "Vi säljer inte likes separat. Varje paket ger riktiga människor som hittar din profil, tittar på dina videor och gillar det de tycker om: oftast {starter_likes} likes i månaden med {starter_name}.",
        "hero": {"image": "tiktok-likes", "alt": "Likes från riktiga tittare som stiger från en TikTok-video"},
        "sections": [
            {
                "h2": "En like räknas bara med en människa bakom",
                "p": [
                    "TikTok ser vad som händer runt en like: tittade personen vidare, följde, kom tillbaka? Likes från bottar svarar nej på allt, så de lägger till en siffra och tar bort räckvidd.",
                    "Likes från riktiga människor kommer med resten: tittartid, följningar och kommentarer. Det är signalen som hjälper en video att spridas.",
                ],
                "image": {"image": "tiktok-watch-time", "alt": "Tittare som ser en TikTok-video till slutet och gillar den"},
            },
            {
                "h2": "Så många likes ger varje paket",
                "ul": [
                    "{starter_name} ({starter_price} i månaden): oftast {starter_likes} likes.",
                    "{rising_name} ({rising_price} i månaden): oftast {rising_likes} likes, på videorna du väljer.",
                    "{pro_name} ({pro_price} i månaden): oftast {pro_likes} likes, med prioriterad placering.",
                ],
            },
            {
                "h2": "Varför vi inte säljer likes separat",
                "p": [
                    "Likes som kommer utan visningar, följningar eller kommentarer ser ut precis som det de är. I ett paket kommer varje like från någon som har tittat, så dina siffror rör sig tillsammans, som verklig tillväxt gör.",
                ],
            },
        ],
        "faqs": [
            ("Kan jag få TikTok-likes utan paket?", "Nej. Likes, visningar och kommentarer kommer bara i våra månadspaket, från samma riktiga människor. Det är det som håller dem naturliga."),
            ("Vilka videor får likes?", "Riktiga människor gillar det de tycker om, oftast dina senaste videor. Med {rising_name} och {pro_name} kan du välja vilka videor som får uppmärksamheten."),
            ("Hur snabbt kommer likes?", "Lite varje dag, under månaden. Aldrig direkt: en like som kommer direkt är en bott."),
            ("Behöver ni mitt TikTok-lösenord?", "Aldrig. Vi behöver bara ditt användarnamn, och kontot ska vara offentligt."),
        ],
    },
]
