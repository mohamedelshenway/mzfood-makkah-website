# -*- coding: utf-8 -*-
"""
MZ FOOD — single source of truth for site content (RU authoritative, EN/AR translated).
Only real, verified facts. Anything not confirmed is marked NEEDS_CONFIRMATION and
rendered as an honest "ask on WhatsApp" placeholder instead of invented data.
"""

BASE_URL = "https://mohamedelshenway.github.io/mzfood-makkah-website"
BASE_PATH = "/mzfood-makkah-website"  # GitHub Pages project-site prefix

LANGS = ["ru", "en", "ar"]
DEFAULT_LANG = "ru"

LANG_META = {
    "ru": {"dir": "ltr", "html_lang": "ru", "label": "Русский", "short": "RU"},
    "en": {"dir": "ltr", "html_lang": "en", "label": "English", "short": "EN"},
    "ar": {"dir": "rtl", "html_lang": "ar", "label": "العربية", "short": "AR"},
}

# RU keeps its existing, already-indexed slugs. EN/AR use latin slugs for consistency.
SLUGS = {
    "home":        {"ru": "",            "en": "",             "ar": ""},
    "menu":        {"ru": "menu",        "en": "menu",         "ar": "menu"},
    "about":       {"ru": "o-nas",       "en": "about",        "ar": "about"},
    "delivery":    {"ru": "dostavka",    "en": "delivery",     "ar": "delivery"},
    "reviews":     {"ru": "otzyvy",      "en": "reviews",      "ar": "reviews"},
    "contacts":    {"ru": "kontakty",    "en": "contacts",     "ar": "contacts"},
    "lowcalories": {"ru": "low-calories","en": "low-calories", "ar": "low-calories"},
    # Non-branded SEO landing pages (added 15 Sep 2026) — for searchers who don't
    # know the MZ FOOD name yet and search by cuisine/dish instead. Not in main nav,
    # but included in sitemap/hreflang and cross-linked from Menu.
    "uzbek_cuisine": {"ru": "uzbekskaya-kuhnya-v-mekke", "en": "uzbek-food-makkah", "ar": "uzbek-food-makkah"},
    "plov":          {"ru": "plov-v-mekke",              "en": "plov-in-makkah",   "ar": "plov-in-makkah"},
}

PAGE_ORDER = ["home", "menu", "about", "delivery", "reviews", "contacts"]

CONTACT = {
    "phone_display": "+966 55 083 9208",
    "phone_tel": "+966550839208",
    "whatsapp_number": "966550839208",
    "email": "mzfoodksa@gmail.com",
    "instagram_url": "https://instagram.com/mzfoodksa",
    "instagram_handle": "@mzfoodksa",
    "maps_url": "https://www.google.com/maps/search/?api=1&query=MZ+Food+Makkah+Omran+Ibn+Hisn+St+Al+Zahir",
    # Address kept in Latin script consistently across all languages — this is the
    # verified real address as used on the live site and Google Business Profile.
    "address_line": "Omran Ibn Hisn St, Al Zahir, Makkah 24225",
    "address_country": {"ru": "Саудовская Аравия", "en": "Saudi Arabia", "ar": "المملكة العربية السعودية"},
}

NAV = {
    "home":     {"ru": "Главная",  "en": "Home",     "ar": "الرئيسية"},
    "menu":     {"ru": "Меню",     "en": "Menu",     "ar": "المنيو"},
    "about":    {"ru": "О нас",    "en": "About",    "ar": "من نحن"},
    "delivery": {"ru": "Доставка", "en": "Delivery", "ar": "التوصيل"},
    "reviews":  {"ru": "Отзывы",   "en": "Reviews",  "ar": "التقييمات"},
    "contacts": {"ru": "Контакты", "en": "Contacts", "ar": "تواصل"},
    "lowcalories": {"ru": "Low Calories", "en": "Low Calories", "ar": "Low Calories"},
    # Breadcrumb labels only — these two are not in PAGE_ORDER, so they don't appear in the main nav.
    "uzbek_cuisine": {"ru": "Узбекская кухня", "en": "Uzbek Cuisine", "ar": "المطبخ الأوزبكي"},
    "plov": {"ru": "Плов", "en": "Plov", "ar": "البلوف"},
}

