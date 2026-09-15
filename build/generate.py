# -*- coding: utf-8 -*-
"""
MZ FOOD static site generator.
Reads build/data.py (single source of truth, real facts only) and renders
plain, dependency-free HTML/CSS/JS into the repo root — RU at the existing
indexed paths, EN under /en/, AR (RTL) under /ar/.

Run:  python3 build/generate.py
"""
import json
import os
import shutil
import sys

sys.path.insert(0, os.path.dirname(__file__))
from data import (  # noqa: E402
    BASE_URL, BASE_PATH, LANGS, DEFAULT_LANG, LANG_META, SLUGS, PAGE_ORDER,
    CONTACT, NAV, CTA, WA_TEXT, wa_link, wa_link_dish, SITE_TITLE, TAGLINE,
    MENU_CATEGORIES, KUNAFA, POPULAR_DISH_KEYS, HERO, WHY_MZFOOD, BRAND_STORY,
    HOW_TO_ORDER, LOW_CALORIES, REVIEWS_EMPTY, FINAL_CTA, ABOUT_PRINCIPLES,
    DELIVERY_AREAS, DELIVERY_STEPS, HOTELS_TEASER, META,
    UZBEK_CUISINE_PAGE, PLOV_PAGE, RUSSIAN_CUISINE_PAGE, CHECHEN_CUISINE_PAGE,
)
from icons import icon  # noqa: E402

REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

WA_GENERAL = wa_link("general")
WA_ORDER = wa_link("order")
WA_PARTNER = wa_link("partner")
WA_REVIEW = wa_link("review")
WA_MENU_WORD = wa_link("menu_word")
WA_LOWCAL = wa_link("lowcal")


def bdi(text):
    """Isolate LTR content (phone numbers, email, prices) inside RTL pages
    so digits/Latin text don't get visually scrambled by the bidi algorithm."""
    return f"<bdi>{text}</bdi>"


PHONE_BDI = bdi(CONTACT["phone_display"])
EMAIL_BDI = bdi(CONTACT["email"])
ADDRESS_BDI = bdi(CONTACT["address_line"])


# ---------------------------------------------------------------------------
# URL helpers
# ---------------------------------------------------------------------------
def _rel_path(page_key, lang):
    """Path relative to the site root, e.g. '' , 'menu/', 'en/menu/', 'ar/'."""
    slug = SLUGS[page_key][lang]
    if slug == "":
        return "" if lang == DEFAULT_LANG else f"{lang}/"
    prefix = "" if lang == DEFAULT_LANG else f"{lang}/"
    return f"{prefix}{slug}/"


def page_path(page_key, lang):
    """Site-root-relative path for use in href/src attributes, e.g. /mzfood-makkah-website/en/menu/"""
    return f"{BASE_PATH}/{_rel_path(page_key, lang)}"


def page_url(page_key, lang):
    """Absolute URL for canonical/hreflang/sitemap/OG — BASE_URL already includes the GitHub Pages project path."""
    return f"{BASE_URL.rstrip('/')}/{_rel_path(page_key, lang)}"


def asset(path):
    return f"{BASE_PATH}/assets/{path}"


def out_dir_for(page_key, lang):
    slug = SLUGS[page_key][lang]
    if slug == "":
        return REPO_ROOT if lang == DEFAULT_LANG else os.path.join(REPO_ROOT, lang)
    prefix = "" if lang == DEFAULT_LANG else lang
    return os.path.join(REPO_ROOT, prefix, slug) if prefix else os.path.join(REPO_ROOT, slug)


# ---------------------------------------------------------------------------
# Shared chrome: <head>, header, footer, mobile sticky CTA
# ---------------------------------------------------------------------------
def google_fonts_link(lang):
    if lang == "ar":
        fam = "El+Messiri:wght@600;700&family=Cairo:wght@400;500;600;700;800"
    else:
        fam = "Playfair+Display:ital,wght@0,600;0,700;0,900;1,600;1,700&family=Manrope:wght@400;500;600;700;800"
    return (
        '<link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>'
        f'<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family={fam}&display=swap">'
    )


def hreflang_links(page_key):
    links = []
    for lang in LANGS:
        links.append(f'<link rel="alternate" hreflang="{LANG_META[lang]["html_lang"]}" href="{page_url(page_key, lang)}">')
    links.append(f'<link rel="alternate" hreflang="x-default" href="{page_url(page_key, DEFAULT_LANG)}">')
    return "\n".join(links)


def organization_schema():
    return {
        "@context": "https://schema.org",
        "@type": "Organization",
        "@id": f"{BASE_URL}/#organization",
        "name": "MZ FOOD",
        "url": BASE_URL,
        "logo": f"{BASE_URL}/logo.jpg",
        "sameAs": [CONTACT["instagram_url"]],
    }


