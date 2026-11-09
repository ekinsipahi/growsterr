"""Belarusian UI of the money pages: section titles and the blocks every page shares (mirrors en/ui.py).

Word forms, chosen once and written around everywhere:
    {audience} genitive plural ("новых {audience}", "больш {audience}"), the same on every platform
    {follow} an infinitive ("вырашылі {follow}") · {profile} профіль/канал, nominative = accusative
    {handle} nominative = accusative, ends in a vowel ("{handle} ў {platform}")
    {content} plural, nominative = accusative ("вашы {content}")
    {service} the counting form after a number ("{quantity} {service}": 1000 падпісчыкаў)
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "падпісчыкаў", "tiktok": "падпісчыкаў", "youtube": "падпісчыкаў"},
    "follow": {"instagram": "падпісацца", "tiktok": "падпісацца", "youtube": "падпісацца"},
    "profile": {"instagram": "профіль", "tiktok": "профіль", "youtube": "канал"},
    "handle": {"instagram": "імя карыстальніка", "tiktok": "імя карыстальніка", "youtube": "псеўданім канала"},
    "content": {"instagram": "публікацыі", "tiktok": "відэа", "youtube": "відэа"},
    "service_names": {"followers": "Падпісчыкі", "subscribers": "Падпісчыкі", "likes": "Лайкі",
                      "views": "Прагляды", "comments": "Каментары"},
    "service_words": {"followers": "падпісчыкаў", "subscribers": "падпісчыкаў", "likes": "лайкаў",
                      "views": "праглядаў", "comments": "каментароў"},

    # Page chrome
    "home": "Галоўная",
    "crumbs_label": "Навігацыйны ланцужок",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Рост у {platform}",
    "cta": "Пачаць з {pick_name}",
    "cta_more": "Усе пакеты",
    "trust": ["Жывыя людзі, ніколі не боты", "Мы ніколі не просім ваш пароль", "Штомесяц, скасаванне ў любы момант"],
    "product_name": "Пакеты росту для {platform}",
    "sticky_cta": "Пачаць",

    # Packages
    "packages_title": "Выберыце свой пакет",
    "packages_lead": "Тры штомесячныя пакеты. Кожны прыносіць новых {audience}, лайкі, прагляды і каментары — ад тых жа жывых людзей.",
    "packages_note": "Тыповыя месячныя дыяпазоны, а не фіксаваная колькасць: кожны з вашых новых {audience} — жывы чалавек, які сам вырашыў {follow}, таму кожны месяц крыху іншы.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Што ўваходзіць",
    "included_lead": "Кожны пакет дае поўную карціну — ад тых жа жывых людзей.",
    "included_items": {
        "audience": ("Больш {audience}", "Жывыя людзі, якія знайшлі ваш {profile} і самі вырашылі {follow}. Звычайна {starter_audience} за месяц з пакетам {starter_name}."),
        "likes": ("Лайкі ад тых жа людзей", "Звычайна {starter_likes} за месяц з пакетам {starter_name}: лайкі атрымліваюць вашы {content}, якія спадабаліся людзям."),
        "comments": ("Каментары іх уласнымі словамі", "Звычайна {starter_comments} за месяц з пакетам {starter_name}. Іх пішуць людзі, а не скрыпты."),
        "views": ("Прагляды разам з усім астатнім", "Тыя ж людзі самі глядзяць вашы {content}. Мы не лічым прагляды наперад: за кожным стаіць чалавек."),
        "days": ("Размеркавана на 30 дзён", "Патроху кожны дзень, з выбранага вамі месца. Ніколі не ўсё адразу."),
        "dashboard": ("Ваша панэль статыстыкі", "Што мы вымералі, дзень за днём: колькасць наведванняў з вашай кампаніі і новых {audience}, якіх яны прывялі."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Як гэта працуе",
    "steps_lead": "Штомесячная падпіска: вы выбіраеце пакет, мы запускаем кампанію, а вырашаюць жывыя людзі.",
    "steps": [
        ("Выберыце пакет", "{starter_name}, {rising_name} або {pro_name}, з аплатай раз на месяц. Скасаваць можна ў любы момант у вашым акаўнце."),
        ("Мы запускаем вашу кампанію", "Скажыце нам {handle} ў {platform} і адкуль павінна прыходзіць ваша аўдыторыя. Пароль мы ніколі не просім."),
        ("Жывыя людзі знаходзяць ваш {profile}", "Кожны дзень ваш {profile} бачаць жывыя людзі. Тыя, каму спадабалася ўбачанае, самі вырашаюць {follow}, паставіць лайк і пракаментаваць."),
        ("Панэль паказвае, што мы вымералі", "Колькасць наведванняў з вашай кампаніі і новых {audience}, якіх яны прывялі, дзень за днём. Вымераныя лічбы, а не здагадкі."),
    ],

    # Real people vs bots / instant
    "compare_title": "Жывыя людзі, а не боты",
    "compare_lead": "«Імгненна» азначае боты: ніводзін жывы чалавек не вырашае {follow} праз секунды пасля аплаты.",
    "compare_cols": ("Што мяняецца", "Імгненныя сэрвісы і боты", "Growsterr"),
    "compare": [
        ("Хто яны", "Боты і фэйкавыя профілі", "Жывыя людзі, якія самі вырашылі {follow}"),
        ("Хуткасць", "Тысячы за хвіліны", "Патроху кожны дзень, увесь месяц"),
        ("Лайкі і каментары", "Прадаюцца асобна, ад яшчэ большай колькасці ботаў", "Ад тых жа людзей, у межах вашага пакета"),
        ("Ваш ахоп", "Ціха падае: аўдыторыя, якая ніколі не рэагуе, падказвае {platform}, што вашы {content} не варта паказваць", "Расце разам з людзьмі, якія глядзяць, ставяць лайкі і вяртаюцца"),
        ("Ваш пароль", "Часта просяць", "Ніколі"),
        ("Што вы бачыце", "Лічба, якая можа знікнуць пасля наступнай чысткі", "Панэль з тым, што мы вымералі"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Як дайсці да {quantity} {service}",
    "quantity_lead": "Мы не прадаём {quantity} адным махам. Жывыя людзі вырашаюць самі, таму штомесячны пакет даводзіць вас да мэты ў натуральным тэмпе.",
    "pace_title": "Тыповы тэмп з пакетам {pick_name}",
    "pace_month": "Месяц {n}",
    "pace_goal": "Мэта: {quantity}",
    "pace_note": "Тыповыя дыяпазоны паводле таго, што робяць жывыя людзі, а не абяцанне. Адны месяцы прыносяць больш, іншыя менш.",
    "by_plan_title": "Колькі часу да {quantity}: па пакетах",
    "a_month": "{range} за месяц",
    "when_first": "звычайна ўжо ў першы месяц",
    "when_about": "звычайна каля {n} месяцаў",
    "when_range": "звычайна ад {low} да {high} месяцаў",
    "views_pace": "Прагляды прыходзяць ад тых жа жывых людзей, якія знаходзяць ваш {profile}, таму мы не лічым іх наперад. Пакет {pick_name} лепш за ўсё падыходзіць для гэтай мэты.",

    # FAQ, related pages, closing
    "faq_title": "Пытанні і адказы",
    "related_title": "Глядзіце таксама",
    "related": {
        "platform": "Больш пра {platform}",
        "platforms": "На іншых платформах",
        "quantities": "Іншыя мэты",
        "modifiers": "Іншыя спосабы расці",
        "articles": "Чытайце далей",
        "hubs": "Расціце з жывымі людзьмі ў",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Разлічыць",
        "followers": "Падпісчыкі",
        "avg_likes": "Сярэдняя колькасць лайкаў на публікацыю",
        "avg_comments": "Сярэдняя колькасць каментароў на публікацыю",
        "engagement_title": "Ваш узровень залучанасці",
        "engagement_lead": "Колькі вашых падпісчыкаў рэагуе на звычайную публікацыю. Увядзіце лічбы з некалькіх апошніх публікацый.",
        "engagement_result": "Ваш узровень залучанасці — {rate}%.",
        "engagement_note": "Узровень расце, калі людзям, якія на вас падпісаны, сапраўды цікавыя вашы публікацыі. Падпісчыкі, якія ніколі не рэагуюць, яго зніжаюць, колькі б іх ні было.",
        "growth_title": "Колькі часу да вашай мэты?",
        "growth_lead": "Увядзіце, дзе вы зараз і куды хочаце дайсці. Мы разлічым гэта паводле тыповага месячнага дыяпазону кожнага пакета.",
        "current": "Падпісчыкаў сёння",
        "goal": "Ваша мэта",
        "when_first": "звычайна ўжо ў першы месяц",
        "when_range": "звычайна ад {low} да {high} месяцаў",
        "when_about": "каля {n} месяцаў",
        "reached": "Вы ўжо дасягнулі мэты.",
        "growth_note": "Тыповыя дыяпазоны, а не абяцанне: жывыя людзі самі вырашаюць, ці падпісвацца.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Гайд",
        "alternative": "Параўнанне",
        "payment": "Аплата",
        "agency": "Агенцтва росту",
        "tool": "Інструмент",
        "intent": "Шчыры адказ",
    },
    "cta_title": "Гатовыя расці ў {platform}?",
    "cta_text": "Выберыце пакет, і мы запусцім вашу кампанію. Астатняе вырашаюць жывыя людзі, а ваша панэль паказвае, што мы вымералі.",

    # Platform hubs
    "services_title": "Што мы развіваем у {platform}",
    "services_lead": "Адзін пакет дае ўсё гэта — ад тых жа жывых людзей.",
    "teasers": {
        "audience": "Жывыя людзі, якія знаходзяць ваш {profile} і вырашаюць {follow}.",
        "likes": "Лайкі ад людзей, якім падабаюцца вашы {content}.",
        "views": "Прагляды ад людзей, якія самі вырашаюць паглядзець, а не ад скрыптоў.",
        "comments": "Каментары, напісаныя жывымі людзьмі, іх уласнымі словамі.",
    },
    "explore": "Падрабязней",
    "in_package": "У кожным пакеце",
    "goals_title": "Больш спосабаў расці ў {platform}",
    "other_hubs_title": "Мы таксама развіваем",
}