CTA = {
    "order_whatsapp": {"ru": "Заказать в WhatsApp", "en": "Order on WhatsApp", "ar": "اطلب عبر واتساب"},
    "view_menu":       {"ru": "Смотреть меню",       "en": "View Menu",        "ar": "عرض المنيو"},
    "view_full_menu":  {"ru": "Всё меню и цены",     "en": "Full Menu & Prices","ar": "كل المنيو والأسعار"},
    "call":            {"ru": "Позвонить",           "en": "Call",             "ar": "اتصل بنا"},
    "read_more":       {"ru": "Подробнее",           "en": "Read more",        "ar": "المزيد"},
    "open_maps":       {"ru": "Открыть в Google Картах", "en": "Open in Google Maps", "ar": "فتح في خرائط جوجل"},
    "leave_review":    {"ru": "Оставить отзыв в Google", "en": "Leave a review on Google", "ar": "أضف تقييمك على جوجل"},
    "share_whatsapp":  {"ru": "Поделиться мнением в WhatsApp", "en": "Share feedback on WhatsApp", "ar": "شاركنا رأيك عبر واتساب"},
    "view_lowcal":     {"ru": "Посмотреть Low Calories", "en": "View Low Calories", "ar": "تعرف على Low Calories"},
    "discuss_partner":{"ru": "Обсудить сотрудничество", "en": "Discuss partnership", "ar": "تواصل للشراكة"},
}

WA_TEXT = {
    "general": {
        "ru": "Здравствуйте! У меня вопрос о MZ FOOD.",
        "en": "Hello! I have a question about MZ FOOD.",
        "ar": "مرحبًا! عندي سؤال عن MZ FOOD.",
    },
    "order": {
        "ru": "Здравствуйте! Хочу заказать еду в MZ FOOD.",
        "en": "Hello! I'd like to order food from MZ FOOD.",
        "ar": "مرحبًا! أرغب في طلب أكل من MZ FOOD.",
    },
    "partner": {
        "ru": "Здравствуйте! Я представляю отель/туристическую компанию, хочу обсудить сотрудничество с MZ FOOD.",
        "en": "Hello! I represent a hotel/tour company and would like to discuss a partnership with MZ FOOD.",
        "ar": "مرحبًا! أمثل فندقًا/شركة سياحية وأرغب في مناقشة تعاون مع MZ FOOD.",
    },
    "review": {
        "ru": "Здравствуйте! Хочу поделиться впечатлением о заказе в MZ FOOD.",
        "en": "Hello! I'd like to share my feedback about my MZ FOOD order.",
        "ar": "مرحبًا! أحب أشارككم رأيي في طلبي من MZ FOOD.",
    },
    "menu_word": {
        "ru": "Меню",
        "en": "Menu",
        "ar": "المنيو",
    },
    "lowcal": {
        "ru": "Здравствуйте! Хочу узнать про линейку Low Calories в MZ FOOD.",
        "en": "Hello! I'd like to know more about the Low Calories line at MZ FOOD.",
        "ar": "مرحبًا! أرغب أعرف أكتر عن خط Low Calories في MZ FOOD.",
    },
}

def wa_link(text_key):
    from urllib.parse import quote
    text = WA_TEXT[text_key]
    return {lang: f"https://wa.me/{CONTACT['whatsapp_number']}?text={quote(text[lang])}" for lang in LANGS}

def wa_link_dish(dish_name_by_lang, weight_by_lang, price_sar):
    """Pre-filled WhatsApp message for a specific dish order button."""
    from urllib.parse import quote
    templates = {
        "ru": "Здравствуйте! Хочу заказать: {name}{weight} — {price} SAR.",
        "en": "Hello! I'd like to order: {name}{weight} — {price} SAR.",
        "ar": "مرحبًا! أرغب أطلب: {name}{weight} — {price} ريال سعودي.",
    }
    out = {}
    for lang in LANGS:
        w = f" ({weight_by_lang[lang]})" if weight_by_lang.get(lang) else ""
        msg = templates[lang].format(name=dish_name_by_lang[lang], weight=w, price=price_sar)
        out[lang] = f"https://wa.me/{CONTACT['whatsapp_number']}?text={quote(msg)}"
    return out

SITE_TITLE = {"ru": "MZ FOOD", "en": "MZ FOOD", "ar": "MZ FOOD"}
TAGLINE = {"ru": "MAKKAH MADE", "en": "MAKKAH MADE", "ar": "MAKKAH MADE"}