def restaurant_schema(lang):
    return {
        "@context": "https://schema.org",
        "@type": "Restaurant",
        "@id": f"{BASE_URL}/#restaurant",
        "name": "MZ FOOD",
        "image": f"{BASE_URL}/logo.jpg",
        "url": page_url("home", lang),
        "telephone": CONTACT["phone_tel"],
        "servesCuisine": ["Russian", "Chechen", "Caucasian"],
        "priceRange": "SAR 18-35",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": CONTACT["address_line"],
            "addressLocality": "Makkah",
            "addressCountry": "SA",
        },
    }


def menu_schema(lang):
    items = []
    for cat in MENU_CATEGORIES:
        for it in cat["items"]:
            items.append({
                "@type": "MenuItem",
                "name": it["name"][lang],
                "offers": {
                    "@type": "Offer",
                    "price": str(it["price"]),
                    "priceCurrency": "SAR",
                },
            })
    return {
        "@context": "https://schema.org",
        "@type": "Menu",
        "@id": f"{BASE_URL}/#menu",
        "name": {"ru": "Меню MZ FOOD", "en": "MZ FOOD Menu", "ar": "منيو MZ FOOD"}[lang],
        "hasMenuItem": items,
    }


def render_schema_scripts(schemas):
    out = []
    for s in schemas:
        out.append(f'<script type="application/ld+json">{json.dumps(s, ensure_ascii=False)}</script>')
    return "\n".join(out)


def head(lang, page_key, title, description, extra_schema=None):
    schemas = [organization_schema()]
    if page_key == "home":
        schemas.append(restaurant_schema(lang))
    if extra_schema:
        schemas.extend(extra_schema)
    canonical = page_url(page_key, lang)
    og_locale = {"ru": "ru_RU", "en": "en_US", "ar": "ar_SA"}[lang]
    return f"""<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
{hreflang_links(page_key)}
<link rel="icon" href="{BASE_PATH}/favicon.ico">
<link rel="stylesheet" href="{asset('css/style.css')}">
{google_fonts_link(lang)}
<meta property="og:type" content="website">
<meta property="og:site_name" content="MZ FOOD">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{BASE_URL}/logo.jpg">
<meta property="og:locale" content="{og_locale}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{BASE_URL}/logo.jpg">
{render_schema_scripts(schemas)}"""


ARIA_CURRENT_PAGE = ' aria-current="page"'
ARIA_CURRENT_TRUE = ' aria-current="true"'


def header_html(lang, page_key):
    meta = LANG_META[lang]
    nav_items = "".join(
        '<a href="{}"{}>{}</a>'.format(page_path(p, lang), ARIA_CURRENT_PAGE if p == page_key else "", NAV[p][lang])
        for p in PAGE_ORDER
    )
    lang_switch = "".join(
        '<a href="{}"{}>{}</a>'.format(page_path(page_key, l), ARIA_CURRENT_TRUE if l == lang else "", LANG_META[l]["short"])
        for l in LANGS
    )
    return f"""<header class="site-header">
  <div class="container">
    <a class="brand" href="{page_path('home', lang)}">
      <img src="{BASE_PATH}/logo.jpg" alt="MZ FOOD" width="36" height="36">
      <span>MZ FOOD</span>
    </a>
    <nav class="main-nav" data-open="false" aria-label="{NAV['home'][lang]}">
      {nav_items}
    </nav>
    <div class="header-actions">
      <div class="lang-switch" role="group" aria-label="Language">{lang_switch}</div>
      <a class="btn btn-whatsapp header-order-btn" href="{WA_ORDER[lang]}">{icon('whatsapp', 18)}{CTA['order_whatsapp'][lang]}</a>
      <button class="nav-toggle" aria-label="Menu" aria-expanded="false">{icon('menu', 26)}</button>
    </div>
  </div>
</header>"""


def footer_html(lang):
    meta = LANG_META[lang]
    nav_items = "".join(f'<li><a href="{page_path(p, lang)}">{NAV[p][lang]}</a></li>' for p in PAGE_ORDER)
    year_label = {"ru": "©", "en": "©", "ar": "©"}[lang]
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-tag">{TAGLINE[lang]}</div>
        <div class="footer-brand">MZ FOOD</div>
        <p>{HERO['sub'][lang][:120]}{"…" if len(HERO['sub'][lang]) > 120 else ""}</p>
      </div>
      <div class="footer-col">
        <h4>{ {"ru":"Навигация","en":"Navigation","ar":"روابط"}[lang] }</h4>
        <ul>{nav_items}</ul>
      </div>
      <div class="footer-col">
        <h4>{NAV['contacts'][lang]}</h4>
        <ul>
          <li><a href="tel:{CONTACT['phone_tel']}">{PHONE_BDI}</a></li>
          <li><a href="{CONTACT['maps_url']}">{ADDRESS_BDI}</a></li>
          <li><a href="mailto:{CONTACT['email']}">{EMAIL_BDI}</a></li>
          <li><a href="{CONTACT['instagram_url']}">{CONTACT['instagram_handle']}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>{year_label} 2026 MZ FOOD · Makkah, {CONTACT['address_country'][lang]}</span>
      <span>{PHONE_BDI} · {EMAIL_BDI}</span>
    </div>
  </div>
