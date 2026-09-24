#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MAXRENTAL v2 static site generator.

    python3 build.py

Writes every .html page from the copy in content.py and the catalogue in
js/products.js. Structure follows all-natural.framer.website (see TEARDOWN.md);
content and colour are MAXRENTAL's own.
"""

import os
import re
import html
import content as C

ROOT = os.path.dirname(os.path.abspath(__file__))


def asset_version():
    newest = 0
    for rel in ("css/app.css", "js/app.js", "js/products.js"):
        f = os.path.join(ROOT, rel)
        if os.path.exists(f):
            newest = max(newest, int(os.path.getmtime(f)))
    return str(newest)


VER = asset_version()


# ---------------------------------------------------------------- catalogue

def load_products():
    src = open(os.path.join(ROOT, "js", "products.js"), encoding="utf-8").read()
    body = src[src.index("window.PRODUCTS = ["):]
    items = []
    for block in re.findall(r"\{(.*?)\n    \}", body, re.S):
        item = {}
        for k, v in re.findall(r"(\w+):\s*'((?:[^'\\]|\\.)*)'", block):
            item[k] = v.replace("\\'", "'")
        for k, v in re.findall(r"(\w+):\s*(\d+),", block):
            item[k] = int(v)
        if "key" in item:
            items.append(item)
    return items


PRODUCTS = load_products()

# Plan SKUs ship as posters, not photographs — swap in a real device cutout.
PLAN_IMAGE = {
    "desktop-rental-plan": "dell-optiplex-3060-desktop",
    "desktop-rental-monthly-plan-basic": "dell-optiplex-3060-desktop",
    "desktop-rental-monthly-plan-mid-range": "hp-elitedesk-800-g3-desktop",
    "desktop-rental-monthly-plan-mid-range-2": "hp-elitedesk-800-g3-desktop",
    "desktop-rental-monthly-plan-advanced": "dell-optiplex-5080sff-desktop",
    "desktop-rental-monthly-plan-advanced-2": "dell-optiplex-5080sff-desktop",
    "laptop-rental-monthly-plan-basic": "dell-latitude-3400-laptop",
    "laptop-rental-monthly-plan-basic-2": "dell-latitude-3400-laptop",
    "laptop-rental-monthly-plan-mid-range": "dell-latitude-5400-laptop",
    "laptop-rental-monthly-plan-mid-range-2": "dell-latitude-5400-laptop",
    "laptop-rental-monthly-plan-advanced": "dell-latitude-5420-laptop",
    "laptop-rental-monthly-plan-advanced-2": "dell-latitude-5420-laptop",
    "apple-macbook-air-m2-short-rental-plan": "apple-macbook-air-m2",
    "laptop-rental-plan-macbook": "apple-macbook-air-m2",
}

CATEGORY_LABEL = {
    "short-term": "Short term",
    "long-term": "Long term",
    "new-laptop": "New laptop",
    "new-desktop": "New desktop",
    "ref-laptop": "Refurbished laptop",
    "ref-desktop": "Refurbished desktop",
    "others": "Software",
}


def image_for(p, index=1):
    base = PLAN_IMAGE.get(p["key"], p["key"])
    path = "img/tiles/%s-%d.webp" % (base, index)
    if os.path.exists(os.path.join(ROOT, path)):
        return path
    return "img/tiles/%s-1.webp" % base


def e(s):
    return html.escape(str(s), quote=True)


# ------------------------------------------------------------------- chrome

def head(meta):
    return """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>{title}</title>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
<meta name="description" content="{description}" />
<meta name="theme-color" content="#ffffff" />
<meta property="og:title" content="{title}" />
<meta property="og:description" content="{description}" />
<meta property="og:type" content="website" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap" />
<link rel="stylesheet" href="css/app.css?v={ver}" />
<link rel="icon" href="img/mark-512.png" />
</head>
<body>""".format(ver=VER, **{k: e(v) for k, v in meta.items()})


def header(current=""):
    links = "\n".join(
        '        <a href="{0}"{2}>{1}</a>'.format(
            href, label, ' aria-current="page"' if href == current else ""
        )
        for href, label in C.NAV
    )
    return """
  <header class="header">
    <div class="container header__inner">
      <nav class="nav">
{links}
      </nav>
      <button class="nav-toggle" type="button" aria-expanded="false">Menu</button>
      <a class="brand" href="index.html" aria-label="MAXRENTAL home">
        <img src="img/logo-ink.png" alt="MAXRENTAL" width="176" height="37" />
      </a>
      <div class="header__end">
        <a href="contact.html">Contact</a>
        <button class="header__cart" type="button" data-open-cart
                aria-haspopup="dialog" aria-expanded="false">Cart
          <span class="cart-badge" data-cart-count hidden>0</span>
        </button>
      </div>
    </div>
  </header>""".format(links=links)


def footer():
    addr = "<br />".join(e(l) for l in C.COMPANY["address"])
    return """
  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div>
          <img src="img/logo-white.png" alt="MAXRENTAL" width="196" height="41"
               style="margin-bottom:16px" />
          <p class="t-meta" style="max-width:30ch">
            Office IT rental and support across Malaysia since 2006.
          </p>
        </div>
        <div>
          <h4>Rent</h4>
          <ul>
            <li><a href="short-term.html">Short term</a></li>
            <li><a href="long-term.html">Long term</a></li>
            <li><a href="products.html">All equipment</a></li>
          </ul>
        </div>
        <div>
          <h4>Services</h4>
          <ul>
            <li><a href="services.html">PC sales</a></li>
            <li><a href="services.html">IT support</a></li>
            <li><a href="services.html">Backup solutions</a></li>
          </ul>
        </div>
        <div>
          <h4>Company</h4>
          <ul>
            <li><a href="about.html">About</a></li>
            <li><a href="news.html">Journal</a></li>
            <li><a href="contact.html">Contact</a></li>
            <li><a href="{instagram}" target="_blank" rel="noopener">Instagram</a></li>
          </ul>
        </div>
        <div>
          <h4>Get in touch</h4>
          <ul>
            <li>{addr}</li>
            <li><a href="mailto:{email}">{email}</a></li>
            <li><a href="tel:{phone_href}">{phone}</a></li>
          </ul>
        </div>
      </div>
      <div class="footer__legal">
        <span>&copy; {year} {legal} &middot; {reg}</span>
        <span>
          <a href="terms.html">Terms</a> &nbsp;
          <a href="privacy.html">Privacy</a>
        </span>
      </div>
    </div>
  </footer>""".format(addr=addr, **{k: e(v) for k, v in C.COMPANY.items() if isinstance(v, str)})


def tail():
    return """
  <script src="js/products.js?v={ver}"></script>
  <script>window.MR_PLAN_IMAGE = {plan_map};</script>
  <script src="js/app.js?v={ver}"></script>