# ---------------------------------------------------------------------------
# MENU — reconciled against the corrected Google Business Profile (14 Sep 2026).
# "Хычины с мясом" was confirmed removed from the real menu (wrong item) and is
# NOT included here. Two data conflicts between the old website and the current
# Google Business Profile are flagged below with NOTE — resolved using the GBP
# value (actively maintained by the owner) but must be confirmed by the client.
# ---------------------------------------------------------------------------
MENU_CATEGORIES = [
    {
        "key": "hot",
        "name": {"ru": "Горячие блюда", "en": "Hot Dishes", "ar": "أطباق ساخنة"},
        "items": [
            {"key": "borsch", "name": {"ru": "Борщ", "en": "Borscht", "ar": "بورش"},
             "weight": {"ru": "500 мл", "en": "500 ml", "ar": "500 مل"}, "price": 30},
            {"key": "lagman", "name": {"ru": "Лагман", "en": "Lagman", "ar": "لغمان"},
             "weight": {"ru": "500 мл", "en": "500 ml", "ar": "500 مل"}, "price": 35},
            {"key": "kotlety", "name": {"ru": "Котлеты с пюре", "en": "Meat Cutlets with Mashed Potato", "ar": "كفتة مع بيوريه بطاطس"},
             "weight": {"ru": "2 котлеты по 100 г + пюре 250 г", "en": "2 cutlets 100 g + mash 250 g", "ar": "قطعتان 100 جم + بيوريه 250 جم"}, "price": 35},
            {"key": "plov_govyadina", "name": {"ru": "Плов с говядиной", "en": "Beef Plov", "ar": "بلوف باللحم البقري"},
             "weight": {"ru": "450 г", "en": "450 g", "ar": "450 جم"}, "price": 35},
            {"key": "plov_sweet", "name": {"ru": "Сладкий плов с сухофруктами", "en": "Sweet Plov with Dried Fruit", "ar": "بلوف حلو بالفواكه المجففة"},
             "weight": {"ru": "400 г", "en": "400 g", "ar": "400 جم"}, "price": 30},
        ],
    },
    {
        "key": "bread",
        "name": {"ru": "Лепёшки и блины", "en": "Flatbreads & Pancakes", "ar": "أرغفة وفطائر"},
        "items": [
            {"key": "khychiny_syr", "name": {"ru": "Хычины с сыром", "en": "Khychiny with Cheese", "ar": "خيتشيني بالجبن"},
             "weight": {"ru": "", "en": "", "ar": ""}, "price": 25},
            {"key": "khingalsh", "name": {"ru": "Хингалш", "en": "Khingalsh", "ar": "خينغالش"},
             "weight": {"ru": "", "en": "", "ar": ""}, "price": 25,
             "note_ru": "На сайте раньше было указано «Хинкали» — уточнить у владельца точное название блюда."},
            {"key": "bliny_myaso", "name": {"ru": "Блины с мясом", "en": "Pancakes with Meat", "ar": "فطائر باللحم"},
             "weight": {"ru": "3 шт", "en": "3 pcs", "ar": "3 قطع"}, "price": 35,
             "note_ru": "На сайте раньше было указано «5 шт» — в Google Business указано «3 шт»; уточнить с владельцем."},
            {"key": "bliny_dzhem", "name": {"ru": "Блины с джемом", "en": "Pancakes with Jam", "ar": "فطائر بالمربى"},
             "weight": {"ru": "5 шт", "en": "5 pcs", "ar": "5 قطع"}, "price": 25},
            {"key": "bliny_smetana", "name": {"ru": "Блины со сметаной", "en": "Pancakes with Sour Cream", "ar": "فطائر بالقشدة الحامضة"},
             "weight": {"ru": "5 шт", "en": "5 pcs", "ar": "5 قطع"}, "price": 25},
        ],
    },
    {
        "key": "salads",
        "name": {"ru": "Салаты", "en": "Salads", "ar": "سلطات"},
        "items": [
            {"key": "vinegret", "name": {"ru": "Винегрет", "en": "Vinaigrette Salad", "ar": "سلطة فينيغريت"},
             "weight": {"ru": "350 г", "en": "350 g", "ar": "350 جم"}, "price": 25},
        ],
    },
    {
        "key": "drinks",
        "name": {"ru": "Напитки", "en": "Drinks", "ar": "مشروبات"},
        "items": [
            {"key": "kompot", "name": {"ru": "Компот из сухофруктов", "en": "Dried Fruit Compote", "ar": "كمبوت الفواكه المجففة"},
             "weight": {"ru": "1 л", "en": "1 L", "ar": "1 لتر"}, "price": 18},
        ],
    },
]

# Off-menu item with unconfirmed price — kept honest, not invented.
KUNAFA = {"ru": "Кунафа", "en": "Kunafa", "ar": "كنافة"}

# Popular dishes shown on the homepage (subset of the real menu above).
POPULAR_DISH_KEYS = ["borsch", "plov_govyadina", "lagman", "khychiny_syr", "khingalsh", "bliny_myaso"]

