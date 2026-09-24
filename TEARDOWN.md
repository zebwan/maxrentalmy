# all-natural.framer.website — teardown

Reference for MAXRENTAL v2. Measured from the live site on 24 Sep 2026.

A commercial **Framer e-commerce template** ("All Natural™"), skincare brand.
Framer build `570e25b`, React + Motion, CMS-driven.

> Worth knowing: this one is a template that's **sold**, not a one-off demo like
> the last reference. We're reimplementing layout and motion in our own code
> with entirely different content, which is the usual footing — but if the
> client ever wants the actual Framer build, the honest route is to buy a
> licence rather than have me clone it.

---

## 1. Stack

| Layer | What |
|---|---|
| Platform | Framer (hosted), single `script_main.*.mjs` bundle |
| Animation | Motion (Framer's own) — opacity/transform reveals, no scroll-scrub |
| Type | **Inter 500** does ~95% of the work; Inter Tight, Azeret Mono, Geist appear in small doses |
| Media | MP4, silent, `loop autoplay muted playsinline`, `object-fit: cover` |
| Commerce | CMS collections for products, categories, journal |

No GSAP, no Lenis, no Barba, no pinning. Motion is far lighter than the last
reference — this is a **content-and-photography-led** design, not an effects one.

---

## 2. Pages (~38)

```
/                    home
/collections  /all  /kits  /sale        shop surfaces
/body  /skin  /hair                     category pages
/shop/<product>                         ~14 product pages
/journal  /journal/<post>               editorial
/about  /values  /ingredients  /environment
/stores  /stockists  /contact  /faq
/favorites                              wishlist
/terms-of-service  /return-policy  /privacy-policy
```

---

## 3. Design tokens

### Colour — near-monochrome
| Token | Value | Use |
|---|---|---|
| Page | `#FFFFFF` | Body background |
| Ink | `#000000` | All text |
| Ink soft | `#2E2E2E` | Secondary |
| Grey | `#C9C9C9` / `#D4D4D4` | Dividers, disabled |
| Surface | `#F6F6F6` | Product tiles, section blocks |
| Sale red | `#E01616` | Discount pills only |
| Overlays | `rgba(0,0,0,.03 / .05 / .1 / .2 / .3 / .4 / .5)` | Layered scrims |

**The colour comes entirely from the photography and video.** The UI itself is
black on white. That's the whole trick of this design.

### Type — Inter 500 throughout, tight negative tracking
| Element | Size / line-height | Tracking |
|---|---|---|
| h1 | 46px / 46px (1.0) | `-1.85px` (≈ -0.04em) |
| h2 | 30px / 31.5px (1.05) | `-1.25px` |
| h3 | 25px / 25px (1.0) | `-1.25px` |
| body | 14px / 17.5px (1.25) | `-0.5px` |
| nav, meta | 12px | ~0 |

Everything is weight **500**. No bold, no light. Sentence case, not uppercase —
the opposite of the last reference.

### Shape
Radii in use: `4 · 5 · 6.67 · 7 · 8 · 10 · 12 · 40 · 50px`. Product tiles and
media are softly rounded (~8–12px); pills and buttons are fully rounded (50px).

---

## 4. Home page structure

1. **Hero** — full-bleed 1440×900 product video, headline bottom-left, `Discover` + ↓
2. **"FEATURED IN"** logo row
3. **Tabbed product grid** — Trending / Bestsellers / Kits, 4-up, `Shop all` link
4. **Shop by Category** — Body / Skin / Hair image cards
5. **Featured** — larger product grid, `New` and `-30%` badges
6. **Statement band** — "Advanced Natural Formulations for all skin types"
7. **Our Shops** — imagery + copy
8. **From the Journal** — 3 posts
9. **Bundles / Gift Cards** — two promo tiles
10. **Product spotlight** — single product, large
11. **Backed by Science** — trust row: Collect In Store / Free Returns / Gift Wrapping / Secure Payment
12. **Sale band** with countdown
13. **Testimonials** — looping carousel, quote + product link
14. Footer

---

## 5. Motion

Deliberately restrained. No pinning, no scrub, no parallax.

- **Scroll reveals** — Motion sets inline `opacity: 0 → 1` as sections enter. Short, soft, no large translations.
- **Hover** — `transition: all` on tiles; image swap and a subtle lift.
- **Tabs** — Trending/Bestsellers/Kits swap the grid in place.
- **Testimonials** — continuous horizontal loop.
- **Countdown** — live timer on the sale band.
- **Hero video** — see below. This is where all the energy is.

---

## 6. The hero video system ← the part worth copying

The hero is a **full-bleed silent looping product film**, and the site pulls
these from the CMS per product, so the hero cycles.

| Slot | Resolution | Duration | Notes |
|---|---|---|---|
| Hero (landscape) | **1920×1080** | **6.0s**, 25fps | `object-fit: cover` into 1440×900 |
| Product card (portrait) | 1080×1920 | 8.4s | |
| Feature block (square-ish) | 1500×1558 | 8.0s | |
| Small tile (portrait) | 720×896 | 5.6s | |

All are `loop autoplay muted playsinline`. Bitrate ~1.15 Mb/s; the 6s hero is
**868 KB** — small enough to be the first thing that loads.

### What's actually on screen
Photoreal **CGI product renders**, not live action:

- one product, centred, filling roughly a third of frame height
- an infinite seamless backdrop with a soft **vertical gradient** — dark at the top, lifting toward the bottom
- a single large soft key from upper-left, a faint rim on the opposite edge, and a soft contact shadow
- the product **rotates very slowly** (a few degrees over the whole clip) and drifts slightly
- shallow depth of field; the backdrop falls off out of focus
- the backdrop is tinted to the product (slate-blue for the blue jar, olive for the cream bottle) — **colour comes from the render, not the UI**

That last point is the one to carry over: the page is black-on-white, and every
bit of colour arrives through the product film.

---

## 7. What this means for MAXRENTAL

The design suits them better than the last reference did:

- It is **light**, which matches maxrental.my's own treatment
- It is **product-led** — and we now have 72 clean, watermark-free cutouts
- It is **calm**, which fits a B2B IT leasing brand far better than a fashion site
- The restraint means the build is simpler and faster than the X8 clone

Two things need solving before build:

1. **Hero videos.** They have none. See `docs/VIDEO-PROMPTS.md`.
2. **Colour.** The template leans on beauty photography for warmth. MAXRENTAL's
   palette is navy `#0D1126` and cyan `#00A2E8` — the product films should carry
   those tones so the site has colour without tinting the UI.