</body>
</html>
""".format(ver=VER, plan_map=str(PLAN_IMAGE).replace("'", '"'))



def cart_drawer():
    """Shopping cart.

    Rentals bill monthly and outright purchases bill once, so the two can never
    be summed into a single figure; the footer keeps them on separate lines.

    NOTE: there is no payment gateway yet. Checkout routes to the contact form
    as a placeholder — swap that href for the gateway's session URL when it
    exists, and the totals here are what it should be handed.
    """
    return """
  <div class="cart" data-cart-drawer hidden>
    <div class="cart__scrim" data-close-cart></div>
    <aside class="cart__panel" role="dialog" aria-modal="true" aria-label="Cart">
      <header class="cart__head">
        <h2 class="cart__title">Cart</h2>
        <button class="cart__x" type="button" data-close-cart aria-label="Close">&times;</button>
      </header>

      <div class="cart__body" data-cart-body></div>

      <footer class="cart__foot" data-cart-foot hidden>
        <div class="cart__sum" data-sum-rent hidden>
          <span>Monthly rental</span>
          <strong data-cart-rent>RM0</strong>
        </div>
        <div class="cart__sum" data-sum-buy hidden>
          <span>One-off purchase</span>
          <strong data-cart-buy>RM0</strong>
        </div>
        <p class="cart__note">
          Rental prices are per desk, per month. Delivery and installation included.
        </p>
        <!-- Placeholder target: point this at the payment gateway once it exists. -->
        <a class="pill cart__cta" href="contact.html">Checkout</a>
        <button class="cart__clear" type="button" data-clear-cart>Clear cart</button>
      </footer>
    </aside>
  </div>"""


def page(meta, body, current=""):
    return (head(meta) + header(current) + "\n  <main>" + body + "\n  </main>"
            + footer() + cart_drawer() + tail())


# -------------------------------------------------------------- components

def title_case(t):
    """The catalogue ships names shouting in caps; display them in title case.

    Mirrors the same function in the product page's inline JS, so a card and
    the page it opens agree.
    """
    keep = {"ssd", "ram", "hdd", "sff", "hp", "pc", "i3", "i5", "i7", "gb", "tb"}
    out = []
    for w in str(t).split():
        out.append(w.upper() if w.lower().strip(",.") in keep else w.capitalize())
    return " ".join(out)


def product_card(p, delay=0):
    cat = CATEGORY_LABEL.get(p["collection"], p["collection"])
    price_html = (
        '<span class="pcard__was">%s</span>%s' % (e(p["was"]), e(p["price"]))
        if p.get("was") else e(p["price"])
    )
    badge = ""
    if p.get("was"):
        badge = '<span class="pcard__badge pcard__badge--sale">Sale</span>'
    elif p["collection"] in ("new-laptop", "new-desktop"):
        badge = '<span class="pcard__badge">New</span>'

    return """
          <a class="pcard reveal" data-reveal-delay="{delay}" data-collection="{coll}"
             href="product.html?model={key}">
            <div class="pcard__media">
              {badge}
              <button class="pcard__fav" type="button" data-fav="{key}"
                      aria-pressed="false" aria-label="Save {name}">&#9825;</button>
              <img class="is-base" src="{img1}" alt="{name}" loading="lazy" />
              <img class="is-hover" src="{img2}" alt="" aria-hidden="true" loading="lazy" />
            </div>
            <div class="pcard__body">
              <span class="pcard__name">{disp}</span>
              <span class="pcard__price">{price}</span>
              <span class="pcard__cat">{cat}</span>
            </div>
          </a>""".format(
        delay=delay, coll=e(p["collection"]), key=e(p["key"]), name=e(p["name"]),
        price=price_html, cat=e(cat), badge=badge, disp=e(title_case(p["name"])),
        img1=image_for(p, 1), img2=image_for(p, 2),
    )


def product_grid(items, start_delay=0):
    return "\n".join(product_card(p, (i % 4) * 60 + start_delay) for i, p in enumerate(items))


def tier_row(tiers, panel, group, hidden=False):
    cards = []
    for name, price, spec in tiers:
        includes = "\n".join(
            "                <li>%s</li>" % e(i) for i in C.PLAN_INCLUDES
        )
        cards.append("""
            <div class="reveal" style="border:1px solid var(--rule);border-radius:var(--r-media);padding:22px">
              <p class="t-meta">{name}</p>
              <p class="t-h2" style="margin-top:14px">{price}<span class="t-meta"> / month</span></p>
              <p class="t-body grey" style="margin-top:12px">{spec}</p>
              <ul style="margin-top:16px;border-top:1px solid var(--rule)">
{includes}
              </ul>
              <p style="margin-top:18px"><a class="pill" href="contact.html">Talk to us</a></p>
            </div>""".format(name=e(name), price=e(price), spec=e(spec), includes=includes))

    return """
        <div class="grid grid--3" data-tab-panel="{panel}" data-tabs-for="{group}"{hidden}>
{cards}
        </div>""".format(panel=panel, group=group, cards="\n".join(cards),
                         hidden=" hidden" if hidden else "")


# ------------------------------------------------------------------- pages

def hero_slides(slides):
    """Markup for the hero slideshow.

    Only the first slide's video carries a src; the rest are handed over as
    data- attributes and set when that slide first becomes active, so landing
    on the page downloads one film rather than three.
    """
    out, dots = [], []
    for i, sl in enumerate(slides):
        active = " is-active" if i == 0 else ""
        tone = " hero__slide--light" if sl.get("tone") == "light" else ""

        if sl["media"] == "video":
            attrs = (
                'data-wide="{src}" data-wide-poster="{poster}" '
                'data-tall="{tall}" data-tall-poster="{tallposter}"'
            ).format(src=sl["src"], poster=sl["poster"],
                     tall=sl["src_tall"], tallposter=sl["poster_tall"])
            media = ('<video autoplay loop muted playsinline preload="{pre}" '
                     'poster="{poster}" {attrs}></video>').format(
                         pre="auto" if i == 0 else "none",
                         poster=sl["poster"], attrs=attrs)
        else:
            media = '<img src="{src}" alt="" {load}/>'.format(
                src=sl["src"], load="" if i == 0 else 'loading="lazy" ')

        out.append("""
      <div class="hero__slide{tone}{active}" data-slide="{i}" aria-hidden="{hidden}">
        {media}
        <div class="hero__scrim"></div>
        <div class="container hero__inner">
          <p class="hero__eyebrow">{eyebrow}</p>
          <h1>{h1}</h1>
          <div class="hero__actions">
            <a class="pill {btn}" href="{href}">{cta}</a>
          </div>
        </div>
      </div>""".format(
            tone=tone, active=active, i=i, hidden="false" if i == 0 else "true",
            media=media, eyebrow=e(sl["eyebrow"]), h1=e(sl["h1"]),
            href=sl["href"], cta=e(sl["cta"]),
            btn="pill--dark" if sl.get("tone") == "light" else "pill--light"))

        dots.append(
            '        <button type="button" class="hero__dot{active}" data-goto="{i}" '
            'role="tab" aria-selected="{sel}" aria-label="Slide {n}">'
            '<span class="hero__dot-fill"></span></button>'.format(
                active=" is-active" if i == 0 else "", i=i,
                sel="true" if i == 0 else "false", n=i + 1))

    return "\n".join(out), "\n".join(dots)


def build_home():
    H = C.HOME
    slides, dots = hero_slides(H["hero_slides"])

    plans = [p for p in PRODUCTS if p["collection"] in ("short-term", "long-term")][:8]
    laptops = [p for p in PRODUCTS if "laptop" in p["collection"]][:8]
    desktops = [p for p in PRODUCTS if "desktop" in p["collection"]][:8]

    marquee = '<div class="marquee__set">%s</div>' % "".join(
        '<span><img src="img/brands/%s" alt="%s" height="%d" /></span>'
        % (f, e(n), h) for n, f, h in H["marquee"])

    tab_buttons = "\n".join(
        '          <button type="button" data-tab="{0}" aria-selected="{2}">{1}</button>'.format(
            slug, label, "true" if i == 0 else "false")
        for i, (slug, label) in enumerate(H["tabs"])
    )

    cats = "\n".join("""
          <a class="cat reveal" data-reveal-delay="{d}" href="{href}">
            <img src="{img}" alt="{label}" loading="lazy" />
            <span class="cat__label">{label}</span>
          </a>""".format(d=i * 80, href=href, label=e(label), img=img)
        for i, (href, label, img) in enumerate(H["cats"]))

    trust = "\n".join("""
          <div class="reveal" data-reveal-delay="{d}">
            <h4>{t}</h4>
            <p>{s}</p>
          </div>""".format(d=i * 60, t=e(t), s=e(s))
        for i, (t, s) in enumerate(H["trust"]))

    journal = "\n".join("""
          <a class="post reveal" data-reveal-delay="{d}" href="news.html">
            <div class="post__media"><img src="{img}" alt="" loading="lazy" /></div>
            <p class="post__tag">{tag}</p>
            <h3>{title}</h3>
            <p class="post__more link-more">Read more</p>
          </a>""".format(d=i * 80, tag=e(tag), title=e(title), img=img)
        for i, (tag, title, img) in enumerate(C.JOURNAL))

    quotes = "".join("""
        <figure class="quote">
          <figcaption class="quote__who">{who}</figcaption>
          <p>&ldquo;{text}&rdquo;</p>
          <p class="quote__product">{prod}</p>
        </figure>""".format(who=e(who), text=e(text), prod=e(prod))
        for who, text, prod in C.REVIEWS) * 2

    body = """
    <section class="hero" data-hero>
{slides}
      <div class="hero__dots" role="tablist" aria-label="Hero slides">
{dots}
      </div>
    </section>

    <section class="marquee">
      <div class="container"><p class="marquee__label">{marquee_label}</p></div>
      <div class="marquee__track">{marquee}</div>
    </section>

    <section class="section container">
      <div class="section-head">
        <div class="tabs" data-tabs="home">
{tab_buttons}
        </div>
        <a class="link-more" href="products.html">All equipment</a>
      </div>
      <div class="grid" data-tab-panel="plans" data-tabs-for="home">
{plans}
      </div>
      <div class="grid" data-tab-panel="laptops" data-tabs-for="home" hidden>
{laptops}
      </div>
      <div class="grid" data-tab-panel="desktops" data-tabs-for="home" hidden>
{desktops}
      </div>
    </section>

    <section class="section--tight container">
      <div class="section-head"><h2>{cats_head}</h2></div>
      <div class="grid grid--3">
{cats}
      </div>
    </section>

    <section class="band-navy">
      <div class="container">
        <h2 class="statement reveal">{statement}</h2>
        <p class="t-lead reveal" data-reveal-delay="80" style="margin-top:20px;max-width:52ch">{statement_sub}</p>
      </div>
    </section>

    <section class="section--tight container">
      <div class="band reveal">
        <img src="img/editorial/band-team.jpg" alt="The MMX Solutions team preparing rental laptops in Kepong" />
        <div class="band__inner">
          <h2>{band_head}</h2>
          <p class="t-body">{band_copy}</p>
          <p style="margin-top:22px"><a class="pill pill--light" href="about.html">{band_cta}</a></p>
        </div>
      </div>
    </section>

    <section class="section container">
      <div class="trust">
{trust}
      </div>
    </section>

    <section class="section--tight container">
      <div class="section-head">
        <h2>{journal_head}</h2>
        <a class="link-more" href="news.html">All posts</a>
      </div>
      <div class="grid grid--3">
{journal}
      </div>
    </section>

    <section class="quotes">
      <div class="container"><h2 style="margin-bottom:26px">{quotes_head}</h2></div>
      <div class="quotes__track">{quotes}</div>
    </section>
