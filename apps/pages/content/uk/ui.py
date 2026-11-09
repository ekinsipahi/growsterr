"""Ukrainian UI of the money pages: section titles and the blocks every page shares (mirrors en/ui.py).

Word forms, chosen once and written around everywhere:
    {audience} genitive plural ("нових {audience}", "більше {audience}"), the same on every platform
    {follow} an infinitive ("вирішили {follow}") · {profile} профіль/канал, nominative = accusative
    {handle} nominative = accusative · {content} plural, nominative = accusative ("ваші {content}")
    {service} the counting form after a number ("{quantity} {service}": 1 000 підписників)
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "підписників", "tiktok": "підписників", "youtube": "підписників"},
    "follow": {"instagram": "підписатися", "tiktok": "підписатися", "youtube": "підписатися"},
    "profile": {"instagram": "профіль", "tiktok": "профіль", "youtube": "канал"},
    "handle": {"instagram": "ім'я користувача", "tiktok": "ім'я користувача", "youtube": "псевдонім каналу"},
    "content": {"instagram": "публікації", "tiktok": "відео", "youtube": "відео"},
    "service_names": {"followers": "Підписники", "subscribers": "Підписники", "likes": "Лайки",
                      "views": "Перегляди", "comments": "Коментарі"},
    "service_words": {"followers": "підписників", "subscribers": "підписників", "likes": "лайків",
                      "views": "переглядів", "comments": "коментарів"},

    # Page chrome
    "home": "Головна",
    "crumbs_label": "Навігаційний ланцюжок",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "Зростання в {platform}",
    "cta": "Почати з {pick_name}",
    "cta_more": "Усі пакети",
    "trust": ["Живі люди, ніколи не боти", "Ми ніколи не просимо ваш пароль", "Щомісяця, скасування будь-коли"],
    "product_name": "Пакети зростання {platform}",
    "sticky_cta": "Почати",

    # Packages
    "packages_title": "Оберіть свій пакет",
    "packages_lead": "Три щомісячні пакети. Кожен приносить нових {audience}, лайки, перегляди й коментарі — від тих самих живих людей.",
    "packages_note": "Типові місячні діапазони, а не фіксована кількість: кожен із ваших нових {audience} — жива людина, яка сама вирішила {follow}, тож кожен місяць трохи інший.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "Що входить",
    "included_lead": "Кожен пакет дає повну картину — від тих самих живих людей.",
    "included_items": {
        "audience": ("Більше {audience}", "Живі люди, які знайшли ваш {profile} і самі вирішили {follow}. Зазвичай {starter_audience} на місяць із {starter_name}."),
        "likes": ("Лайки від тих самих людей", "Зазвичай {starter_likes} на місяць із {starter_name}: люди лайкають ваші {content}, які їм до вподоби."),
        "comments": ("Коментарі їхніми словами", "Зазвичай {starter_comments} на місяць із {starter_name}. Їх пишуть люди, а не скрипти."),
        "views": ("Перегляди разом з усім іншим", "Ті самі люди самі переглядають ваші {content}. Ми не рахуємо перегляди наперед: за кожним стоїть людина."),
        "days": ("Розподілено на 30 днів", "Потроху щодня, з обраного вами місця. Ніколи не все одразу."),
        "dashboard": ("Ваша панель статистики", "Що ми виміряли, день за днем: візити з вашої кампанії та нових {audience}, яких вони привели."),
    },

    # How it works: the subscription, step by step
    "steps_title": "Як це працює",
    "steps_lead": "Щомісячна підписка: ви обираєте пакет, ми запускаємо кампанію, а вирішують живі люди.",
    "steps": [
        ("Оберіть пакет", "{starter_name}, {rising_name} або {pro_name}, оплата щомісяця. Скасувати можна будь-коли у вашому акаунті."),
        ("Ми запускаємо вашу кампанію", "Вкажіть {handle} в {platform} і звідки має бути ваша аудиторія. Пароль ми ніколи не просимо."),
        ("Живі люди знаходять ваш {profile}", "Щодня ваш {profile} бачать живі люди. Ті, кому подобається побачене, самі вирішують {follow}, лайкнути й прокоментувати."),
        ("Панель показує, що ми виміряли", "Візити з вашої кампанії та нових {audience}, яких вони привели, день за днем. Виміряні цифри, а не здогадки."),
    ],

    # Real people vs bots / instant
    "compare_title": "Живі люди, а не боти",
    "compare_lead": "«Миттєво» означає боти: жодна жива людина не вирішує {follow} за кілька секунд після оплати.",
    "compare_cols": ("Що змінюється", "Миттєві сервіси й боти", "Growsterr"),
    "compare": [
        ("Хто вони", "Боти й фейкові профілі", "Живі люди, які самі вирішили {follow}"),
        ("Швидкість", "Тисячі за хвилини", "Потроху щодня, увесь місяць"),
        ("Лайки й коментарі", "Продаються окремо, від іще більшої кількості ботів", "Від тих самих людей, у межах вашого пакета"),
        ("Ваше охоплення", "Тихо падає: аудиторія, яка ніколи не реагує, підказує {platform}, що ваші {content} не варто показувати", "Зростає разом із людьми, які дивляться, лайкають і повертаються"),
        ("Ваш пароль", "Часто просять", "Ніколи"),
        ("Що ви бачите", "Цифра, що може зникнути після наступного чищення", "Панель із тим, що ми виміряли"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "Як дійти до {quantity} {service}",
    "quantity_lead": "Ми не продаємо {quantity} одним махом. Живі люди вирішують самі, тож щомісячний пакет доводить вас до мети в природному темпі.",
    "pace_title": "Типовий темп із {pick_name}",
    "pace_month": "Місяць {n}",
    "pace_goal": "Мета: {quantity}",
    "pace_note": "Типові діапазони з того, що роблять живі люди, а не обіцянка. Одні місяці приносять більше, інші менше.",
    "by_plan_title": "Скільки часу до {quantity}: за пакетами",
    "a_month": "{range} на місяць",
    "when_first": "зазвичай уже в перший місяць",
    "when_about": "зазвичай близько {n} місяців",
    "when_range": "зазвичай від {low} до {high} місяців",
    "views_pace": "Перегляди приходять від тих самих живих людей, які знаходять ваш {profile}, тому ми не рахуємо їх наперед. {pick_name} — пакет, який найкраще підходить для цієї мети.",

    # FAQ, related pages, closing
    "faq_title": "Запитання й відповіді",
    "related_title": "Дивіться також",
    "related": {
        "platform": "Більше про {platform}",
        "platforms": "На інших платформах",
        "quantities": "Інші цілі",
        "modifiers": "Інші способи зростати",
        "articles": "Читайте далі",
        "hubs": "Зростайте з живими людьми в",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "Порахувати",
        "followers": "Підписники",
        "avg_likes": "Середня кількість лайків на публікацію",
        "avg_comments": "Середня кількість коментарів на публікацію",
        "engagement_title": "Ваш рівень залученості",
        "engagement_lead": "Яка частка ваших підписників реагує на типову публікацію. Введіть цифри з кількох останніх публікацій.",
        "engagement_result": "Ваш рівень залученості — {rate}%.",
        "engagement_note": "Рівень зростає, коли вашим підписникам справді цікаві ваші публікації. Підписники, які ніколи не реагують, знижують його, хоч би скільки їх було.",
        "growth_title": "Скільки часу до вашої мети?",
        "growth_lead": "Вкажіть, де ви зараз і куди хочете дійти. Ми порахуємо це за типовим місячним діапазоном кожного пакета.",
        "current": "Підписників сьогодні",
        "goal": "Ваша мета",
        "when_first": "зазвичай уже в перший місяць",
        "when_range": "зазвичай від {low} до {high} місяців",
        "when_about": "близько {n} місяців",
        "reached": "Ви вже досягли мети.",
        "growth_note": "Типові діапазони, а не обіцянка: живі люди самі вирішують, чи підписуватися.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "Гайд",
        "alternative": "Порівняння",
        "payment": "Оплата",
        "agency": "Агенція зростання",
        "tool": "Інструмент",
        "intent": "Пряма відповідь",
    },
    "cta_title": "Готові зростати в {platform}?",
    "cta_text": "Оберіть пакет, і ми запустимо вашу кампанію. Решту вирішують живі люди, а ваша панель показує, що ми виміряли.",

    # Platform hubs
    "services_title": "Що ми розвиваємо в {platform}",
    "services_lead": "Один пакет дає все це — від тих самих живих людей.",
    "teasers": {
        "audience": "Живі люди, які знаходять ваш {profile} і самі вирішують {follow}.",
        "likes": "Лайки від людей, яким подобаються ваші {content}.",
        "views": "Перегляди від людей, які самі вирішили подивитися, а не від скриптів.",
        "comments": "Коментарі, написані живими людьми, власними словами.",
    },
    "explore": "Переглянути",
    "in_package": "У кожному пакеті",
    "goals_title": "Більше способів зростати в {platform}",
    "other_hubs_title": "Ми також розвиваємо",
}