</footer>"""


def mobile_cta_html(lang):
    return f"""<div class="mobile-cta">
  <a class="btn btn-outline" href="{page_path('menu', lang)}">{CTA['view_menu'][lang]}</a>
  <a class="btn btn-whatsapp" href="{WA_ORDER[lang]}">{icon('whatsapp', 18)}{CTA['order_whatsapp'][lang]}</a>
</div>"""


def layout(lang, page_key, title, description, body, extra_schema=None):
    meta = LANG_META[lang]
    return f"""<!doctype html>
<html lang="{meta['html_lang']}" dir="{meta['dir']}">
<head>
{head(lang, page_key, title, description, extra_schema)}
</head>
<body>
{header_html(lang, page_key)}
<main>
{body}
</main>
{footer_html(lang)}
{mobile_cta_html(lang)}
<script src="{asset('js/main.js')}" defer></script>
</body>
</html>"""


# ---------------------------------------------------------------------------
# Page bodies
# ---------------------------------------------------------------------------
def all_items_by_key():
    d = {}
    for cat in MENU_CATEGORIES:
        for it in cat["items"]:
            d[it["key"]] = it
    return d


def dish_card_html(lang, item, show_note=False):
    wa = wa_link_dish(item["name"], item["weight"], item["price"])[lang]
    weight = item["weight"][lang]
    note = f' <span class="dish-note" style="color:#b34a2e;font-size:.75rem;">*</span>' if show_note and item.get("note_ru") else ""
    return f"""<article class="dish-card">
  <div class="dish-photo"><span>{ {"ru":"Фото скоро","en":"Photo coming soon","ar":"صورة قريبًا"}[lang] }</span></div>
  <div class="dish-body">
    <h3 class="dish-name">{item['name'][lang]}{note}</h3>
    {f'<p class="dish-weight">{weight}</p>' if weight else ''}
    <div class="dish-foot">
      <span class="dish-price">{bdi(f"{item['price']} SAR")}</span>
      <a class="dish-order-btn" href="{wa}">{icon('whatsapp', 15)}{ {"ru":"Заказать","en":"Order","ar":"اطلب"}[lang] }</a>
    </div>
  </div>
</article>"""


def home_body(lang):
    items = all_items_by_key()
    popular = "".join(dish_card_html(lang, items[k]) for k in POPULAR_DISH_KEYS)
    why_cards = "".join(f"""<div class="feature-card">
  <div class="feature-icon">{icon(w['icon'], 24)}</div>
  <h3>{w['title'][lang]}</h3>
  <p>{w['text'][lang]}</p>
</div>""" for w in WHY_MZFOOD)
    steps = "".join(f"""<div class="step">
  <div class="step-num">{s['n']}</div>
  <h3>{s['title'][lang]}</h3>
  <p>{s['text'][lang]}</p>
</div>""" for s in HOW_TO_ORDER)
    trust_items = f"""<li>{icon('pin',22)}<div><strong>{ADDRESS_BDI}</strong>{CONTACT['address_country'][lang]}</div></li>
<li>{icon('whatsapp',22)}<div><strong>{PHONE_BDI}</strong>{ {"ru":"Заказ и вопросы","en":"Orders & questions","ar":"للطلب والاستفسار"}[lang] }</div></li>
<li>{icon('instagram',22)}<div><strong>{CONTACT['instagram_handle']}</strong>Instagram</div></li>
<li>{icon('clock',22)}<div><strong>{ {"ru":"Часы работы","en":"Opening hours","ar":"ساعات العمل"}[lang] }</strong>{ {"ru":"Уточняйте в WhatsApp","en":"Ask on WhatsApp","ar":"استفسر عبر واتساب"}[lang] }</div></li>"""

    return f"""