HERO = {
    "eyebrow": TAGLINE,
    "h1": {
        "ru": "Вкус дома в сердце Мекки",
        "en": "The taste of home in the heart of Makkah",
        "ar": "طعم البيت في قلب مكة",
    },
    "sub": {
        "ru": "Домашняя халяльная еда в Мекке для русскоязычных гостей, паломников и путешественников из России, Чечни, Кавказа и стран СНГ.",
        "en": "Home-style halal food in Makkah for Russian-speaking guests, pilgrims and travelers from Russia, Chechnya, the Caucasus and the CIS.",
        "ar": "أكل بيتي حلال في مكة المكرمة لضيوف روسيا والشيشان والقوقاز ودول رابطة الدول المستقلة، وحجاج ومعتمرين ناطقين بالروسية.",
    },
    "badges": {
        "makkah": {"ru": "Мекка", "en": "Makkah", "ar": "مكة"},
        "delivery": {"ru": "Доставка", "en": "Delivery", "ar": "توصيل"},
        "whatsapp": {"ru": "WhatsApp", "en": "WhatsApp", "ar": "واتساب"},
    },
}

WHY_MZFOOD = [
    {"icon": "home", "title": {"ru": "Знакомый вкус вдали от дома", "en": "A familiar taste far from home", "ar": "طعم مألوف بعيدًا عن البيت"},
     "text": {"ru": "Борщ, плов, хинкали, лагман — блюда, к которым вы привыкли.", "en": "Borscht, plov, khinkali, lagman — the dishes you already know.", "ar": "بورش، بلوف، خينكالي، لغمان — أطباق أنت متعود عليها."}},
    {"icon": "chef", "title": {"ru": "Готовим в Мекке", "en": "Cooked fresh in Makkah", "ar": "نطبخ في مكة"},
     "text": {"ru": "Halal-еда, приготовленная на месте, а не разогретые полуфабрикаты.", "en": "Halal food prepared here, not reheated ready-meals.", "ar": "أكل حلال يُحضّر في المكان، مش أكل جاهز مسخّن."}},
    {"icon": "truck", "title": {"ru": "Доставка", "en": "Delivery", "ar": "توصيل"},
     "text": {"ru": "По Мекке и в отели — заказ принимаем через WhatsApp.", "en": "Across Makkah and to hotels — order directly on WhatsApp.", "ar": "لكل مكة وللفنادق — الطلب مباشرة عبر واتساب."}},
    {"icon": "users", "title": {"ru": "Для гостей и паломников", "en": "For guests and pilgrims", "ar": "للضيوف والحجاج"},
     "text": {"ru": "Готовим и на одного человека, и на большую группу.", "en": "We cook for a single guest or a whole group.", "ar": "نطبخ لشخص واحد ولمجموعات كبيرة."}},
]

BRAND_STORY = {
    "title": {"ru": "MZ FOOD — вкус дома, пока вы в гостях у Мекки", "en": "MZ FOOD — the taste of home while you're a guest of Makkah", "ar": "MZ FOOD — طعم البيت وأنت ضيف على مكة"},
    "text": {
        "ru": "MZ FOOD готовит домашнюю халяльную еду для гостей, которым важен знакомый вкус, — семей, паломников и путешественников из России, Чечни, Кавказа и стран СНГ. Мы делаем ставку на качество, привычные блюда и быстрый заказ, а не на громкие обещания.",
        "en": "MZ FOOD cooks home-style halal food for guests who value a familiar taste — families, pilgrims and travelers from Russia, Chechnya, the Caucasus and the CIS. We focus on quality, familiar dishes and a fast order — not big promises.",
        "ar": "تُعِدّ MZ FOOD أكلًا بيتيًا حلالًا لضيوف يهمهم الطعم المألوف — عائلات وحجاج ومسافرين من روسيا والشيشان والقوقاز ودول رابطة الدول المستقلة. تركيزنا على الجودة والأطباق المألوفة وسرعة الطلب، مش على وعود كبيرة.",
    },
}

HOW_TO_ORDER = [
    {"n": 1, "title": {"ru": "Выберите блюда", "en": "Choose your dishes", "ar": "اختر أطباقك"},
     "text": {"ru": "Посмотрите меню на сайте или напишите «Меню» в WhatsApp.", "en": "Browse the menu on the site or send \"Menu\" on WhatsApp.", "ar": "تصفح المنيو في الموقع أو اكتب «المنيو» في واتساب."}},
    {"n": 2, "title": {"ru": "Отправьте заказ в WhatsApp", "en": "Send your order on WhatsApp", "ar": "أرسل طلبك عبر واتساب"},
     "text": {"ru": "Мы подтвердим состав, цену и время.", "en": "We'll confirm items, price and timing.", "ar": "هنأكدلك الأصناف والسعر والوقت."}},
    {"n": 3, "title": {"ru": "Получите доставку", "en": "Get your delivery", "ar": "استلم طلبك"},
     "text": {"ru": "По Мекке и в отели, включая период Умры и Хаджа.", "en": "Across Makkah and to hotels, including during Umrah and Hajj.", "ar": "في مكة وللفنادق، حتى في مواسم العمرة والحج."}},
]

