"""Arabic (Modern Standard, RTL) UI of the money pages (mirrors en/ui.py key by key).

{audience} is the oblique plural (متابعين/مشتركين): it takes ال (المتابعين) and follows
prepositions. {service} is the singular that follows a number (1000 متابع). {follow} is the
verbal noun (المتابعة/الاشتراك), {profile} and {content} carry the possessive (ملفك الشخصي).
"""

UI = {
    # Words that change with the platform or the service
    "audience": {"instagram": "متابعين", "tiktok": "متابعين", "youtube": "مشتركين"},
    "follow": {"instagram": "المتابعة", "tiktok": "المتابعة", "youtube": "الاشتراك"},
    "profile": {"instagram": "ملفك الشخصي", "tiktok": "ملفك الشخصي", "youtube": "قناتك"},
    "handle": {"instagram": "اسم المستخدم", "tiktok": "اسم المستخدم", "youtube": "معرّف القناة"},
    "content": {"instagram": "منشوراتك", "tiktok": "فيديوهاتك", "youtube": "فيديوهاتك"},
    "service_names": {"followers": "المتابعون", "subscribers": "المشتركون", "likes": "الإعجابات",
                      "views": "المشاهدات", "comments": "التعليقات"},
    "service_words": {"followers": "متابع", "subscribers": "مشترك", "likes": "إعجاب",
                      "views": "مشاهدة", "comments": "تعليق"},

    # Page chrome
    "home": "الرئيسية",
    "crumbs_label": "مسار التنقل",
    "eyebrow": "{platform} · {service_name}",
    "eyebrow_hub": "النمو على {platform}",
    "cta": "ابدأ بباقة {pick_name}",
    "cta_more": "عرض كل الباقات",
    "trust": ["أشخاص حقيقيون، لا بوتات", "لا نطلب كلمة المرور أبدًا", "اشتراك شهري، ألغِ متى شئت"],
    "product_name": "باقات النمو على {platform}",
    "sticky_cta": "ابدأ",

    # Packages
    "packages_title": "اختر باقتك",
    "packages_lead": "ثلاث باقات شهرية تجلب لك {audience} جددًا وإعجابات ومشاهدات وتعليقات معًا، من الأشخاص الحقيقيين أنفسهم.",
    "packages_note": "نطاقات شهرية معتادة، لا عدد ثابت: كل واحد من ال{audience} الجدد شخص حقيقي اختار {follow}، لذلك يختلف كل شهر قليلًا عن غيره.",

    # What's included: the page's own service comes first, then the rest in this order.
    "included_title": "ما الذي تتضمنه الباقة",
    "included_lead": "كل باقة تقدّم الصورة كاملة، من الأشخاص الحقيقيين أنفسهم.",
    "included_items": {
        "audience": ("مزيد من ال{audience}", "أشخاص حقيقيون اكتشفوا {profile} واختاروا {follow}. عادةً {starter_audience} شهريًا مع {starter_name}."),
        "likes": ("إعجابات من الأشخاص أنفسهم", "عادةً {starter_likes} شهريًا مع {starter_name}، على {content} التي تعجبهم."),
        "comments": ("تعليقات بكلماتهم الخاصة", "عادةً {starter_comments} شهريًا مع {starter_name}. يكتبها أشخاص، ولا تأتي من نصوص جاهزة أبدًا."),
        "views": ("مشاهدات تأتي معها", "يشاهد الأشخاص أنفسهم {content} من تلقاء أنفسهم. لا نحسب المشاهدات مسبقًا: وراء كل مشاهدة شخص."),
        "days": ("موزعة على 30 يومًا", "قليلًا كل يوم، من الموقع الذي تختاره. لا شيء دفعة واحدة."),
        "dashboard": ("لوحة التحكم الخاصة بك", "ما قسناه يومًا بيوم: عدد الزيارات القادمة من حملتك وعدد ال{audience} الجدد الذين جلبتهم."),
    },

    # How it works: the subscription, step by step
    "steps_title": "كيف يعمل",
    "steps_lead": "اشتراك شهري: أنت تختار الباقة، ونحن ندير الحملة، والأشخاص الحقيقيون يقررون.",
    "steps": [
        ("اختر باقة", "{starter_name} أو {rising_name} أو {pro_name}، بفوترة شهرية. ألغِ متى شئت من حسابك."),
        ("نبدأ حملتك", "أرسل لنا {handle} على {platform} ومن أين تريد أن يأتي جمهورك. لا نطلب كلمة المرور أبدًا."),
        ("أشخاص حقيقيون يكتشفون {profile}", "كل يوم يُعرض {profile} على أشخاص حقيقيين، ومن يعجبه ما يراه يختار {follow} والإعجاب والتعليق بنفسه."),
        ("لوحة التحكم تعرض ما قسناه", "عدد الزيارات القادمة من حملتك وعدد ال{audience} الجدد الذين جلبتهم، يومًا بيوم. أرقام مقيسة، لا تخمينات."),
    ],

    # Real people vs bots / instant
    "compare_title": "أشخاص حقيقيون، لا بوتات",
    "compare_lead": "الفوري يعني بوتات: لا يختار أي شخص حقيقي {follow} بعد ثوانٍ من الدفع.",
    "compare_cols": ("ما الذي يتغير", "الخدمات الفورية والبوتات", "Growsterr"),
    "compare": [
        ("من هم", "بوتات وحسابات وهمية", "أشخاص حقيقيون اختاروا {follow}"),
        ("السرعة", "الآلاف خلال دقائق", "قليلًا كل يوم، طوال الشهر"),
        ("الإعجابات والتعليقات", "تُباع منفصلة، من مزيد من البوتات", "من الأشخاص أنفسهم، داخل باقتك"),
        ("وصولك", "يتراجع بصمت: جمهور لا يتفاعل أبدًا يُخبر {platform} أن {content} لا تستحق الظهور", "ينمو مع أشخاص يشاهدون ويعجبون ويعودون"),
        ("كلمة المرور", "تُطلب غالبًا", "أبدًا"),
        ("ما تراه", "رقم قد يختفي في حملة التنظيف التالية", "لوحة تحكم بما قسناه"),
    ],

    # Quantity pages: how a monthly package gets you to the goal
    "quantity_title": "كيف تصل إلى {quantity} {service}",
    "quantity_lead": "لا نبيع حزمة ثابتة من {quantity} {service}. الأشخاص الحقيقيون يقررون بأنفسهم، لذلك توصلك باقة شهرية إلى هدفك بوتيرة طبيعية.",
    "pace_title": "الوتيرة المعتادة مع {pick_name}",
    "pace_month": "الشهر {n}",
    "pace_goal": "الهدف: {quantity}",
    "pace_note": "نطاقات معتادة مبنية على ما يفعله الأشخاص الحقيقيون، وليست وعدًا أبدًا. بعض الأشهر تجلب أكثر، وبعضها أقل.",
    "by_plan_title": "المدة حتى {quantity} حسب الباقة",
    "a_month": "{range} شهريًا",
    "when_first": "عادةً خلال الشهر الأول",
    "when_about": "عادةً نحو {n} أشهر",
    "when_range": "عادةً {low}–{high} أشهر",
    "views_pace": "تأتي المشاهدات من الأشخاص الحقيقيين أنفسهم الذين يكتشفون {profile}، لذلك لا نحسبها مسبقًا. باقة {pick_name} هي الأنسب لهذا الهدف.",

    # FAQ, related pages, closing
    "faq_title": "أسئلة وأجوبة",
    "related_title": "واصل الاستكشاف",
    "related": {
        "platform": "المزيد عن {platform}",
        "platforms": "على منصات أخرى",
        "quantities": "أهداف أخرى",
        "modifiers": "طرق أخرى للنمو",
        "articles": "اقرأ أيضًا",
        "hubs": "انمُ مع أشخاص حقيقيين على",
    },
    # The tools a page can carry ("tool"): they run in the browser, nothing is sent.
    "tools": {
        "calculate": "احسب",
        "followers": "عدد المتابعين",
        "avg_likes": "متوسط الإعجابات لكل منشور",
        "avg_comments": "متوسط التعليقات لكل منشور",
        "engagement_title": "معدل تفاعلك",
        "engagement_lead": "كم من متابعيك يتفاعلون مع منشور عادي؟ أدخل أرقام آخر بضعة منشورات.",
        "engagement_result": "معدل تفاعلك هو {rate}%.",
        "engagement_note": "يرتفع المعدل عندما يهتم من يتابعونك بمنشوراتك فعلًا. أما المتابعون الذين لا يتفاعلون أبدًا فيخفضونه، مهما كان عددهم.",
        "growth_title": "كم يستغرق الوصول إلى هدفك؟",
        "growth_lead": "أدخل أين أنت الآن وأين تريد أن تصل. نحسب ذلك من النطاق الشهري المعتاد لكل باقة.",
        "current": "عدد متابعيك اليوم",
        "goal": "هدفك",
        "when_first": "عادةً خلال الشهر الأول",
        "when_range": "عادةً {low}–{high} أشهر",
        "when_about": "نحو {n} أشهر",
        "reached": "لقد وصلت إلى هدفك بالفعل.",
        "growth_note": "نطاقات معتادة، لا وعود: الأشخاص الحقيقيون يقررون بأنفسهم إن كانوا سيتابعونك.",
    },
    # Eyebrow above the headline of pages outside the platform x service grid (by "kind").
    "article_eyebrows": {
        "guide": "دليل",
        "alternative": "مقارنة",
        "payment": "الدفع",
        "agency": "وكالة نمو",
        "tool": "أداة",
        "intent": "إجابة صريحة",
    },
    "cta_title": "مستعد للنمو على {platform}؟",
    "cta_text": "اختر باقة ونبدأ حملتك. الأشخاص الحقيقيون يقررون الباقي، ولوحة التحكم تعرض ما قسناه.",

    # Platform hubs
    "services_title": "ما الذي ننمّيه على {platform}",
    "services_lead": "باقة واحدة تجلب كل ذلك، من الأشخاص الحقيقيين أنفسهم.",
    "teasers": {
        "audience": "أشخاص حقيقيون يكتشفون {profile} ويختارون {follow}.",
        "likes": "إعجابات من أشخاص تعجبهم {content}.",
        "views": "مشاهدات من أشخاص يختارون المشاهدة، لا من برامج آلية أبدًا.",
        "comments": "تعليقات يكتبها أشخاص حقيقيون بكلماتهم الخاصة.",
    },
    "explore": "استكشف",
    "in_package": "في كل باقة",
    "goals_title": "طرق أخرى للنمو على {platform}",
    "other_hubs_title": "ننمّي حسابك أيضًا على",
}