""".format(
        marquee=marquee, tab_buttons=tab_buttons,
        plans=product_grid(plans), laptops=product_grid(laptops), desktops=product_grid(desktops),
        cats=cats, trust=trust, journal=journal, quotes=quotes,
        slides=slides, dots=dots,
        **{k: e(v) for k, v in H.items() if isinstance(v, str)}
    )
    return page(H, body)


def build_products():
    meta = {
        "title": "Equipment — MAXRENTAL",
        "description": "Every laptop, desktop and rental plan MAXRENTAL offers, from Dell, HP and Lenovo.",
    }
    options = "\n".join(
        '            <option value="%s">%s</option>' % (slug, e(label))
        for slug, label in CATEGORY_LABEL.items()
        if any(p["collection"] == slug for p in PRODUCTS)
    )
    body = """
    <section class="section--tight container">
      <h1 class="reveal">Equipment</h1>
      <div class="section-head" style="margin-top:26px">
        <p class="t-meta">{n} products</p>
        <label class="t-meta">
          Filter
          <select data-filter style="margin-left:8px;font:inherit;border:0;background:none">
            <option value="all">All categories</option>
{options}
          </select>
        </label>
      </div>
      <div class="grid">
{grid}
      </div>
      <p class="t-lead" data-filter-empty hidden style="padding-block:40px">
        Nothing in this category yet. <a class="link-more" href="contact.html">Ask us what's coming</a>
      </p>
    </section>