<section class="hero">
  <div class="container">
    <div class="hero-content">
      <span class="eyebrow">{HERO['eyebrow'][lang]}</span>
      <h1>{HERO['h1'][lang]}</h1>
      <p class="lede">{HERO['sub'][lang]}</p>
      <div class="hero-actions">
        <a class="btn btn-whatsapp" href="{WA_ORDER[lang]}">{icon('whatsapp',20)}{CTA['order_whatsapp'][lang]}</a>
        <a class="btn btn-outline" href="{page_path('menu', lang)}">{CTA['view_menu'][lang]}</a>
      </div>
      <div class="hero-badges">
        <span class="hero-badge">{icon('pin',16)}{HERO['badges']['makkah'][lang]}</span>
        <span class="hero-badge">{icon('truck',16)}{HERO['badges']['delivery'][lang]}</span>
        <span class="hero-badge">{icon('whatsapp',16)}{HERO['badges']['whatsapp'][lang]}</span>
      </div>
    </div>
    <div class="hero-media">
      <span class="hero-media-tag">100% {"ХАЛЯЛЬ" if lang=="ru" else ("HALAL" if lang=="en" else "حلال 100%")}</span>
      <div class="hero-media-caption">MZ FOOD<br>{TAGLINE[lang]}</div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="grid-4">
      {why_cards}
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{NAV['menu'][lang]}</span>
      <h2>{ {"ru":"Несколько любимых блюд","en":"A few guest favorites","ar":"أشهر الأطباق عندنا"}[lang] }</h2>
      <p>{ {"ru":f"Полное меню — {sum(len(c['items']) for c in MENU_CATEGORIES)} блюд в {len(MENU_CATEGORIES)} разделах.","en":f"Full menu — {sum(len(c['items']) for c in MENU_CATEGORIES)} dishes across {len(MENU_CATEGORIES)} categories.","ar":f"المنيو الكامل — {sum(len(c['items']) for c in MENU_CATEGORIES)} طبق في {len(MENU_CATEGORIES)} أقسام."}[lang] }</p>
    </div>
    <div class="dish-grid">{popular}</div>
    <div class="section-cta-row">
      <a class="btn btn-outline" href="{page_path('menu', lang)}">{CTA['view_full_menu'][lang]}</a>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="story">
      <div class="story-media">{ {"ru":"Фото скоро","en":"Photo coming soon","ar":"صورة قريبًا"}[lang] }</div>
      <div>
        <span class="eyebrow">{ {"ru":"О нас","en":"About us","ar":"من نحن"}[lang] }</span>
        <h2>{BRAND_STORY['title'][lang]}</h2>
        <p>{BRAND_STORY['text'][lang]}</p>
        <a class="btn btn-outline" href="{page_path('about', lang)}">{CTA['read_more'][lang]} →</a>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="section-head" style="margin-inline:auto;text-align:center;max-width:620px;">
      <span class="eyebrow">{ {"ru":"Как заказать","en":"How to order","ar":"كيف تطلب"}[lang] }</span>
      <h2>{ {"ru":"Три простых шага","en":"Three simple steps","ar":"ثلاث خطوات بسيطة"}[lang] }</h2>
    </div>
    <div class="steps">{steps}</div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="lowcal-panel">
      <div>
        <span class="lowcal-badge">{LOW_CALORIES['title'][lang]}</span>
        <h2>{LOW_CALORIES['title'][lang]}</h2>
        <p>{LOW_CALORIES['subtitle'][lang]}</p>
        <p style="font-size:.85rem;opacity:.85;">{LOW_CALORIES['pending_note'][lang]}</p>
      </div>
      <a class="btn btn-whatsapp" href="{page_path('lowcalories', lang)}">{icon('whatsapp',18)}{CTA['view_lowcal'][lang]}</a>
    </div>
  </div>
</section>

<section>
  <div class="container">
    <div class="trust-grid">
      <div>
        <span class="eyebrow">MZ FOOD</span>
        <h2>{ {"ru":"Мекка, WhatsApp, Google","en":"Makkah, WhatsApp, Google","ar":"مكة، واتساب، جوجل"}[lang] }</h2>
        <ul class="trust-list">{trust_items}</ul>
      </div>
      <div class="map-frame">
        <iframe loading="lazy" title="MZ FOOD — Google Maps"
          src="https://www.google.com/maps?q={CONTACT['address_line'].replace(' ', '+')}+Makkah&output=embed"></iframe>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="section-head" style="margin-inline:auto;text-align:center;max-width:620px;">
      <span class="eyebrow">{NAV['reviews'][lang]}</span>
      <h2>{REVIEWS_EMPTY['title'][lang]}</h2>
      <p>{REVIEWS_EMPTY['text'][lang]}</p>
      <div class="section-cta-row">
        <a class="btn btn-outline" href="{page_path('reviews', lang)}">{CTA['leave_review'][lang]}</a>
      </div>
    </div>
  </div>
</section>

<section class="section-alt">
  <div class="container">
    <div class="feature-card" style="max-width:760px;margin-inline:auto;text-align:center;">
      <h3>{HOTELS_TEASER['title'][lang]}</h3>
      <p>{HOTELS_TEASER['text'][lang]}</p>
      <a class="btn btn-outline" href="{WA_PARTNER[lang]}">{CTA['discuss_partner'][lang]} →</a>
    </div>
  </div>
</section>

<section class="section-deep final-cta">
  <div class="container container--narrow">
    <h2>{FINAL_CTA['title'][lang]}</h2>
    <p>{FINAL_CTA['text'][lang]}</p>
    <a class="btn btn-whatsapp" href="{WA_ORDER[lang]}">{icon('whatsapp',22)}{CTA['order_whatsapp'][lang]}</a>
    <p class="final-cta-phone">{ {"ru":"Или позвоните","en":"Or call","ar":"أو اتصل"}[lang] }: <a href="tel:{CONTACT['phone_tel']}">{PHONE_BDI}</a></p>
  </div>
</section>
"""


def page_header_html(lang, page_key, title, kicker=None):
    return f"""<section class="page-header">
  <div class="container">
    <div class="breadcrumb"><a href="{page_path('home', lang)}">{NAV['home'][lang]}</a> / {NAV[page_key][lang]}</div>
    {f'<span class="eyebrow">{kicker}</span>' if kicker else ''}
    <h1>{title}</h1>
  </div>