LOW_CALORIES = {
    "title": {"ru": "Low Calories", "en": "Low Calories", "ar": "Low Calories"},
    "subtitle": {
        "ru": "Более лёгкая линейка блюд от MZ FOOD — для гостей, которые следят за питанием.",
        "en": "A lighter line of dishes from MZ FOOD — for guests who watch what they eat.",
        "ar": "خط أطباق أخف من MZ FOOD — للضيوف اللي بيهتموا بنوعية أكلهم.",
    },
    # No real Low Calories menu/pricing data exists yet — deliberately not invented.
    "pending_note": {
        "ru": "Меню Low Calories скоро появится здесь. Актуальные варианты уточняйте в WhatsApp.",
        "en": "The Low Calories menu is coming soon. Ask about current options on WhatsApp.",
        "ar": "منيو Low Calories هيتضاف قريبًا هنا. اسأل عن الخيارات المتاحة حاليًا عبر واتساب.",
    },
}

REVIEWS_EMPTY = {
    "title": {"ru": "Отзывы наших гостей", "en": "What our guests say", "ar": "آراء ضيوفنا"},
    "text": {
        "ru": "MZ FOOD — молодой бренд, и мы только начинаем собирать отзывы в Google. Мы намеренно не публикуем здесь ничего, кроме реальных слов наших гостей — этот раздел заполнится, как только появятся первые оценки.",
        "en": "MZ FOOD is a young brand, and we're just starting to collect reviews on Google. We deliberately publish nothing here except our guests' real words — this section will fill in as soon as the first ratings arrive.",
        "ar": "MZ FOOD براند جديد، ولسه بنبدأ نجمع تقييمات على جوجل. عن قصد إحنا مش بننشر هنا غير كلام ضيوفنا الحقيقي — القسم ده هيتملى أول ما توصل أول تقييمات.",
    },
}

FINAL_CTA = {
    "title": {"ru": "Хотите заказать?", "en": "Ready to order?", "ar": "عايز تطلب؟"},
    "text": {
        "ru": "Напишите нам в WhatsApp — поможем выбрать и оформим заказ.",
        "en": "Message us on WhatsApp — we'll help you choose and place the order.",
        "ar": "ابعتلنا رسالة على واتساب — هنساعدك تختار ونجهز طلبك.",
    },
}

ABOUT_PRINCIPLES = [
    {"title": {"ru": "Халяль без вопросов", "en": "Halal, no exceptions", "ar": "حلال من غير أي استفسار"},
     "text": {"ru": "Мы готовим только халяльную еду — это не преимущество, а обязательное условие.", "en": "We cook only halal food — not a selling point, a baseline requirement.", "ar": "إحنا بنطبخ أكل حلال بس — ده مش ميزة، ده شرط أساسي."}},
    {"title": {"ru": "Домашний вкус", "en": "Home-style taste", "ar": "طعم بيتي"},
     "text": {"ru": "Рецепты, привычные гостям из России, Чечни, Кавказа и стран СНГ — не адаптация под туриста.", "en": "Recipes familiar to guests from Russia, Chechnya, the Caucasus and the CIS — not adapted for tourists.", "ar": "وصفات مألوفة لضيوف روسيا والشيشان والقوقاز ودول رابطة الدول المستقلة — مش نسخة موجهة للسياح."}},
    {"title": {"ru": "Простой заказ", "en": "A simple order", "ar": "طلب بسيط"},
     "text": {"ru": "Всё общение — на русском языке, через WhatsApp, без сложных форм и приложений.", "en": "All communication happens on WhatsApp, in Russian — no complicated forms or apps.", "ar": "كل التواصل عبر واتساب باللغة الروسية، من غير نماذج أو تطبيقات معقدة."}},
    {"title": {"ru": "Для гостя и для группы", "en": "For one guest or a whole group", "ar": "للضيف الفردي وللمجموعات"},
     "text": {"ru": "Готовим и на одного человека, и на большую паломническую группу.", "en": "We cook for a single guest and for large pilgrimage groups alike.", "ar": "بنطبخ للفرد وللمجموعات الكبيرة من الحجاج بنفس الاهتمام."}},
]