""".format(n=len(PRODUCTS), options=options, grid=product_grid(PRODUCTS))
    return page(meta, body, "products.html")


def build_plan(slug):
    P = C.PLANS[slug]
    addons = "\n".join(
        '            <li style="display:flex;justify-content:space-between;gap:16px;'
        'padding:10px 0;border-top:1px solid var(--rule)">'
        '<span>%s</span><span class="grey">%s</span></li>' % (e(n), e(p))
        for n, p in C.ADDONS
    )
    body = """
    <section class="section--tight container">
      <h1 class="reveal">{h1}</h1>
      <p class="t-lead reveal" data-reveal-delay="60" style="margin-top:16px;max-width:52ch">{lead}</p>

      <div class="section-head" style="margin-top:40px">
        <div class="tabs" data-tabs="plan">
          <button type="button" data-tab="desktop" aria-selected="true">Desktop</button>
          <button type="button" data-tab="laptop" aria-selected="false">Laptop</button>
        </div>
        <p class="t-meta">{terms}</p>
      </div>
{desktop}
{laptop}

      <div class="grid grid--2" style="margin-top:56px;align-items:start">
        <div class="reveal">
          <h2>Optional add-ons</h2>
          <ul style="margin-top:18px">
{addons}
          </ul>
          <p class="t-meta" style="margin-top:12px">Prices include 6% SST.</p>
        </div>
        <div class="reveal" data-reveal-delay="80">
          <h2>Also available</h2>
          <p class="t-body grey" style="margin-top:14px">
            Looking for a different commitment? {other_label} runs on {other_terms}.
          </p>
          <p style="margin-top:20px"><a class="pill" href="{other}">{other_label}</a></p>
        </div>
      </div>
    </section>
