# Media credits — MAXRENTAL v2

## Video

The hero runs as a 3-slide show — two films and one still — the way the
reference template does. All Pexels licence: free for commercial use, no
attribution required.

| File | Source | Why |
|---|---|---|
| `hero-product.mp4` / `-tall` | ["Product Shoot of a Laptop"](https://www.pexels.com/video/product-shoot-of-a-laptop-5107906/), 21.6–25.2s | Keyboard macro. The shoot is of a **Dell**, their primary brand. |
| `hero-turntable.mp4` / `-tall` | ["A Detail Shot of a Computer Laptop"](https://www.pexels.com/video/a-detail-shot-of-a-computer-laptop-4202428/) | **Lenovo** turntable on white — a true product film. Drives the light slide. |
| `img/editorial/hero-fleet.jpg` | frame from ["Computer and Gadgets In a Office"](https://www.pexels.com/video/computer-and-gadgets-in-a-office-8347249/) | A fitted-out office with no people — the outcome they sell. |
| `hero-dell.mp4` / `-tall` | 5107906, 2.6–7.4s | **Unused.** The Dell badge fills the frame and reads as a Dell ad. |

The 5107906 source carries baked 2.35:1 letterbox bars; every cut strips them
(`crop=1920:816:0:132`). The keyboard cut is ping-ponged (forward then
reversed) because its camera move is one-way and would jump on loop; the
turntable rotates continuously and needs no such treatment.

Each slide dwells 6s, which is also each film's length, so a film plays once
per turn rather than looping mid-slide — the same relationship the reference has.

## Logo

`img/logo-ink.png` and `img/logo-white.png` are rebuilt at 4x from
`img/mark-512.png` plus the wordmark's own alpha mask, upscaled and
re-thresholded. The supplied `logo-maxrental.png` has a **white** wordmark,
which was invisible against the light header — only the cyan mark ever showed.
Brand proportions are unchanged; only the wordmark's colour and the raster
resolution differ.

## Photography

From MMX Solutions' own library — no stock people anywhere on the site.

| File | Source | Crop reason |
|---|---|---|
| `img/editorial/band-team.jpg` | `mmx-solutions-laptop-rental-malaysia.webp` | Stops at x=1000 to drop the baked MMX banner |
| `img/editorial/premises-wide.jpg` | same file, lower window | Bench of machines; clear of the "ready for what's next" box |
| `img/editorial/band-support.jpg` | `IT-Support-banner.webp` | Right end of a 5.5:1 marquee, where the hands are |

`img/editorial/journal-1..3.jpg` and `about-detail.jpg` are composited from the
real catalogue cutouts in the brand kit (`/tmp/make_editorial.py`), on the same
navy backdrop as the hero.

## Office fleet footage held in reserve

`8347236` and `8346903` (same shoot as the hero still) were downloaded and
judged but are not in the build. They are in the session scratchpad if another
band needs motion later.

## Authorised-dealer logos

`img/brands/*.svg` — each vendor's own primary logo, **not recoloured**, since
vendor brand guidelines generally forbid it. Monochrome was tried and rejected:
Microsoft's mark is four coloured squares and collapses to a grey block.

| Brand | Source |
|---|---|
| Dell | Wikimedia Commons, `Dell logo 2016.svg` |
| HP | Wikimedia Commons, `HP logo 1979.svg` |
| Lenovo | Wikimedia Commons, `Lenovo logo 2015.svg` |
| Microsoft | Wikimedia Commons, `Microsoft logo.svg` |
| Kaspersky | Wikimedia Commons, `Kaspersky Lab logo.svg` |
| Acronis | Wikimedia Commons, `Acronis-logo.svg` |

Render heights are tuned per mark in `content.py` (`HOME["marquee"]`), not
shared: a round mark and a long wordmark set to the same height do not read as
the same size. Current values — Dell 34, HP 30, Microsoft 24, Lenovo 18,
Kaspersky 18, Acronis 18.

> MMX's About page states they are an authorised dealer for **Dell, HP and
> Lenovo**; Microsoft, Kaspersky and Acronis are software they resell. Before
> this goes live, confirm with MMX that each vendor permits logo use and
> replace these with the files from each vendor's own brand/partner portal —
> Wikimedia versions are fine for a mockup but are not the official assets.