</section>"""


def menu_body(lang):
    cats_html = ""
    for cat in MENU_CATEGORIES:
        rows = ""
        for it in cat["items"]:
            weight = it["weight"][lang]
            note = ""
            if it.get("note_ru") and lang == "ru":
                note = f' <span style="color:#b34a2e;font-weight:600;font-size:.78rem;">({it["note_ru"]})</span>'
            rows += f"""<div class="menu-item">
  <div>
    <div class="menu-item-name">{it['name'][lang]}{note}</div>
    {f'<div class="menu-item-weight">{weight}</div>' if weight else ''}
  </div>
  <div class="menu-item-price">{bdi(f"{it['price']} SAR")}</div>
</div>"""
        cats_html += f"""<div class="menu-category">
  <h2>{cat['name'][lang]}</h2>
  <div class="menu-items">{rows}</div>
</div>"""

    off_menu = f"""<div class="menu-offmenu">
  <div>
    <div class="menu-item-name">{KUNAFA[lang]}</div>
    <div class="menu-item-weight">{ {"ru":"Уточняйте цену в WhatsApp","en":"Ask for the price on WhatsApp","ar":"استفسر عن السعر عبر واتساب"}[lang] }</div>
  </div>
  <a class="btn btn-whatsapp" href="{WA_GENERAL[lang]}">{icon('whatsapp',16)}{CTA['order_whatsapp'][lang]}</a>
</div>"""

    read_also = {
        "ru": "Читайте также",
        "en": "You might also like",
        "ar": "اقرأ أيضًا",
    }[lang]
    cuisine_landing_keys = ["russian_cuisine", "chechen_cuisine", "uzbek_cuisine", "plov"]
    cuisine_links = " · ".join(
        f'<a href="{page_path(k, lang)}" style="font-weight:700;text-decoration:underline;">{NAV[k][lang]}</a>'
        for k in cuisine_landing_keys
    )
    return f"""
{page_header_html(lang, 'menu', {"ru":"Меню MZ FOOD","en":"MZ FOOD Menu","ar":"منيو MZ FOOD"}[lang], {"ru":"Домашние блюда, знакомые вам с детства","en":"Home-style dishes you've known since childhood","ar":"أطباق بيتية تعرفها من زمان"}[lang])}
<section class="section--tight">
  <div class="container container--narrow">
    <p class="menu-note">{ {"ru":"Все цены указаны в саудовских риалах (SAR). Актуальный состав и наличие уточняйте в WhatsApp.","en":"All prices are in Saudi Riyals (SAR). Please confirm current availability on WhatsApp.","ar":"كل الأسعار بالريال السعودي. تأكد من توفر الطبق عبر واتساب."}[lang] }</p>
    {cats_html}
    {off_menu}
    <div class="section-cta-row" style="flex-direction:column;gap:16px;align-items:center;">
      <a class="btn btn-whatsapp btn-block" href="{WA_ORDER[lang]}" style="max-width:360px;">{icon('whatsapp',20)}{CTA['order_whatsapp'][lang]}</a>
      <a href="{page_path('delivery', lang)}" style="font-weight:700;text-decoration:underline;">{ {"ru":"Готовите для группы или отеля? Смотрите условия доставки","en":"Ordering for a group or hotel? See delivery details","ar":"بتطلب لمجموعة أو فندق؟ شوف تفاصيل التوصيل"}[lang] } →</a>
    </div>
    <div class="menu-note" style="margin-top:24px;text-align:center;">
      {read_also}:
      {cuisine_links}
    </div>
  </div>
</section>
"""


def about_body(lang):
    principles = "".join(f"""<div class="feature-card">
  <div class="feature-icon">{icon('check',22)}</div>
  <h3>{p['title'][lang]}</h3>
  <p>{p['text'][lang]}</p>
</div>""" for p in ABOUT_PRINCIPLES)
    return f"""
{page_header_html(lang, 'about', {"ru":"MZ FOOD — вкус дома в Мекке","en":"MZ FOOD — the taste of home in Makkah","ar":"MZ FOOD — طعم البيت في مكة"}[lang])}
<section class="section--tight">
  <div class="container container--narrow">
    <p>{BRAND_STORY['text'][lang]}</p>
    <p>{ {"ru":"Мы понимаем, что во время Умры и Хаджа многие приезжают издалека и скучают по привычному вкусу. Наша цель — качество, узнаваемый вкус и быстрое, удобное обслуживание, а не громкие обещания.","en":"We understand that during Umrah and Hajj, many guests travel far from home and miss a familiar taste. Our goal is quality, a recognizable flavor and fast, convenient service — not big promises.","ar":"إحنا فاهمين إن كتير من الضيوف في العمرة والحج بيسافروا من بعيد ويفتقدوا الطعم المألوف. هدفنا الجودة والطعم المعروف والخدمة السريعة المريحة، مش وعود كبيرة."}[lang] }</p>
    <p>{ {"ru":"Заказать можно напрямую через WhatsApp — на русском языке, без лишних шагов.","en":"You can order directly on WhatsApp — in Russian, with no extra steps.","ar":"تقدر تطلب مباشرة عبر واتساب — باللغة الروسية، من غير خطوات زيادة."}[lang] }</p>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-head">
      <span class="eyebrow">{ {"ru":"Наши принципы","en":"Our principles","ar":"مبادئنا"}[lang] }</span>
      <h2>{ {"ru":"На чём мы не идём на компромисс","en":"What we never compromise on","ar":"اللي مبنتنازلش فيه"}[lang] }</h2>
    </div>
    <div class="principles-grid">{principles}</div>
  </div>