DELIVERY_AREAS = [
    {"title": {"ru": "По всей Мекке", "en": "Across all of Makkah", "ar": "في كل مكة"},
     "text": {"ru": "Доставляем по адресам в Мекке, включая период Умры и Хаджа, когда город особенно оживлён.", "en": "We deliver across Makkah, including during Umrah and Hajj when the city is busiest.", "ar": "بنوصل لعناوين في مكة، حتى في مواسم العمرة والحج لما المدينة بتكون مزدحمة."}},
    {"title": {"ru": "В отель", "en": "To your hotel", "ar": "للفندق"},
     "text": {"ru": "Доставляем гостям, которые остановились в отелях рядом с Харамом и в других районах Мекки.", "en": "We deliver to guests staying in hotels near the Haram and across other areas of Makkah.", "ar": "بنوصل للضيوف النازلين في فنادق قريبة من الحرم وفي باقي أحياء مكة."}},
    {"title": {"ru": "Групповые заказы", "en": "Group orders", "ar": "طلبات المجموعات"},
     "text": {"ru": "Работаем с семьями, паломническими группами и руководителями групп — заказ на несколько человек сразу.", "en": "We work with families, pilgrimage groups and group leaders — one order for many people at once.", "ar": "بنشتغل مع العائلات ومجموعات الحجاج وقادة المجموعات — طلب واحد لعدد كبير من الأشخاص."}},
]

DELIVERY_STEPS = [
    {"n": 1, "text": {"ru": f"Напишите слово «Меню» на {CONTACT['phone_display']}", "en": f"Send the word \"Menu\" to {CONTACT['phone_display']}", "ar": f"اكتب كلمة «المنيو» على {CONTACT['phone_display']}"}},
    {"n": 2, "text": {"ru": "Выберите блюда — поможем определиться с выбором", "en": "Choose your dishes — we'll help you decide", "ar": "اختار الأطباق — هنساعدك تحدد اختيارك"}},
    {"n": 3, "text": {"ru": "Укажите адрес или отель — доставим заказ", "en": "Share your address or hotel — we'll deliver", "ar": "ابعت العنوان أو اسم الفندق — وهنوصل الطلب"}},
]

HOTELS_TEASER = {
    "title": {"ru": "Отелям и группам", "en": "Hotels & groups", "ar": "للفنادق والمجموعات"},
    "text": {
        "ru": "Работаем с руководителями паломнических групп, туроператорами и отелями — организуем питание для гостей напрямую.",
        "en": "We work with pilgrimage group leaders, tour operators and hotels — arranging meals for guests directly.",
        "ar": "بنشتغل مع قادة مجموعات الحج والمعتمرين ومنظمي الرحلات والفنادق — بننظم وجبات للضيوف مباشرة.",
    },
}

# ---------------------------------------------------------------------------
# Non-branded SEO landing pages (added 15 Sep 2026).
# Goal: appear for searchers who don't know "MZ FOOD" yet and search by cuisine
# or dish instead (see seo-strategy doc, section 4). Content is genuinely
# different from the homepage/menu (not duplicate content), uses only real
# menu items already listed in MENU_CATEGORIES above, and is written naturally
# rather than keyword-stuffed.
# ---------------------------------------------------------------------------
UZBEK_CUISINE_PAGE = {
    "h1": {
        "ru": "Узбекская кухня в Мекке: плов и лагман",
        "en": "Uzbek & Central Asian Food in Makkah: Plov and Lagman",
        "ar": "المطبخ الأوزبكي في مكة: بلوف ولغمان",
    },
    "kicker": {"ru": "Мекка", "en": "Makkah", "ar": "مكة"},
    "intro": {
        "ru": "Многие блюда, которые готовит MZ FOOD, — общие для русской, чеченской, кавказской и среднеазиатской кухни. Поэтому гости из Узбекистана, Таджикистана и Киргизстана тоже находят у нас знакомый вкус. Если вы ищете узбекскую кухню в Мекке или привычный плов, — вот несколько блюд, которые стоит попробовать.",
        "en": "Many of the dishes MZ FOOD cooks are shared across Russian, Chechen, Caucasian and Central Asian cuisine. That's why guests from Uzbekistan, Tajikistan and Kyrgyzstan often find a familiar taste here too. If you're looking for Uzbek food in Makkah or a plov you already know, here are a few dishes worth trying.",
        "ar": "كتير من الأطباق اللي بتعملها MZ FOOD مشتركة بين المطبخ الروسي والشيشاني والقوقازي وآسيا الوسطى. عشان كده ضيوف من أوزبكستان وطاجيكستان وقيرغيزستان بيلاقوا عندنا طعم مألوف. لو بتدوّر على أكل أوزبكي في مكة أو بلوف تعرفه كويس، دول كام طبق يستاهلوا التجربة.",
    },
    "dish_keys": ["plov_govyadina", "lagman", "plov_sweet"],
    "note": {
        "ru": "Мы не позиционируем себя как узбекский ресторан — MZ FOOD готовит русскую, чеченскую и кавказскую кухню, часть блюд которой знакома и гостям из Центральной Азии.",
        "en": "We don't present ourselves as an Uzbek restaurant — MZ FOOD cooks Russian, Chechen and Caucasian food, and some of it happens to be familiar to guests from Central Asia too.",
        "ar": "احنا مش بنقدّم نفسنا كمطعم أوزبكي — MZ FOOD بتطبخ أكل روسي وشيشاني وقوقازي، وجزء منه بيبقى مألوف كمان لضيوف آسيا الوسطى.",
    },
    "closing_title": {"ru": "Хотите попробовать?", "en": "Want to try it?", "ar": "عايز تجرب؟"},
    "closing_text": {
        "ru": "Напишите нам в WhatsApp — поможем выбрать и оформим доставку.",
        "en": "Message us on WhatsApp — we'll help you choose and arrange delivery.",
        "ar": "ابعتلنا واتساب — هنساعدك تختار ونظبطلك التوصيل.",
    },
}