""".format(
        desktop=tier_row(P["desktop"], "desktop", "plan"),
        laptop=tier_row(P["laptop"], "laptop", "plan", hidden=True),
        addons=addons,
        other_terms=e(C.PLANS[P["other"].replace(".html", "")]["terms"]),
        **{k: e(v) for k, v in P.items() if isinstance(v, str)}
    )
    return page(P, body, slug + ".html")


def build_services():
    S = C.SERVICES
    items = "\n".join("""
        <article class="reveal" data-reveal-delay="{d}" style="border-top:1px solid var(--rule);padding-top:22px">
          <h2>{name}</h2>
          <p class="t-body grey" style="margin-top:14px;max-width:46ch">{copy}</p>
          <ul style="margin-top:18px">
{bullets}
          </ul>
        </article>""".format(
            d=i * 80, name=e(name), copy=e(copy),
            bullets="\n".join(
                '            <li class="t-meta" style="padding:7px 0;border-bottom:1px solid var(--rule)">%s</li>' % e(b)
                for b in bullets))
        for i, (name, copy, bullets) in enumerate(S["items"]))

    body = """
    <section class="section--tight container">
      <h1 class="reveal">{h1}</h1>
      <p class="t-lead reveal" data-reveal-delay="60" style="margin-top:16px;max-width:54ch">{lead}</p>
      <div class="grid grid--3" style="margin-top:48px;align-items:start">
{items}
      </div>
      <div class="band reveal" style="margin-top:64px">
        <img src="img/editorial/band-support.jpg" alt="An MMX technician servicing a rental laptop" />
        <div class="band__inner">
          <h2>Support that doesn't stop at delivery</h2>
          <p class="t-body">Raise a ticket on WhatsApp {support}. Remote first, on-site within the Klang Valley. {hours}, excluding public holidays.</p>
          <p style="margin-top:22px"><a class="pill pill--light" href="contact.html">Talk to the team</a></p>
        </div>
      </div>
    </section>
""".format(items=items, support=e(C.COMPANY["support"]), hours=e(C.COMPANY["hours"]),
           **{k: e(v) for k, v in S.items() if isinstance(v, str)})
    return page(S, body, "services.html")


def build_about():
    A = C.ABOUT
    paras = "\n".join(
        '        <p class="t-lead reveal" data-reveal-delay="%d" style="margin-top:20px">%s</p>' % (i * 60, e(p))
        for i, p in enumerate(A["body"]))
    timeline = "\n".join("""
          <div class="reveal" data-reveal-delay="{d}"
               style="display:grid;grid-template-columns:72px 1fr;gap:18px;padding:14px 0;border-top:1px solid var(--rule)">
            <span class="t-meta" style="color:var(--accent-deep)">{y}</span>
            <span class="t-body grey">{t}</span>
          </div>""".format(d=i * 50, y=e(y), t=e(t))
        for i, (y, t) in enumerate(A["timeline"]))

    body = """
    <section class="section--tight container">
      <h1 class="statement reveal" style="max-width:20ch">{h1}</h1>
    </section>

    <section class="container">
      <div class="band reveal" style="min-height:clamp(280px,34vw,460px)">
        <img src="img/editorial/premises-wide.jpg" alt="MMX Solutions, Kepong" />
        <div class="band__inner">
          <p class="t-meta" style="color:rgba(255,255,255,.7)">Kepong, Kuala Lumpur</p>
        </div>
      </div>
    </section>

    <section class="section container">
      <div class="grid grid--2" style="align-items:start">
        <div>
{paras}
        </div>
        <div>
{timeline}
        </div>
      </div>
    </section>