</section>
<section class="section-deep final-cta">
  <div class="container container--narrow">
    <h2>{ {"ru":"Остались вопросы?","en":"Still have questions?","ar":"عندك سؤال؟"}[lang] }</h2>
    <p>{ {"ru":"Напишите нам в WhatsApp — ответим быстро.","en":"Message us on WhatsApp — we reply quickly.","ar":"ابعتلنا واتساب — هنرد بسرعة."}[lang] }</p>
    <a class="btn btn-whatsapp" href="{WA_GENERAL[lang]}">{icon('whatsapp',20)}{CTA['order_whatsapp'][lang]}</a>
  </div>
</section>
"""


def delivery_body(lang):
    areas = "".join(f"""<div class="feature-card">
  <div class="feature-icon">{icon('truck',22)}</div>
  <h3>{a['title'][lang]}</h3>
  <p>{a['text'][lang]}</p>
</div>""" for a in DELIVERY_AREAS)
    steps = "".join(f"""<div class="step">
  <div class="step-num">{s['n']}</div>
  <p>{s['text'][lang]}</p>
</div>""" for s in DELIVERY_STEPS)
    return f"""
{page_header_html(lang, 'delivery', {"ru":"Доставляем домашнюю еду по всей Мекке","en":"We deliver home-style food across Makkah","ar":"بنوصل أكل بيتي في كل مكة"}[lang])}
<section class="section--tight">
  <div class="container">
    <div class="grid-3">{areas}</div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="section-head" style="margin-inline:auto;text-align:center;max-width:620px;">
      <span class="eyebrow">{ {"ru":"Как оформить","en":"How to order","ar":"إزاي تطلب"}[lang] }</span>
      <h2>{ {"ru":"Через WhatsApp — на русском языке","en":"On WhatsApp — in Russian","ar":"عبر واتساب — باللغة الروسية"}[lang] }</h2>
    </div>
    <div class="steps">{steps}</div>
    <div class="section-cta-row">
      <a class="btn btn-whatsapp" href="{WA_ORDER[lang]}">{icon('whatsapp',20)}{CTA['order_whatsapp'][lang]}</a>
    </div>
  </div>
</section>
<section>
  <div class="container container--narrow">
    <span class="eyebrow">{ {"ru":"Зона доставки","en":"Delivery area","ar":"منطقة التوصيل"}[lang] }</span>
    <p>{ADDRESS_BDI}, {CONTACT['address_country'][lang]} — { {"ru":"и близлежащие районы. Уточните ваш адрес или название отеля в WhatsApp, чтобы мы подтвердили доставку.","en":"and nearby areas. Share your address or hotel name on WhatsApp so we can confirm delivery.","ar":"والمناطق القريبة. ابعت عنوانك أو اسم الفندق عبر واتساب عشان نأكدلك التوصيل."}[lang] }</p>
  </div>
</section>
"""


def reviews_body(lang):
    return f"""
{page_header_html(lang, 'reviews', REVIEWS_EMPTY['title'][lang])}
<section class="section--tight">
  <div class="container">
    <div class="empty-state">
      <h3>{ {"ru":"Отзывы скоро появятся здесь","en":"Reviews will appear here soon","ar":"التقييمات هتظهر هنا قريبًا"}[lang] }</h3>
      <p>{REVIEWS_EMPTY['text'][lang]}</p>
      <div class="empty-state-actions">
        <a class="btn btn-whatsapp" href="{CONTACT['maps_url']}">{icon('star',18)}{CTA['leave_review'][lang]}</a>
        <a class="btn btn-outline" href="{WA_REVIEW[lang]}">{CTA['share_whatsapp'][lang]}</a>
      </div>
    </div>
  </div>
</section>
"""


def contacts_body(lang):
    cards = f"""<div class="contact-card">
  <h3>WhatsApp</h3>
  <a class="value" href="{WA_GENERAL[lang]}">{PHONE_BDI}</a>
</div>
<div class="contact-card">
  <h3>{ {"ru":"Телефон","en":"Phone","ar":"الهاتف"}[lang] }</h3>
  <a class="value" href="tel:{CONTACT['phone_tel']}">{PHONE_BDI}</a>