PLOV_PAGE = {
    "h1": {
        "ru": "Плов в Мекке",
        "en": "Plov in Makkah",
        "ar": "بلوف في مكة",
    },
    "kicker": {"ru": "Мекка", "en": "Makkah", "ar": "مكة"},
    "intro": {
        "ru": "Плов — одно из самых узнаваемых блюд узбекской, таджикской и в целом среднеазиатской кухни, но его так же готовят и любят в Чечне, на Кавказе и в России. В MZ FOOD есть два варианта плова — сытный плов с говядиной и сладкий плов с сухофруктами.",
        "en": "Plov is one of the most recognizable dishes of Uzbek, Tajik and Central Asian cuisine in general, but it's also cooked and loved in Chechnya, the Caucasus and Russia. MZ FOOD serves two versions — a hearty beef plov and a sweet plov with dried fruit.",
        "ar": "البلوف من أشهر أطباق المطبخ الأوزبكي والطاجيكي وآسيا الوسطى بشكل عام، لكنه كمان معروف ومحبوب في الشيشان والقوقاز وروسيا. في MZ FOOD عندنا نسختين من البلوف — بلوف باللحم البقري وبلوف حلو بالفواكه المجففة.",
    },
    "dish_keys": ["plov_govyadina", "plov_sweet"],
    "closing_title": {"ru": "Заказать плов", "en": "Order plov", "ar": "اطلب بلوف"},
    "closing_text": {
        "ru": "Заказ принимаем через WhatsApp — доставка по Мекке и в отели.",
        "en": "We take orders on WhatsApp — delivery across Makkah and to hotels.",
        "ar": "بنستقبل الطلبات عبر واتساب — توصيل في كل مكة وللفنادق.",
    },
}