""".format(paras=paras, timeline=timeline, **{k: e(v) for k, v in A.items() if isinstance(v, str)})
    return page(A, body, "about.html")


def build_news():
    meta = {
        "title": "Journal — MAXRENTAL",
        "description": "Company news and practical guides from MMX Solutions.",
    }
    posts = "\n".join("""
          <a class="post reveal" data-reveal-delay="{d}" href="#">
            <div class="post__media"><img src="{img}" alt="" loading="lazy" /></div>
            <p class="post__tag">{tag}</p>
            <h3>{title}</h3>
            <p class="post__more link-more">Read more</p>
          </a>""".format(d=(i % 3) * 80, tag=e(tag), title=e(title), img=img)
        for i, (tag, title, img) in enumerate(C.JOURNAL))
    body = """
    <section class="section--tight container">
      <h1 class="reveal">Journal</h1>
      <div class="grid grid--3" style="margin-top:40px">
{posts}
      </div>
    </section>
""".format(posts=posts)
    return page(meta, body, "news.html")


def build_contact():
    K = C.CONTACT
    topics = "\n".join('            <option>%s</option>' % e(t) for t in K["topics"])
    addr = "<br />".join(e(l) for l in C.COMPANY["address"])
    field = ('<label style="display:block;margin-bottom:18px">'
             '<span class="t-meta">{label}</span>'
             '<{tag} {attrs} style="display:block;width:100%;margin-top:6px;padding:11px 0;'
             'font:inherit;border:0;border-bottom:1px solid var(--rule);background:none"></{tag}>'
             '</label>')
    body = """
    <section class="section--tight container">
      <div class="grid grid--2" style="align-items:start;gap:48px 40px">
        <div>
          <h1 class="reveal">{h1}</h1>
          <p class="t-lead reveal" data-reveal-delay="60" style="margin-top:16px;max-width:40ch">{lead}</p>
          <div class="reveal" data-reveal-delay="120" style="margin-top:36px">
            <p class="t-body">{addr}</p>
            <p class="t-body" style="margin-top:14px">
              <a href="mailto:{email}">{email}</a><br />
              <a href="tel:{phone_href}">{phone}</a><br />
              Support: WhatsApp {support}
            </p>
            <p class="t-meta" style="margin-top:14px">{hours}, excluding public holidays</p>
          </div>
        </div>
        <form class="reveal" data-reveal-delay="80" onsubmit="return false">
          {name}
          {company}
          {email_f}
          <label style="display:block;margin-bottom:18px">
            <span class="t-meta">Topic</span>
            <select style="display:block;width:100%;margin-top:6px;padding:11px 0;font:inherit;border:0;border-bottom:1px solid var(--rule);background:none">
{topics}
            </select>
          </label>
          <label style="display:block;margin-bottom:24px">
            <span class="t-meta">How many desks, and what for?</span>
            <textarea rows="4" style="display:block;width:100%;margin-top:6px;padding:11px 0;font:inherit;border:0;border-bottom:1px solid var(--rule);background:none"></textarea>
          </label>
          <button class="pill" type="submit">Send enquiry</button>
        </form>
      </div>
    </section>
""".format(
        topics=topics, addr=addr,
        name=field.format(label="Name", tag="input", attrs='type="text"'),
        company=field.format(label="Company", tag="input", attrs='type="text"'),
        email_f=field.format(label="Email", tag="input", attrs='type="email"'),
        email=e(C.COMPANY["email"]), phone=e(C.COMPANY["phone"]),
        phone_href=e(C.COMPANY["phone_href"]), support=e(C.COMPANY["support"]),
        hours=e(C.COMPANY["hours"]),
        **{k: e(v) for k, v in K.items() if isinstance(v, str)}
    )
    return page(K, body, "contact.html")


def build_legal(which):
    L = C.LEGAL[which]
    blocks = "\n".join("""
        <div class="reveal" data-reveal-delay="{d}" style="border-top:1px solid var(--rule);padding:22px 0">
          <h3>{t}</h3>
          <p class="t-body grey" style="margin-top:12px;max-width:68ch">{b}</p>
        </div>""".format(d=min(i, 4) * 50, t=e(t), b=e(b))
        for i, (t, b) in enumerate(L["blocks"]))
    body = """
    <section class="section--tight container">
      <h1 class="reveal">{h1}</h1>
      <div style="margin-top:36px">
{blocks}
      </div>
    </section>