</div>
<div class="contact-card">
  <h3>{ {"ru":"Адрес","en":"Address","ar":"العنوان"}[lang] }</h3>
  <p class="value" style="margin:0;">{ADDRESS_BDI}<br>{CONTACT['address_country'][lang]}</p>
  <a href="{CONTACT['maps_url']}" style="font-weight:700;text-decoration:underline;">{CTA['open_maps'][lang]} →</a>
</div>
<div class="contact-card">
  <h3>{ {"ru":"Мы в соцсетях","en":"Social media","ar":"تابعنا"}[lang] }</h3>
  <a class="value" href="{CONTACT['instagram_url']}">{icon('instagram',18)} {CONTACT['instagram_handle']}</a>
</div>"""
    return f"""
{page_header_html(lang, 'contacts', {"ru":"Свяжитесь с MZ FOOD","en":"Get in touch with MZ FOOD","ar":"تواصل مع MZ FOOD"}[lang])}
<section class="section--tight">
  <div class="container">
    <div class="contact-cards">{cards}</div>
  </div>
</section>
<section class="section-alt">
  <div class="container">
    <div class="map-frame" style="max-width:900px;margin-inline:auto;">
      <iframe loading="lazy" title="MZ FOOD — Google Maps"
        src="https://www.google.com/maps?q={CONTACT['address_line'].replace(' ', '+')}+Makkah&output=embed"></iframe>
    </div>
  </div>
</section>
"""


def lowcalories_body(lang):
    return f"""
{page_header_html(lang, 'lowcalories', LOW_CALORIES['title'][lang], "MZ FOOD")}
<section class="section--tight">
  <div class="container container--narrow" style="text-align:center;">
    <p>{LOW_CALORIES['subtitle'][lang]}</p>
    <div class="empty-state" style="margin-top:32px;">
      <h3>{LOW_CALORIES['title'][lang]}</h3>
      <p>{LOW_CALORIES['pending_note'][lang]}</p>
      <div class="empty-state-actions">
        <a class="btn btn-whatsapp" href="{WA_LOWCAL[lang]}">{icon('whatsapp',18)}{CTA['order_whatsapp'][lang]}</a>
        <a class="btn btn-outline" href="{page_path('menu', lang)}">{CTA['view_full_menu'][lang]}</a>
      </div>
    </div>
  </div>
</section>
"""


def cuisine_landing_body(lang, page_key, data):
    """Shared renderer for non-branded SEO landing pages (Uzbek cuisine, Plov,
    Russian cuisine, Chechen & Caucasian cuisine) — same visual language as the
    rest of the site (page-header, dish-grid, final-cta), just a different,
    genuinely unique block of copy and a curated subset of real dishes.
    Cross-links to sibling cuisine pages come from data['related'] (a list of
    page_keys), so this scales to any number of landing pages, not just a pair."""
    items = all_items_by_key()
    dish_cards = "".join(dish_card_html(lang, items[k]) for k in data["dish_keys"])
    note_html = f'<p class="menu-note">{data["note"][lang]}</p>' if data.get("note") else ""
    related_keys = data.get("related", [])
    read_also_label = {"ru": "Читайте также", "en": "You might also like", "ar": "اقرأ أيضًا"}[lang]
    related_links = " · ".join(
        f'<a href="{page_path(k, lang)}" style="font-weight:700;text-decoration:underline;">{NAV[k][lang]}</a>'
        for k in related_keys
    )
    related_html = (
        f'<div class="menu-note" style="margin-top:16px;text-align:center;">{read_also_label}: {related_links}</div>'
        if related_links else ""
    )
    return f"""
{page_header_html(lang, page_key, data['h1'][lang], data['kicker'][lang])}
<section class="section--tight">
  <div class="container container--narrow">
    <p>{data['intro'][lang]}</p>
  </div>
</section>
<section>
  <div class="container">
    <div class="dish-grid">{dish_cards}</div>
    {note_html}
    <div class="section-cta-row" style="flex-direction:column;gap:16px;align-items:center;">
      <a class="btn btn-outline" href="{page_path('menu', lang)}">{CTA['view_full_menu'][lang]}</a>
    </div>
    {related_html}
  </div>
</section>
<section class="section-deep final-cta">
  <div class="container container--narrow">
    <h2>{data['closing_title'][lang]}</h2>
    <p>{data['closing_text'][lang]}</p>
    <a class="btn btn-whatsapp" href="{WA_ORDER[lang]}">{icon('whatsapp',22)}{CTA['order_whatsapp'][lang]}</a>
  </div>
</section>
"""


def uzbek_cuisine_body(lang):
    return cuisine_landing_body(lang, "uzbek_cuisine", UZBEK_CUISINE_PAGE)


def plov_body(lang):
    return cuisine_landing_body(lang, "plov", PLOV_PAGE)


def russian_cuisine_body(lang):
    return cuisine_landing_body(lang, "russian_cuisine", RUSSIAN_CUISINE_PAGE)


def chechen_cuisine_body(lang):
    return cuisine_landing_body(lang, "chechen_cuisine", CHECHEN_CUISINE_PAGE)


def error_404_body(lang):
    return f"""
