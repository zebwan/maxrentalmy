# MAXRENTAL — brand kit

Everything carried forward for the next design. Design-agnostic: no reference
site, no layout decisions, just the brand, the facts and the assets.

Sources: maxrental.my (live), its WooCommerce store API, its Elementor kit, and
MMX Solutions' "General Terms & Conditions of Rental Agreement" PDF (Oct 2025).
Nothing here is invented.

---

## 1. The company

| | |
|---|---|
| Trading brand | **MAXRENTAL** |
| Legal entity | MMX Solutions Sdn Bhd |
| Registration | 200601022957 (742711-T) |
| Address | 175, Jalan KIP 5, Taman Perindustrian KIP, 52200 Kepong, Wilayah Persekutuan Kuala Lumpur |
| Email | info@mmxsolutions.com.my |
| Phone / WhatsApp | +6012-219 9211 |
| Support line | WhatsApp 012-457 9211 |
| Service hours | Monday to Friday, 9am to 6pm, excluding public holidays |
| On-site coverage | **Klang Valley only** |
| Second domain | mmxsolutions.com.my |
| Social | [Facebook](https://www.facebook.com/maxrental.my/) · [Instagram](https://www.instagram.com/maxrental.my/) |

MAXRENTAL is the rental **scheme**; MMX Solutions is the company. Page titles on
the live site say "MMX Solutions" even though the domain is maxrental.my.

### History
- **1997** — parent company Mewamax Sdn Bhd, multifunction printers
- **2006** — MMX Solutions incorporated under Mewamax, IT support services
- **2018** — moved into trading, leasing and renting computers
- **2019** — authorised dealer for Dell, HP and Lenovo; added IT support and backup
- **2022** — restructured as an *associate* company of Mewamax; launched MAXRENTAL
- **2024** — continued growth

### Mission / vision (their words)
- Mission: reliable, efficient computer leasing with maximum customer satisfaction.
- Vision: establish MAXRENTAL as a nationally recognised brand and the premier provider in computer leasing.
- Values: customers first; perfection in every detail; strength in unity.

### Market
Malaysian SMEs, startups and scaling offices. The pitch is cash flow — avoid
capex, stay current, scale headcount up and down.

---

## 2. Visual identity

Taken from the live Elementor kit.

| Role | Hex | Notes |
|---|---|---|
| Primary | `#282828` | Their stated primary |
| **Accent** | **`#00A2E8`** | The MAXRENTAL cyan — the signature colour |
| Deep navy | `#0D1126` | |
| Body text | `#6C6B69` | |
| Muted sage | `#B7C3C0` | |
| Off-white | `#FAFAFA` | |
| Yellow highlight | `#FFE15D` | Used sparingly |

**Typeface:** Roboto (300 / 400 / 500 / 600 / 700) across the whole live site.

**Logo:** `img/logo/logo-maxrental.png` — white "MAXRENTAL" wordmark with a cyan
circular double-A mark, transparent background, 260×55. Built for dark
backgrounds; on light backgrounds it needs a dark variant, which MMX has not
supplied. `img/logo/mark-512.png` is the mark alone at 513×513 (favicon source).

**Their live site is light** (white background, dark text, cyan accents). Worth
matching unless there's a reason not to.

---

## 3. What they sell

### Rental plans — per seat, per month
Desktop and laptop are the same price; desktops include a 22" monitor, laptops a
14" display.

| Tier | Specification | Long term (24/36 mo) | Short term (1–12 mo) |
|---|---|---|---|
| Basic | i5-6th Gen, 8GB, 128GB SSD, Win10 Pro | **RM50** | **RM100** |
| Mid Range | i5-8th Gen, 16GB, 256GB SSD, Win11 Pro | **RM70** | **RM140** |
| Advanced | i7-8th Gen, 16GB, 512GB SSD, Win11 Pro | **RM90** | **RM180** |

**MacBook Air M2** (8GB / 256GB) is separate: RM300/mo short term, RM220/mo at
24 months or RM150/mo at 36 — with a **refundable RM2,000 deposit**.

Every plan includes: quick approval, free delivery and installation, hardware
warranty and insurance, remote and on-site support and maintenance.

**Add-ons** (inc. 6% SST): RAM 8→16GB RM21.20 · MS Office H&B 2024 RM53 ·
Kaspersky Endpoint RM10.60.

### Outright sales
30 SKUs total, all Dell / HP / Lenovo.

- Brand-new laptops RM2,500–3,500 (HP ProBook 440 G10, Dell Latitude 3450, Dell DC 15250)
- Refurbished laptops RM700–2,000 (HP ZBook/ProBook, Dell Latitude ×6, Lenovo L380)
- Refurbished desktops RM900–2,000 (Dell OptiPlex 5080 SFF / 3060, HP EliteDesk 800 G3)
- Microsoft Office Home & Business 2024 licence RM954 (was RM1,000)

Full machine-readable catalogue: `docs/catalogue.js` and
`docs/maxrental-products.json`.

### Services
- **PC Sales** — new and refurbished, spec matching, bulk discounts, warranty, fast delivery
- **IT Support** — remote first, on-site within Klang Valley, hardware/software/network
- **Backup Solutions** — end-of-rental data transfer to drive or cloud, optional secure wipe

---

## 4. Commercial terms that shape the pitch

From the rental agreement PDF (`docs/rental-terms-oct-2025.pdf`):

- Contracts **auto-renew month to month** after the initial period unless written notice
- Early termination = pay the remaining unexpired period in full
- MMX owns the equipment throughout; deposit refunded on return in acceptable condition
- Insurance covers fire, flood, theft, traffic accidents (police report required)
- **Human error is explicitly excluded** — spills, drops, mishandling
- On-site visits may be chargeable if MMX judges the fault customer-caused
- 1.5% per month interest on late payment; Malaysian law

There is a soft contradiction worth being careful with: the marketing pages
promise "ongoing on-site support" as a free inclusion, while the T&C says
remote-first with chargeable on-site.

---

## 5. Social proof

54 Google reviews, rated Excellent (Trustindex). Staff named repeatedly in
reviews: **Hanis** (sales) and **Fariza** (technical). Reviews mention Mac rental,
fast approval, and the team visiting offices repeatedly to resolve issues.

They have a real **SME100 Awards** photo and badge in their media library
(`img/library/Industry-Recog.webp`, `img/library/SME-AWARD.webp`) — but these are
**not used anywhere on the live site**.

---

## 6. Assets in this kit

```
img/logo/            logo-maxrental.png (wordmark, transparent)
                     mark-512.png (mark only)
img/products/        85 originals from their store, untouched.
                     ~1770×1328, white background, faint tiled "MAXRENTAL"
                     watermark and a solid logo top-left
img/products-cutout/ 72 cutouts across 17 products — background, watermark and
                     logo all gone, trimmed to the device, max 1400px.
                     .png (26.7 MB total) and .webp (4.2 MB) side by side
   └ _promo-graphics/ the 14 rental-plan SKUs whose only "photo" is a marketing
                     poster, not a product shot. Cut badly. Do not use —
                     see docs/plan-image-map.json instead
img/library/         every image currently on maxrental.my (85 files):
                     real premises photo, SME100 award, service banners,
                     blog thumbnails, timeline graphics
docs/                copy, catalogue, plan→image map, rental terms PDF
```

**Use `img/products-cutout/`, and prefer the `.webp`** (16% of the PNG size,
alpha intact). The originals carry MMX's tiled watermark, which looks cheap at
anything above thumbnail size.

### How the cutouts were made
`rembg` with the **u2net** model, forced onto `CPUExecutionProvider` — the
default tries to compile to CoreML and hangs for minutes. ~1s per image.
Afterwards a cleanup pass zeroes any pixel that is simultaneously
semi-transparent, very light and almost colourless, which is exactly the grey
watermark tiling; a real silver chassis is opaque inside the mask so it survives.
`isnet-general-use` was tried and rejected — it treats the watermark as
foreground.

### Rental-plan SKUs have no product photo
The six desktop tiers, six laptop tiers and two MacBook plans are sold with
poster graphics, not photographs. `docs/plan-image-map.json` maps each plan SKU
to a real device cutout that represents it, e.g.

| Plan SKU | Use this cutout |
|---|---|
| desktop basic / long basic | `dell-optiplex-3060-desktop` |
| desktop mid range | `hp-elitedesk-800-g3-desktop` |
| desktop advanced | `dell-optiplex-5080sff-desktop` |
| laptop basic | `dell-latitude-3400-laptop` |
| laptop mid range | `dell-latitude-5400-laptop` |
| laptop advanced | `dell-latitude-5420-laptop` |
| MacBook plans | `apple-macbook-air-m2` |

The MacBook cutout was carved out of its poster by cropping to the rendered
device first, then matting. It is the one salvaged asset in that folder.

Pick of the library:
- `mmx-solutions-laptop-rental-malaysia.webp` (1672×941) — their **real Kepong premises** with staff. The best authentic image they have.
- `Industry-Recog.webp` — real SME100 Awards photo
- `MMX-home.webp` — rows of desktops in an office
- `Reliable-Support-Throughout-Your-Rental-Journey.webp` — helpdesk
- Most others are small (394×240) or gradient banners of little use

---

## 7. Gaps — things MMX still has to supply

1. **No dark-on-light logo.** Only the white wordmark exists.
2. **No award or partner logos in use.** The live homepage has an "Industry
   Recognition and Achievements" section with no images in it, and the
   brand-partner carousel ships placeholder "logo ipsum" files instead of
   Dell / HP / Lenovo. Real badges and logos have to come from them.
3. **Brand New Desktop is an empty category** on their live site.
4. **No photography of their own operation** beyond the one premises shot.
5. **No video.**
6. Blog post bodies read like unfinished briefs to a writer.

---

## 8. Rules for any MAXRENTAL build

Carried over from previous work and client feedback:

- Never darken, tint or blur their photos; captions go off-image
- No caps-and-letterspaced micro-labels, no 01/02 index numbers, no eyebrow dashes
- No em-dash clauses in hero subtexts — one short sentence
- Never publish a fact that isn't in this document or on their site
- Short client messages: the ask only, ~60 words