META = {
    "home": {
        "title": {
            "ru": "MZ FOOD — русская, чеченская и кавказская еда в Мекке",
            "en": "MZ FOOD — Russian, Chechen & Caucasian Food in Makkah",
            "ar": "MZ FOOD — أكل روسي وشيشاني وقوقازي في مكة",
        },
        "desc": {
            "ru": "Домашняя халяльная еда в Мекке для русскоязычных гостей, паломников и путешественников из России, Чечни, Кавказа и СНГ. Заказ через WhatsApp.",
            "en": "Home-style halal food in Makkah for Russian-speaking guests, pilgrims and travelers from Russia, Chechnya, the Caucasus and the CIS. Order on WhatsApp.",
            "ar": "أكل بيتي حلال في مكة لضيوف روسيا والشيشان والقوقاز ودول رابطة الدول المستقلة، وحجاج ومعتمرين ناطقين بالروسية. الطلب عبر واتساب.",
        },
    },
    "menu": {
        "title": {"ru": "Меню — русская, чеченская и кавказская кухня в Мекке — MZ FOOD",
                  "en": "Menu — Russian, Chechen & Caucasian Cuisine in Makkah — MZ FOOD",
                  "ar": "المنيو — مطبخ روسي وشيشاني وقوقازي في مكة — MZ FOOD"},
        "desc": {"ru": "Полное меню MZ FOOD: борщ, плов, лагман, хычины, хингалш и другие домашние блюда. Все цены в риалах.",
                  "en": "The full MZ FOOD menu: borscht, plov, lagman, khychiny, khingalsh and other home-style dishes. All prices in SAR.",
                  "ar": "منيو MZ FOOD الكامل: بورش، بلوف، لغمان، خيتشيني، خينغالش وأطباق بيتية تانية. كل الأسعار بالريال السعودي."},
    },
    "about": {
        "title": {"ru": "О нас — MZ FOOD в Мекке", "en": "About MZ FOOD in Makkah", "ar": "من نحن — MZ FOOD في مكة"},
        "desc": {"ru": "MZ FOOD готовит домашнюю халяльную еду в Мекке для русскоязычных гостей, паломников из Чечни, Кавказа и стран СНГ.",
                  "en": "MZ FOOD cooks home-style halal food in Makkah for Russian-speaking guests and pilgrims from Chechnya, the Caucasus and the CIS.",
                  "ar": "تُعِدّ MZ FOOD أكلًا بيتيًا حلالًا في مكة لضيوف ناطقين بالروسية وحجاج من الشيشان والقوقاز ودول رابطة الدول المستقلة."},
    },
    "delivery": {
        "title": {"ru": "Доставка еды в Мекке — MZ FOOD", "en": "Food Delivery in Makkah — MZ FOOD", "ar": "توصيل أكل في مكة — MZ FOOD"},
        "desc": {"ru": "Доставляем домашнюю халяльную еду по всей Мекке и в отели, включая период Умры и Хаджа. Заказ через WhatsApp.",
                  "en": "We deliver home-style halal food across Makkah and to hotels, including during Umrah and Hajj. Order on WhatsApp.",
                  "ar": "بنوصل أكل بيتي حلال في كل مكة وللفنادق، حتى في مواسم العمرة والحج. الطلب عبر واتساب."},
    },
    "reviews": {
        "title": {"ru": "Отзывы — MZ FOOD в Мекке", "en": "Reviews — MZ FOOD in Makkah", "ar": "التقييمات — MZ FOOD في مكة"},
        "desc": {"ru": "Отзывы гостей MZ FOOD в Мекке.", "en": "Guest reviews for MZ FOOD in Makkah.", "ar": "آراء ضيوف MZ FOOD في مكة."},
    },
    "contacts": {
        "title": {"ru": "Контакты — MZ FOOD в Мекке", "en": "Contact MZ FOOD in Makkah", "ar": "تواصل مع MZ FOOD في مكة"},
        "desc": {"ru": "Свяжитесь с MZ FOOD в Мекке: WhatsApp, телефон, адрес и Instagram.",
                  "en": "Contact MZ FOOD in Makkah: WhatsApp, phone, address and Instagram.",
                  "ar": "تواصل مع MZ FOOD في مكة: واتساب، هاتف، العنوان وإنستجرام."},
    },
    "lowcalories": {
        "title": {"ru": "Low Calories — лёгкие блюда от MZ FOOD в Мекке", "en": "Low Calories — Lighter Dishes by MZ FOOD in Makkah", "ar": "Low Calories — أطباق أخف من MZ FOOD في مكة"},
        "desc": {"ru": "Low Calories — линейка более лёгких блюд от MZ FOOD для гостей, которые следят за питанием.",
                  "en": "Low Calories — a lighter line of dishes by MZ FOOD for health-conscious guests.",
                  "ar": "Low Calories — خط أطباق أخف من MZ FOOD للضيوف المهتمين بنوعية أكلهم."},
    },
    "uzbek_cuisine": {
        "title": {"ru": "Узбекская кухня в Мекке — плов, лагман | MZ FOOD",
                  "en": "Uzbek Food in Makkah — Plov & Lagman | MZ FOOD",
                  "ar": "أكل أوزبكي في مكة — بلوف ولغمان | MZ FOOD"},
        "desc": {"ru": "Плов, лагман и другие блюда среднеазиатской кухни в Мекке. Домашний вкус для гостей из Узбекистана, Таджикистана и Киргизстана. Заказ через WhatsApp.",
                  "en": "Plov, lagman and other Central Asian dishes in Makkah. A familiar home-style taste for guests from Uzbekistan, Tajikistan and Kyrgyzstan. Order on WhatsApp.",
                  "ar": "بلوف ولغمان وأطباق تانية من مطبخ آسيا الوسطى في مكة. طعم بيتي مألوف لضيوف أوزبكستان وطاجيكستان وقيرغيزستان. الطلب عبر واتساب."},
    },
    "plov": {
        "title": {"ru": "Плов в Мекке — заказать с доставкой | MZ FOOD",
                  "en": "Plov in Makkah — Order with Delivery | MZ FOOD",
                  "ar": "بلوف في مكة — اطلب مع توصيل | MZ FOOD"},
        "desc": {"ru": "Плов с говядиной и сладкий плов с сухофруктами в Мекке. Домашний вкус, доставка и заказ через WhatsApp.",
                  "en": "Beef plov and sweet plov with dried fruit in Makkah. Home-style taste, delivery, order on WhatsApp.",
                  "ar": "بلوف باللحم البقري وبلوف حلو بالفواكه المجففة في مكة. طعم بيتي، توصيل، والطلب عبر واتساب."},
    },
}