""".format(blocks=blocks, **{k: e(v) for k, v in L.items() if isinstance(v, str)})
    return page(L, body)


def tile_counts():
    """How many tile images exist per product base, for the gallery rail."""
    counts = {}
    for f in os.listdir(os.path.join(ROOT, "img", "tiles")):
        m = re.match(r"^(.*)-(\d+)\.webp$", f)
        if m:
            counts[m.group(1)] = max(counts.get(m.group(1), 0), int(m.group(2)))
    return counts


def build_product():
    """The single-equipment page.

    Everything is hydrated client-side from js/products.js so one file serves
    all 30 SKUs via ?model=. The layout follows the reference product page:
    thumbnail rail beside a large image, a buy column with variant and
    quantity controls and accordions, then a detail band, a spec list and a
    related row.
    """
    meta = {
        "title": "Equipment detail — MAXRENTAL",
        "description": "Specification, pricing and rental terms for MAXRENTAL equipment.",
    }
    includes = "".join("<li>%s</li>" % e(x) for x in C.PLAN_INCLUDES)
    addons = "".join(
        '<li><span>%s</span><span class="grey">%s</span></li>' % (e(n), e(pr))
        for n, pr in C.ADDONS)

    body = """
    <section class="section--tight container">
      <p class="t-meta pdp__back"><a href="products.html">&larr; All equipment</a></p>

      <div class="pdp">
        <div class="pdp__gallery">
          <div class="pdp__thumbs" data-thumbs></div>
          <div class="pdp__stage"><img data-stage alt="" /></div>
        </div>

        <div class="pdp__buy">
          <div class="pdp__head">
            <div>
              <p class="t-meta" data-cat></p>
              <h1 data-name>Equipment</h1>
            </div>
            <button class="fav" type="button" data-fav="" aria-label="Save">&#9825;</button>
          </div>

          <p class="pdp__price"><span data-price></span><s class="grey" data-was hidden></s></p>
          <p class="t-body grey pdp__spec" data-spec></p>

          <div class="pdp__field" data-term-field hidden>
            <p class="t-meta">Rental term</p>
            <div class="chips" data-terms></div>
          </div>

          <div class="pdp__cart">
            <div class="qty">
              <button type="button" data-qty="-1" aria-label="Fewer">&minus;</button>
              <input type="text" inputmode="numeric" value="1" data-qty-value aria-label="Quantity" />
              <button type="button" data-qty="1" aria-label="More">+</button>
            </div>
            <button class="pill pdp__add" type="button" data-add-cart="">Add to cart</button>
          </div>
          <p class="t-meta"><a class="link-more" href="terms.html">Delivery, support and returns</a></p>

          <div class="acc">
            <details open>
              <summary>Specification</summary>
              <div class="acc__body"><p class="t-body grey" data-acc-spec></p></div>
            </details>
            <details>
              <summary>What's included</summary>
              <div class="acc__body"><ul class="ticks">{includes}</ul></div>
            </details>
            <details>
              <summary>Rental terms</summary>
              <div class="acc__body" data-acc-terms></div>
            </details>
            <details>
              <summary>Optional add-ons</summary>
              <div class="acc__body"><ul class="rows">{addons}</ul></div>
            </details>
          </div>
        </div>
      </div>
    </section>

    <section class="pdp__detail">
      <div class="pdp__detail-media"><img data-detail alt="" /></div>
      <div class="pdp__detail-copy">
        <div>
          <p class="t-meta grey">How it ships</p>
          <p class="t-lead">Delivered and installed anywhere in the Klang Valley, configured and
             joined to your network before we leave. Elsewhere in Malaysia by courier.</p>
        </div>
        <div style="margin-top:34px">
          <p class="t-meta grey">Support</p>
          <p class="t-lead">Raise a ticket on WhatsApp {support}. Remote first, on-site when it
             needs hands. {hours}, excluding public holidays.</p>
        </div>
      </div>
    </section>

    <section class="section container">
      <div class="grid grid--2" style="align-items:start;gap:48px">
        <div>
          <p class="t-meta">Key specification</p>
          <ul class="speclist" data-speclist></ul>
        </div>
        <div class="pdp__panel"><img data-panel alt="" /></div>
      </div>
    </section>

    <section class="section--tight container">
      <div class="section-head"><h2>More like this</h2>
        <a class="link-more" href="products.html">All equipment</a></div>
      <div class="grid" data-related></div>
    </section>

    <script>
      /* products.js now loads at the end of the body so every page's cart
         can read it, which puts it after this block in document order.
         Wait for DOMContentLoaded, by which point it has run. */
      document.addEventListener('DOMContentLoaded', function () {{
        var PLAN = window.MR_PLAN_IMAGE || {{}};
        var CAT = {cat_map};
        var TILES = {tiles};
        var all = window.PRODUCTS || [];
        var q = new URLSearchParams(location.search).get('model');
        var p = all.filter(function (x) {{ return x.key === q; }})[0] || all[0];
        if (!p) return;

        var base = PLAN[p.key] || p.key;
        var n = TILES[base] || 1;
        var img = function (i) {{ return 'img/tiles/' + base + '-' + i + '.webp'; }};

        /* Title case: the catalogue ships names shouting in caps. */
        function title(t) {{
          return String(t).toLowerCase().replace(/\\b([a-z])/g, function (m) {{ return m.toUpperCase(); }})
                  .replace(/\\b(Ssd|Ram|Hdd|Sff|Hp|Pc|I3|I5|I7|Gb|Tb)\\b/gi, function (m) {{ return m.toUpperCase(); }});
        }}

        var stage = document.querySelector('[data-stage]');
        stage.src = img(1);
        stage.alt = p.name;

        var rail = document.querySelector('[data-thumbs]');
        if (n > 1) {{
          for (var i = 1; i <= n; i++) {{
            var b = document.createElement('button');
            b.type = 'button';
            b.className = 'pdp__thumb' + (i === 1 ? ' is-active' : '');
            b.innerHTML = '<img src="' + img(i) + '" alt="" loading="lazy" />';
            (function (src, el) {{
              el.addEventListener('click', function () {{
                stage.src = src;
                rail.querySelectorAll('.pdp__thumb').forEach(function (x) {{ x.classList.remove('is-active'); }});
                el.classList.add('is-active');
              }});
            }})(img(i), b);
            rail.appendChild(b);
          }}
        }} else {{
          rail.hidden = true;
        }}

        document.querySelector('[data-cat]').textContent = CAT[p.collection] || '';
        document.querySelector('[data-name]').textContent = title(p.name);
        document.querySelector('[data-price]').textContent = p.price;
        if (p.was) {{
          var w = document.querySelector('[data-was]');
          w.textContent = p.was; w.hidden = false;
        }}
        document.querySelector('[data-spec]').textContent = p.spec || '';
        document.querySelector('[data-acc-spec]').textContent = p.spec || 'Ask us for the full specification.';
        document.querySelector('[data-add-cart]').setAttribute('data-add-cart', p.key);
        document.querySelector('[data-fav]').setAttribute('data-fav', p.key);
        document.querySelector('[data-detail]').src = img(Math.min(2, n));
        document.querySelector('[data-panel]').src = img(Math.min(3, n));

        /* Rental term reads as a variant selector, the way the reference
           offers sizes. It is carried into the cart line, not a price change. */
        if (p.terms) {{
          document.querySelector('[data-term-field]').hidden = false;
          var wrap = document.querySelector('[data-terms]');
          p.terms.split('/').map(function (t) {{ return t.trim(); }}).forEach(function (t, i) {{
            var b = document.createElement('button');
            b.type = 'button';
            b.className = 'chip' + (i === 0 ? ' is-active' : '');
            var num = t.replace(/[^0-9]/g, '');
            b.textContent = num + (num === '1' ? ' month' : ' months');
            b.addEventListener('click', function () {{
              wrap.querySelectorAll('.chip').forEach(function (x) {{ x.classList.remove('is-active'); }});
              b.classList.add('is-active');
            }});
            wrap.appendChild(b);
          }});
        }}

        var rows = [];
        if (p.terms) rows.push(['Rental term', p.terms]);
        if (p.warranty) rows.push(['Warranty', p.warranty]);
        if (p.note) rows.push(['Note', p.note]);
        rows.push(['Minimum order', 'No minimum. Single units welcome.']);
        document.querySelector('[data-acc-terms]').innerHTML =
          '<ul class="rows">' + rows.map(function (r) {{
            return '<li><span>' + r[0] + '</span><span class="grey">' + r[1] + '</span></li>';
          }}).join('') + '</ul>';

        document.querySelector('[data-speclist]').innerHTML =
          (p.spec || '').split(',').map(function (t) {{ return t.trim(); }})
            .filter(Boolean).map(function (t) {{ return '<li>' + t + '</li>'; }}).join('')
          || '<li>Specification on request</li>';

        var rel = all.filter(function (x) {{ return x.collection === p.collection && x.key !== p.key; }}).slice(0, 3);
        if (!rel.length) rel = all.filter(function (x) {{ return x.key !== p.key; }}).slice(0, 3);
        document.querySelector('[data-related]').innerHTML = rel.map(function (x) {{
          var b = PLAN[x.key] || x.key;
          var m = TILES[b] || 1;
          var one = 'img/tiles/' + b + '-1.webp';
          var two = 'img/tiles/' + b + '-' + Math.min(2, m) + '.webp';
          return '<a class="pcard" href="product.html?model=' + x.key + '">' +
                 '<div class="pcard__media">' +
                 '<img class="is-base" src="' + one + '" alt="" loading="lazy" />' +
                 '<img class="is-hover" src="' + two + '" alt="" aria-hidden="true" loading="lazy" />' +
                 '</div>' +
                 '<div class="pcard__body">' +
                 '<span class="pcard__name">' + title(x.name) + '</span>' +
                 '<span class="pcard__price">' + x.price + '</span>' +
                 '<span class="pcard__cat">' + (CAT[x.collection] || '') + '</span>' +
                 '</div></a>';
        }}).join('');

        /* Quantity is read by the cart when the item is added. */
        var qty = document.querySelector('[data-qty-value]');
        document.querySelectorAll('[data-qty]').forEach(function (b) {{
          b.addEventListener('click', function () {{
            var v = Math.max(1, (parseInt(qty.value, 10) || 1) + Number(b.dataset.qty));
            qty.value = v;
          }});
        }});

        document.title = title(p.name) + ' — MAXRENTAL';
      }});
    </script>
""".format(ver=VER, includes=includes, addons=addons,
           support=e(C.COMPANY["support"]), hours=e(C.COMPANY["hours"]),
           cat_map=str(CATEGORY_LABEL).replace("'", '"'),
           tiles=str(tile_counts()).replace("'", '"'))
    return page(meta, body, "products.html")


PAGES = {
    "index.html": build_home,
    "products.html": build_products,
    "product.html": build_product,
    "short-term.html": lambda: build_plan("short-term"),
    "long-term.html": lambda: build_plan("long-term"),
    "services.html": build_services,
    "about.html": build_about,
    "news.html": build_news,
    "contact.html": build_contact,
    "terms.html": lambda: build_legal("terms"),
    "privacy.html": lambda: build_legal("privacy"),
}


def main():
    for name, fn in PAGES.items():
        out = fn()
        with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
            f.write(out)
        print("%-20s %6d bytes" % (name, len(out)))
    print("\n%d pages, %d products" % (len(PAGES), len(PRODUCTS)))


if __name__ == "__main__":
    main()
