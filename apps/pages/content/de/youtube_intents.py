UPDATED = "2026-11-09"

# German YouTube intent pages: searches for things we don't sell (cheap, instant, free, free
# trial, panels). Each answers honestly, then leads to the monthly package. Keys and placeholders:
# docs/CONTENT.md; angles: docs/keywords/WRITING.md.

PAGES = [
    # --- Subscribers ----------------------------------------------------------------------
    {
        "service": "subscribers",
        "modifier": "cheap",
        "slug": "youtube/abonnenten/guenstig",
        "label": "Günstige YouTube-Abonnenten?",
        "plan": "starter",
        "title": "YouTube-Abonnenten günstig kaufen: der wahre Preis | Growsterr",
        "description": "YouTube-Abonnenten für einen Euro schauen nie und werden aussortiert. Für {starter_price} im Monat bringt {starter_name} meist {starter_audience} echte Zuschauer.",
        "h1": ("YouTube-Abonnenten für einen Euro ", "sehen nie ein einziges Video."),
        "intro": "Sie überlegen, YouTube-Abonnenten günstig zu kaufen, für einen Euro? Zu diesem Preis bekommen Sie Konten, die nie schauen, liken oder kommentieren, und YouTube entfernt Spam-Konten regelmäßig aus Abonnentenzahlen. Wir verlangen mehr und bringen Zuschauer: mit {starter_name} für {starter_price} in einem typischen Monat {starter_audience} neue Abonnenten, jeder ein Mensch, der Ihren Kanal gefunden und abonniert hat.",
        "hero": {"image": "youtube-subscribers", "alt": "Die Abonnentenzahl eines YouTube-Kanals wächst mit echten Zuschauern"},
        "sections": [
            {
                "h2": "Was ein Abonnent kostet, der nie schaut",
                "p": [
                    "Auf YouTube zählt, was Abonnenten tun, mehr als wie viele es sind. Eine Liste voller Konten, die nie auf Play drücken, lässt jeden neuen Upload uninteressanter wirken, als er ist.",
                    "Ein billiger Abonnent ist also nicht billig. Sie zahlen einmal mit Geld und noch einmal mit den Aufrufen, die Sie nicht bekommen.",
                ],
            },
            {
                "h2": "Was ein echter Abonnent kostet",
                "p": [
                    "Nehmen Sie {starter_name}: {starter_price} im Monat und typischerweise {starter_audience} Abonnenten, die echte Zuschauer aus dem Ort Ihrer Wahl sind. Pro Mensch ist das eine Frage von Cents, und ihre Likes und Kommentare sind im Preis enthalten.",
                ],
            },
            {
                "h2": "Niedriger Preis ohne Risiko",
                "ul": [
                    "Kein Passwort und kein Zugriff auf Ihr Google-Konto: nur Ihr Kanal-Handle.",
                    "Monatliche Abrechnung per Karte über Stripe, in Ihrem Konto kündbar.",
                    "Abonnenten, Likes und Kommentare zu einem Preis, von denselben Menschen.",
                ],
            },
        ],
        "faqs": [
            ("Was kosten echte YouTube-Abonnenten?", "Unsere Pakete beginnen bei {starter_price} im Monat. {starter_name} bringt typischerweise {starter_audience} neue Abonnenten; {rising_name} für {rising_price} bringt {rising_audience}; {pro_name} für {pro_price} bringt {pro_audience}."),
            ("Warum verkaufen manche Seiten Abonnenten so billig?", "Weil sie Konten verkaufen, keine Zuschauer. Konten massenhaft zu erstellen oder zu mieten, kostet sehr wenig; Menschen zu finden, die Ihren Kanal sehen wollen, nicht."),
            ("Gibt es eine sehr günstige Option für einen kleinen Kanal?", "{starter_name} ist für neue und kleine Kanäle gemacht und unser niedrigster Preis."),
            ("Können billige Abonnenten meinem Kanal schaden?", "Das können sie. Die Richtlinie von YouTube zu falschem Engagement umfasst gekaufte Abonnenten, und Kanäle, die sie nutzen, riskieren entfernte Videos oder Strafen für den Kanal."),
            ("Sind Aufrufe im Preis enthalten?", "Ja. Ihre neuen Abonnenten schauen, liken und kommentieren von sich aus, alles im Paket. Aufrufe beziffern wir nicht, denn jeder ist jemand, der sich entscheidet, auf Play zu drücken."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "fast",
        "slug": "youtube/abonnenten/schnell",
        "label": "Schnelle YouTube-Abonnenten?",
        "title": "YouTube-Abonnenten schnell kaufen: echt statt sofort | Growsterr",
        "description": "Echte, sofortige und aktive YouTube-Abonnenten zugleich gibt es nicht. Unsere sind echt und aktiv: Die Kampagne startet in Tagen, Abonnenten kommen täglich.",
        "h1": ("Echt, aktiv und sofort? ", "Nur zwei davon passen zusammen."),
        "intro": "Sie möchten YouTube-Abonnenten schnell kaufen, echt, sofort und aktiv zugleich? Nur zwei davon können zusammen stimmen. Sofort-Abonnenten sind keine Menschen, und echte Menschen abonnieren nicht in der Sekunde, in der Sie zahlen. Wir bringen echte, aktive Abonnenten zügig: Die Kampagne läuft in den ersten Tagen an, und ab dann bringt {pick_name} typischerweise {pick_audience} im Monat, jeden Tag ein paar.",
        "hero": {"image": "youtube-subscribers", "alt": "Neue Abonnenten kommen Tag für Tag zu einem YouTube-Kanal"},
        "sections": [
            {
                "h2": "Warum sofort auf YouTube falsch heißt",
                "p": [
                    "Ein echter Mensch abonniert, nachdem er etwas gesehen hat: ein Video, einen Short, einen Kanaltrailer. Das dauert mindestens Minuten, und es passiert, wenn er dazu kommt. Abonnenten, die direkt nach einer Zahlung zu Hunderten auftauchen, haben das Anschauen übersprungen, und das verrät, dass es keine Menschen waren.",
                ],
            },
            {
                "h2": "Wie schnell echte Abonnenten kommen",
                "p": [
                    "Die Einrichtung dauert die ersten Tage nach Ihrer Bestellung. Ab dann finden jeden Tag neue Zuschauer Ihren Kanal, und wem gefällt, was er sieht, der abonniert. Das Dashboard zeigt jeden Tag so, wie wir ihn messen, also sehen Sie das Tempo ab der ersten Woche.",
                ],
            },
            {
                "h2": "Tempo, das Sie nutzen können",
                "ul": [
                    "Laden Sie hoch, während die Kampagne läuft, damit neue Abonnenten als Nächstes etwas zu sehen haben.",
                    "Räumen Sie Ihre Kanalseite auf: ein klares Banner, ein Trailer und Playlists in sinnvoller Reihenfolge.",
                    "Wählen Sie {pro_name} für die größte Monatsspanne: typischerweise {pro_audience} neue Abonnenten.",
                ],
            },
        ],
        "faqs": [
            ("Wie schnell steigt meine Abonnentenzahl?", "In den ersten Tagen Ihrer Kampagne: anfangs ein paar auf einmal, dann jeden Tag über den Monat."),
            ("Können Sie 1.000 Abonnenten sofort hinzufügen?", "Nein, mit echten Menschen kann das niemand. Tausend in einer Stunde heißt tausend Konten, die nie schauen werden, und genau die räumt YouTube aus."),
            ("Sind Ihre Abonnenten aktiv?", "Es sind echte Menschen, die nach einem Blick auf Ihren Kanal abonniert haben, also so aktiv wie jeder Zuschauer: Sie schauen, liken und kommentieren, wenn ein Video sie interessiert."),
            ("Welches Paket ist am schnellsten?", "{pro_name} bringt jeden Monat am meisten: typischerweise {pro_audience} neue Abonnenten. {starter_name} und {rising_name} bringen kleinere Spannen, genauso über den Monat verteilt."),
            ("Schadet schnelles Wachstum meinem Kanal?", "Nicht in diesem Tempo. Abonnenten kommen täglich von echten Zuschauern, und genau so gewinnen wachsende Kanäle sie ohnehin."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "free",
        "slug": "youtube/abonnenten/kostenlos",
        "label": "Kostenlose YouTube-Abonnenten?",
        "plan": "starter",
        "tool": "growth-calculator",
        "title": "Kostenlose YouTube-Abonnenten? Ein besserer Plan | Growsterr",
        "description": "Kostenlose YouTube-Abonnenten kommen aus Sub-for-Sub-Tausch oder von Bots. Wir bieten keine an; unser Gratis-Rechner zeigt, wie lange echtes Wachstum dauert.",
        "h1": ("Kostenlose YouTube-Abonnenten? ", "Planen Sie lieber echte."),
        "intro": "Sie suchen kostenlose YouTube-Abonnenten oder 1.000 für fünf Euro? Beides bringt keine Menschen, die schauen: Gratis-Angebote beruhen auf Sub-for-Sub-Tausch oder Bot-Konten. Wir verschenken keine Abonnenten. Kostenlos ist auf dieser Seite der Wachstumsrechner: Geben Sie ein, wo Ihr Kanal steht und wohin er soll, und er schätzt die Monate, die jedes Paket typischerweise braucht.",
        "hero": {"image": "youtube-channel", "alt": "Ein YouTuber plant ein Abonnentenziel für die kommenden Monate"},
        "sections": [
            {
                "h2": "Sub-for-Sub und andere Gratis-Tricks",
                "ul": [
                    "Sub-for-Sub-Gruppen: Sie abonnieren Fremde, die abonnieren zurück, und niemand schaut irgendwen.",
                    "Gratis-Abonnenten-Seiten, bei denen Sie sich mit Google anmelden sollen und die dann mit Ihrem Konto andere abonnieren.",
                    "Winzige Gratis-Ladungen von Bot-Konten, damit Sie eine größere kaufen.",
                ],
                "p": [
                    "Alle füllen Ihre Zahl mit Menschen, die kein Interesse an Ihren Videos haben, und das ist schlimmer, als weniger Abonnenten zu haben.",
                ],
            },
            {
                "h2": "Zu diesen 1.000",
                "p": [
                    "Tausend Abonnenten sind für viele Kanäle ein Meilenstein, oft wegen des YouTube-Partnerprogramms. Gekaufte oder getauschte Abonnenten bringen keine Wiedergabezeit, und YouTube behandelt sie als falsches Engagement. Monetarisierung versprechen auch wir nicht: Wir bringen echte Zuschauer, der Rest hängt von Ihren Videos und von YouTube ab.",
                ],
            },
            {
                "h2": "Planen Sie es mit dem Wachstumsrechner",
                "p": [
                    "Der Rechner weiter oben ist kostenlos und funktioniert in Ihrem Browser. Tragen Sie Ihre Abonnentenzahl dort ein, wo nach den Followern von heute gefragt wird, und Ihr Ziel als Ziel. Er rechnet aus der typischen Monatsspanne jedes Pakets aus, wie viele Monate es typischerweise braucht.",
                ],
            },
        ],
        "faqs": [
            ("Kann ich YouTube-Abonnenten kostenlos bekommen?", "Echte nicht, jedenfalls nicht von uns. Jeder Abonnent, den wir bringen, ist ein Zuschauer, erreicht durch eine bezahlte Kampagne. Kostenlos ist hier der Rechner, und den können Sie so oft nutzen, wie Sie wollen."),
            ("Sind 1.000 YouTube-Abonnenten für fünf Euro echt?", "Keine echte Kampagne findet für fünf Euro tausend Menschen, die Ihren Kanal wollen. Zu diesem Preis sind die Abonnenten Konten, keine Zuschauer."),
            ("Wie lange dauert es bis zu 1.000 echten Abonnenten?", "Das hängt von Ihrem Ausgangspunkt ab. {starter_name} bringt typischerweise {starter_audience} neue Abonnenten im Monat; geben Sie Ihre eigenen Zahlen in den Rechner oben ein, um die Monate für Ihren Kanal zu sehen."),
            ("Verstößt Sub-for-Sub gegen die Regeln von YouTube?", "Ja. Die Richtlinie von YouTube zu falschem Engagement umfasst den Tausch von Abos, das kann einen Kanal also gefährden. Außerdem bringt es Abonnenten, die nie schauen."),
            ("Wo sollte ein kleiner Kanal anfangen?", "Mit {starter_name} für {starter_price} im Monat, ohne Vertrag über den laufenden Monat hinaus."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "free-trial",
        "slug": "youtube/abonnenten/kostenlos-testen",
        "label": "YouTube-Abonnenten kostenlos testen?",
        "plan": "starter",
        "title": "YouTube-Abonnenten gratis testen? So prüfen Sie uns | Growsterr",
        "description": "Keinen Gratis-Test für YouTube-Abonnenten: Eine Probe für einen Tag beweist nichts. Ihr erster Monat zeigt echte Zuschauer, gemessen, ohne Vertrag.",
        "h1": ("Ein Gratis-Test für YouTube-Abonnenten ", "würde nichts beweisen. Ein Monat schon."),
        "intro": "Wenn Sie YouTube-Abonnenten erst nach einem kostenlosen Test kaufen möchten, sagen wir es offen: Einen Test bieten wir nicht an. Eine Probe mit 100 Abonnenten an einem Tag würde nur zeigen, dass ein Anbieter Konten übrig hat. Ihr erster Monat ist der Maßstab: {starter_name} für {starter_price}, echte Zuschauer ab den ersten Tagen, ein Dashboard mit Messwerten und kein Vertrag über den Monat hinaus.",
        "hero": {"image": "youtube-hub", "alt": "Die Analysen eines YouTube-Kanals im ersten Monat echten Wachstums"},
        "sections": [
            {
                "h2": "Was ein Test nicht zeigen kann",
                "p": [
                    "Die Frage ist nicht, ob eine Zahl steigen kann, sondern ob echte Menschen schauen, liken und bleiben, und das sieht man erst nach Wochen. Eine Probe für einen Tag ist ein Verkaufstrick, kein Test.",
                ],
            },
            {
                "h2": "So prüfen Sie uns im Laufe des Monats",
                "ul": [
                    "Öffnen Sie alle paar Tage das Dashboard: Besuche aus der Kampagne und neue Abonnenten, so wie gemessen.",
                    "Schauen Sie in Ihre Videoanalysen: Sehen neue Zuschauer zu?",
                    "Lesen Sie die Kommentare: Menschen, die in eigenen Worten über Ihre Videos schreiben.",
                    "Entscheiden Sie vor dem Verlängerungsdatum; kündigen können Sie jederzeit in Ihrem Konto.",
                ],
            },
        ],
        "faqs": [
            ("Gibt es einen kostenlosen Test für YouTube?", "Nein. Tests bieten wir auf keiner Plattform an. Ein Monat ist das kürzeste Paket, und Sie können kündigen, bevor der nächste beginnt."),
            ("Warum kein Test, wenn andere Seiten einen anbieten?", "Jeder Abonnent, den wir bringen, stammt aus einer echten Kampagne, die ab dem ersten Tag Geld kostet. Anbieter, die sich Gratisproben leisten können, schicken meist Konten, keine Zuschauer."),
            ("Was passiert, wenn ich nach einem Monat kündige?", "Es wird nichts mehr berechnet, und der bezahlte Monat läuft bis zu seinem Ende. Echte Abonnenten werden nicht zurückgenommen; sie bleiben, solange sie nicht selbst gehen."),
            ("Sehe ich im ersten Monat Ergebnisse?", "Sie sehen das Tempo: neue Abonnenten jeden Tag, mit {starter_name} typischerweise {starter_audience} über den Monat. Typisch, nicht fest, denn jeder davon ist jemand, der selbst entscheidet."),
            ("Kann ich zuerst ein kleineres Paket ausprobieren?", "{starter_name} ist unser kleinstes und der natürliche Einstieg. Wenn Ihr Kanal mehr braucht, können Sie später aufsteigen."),
        ],
    },
    {
        "service": "subscribers",
        "modifier": "smm-panel",
        "slug": "youtube/abonnenten/smm-panel",
        "label": "YouTube-Abonnenten aus SMM-Panels?",
        "title": "YouTube-Abonnenten über ein SMM-Panel kaufen? | Growsterr",
        "description": "SMM-Panels verkaufen YouTube-Abonnenten und Aufrufe im Tausenderpack, mit Nachfüllung, weil sie fallen. Wir sind eine Agentur: echte Zuschauer, ein Dashboard.",
        "h1": ("Panel-Abonnenten kommen mit Nachfüll-Knopf. ", "Unsere brauchen keinen."),
        "intro": "Bevor Sie YouTube-Abonnenten oder Aufrufe über ein SMM-Panel kaufen, achten Sie auf die Nachfüll-Option, die Panels oft gleich daneben anbieten: Sie rechnen damit, dass die Zahlen fallen. Panels verkaufen Bot-Traffic in Massen weiter. Wir arbeiten als Agentur: Menschen aus unserem Team betreuen Ihre Kampagne, echte Zuschauer finden Ihren Kanal und abonnieren, und das Dashboard zeigt, was wir gemessen haben.",
        "hero": {"image": "youtube-channel", "alt": "Ein Creator prüft ein Dashboard mit gemessenen neuen YouTube-Abonnenten"},
        "sections": [
            {
                "h2": "Abonnenten und Aufrufe im Tausenderpack",
                "p": [
                    "In einem Panel stehen YouTube-Abonnenten, Aufrufe und Wiedergabezeit in einer Liste, pro Tausend bepreist, mit Hinweisen zu Startzeiten und Nachfüllungen. Niemand schaut sich Ihren Kanal an. Die Bestellung landet in einer Warteschlange, und Konten tun, was die Warteschlange sagt.",
                    "Panel-Aufrufe funktionieren genauso: Wiedergaben, ohne dass sich jemand zum Zuschauen entschieden hat, genau die Art, die YouTube aus Aufrufzahlen herauszufiltern versucht.",
                ],
            },
            {
                "h2": "Was sich mit einer Agentur ändert",
                "ul": [
                    "Menschen statt Warteschlangen: Ihr Kanal wird jeden Tag echten Zuschauern gezeigt.",
                    "Jeder Abonnent, jedes Like, jeder Aufruf und jeder Kommentar geht auf einen Menschen zurück.",
                    "Ein Team hinter Ihrer Kampagne und ein Weg, uns zu erreichen, wenn Sie Fragen haben.",
                    "Ein Dashboard mit dem, was wir gemessen haben, kein Zähler, der nachgefüllt werden muss.",
                ],
            },
        ],
        "faqs": [
            ("Sind Panel-Abonnenten echte Menschen?", "Nein. Panels verkaufen Massen-Traffic von Konten weiter, die auf Anweisung abonnieren, und deshalb gehören Nachfüllungen zum Angebot."),
            ("Verkaufen Sie YouTube-Aufrufe einzeln?", "Nein. Aufrufe sind kein eigener Posten. Sie kommen von den Menschen, die unsere Kampagne erreicht, denselben, die abonnieren, liken und kommentieren."),
            ("Können Panel-Aufrufe meinem Kanal schaden?", "Ja. Künstliche Aufrufe verstoßen gegen die Regeln von YouTube zu falschem Engagement; sie können aus Ihrer Zahl gestrichen werden, und wiederholte Nutzung gefährdet den Kanal."),
            ("Bieten Sie ein Reseller-Panel an?", "Nein. Wir verkaufen weder in Massen noch über Wiederverkäufer: Jedes Paket ist eine Kampagne rund um einen Kanal. Agenturen mit mehreren Kanälen können sich bei uns melden, um das zu besprechen."),
            ("Was bringt ein Paket jeden Monat?", "{pick_name} bringt typischerweise {pick_audience} neue Abonnenten im Monat, echte Zuschauer, verteilt über alle 30 Tage."),
        ],
    },
    # --- Views ----------------------------------------------------------------------------
    {
        "service": "views",
        "modifier": "cheap",
        "slug": "youtube/aufrufe/guenstig",
        "label": "Günstige YouTube-Aufrufe?",
        "plan": "starter",
        "title": "YouTube-Views günstig kaufen? Was ein Euro bringt | Growsterr",
        "description": "Günstige YouTube-Views für einen Euro pro Tausend sind Wiedergaben, keine Zuschauer. Unser Paket bringt Menschen, die schauen, abonnieren und kommentieren.",
        "h1": ("Günstige YouTube-Views ", "sind Wiedergaben, keine Zuschauer."),
        "intro": "Wenn Sie YouTube-Views günstig kaufen wollen, etwa tausend für einen Euro, wissen Sie, was ankommt: Wiedergaben von Skripten oder Massenkonten, die höchstens ein paar Sekunden schauen, und YouTube kann sie aus Ihrer Zahl streichen. Aufrufe verkaufen wir nicht einzeln. Unser Monatspaket bringt echte Menschen auf Ihren Kanal, und sie schauen, liken, kommentieren und abonnieren aus eigenem Antrieb.",
        "hero": {"image": "youtube-viewers", "alt": "Echte Zuschauer sehen ein YouTube-Video bis zum Ende"},
        "sections": [
            {
                "h2": "Was ein Aufruf wert ist",
                "p": [
                    "Ein Aufruf hilft, wenn ein Mensch zuschaut. Wie lange er bleibt, ob er liked und welches Video er als Nächstes anklickt, zeigt YouTube, dass ein Video mehr Zuschauer verdient. Ein billiger Aufruf erhöht den Zähler um eins und gibt YouTube nichts, woran es sich halten kann.",
                    "Eine große Aufrufzahl mit fast keiner Wiedergabezeit sendet zudem ein widersprüchliches Signal, und die gekauften Wiedergaben können ohnehin entfernt werden.",
                ],
            },
            {
                "h2": "Ein YouTube-Paket, die ehrliche Sorte",
                "p": [
                    "Wir verkaufen durchaus ein Paket, nur kein Paket an Aufrufen. {starter_name} kostet {starter_price} im Monat: typischerweise {starter_audience} neue Abonnenten, {starter_likes} Likes und {starter_comments} Kommentare von echten Zuschauern, dazu die Aufrufe, die dieselben Menschen Ihren Videos geben.",
                    "Aufrufe zählen wir nicht im Voraus. Sie folgen Ihren Inhalten statt einer Quote, denn jeder ist die Entscheidung eines Menschen.",
                ],
            },
            {
                "h2": "Preis pro Aufruf oder Preis pro Zuschauer",
                "p": [
                    "Zählen Sie Zuschauer, nicht Aufrufe. Ein echter Abonnent kann in den Monaten, die er bleibt, Dutzende Ihrer Videos ansehen. Skript-Wiedergaben für einen Euro sehen nach heute nichts mehr an.",
                ],
            },
        ],
        "faqs": [
            ("Was kosten YouTube-Aufrufe bei Ihnen?", "Aufrufe haben keinen eigenen Preis. Das kleinste Paket, {starter_name}, kostet {starter_price} im Monat und bringt Abonnenten, Likes und Kommentare, mit Aufrufen von denselben Menschen."),
            ("Warum sind Aufrufe für einen Euro so billig?", "Weil niemand sie ansieht. Skripte und Massenkonten erzeugen Wiedergaben für fast nichts, und mehr als Wiedergaben erzeugen sie nicht."),
            ("Bringen billige Aufrufe mir echte Zuschauer?", "Kaum. YouTube schaut darauf, wie Menschen auf ein Video reagieren, nicht nur auf die Zahl, und gekaufte Aufrufe reagieren nicht."),
            ("Kann ich wählen, welche Videos Zuschauer bekommen?", "Nicht direkt: Die Kampagne bewirbt Ihren Kanal, und Zuschauer wählen, was sie sehen. Starke Titel und Thumbnails helfen ihnen, Ihre besten Videos zu finden."),
            ("Gibt es ein sehr günstiges Paket nur für Aufrufe?", "Unterhalb von {starter_name} für {starter_price} im Monat gibt es keine Option nur für Aufrufe, denn Aufrufe kommen von den Menschen, die ein Paket bringt."),
        ],
    },
    {
        "service": "views",
        "modifier": "fast",
        "slug": "youtube/aufrufe/schnell",
        "label": "Schnelle YouTube-Aufrufe?",
        "title": "YouTube-Views schnell? So kommen echte Zuschauer | Growsterr",
        "description": "Sofortige YouTube-Views, auch für Premieren, kommen von Skripten. Echte Zuschauer finden Ihren Kanal ab den ersten Kampagnentagen und kommen immer wieder.",
        "h1": ("Schnelle YouTube-Views? ", "Zuschauer kommen nicht per Lieferung."),
        "intro": "Sie möchten YouTube-Views schnell kaufen, mit Sofort-Lieferung? Aufrufe nach Zeitplan kommen von Skripten, nicht von Menschen: Ein echter Zuschauer klickt, wenn ihm ein Video ins Auge fällt. Aufrufe verkaufen oder liefern wir nicht. Wir bringen ab den ersten Kampagnentagen jeden Tag echte Menschen auf Ihren Kanal, und die schauen, liken und abonnieren von sich aus.",
        "hero": {"image": "youtube-viewers", "alt": "Zuschauer entdecken den neuen YouTube-Upload eines Creators"},
        "sections": [
            {
                "h2": "Schnelle Lieferung ist ein Wort für Pakete aus Pappe",
                "p": [
                    "Lieferzeiten ergeben Sinn für Dinge in Kartons. Bei Aufrufen heißt ein Liefertempo, dass eine Maschine auf Play drückt, und diese Wiedergaben bringen keine Wiedergabezeit, die etwas wert wäre.",
                ],
            },
            {
                "h2": "Premieren-Aufrufe brauchen echte Menschen",
                "p": [
                    "Eine Premiere ist ein Moment: Menschen, die warten, chatten und gemeinsam schauen. Gekaufte Premieren-Aufrufe können einen Zähler füllen, aber nie den Chat. Ein Publikum zu einer festen Minute bringen können auch wir nicht, und wir tun nicht so.",
                    "Was hilft, ist ein größerer Stamm echter Abonnenten, die die Premiere auf ihrer Startseite oder in ihren Abos sehen und sich erinnern lassen können.",
                ],
            },
            {
                "h2": "Wie schnell echte Aufrufe wachsen",
                "ul": [
                    "In den ersten Tagen geht Ihre Kampagne live, und neue Zuschauer erreichen Ihren Kanal.",
                    "Jeder Upload in diesem Monat ist für die Menschen da, die letzte Woche abonniert haben.",
                    "Aufrufe kommen von diesen Abonnenten, solange ihnen Ihre Videos gefallen.",
                ],
            },
        ],
        "faqs": [
            ("Wie schnell steigen meine Aufrufe?", "Sobald die Kampagne läuft, und das passiert in ihren ersten Tagen, steigen die Aufrufe, während neue Menschen Ihren Kanal finden. Sie wachsen mit Ihrem Publikum, statt auf einem Video zu springen."),
            ("Können Sie Sofort-Aufrufe auf einen neuen Upload schicken?", "Nein. Sofort-Aufrufe kommen von Skripten. Echte Aufrufe auf einem neuen Upload kommen von Menschen, die ihn in ihrem Feed oder in den Empfehlungen sehen, und unsere Aufgabe ist, diese Gruppe wachsen zu lassen."),
            ("Können Sie meine Premiere mit Live-Zuschauern füllen?", "Echte Menschen zu einer bestimmten Minute kann niemand versprechen. Wenn Sie vor einer Premiere echte Abonnenten gewinnen, haben Sie mehr Menschen, die vielleicht einschalten."),
            ("Werden Aufrufe in meinem Paket gezählt?", "Sie sind darin enthalten, ohne feste Zahl. Dieselben Menschen, die abonnieren, liken und kommentieren, schauen auch zu, also folgen die Aufrufe Ihrem Publikum."),
            ("Welches Paket bringt die meisten Aufrufe?", "Wir bemessen Pakete nicht nach Aufrufen. Ein größeres Paket erreicht mehr Menschen, also heißt {pro_name} mit typischerweise {pro_audience} neuen Abonnenten im Monat meist, dass mehr Menschen zuschauen."),
        ],
    },
    {
        "service": "views",
        "modifier": "free",
        "slug": "youtube/aufrufe/kostenlos",
        "label": "Kostenlose YouTube-Aufrufe?",
        "plan": "starter",
        "tool": "engagement-calculator",
        "title": "1.000 YouTube-Views kostenlos? Warum sie nicht helfen | Growsterr",
        "description": "Kostenlose YouTube-Views, auch für Shorts, kommen aus Tauschbörsen und Skripten. Wir verschenken keine; prüfen Sie Ihr Engagement mit dem Gratis-Rechner.",
        "h1": ("1.000 kostenlose YouTube-Views ", "sehen Ihr Video nicht an. Echte Menschen schon."),
        "intro": "Angebote für 1.000 kostenlose YouTube-Views oder Gratis-Aufrufe für Shorts laufen über Aufruf-Tauschbörsen, Autoplay-Tricks oder Bot-Wiedergaben, und keines davon bringt jemanden, der zuschaut. Wir verschenken keine Aufrufe. Der Engagement-Rechner unten kostet nichts und zeigt, welcher Anteil Ihrer Abonnenten auf ein typisches Video reagiert. Sollen mehr echte Menschen zuschauen, bringen unsere Pakete sie.",
        "hero": {"image": "youtube-channel", "alt": "Ein YouTuber prüft Likes und Kommentare seiner letzten Videos"},
        "sections": [
            {
                "h2": "Woher Gratis-Aufrufe kommen",
                "ul": [
                    "Aufruf-Tauschbörsen: Sie sehen Videos Fremder für Credits, und die spielen Ihre stumm ab.",
                    "Einbettungen und Autoplay-Tricks, die eine Wiedergabe zählen, die niemand gewählt hat.",
                    "Bot-Wiedergaben in kleinen Portionen, die Ihnen größere verkaufen sollen.",
                    "Gratis-Aufrufe für Shorts von Skripten, die nach einer Sekunde weiterwischen.",
                ],
            },
            {
                "h2": "Prüfen Sie Ihr Engagement mit dem Rechner",
                "p": [
                    "Dieser Rechner läuft komplett in Ihrem Browser, ohne Kosten. Wo er nach Followern fragt, tragen Sie Ihre Abonnenten ein, dann die durchschnittlichen Likes und Kommentare Ihrer letzten Videos. Das Ergebnis ist der Anteil Ihres Publikums, der reagiert, ein weit besserer Gesundheitscheck als eine Aufrufzahl.",
                ],
            },
            {
                "h2": "Kostenlose Wege zu mehr Aufrufen",
                "ul": [
                    "Investieren Sie in Titel und Thumbnail so viel Zeit wie in den Schnitt; sie entscheiden über den Klick.",
                    "Kommen Sie in den ersten Sekunden eines Videos oder Shorts zum Punkt.",
                    "Fügen Sie Endbildschirme und Playlists hinzu, damit ein Aufruf zum nächsten führt.",
                    "Antworten Sie auf Kommentare; Menschen kommen zu Gesprächen zurück.",
                ],
            },
        ],
        "faqs": [
            ("Kann ich 1.000 YouTube-Aufrufe kostenlos bekommen?", "Nicht von echten Menschen und nicht von uns. Tausend Gratis-Aufrufe kommen aus Tauschbörsen oder von Skripten. Der Rechner auf dieser Seite ist das, was wirklich kostenlos ist."),
            ("Sind Gratis-Aufrufe für Shorts anders?", "Nein. Sie kommen aus denselben Tricks. Ein Short verbreitet sich nur, wenn echte Menschen ihn zu Ende sehen, Wiedergaben von Skripten helfen ihm also nicht."),
            ("Können Gratis-Aufrufe meinem Kanal Strafen einbringen?", "Das Risiko ist real. Aufrufe aus automatisierten Systemen oder Tauschbörsen fallen unter die Richtlinie von YouTube zu falschem Engagement, und YouTube kann sie entfernen oder gegen den Kanal vorgehen."),
            ("Haben Sie ein kostenloses Aufruf-Paket?", "Nein. Das kleinste Paket ist {starter_name} für {starter_price} im Monat, und Aufrufe sind darin enthalten, von den echten Menschen, die abonnieren."),
            ("Was sagt mir die Engagement-Rate?", "Wie viel Ihres Publikums wirklich da ist. Eine niedrige Rate bei hoher Abonnentenzahl heißt meist, dass viele Abonnenten nicht mehr zuschauen oder es nie getan haben."),
        ],
    },
    {
        "service": "views",
        "modifier": "free-trial",
        "slug": "youtube/aufrufe/kostenlos-testen",
        "label": "YouTube-Aufrufe kostenlos testen?",
        "plan": "starter",
        "title": "YouTube-Views gratis testen? Prüfen Sie uns richtig | Growsterr",
        "description": "Einen Gratis-Test für YouTube-Views gibt es nicht, und Aufrufe verkaufen wir nie allein. Testen Sie uns einen Monat lang, mit den Analysen von YouTube.",
        "h1": ("Ein Test mit YouTube-Views ", "beweist nur, dass sich ein Zähler bewegt."),
        "intro": "Sie hoffen, YouTube-Views erst kostenlos zu testen, bevor Sie etwas zahlen? Einen Test gibt es hier nicht, und Aufrufe werden auch nie einzeln verkauft. Ein Test mit ein paar Tausend Aufrufen in einer Stunde würde nur zeigen, dass jemand Skripte hat. Wir bieten ein Monatspaket, das echte Menschen auf Ihren Kanal bringt, Aufrufe derselben Menschen inklusive, und Sie können jederzeit kündigen.",
        "hero": {"image": "youtube-hub", "alt": "Ein Creator vergleicht die YouTube-Analysen mit einem Wachstums-Dashboard"},
        "sections": [
            {
                "h2": "Was ein Aufruf-Test misst",
                "p": [
                    "Eines: ob sich die Zahl bewegt. Er sagt nichts darüber, wer geschaut hat, wie lange oder ob jemand wiederkam. Genau das sind die Fragen, die zählen, und beantworten können sie nur echte Zuschauer.",
                ],
            },
            {
                "h2": "Testen Sie uns mit den Zahlen von YouTube",
                "p": [
                    "Öffnen Sie in Ihrem ersten Monat YouTube Studio neben unserem Dashboard. Schauen Sie auf wiederkehrende Zuschauer, durchschnittliche Wiedergabedauer und neue Abonnenten. Echte Menschen hinterlassen in diesen Zahlen eine Spur, die gekaufte Wiedergaben nie hinterlassen.",
                ],
            },
        ],
        "faqs": [
            ("Gibt es einen Test für YouTube-Aufrufe?", "Keine Tests, weder für Aufrufe noch für sonst etwas. Die kürzeste Bindung ist ein Monat eines Pakets, und Sie können kündigen, bevor er sich verlängert."),
            ("Kann ich ein kleines Aufruf-Paket zum Testen kaufen?", "Aufrufe verkaufen wir nicht als eigenes Paket, weder klein noch groß. {starter_name} für {starter_price} im Monat ist der kleinste Einstieg."),
            ("Woran erkenne ich echte Aufrufe im Vergleich zu gekauften?", "Schauen Sie über die Zahl hinaus: Wiedergabezeit, wiederkehrende Zuschauer und die Kommentare, die Menschen schreiben, zeigen, wer wirklich da ist."),
            ("Was, wenn ich nach dem ersten Monat kündige?", "Ihr Paket endet mit dem bezahlten Monat. Zuschauer, die abonniert haben, bleiben abonniert, solange sie nicht selbst gehen."),
            ("Kommen Aufrufe mit Abonnenten?", "Ja. Jedes Paket bringt neue Abonnenten, Likes und Kommentare, und dieselben Menschen sehen sich Ihre Videos an."),
        ],
    },
]