<section class="error-page">
  <div class="container">
    <div class="code">404</div>
    <h1>{ {"ru":"Страница не найдена","en":"Page not found","ar":"الصفحة غير موجودة"}[lang] }</h1>
    <p>{ {"ru":"Похоже, такой страницы больше нет. Вернитесь на главную или посмотрите меню.","en":"This page doesn't seem to exist. Head back home or check the menu.","ar":"يبدو إن الصفحة دي مش موجودة. ارجع للرئيسية أو شوف المنيو."}[lang] }</p>
    <div class="hero-actions" style="justify-content:center;">
      <a class="btn btn-whatsapp" href="{page_path('home', lang)}">{NAV['home'][lang]}</a>
      <a class="btn btn-outline" href="{page_path('menu', lang)}">{CTA['view_menu'][lang]}</a>
    </div>
  </div>
</section>
"""


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
PAGE_BUILDERS = {
    "home": home_body,
    "menu": menu_body,
    "about": about_body,
    "delivery": delivery_body,
    "reviews": reviews_body,
    "contacts": contacts_body,
    "lowcalories": lowcalories_body,
    "uzbek_cuisine": uzbek_cuisine_body,
    "plov": plov_body,
    "russian_cuisine": russian_cuisine_body,
    "chechen_cuisine": chechen_cuisine_body,
}


def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def build_pages():
    written = []
    for lang in LANGS:
        for page_key, builder in PAGE_BUILDERS.items():
            m = META.get(page_key, META["home"])
            title = m["title"][lang]
            desc = m["desc"][lang]
            extra_schema = [menu_schema(lang)] if page_key == "menu" else None
            body = builder(lang)
            html = layout(lang, page_key, title, desc, body, extra_schema)
            out_dir = out_dir_for(page_key, lang)
            out_path = os.path.join(out_dir, "index.html")
            write_file(out_path, html)
            written.append(out_path)
        # 404 per language (root 404.html stays RU-default per GitHub Pages convention)
    # top-level 404.html (GitHub Pages serves this for unmatched paths, RU by default)
    write_file(os.path.join(REPO_ROOT, "404.html"), layout("ru", "home", META["home"]["title"]["ru"], META["home"]["desc"]["ru"], error_404_body("ru")))
    return written


def build_sitemap():
    urls = []
    for lang in LANGS:
        for page_key in list(PAGE_BUILDERS.keys()):
            if page_key == "lowcalories":
                continue  # thin/placeholder page — keep out of sitemap until real content exists
            urls.append((page_url(page_key, lang), page_key, lang))
    entries = []
    for url, page_key, lang in urls:
        alt_links = "".join(
            f'\n    <xhtml:link rel="alternate" hreflang="{LANG_META[l]["html_lang"]}" href="{page_url(page_key, l)}"/>'
            for l in LANGS
        )
        alt_links += f'\n    <xhtml:link rel="alternate" hreflang="x-default" href="{page_url(page_key, DEFAULT_LANG)}"/>'
        entries.append(f"""  <url>
    <loc>{url}</loc>{alt_links}
  </url>""")
    xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
        xmlns:xhtml="http://www.w3.org/1999/xhtml">
{chr(10).join(entries)}
</urlset>
"""
    write_file(os.path.join(REPO_ROOT, "sitemap.xml"), xml)


def build_robots():
    content = f"""User-agent: *
Allow: /

Sitemap: {BASE_URL}/sitemap.xml
"""
    write_file(os.path.join(REPO_ROOT, "robots.txt"), content)


def copy_assets():
    dst_css = os.path.join(REPO_ROOT, "assets", "css")
    dst_js = os.path.join(REPO_ROOT, "assets", "js")
    os.makedirs(dst_css, exist_ok=True)
    os.makedirs(dst_js, exist_ok=True)
    shutil.copy(os.path.join(os.path.dirname(__file__), "style.css"), os.path.join(dst_css, "style.css"))
    shutil.copy(os.path.join(os.path.dirname(__file__), "main.js"), os.path.join(dst_js, "main.js"))


def clean_old_build():
    """Remove the previous Next.js static-export output. Keep real assets
    (logo.jpg, favicon.ico) and the Google Search Console verification file."""
    keep_root_files = {"logo.jpg", "favicon.ico", "google5fb6f872ceaff2fa.html", ".nojekyll", ".git", "build", "CNAME", ".gitignore"}
    keep_root_dirs = {"build", ".git"}
    for name in os.listdir(REPO_ROOT):
        full = os.path.join(REPO_ROOT, name)
        if name in keep_root_files or name in keep_root_dirs:
            continue
        if os.path.isdir(full):
            shutil.rmtree(full)
        else:
            os.remove(full)


if __name__ == "__main__":
    clean_old_build()
    copy_assets()
    written = build_pages()
    build_sitemap()
    build_robots()
    print(f"Generated {len(written)} pages + sitemap.xml + robots.txt")
