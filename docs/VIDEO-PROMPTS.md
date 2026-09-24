# Hero product videos — prompts

For the full-bleed looping hero and the product-card slots, in the style of
all-natural.framer.website but for MAXRENTAL's hardware.

---

## Target specs (measured from the reference)

| Slot | Resolution | Duration | Notes |
|---|---|---|---|
| **Hero** | 1920×1080 | **6s** | the important one |
| Product card | 1080×1920 | 8s | portrait |
| Feature block | 1500×1558 | 8s | square-ish |
| Small tile | 720×896 | 6s | portrait |

All silent, looping, `muted playsinline`, ~1.2 Mb/s. The reference's 6s hero is
868 KB — keep ours under ~1 MB so it loads before anything else.

---

## The look, in one paragraph

One machine, centred, filling about a third of the frame height, floating on an
infinite seamless backdrop with a soft vertical gradient. A single large soft key
from upper-left, a faint cool rim on the opposite edge, a soft contact shadow
below. The product turns *very* slowly — a few degrees across the whole clip.
Shallow depth of field so the backdrop falls away. Photoreal CGI, not live
action. No hands, no desk, no props, no text.

The backdrop carries the brand colour so the page itself can stay black-on-white:
**deep navy `#0D1126`** lifting to a lighter slate, with **cyan `#00A2E8`** only
as a rim or a faint glow.

---

## How to get a seamless loop

Video models don't loop natively. Two ways:

1. **Full 360° turn** over the clip — first and last frame match, so it loops
   cleanly. Say "exactly one complete 360 degree rotation" in the prompt.
2. **Ping-pong** — generate any slow motion, then mirror it:
   ```bash
   ffmpeg -i in.mp4 -filter_complex "[0]reverse[r];[0][r]concat=n=2:v=1[v]" -map "[v]" -an loop.mp4
   ```
   Doubles the length and loops perfectly, but the motion visibly reverses. Fine
   for a float, obvious for a rotation.

Then compress:
```bash
ffmpeg -i loop.mp4 -an -vf "scale=1920:1080" -c:v libx264 -crf 28 -preset slow \
  -movflags +faststart -pix_fmt yuv420p hero.mp4
```

---

## Prompt 1 — Hero, business laptop (primary)

> Photoreal CGI product animation. A single modern unbranded business laptop,
> open at about 110 degrees, dark graphite aluminium body with a matte finish,
> floating centred in an empty infinite studio void. The laptop performs exactly
> one complete slow 360 degree rotation about its vertical axis over the full
> duration, perfectly smooth and constant, no easing. Background is a seamless
> deep navy blue gradient, darker at the top, lifting to a soft lighter slate
> blue toward the bottom, completely smooth with no visible horizon. Lighting:
> one very large soft key light from the upper left creating a gentle highlight
> along the top edge of the screen and the palm rest, plus a subtle cool cyan rim
> light along the right edge, and a soft diffused contact shadow beneath.
> Shallow depth of field, background softly out of focus. Screen is off and
> reflective, dark and glassy. Cinematic commercial product film, 85mm lens,
> locked-off camera, ultra clean, minimal, premium, 4K.
>
> **Negative:** text, letters, words, logos, branding, watermark, UI, icons,
> keyboard legends, hands, people, desk, table, plants, props, clutter,
> reflections of a room, lens flare, fast motion, camera shake, jitter.

---

## Prompt 2 — Hero, desktop tower

> Photoreal CGI product animation. A single modern unbranded small-form-factor
> desktop computer tower, matte black front panel with a subtle perforated
> texture and a brushed dark metal side, standing upright centred in an empty
> infinite studio void. One complete slow 360 degree rotation about its vertical
> axis over the full duration, constant speed, no easing. Background is a
> seamless deep navy blue vertical gradient, near black at the top softening to
> slate blue at the bottom, perfectly smooth. Lighting: one large soft key from
> the upper left raking across the front panel to reveal its texture, a narrow
> cool cyan rim light down the right edge, soft contact shadow at the base.
> Shallow depth of field. Cinematic commercial product film, 85mm lens,
> locked-off camera, ultra clean, premium, 4K.
>
> **Negative:** text, letters, logos, branding, badges, stickers, ports labels,
> watermark, hands, people, desk, cables, props, clutter, fast motion, shake.

---

## Prompt 3 — Hero, slow rise reveal (matches the reference's own motion)

The reference's cream-bottle clip rises into frame from below while the backdrop
brightens. Same idea, our hardware:

> Photoreal CGI product animation. A single modern unbranded thin business
> laptop, closed, dark graphite aluminium, rising slowly and smoothly upward
> from the bottom of the frame into the centre, drifting gently as it rises, and
> rotating just a few degrees. It comes to rest centred. Background is a seamless
> vertical gradient that lifts from near-black deep navy at the start to a
> lighter slate blue as the product rises, perfectly smooth, no horizon.
> Lighting: one very large soft key from the upper left, a faint cool cyan rim on
> the right edge, soft diffused shadow below. Shallow depth of field. Slow,
> weightless, floating. Cinematic commercial product film, 85mm lens, locked-off
> camera, ultra clean, minimal, premium, 4K.
>
> **Negative:** text, letters, logos, branding, watermark, hands, people, desk,
> props, clutter, fast motion, bouncing, camera shake.
>
> Loop this one with the ping-pong method — it has no natural loop point.

---

## Prompt 4 — Product card, portrait 1080×1920

> Photoreal CGI product animation, vertical composition. A single modern
> unbranded business laptop, open, dark graphite aluminium, floating centred in
> the upper two thirds of a tall empty studio void. It turns slowly and
> continuously, a complete 360 degree rotation over the full duration, constant
> speed. Background is a seamless deep navy to slate blue vertical gradient,
> smooth, no horizon. One large soft key from the upper left, faint cyan rim on
> the right, soft shadow below. Shallow depth of field. Generous negative space
> above and below the product. Cinematic commercial product film, locked-off
> camera, ultra clean, premium, 4K vertical.
>
> **Negative:** text, letters, logos, branding, watermark, hands, people, props,
> clutter, fast motion, shake.

---

## Prompt 5 — Macro detail, port edge

A texture shot for a feature block, more intimate than the full product:

> Photoreal CGI macro product animation. Extreme close-up of the side edge of a
> modern unbranded laptop chassis, brushed dark graphite aluminium, showing the
> clean machined port cutouts in sharp relief. The camera drifts very slowly and
> smoothly along the edge from left to right, revealing the ports in sequence.
> Background is a seamless deep navy gradient falling completely out of focus.
> Lighting: one large soft key from the upper left grazing the metal so the
> brushed texture catches the light, plus a narrow cool cyan rim. Very shallow
> depth of field, the near and far ends of the edge softly blurred. Cinematic
> commercial product film, 100mm macro lens, ultra clean, premium, 4K.
>
> **Negative:** text, letters, port icons, symbols, logos, branding, watermark,
> dust, scratches, fingerprints, hands, fast motion, shake.

---

## Prompt 6 — Fleet, slow dolly

For the "scale your fleet" idea, which is MAXRENTAL's actual pitch:

> Photoreal CGI product animation. A neat row of identical modern unbranded
> business laptops, all open at the same angle, dark graphite aluminium, receding
> into the distance in a perfectly straight line on an infinite empty studio
> floor. The camera dollies slowly and smoothly sideways past the row, parallel
> to it, constant speed. Background is a seamless deep navy to slate blue
> gradient with no visible horizon. Lighting: one very large soft key from above
> and left, a faint cool cyan rim along the screen edges, soft contact shadows.
> Shallow depth of field, the far end of the row falling out of focus. Cinematic
> commercial product film, 50mm lens, ultra clean, minimal, premium, 4K.
>
> **Negative:** text, letters, logos, branding, watermark, hands, people, desks,
> chairs, office, cables, clutter, fast motion, shake.

---

## Settings, whichever model you use

- **Aspect / duration** — 16:9 at 6s for the hero; 9:16 at 8s for cards
- **Camera** — say *locked-off* unless the prompt calls for a move. Models add drift by default and it reads as cheap.
- **Motion strength** — lowest setting that still moves. These clips are almost still.
- **Seed** — keep it fixed across the set so the backdrop and lighting match from clip to clip. Mismatched hero clips look broken when the hero cycles.
- **Generate at least 4 takes per prompt.** Most will have a wobble, a warped hinge or hallucinated text on the lid.

### The one failure mode to watch
These models put **text on anything that looks like a product**. A laptop lid is
a magnet for invented logos. Keep the negative prompt on every generation, and
reject any take with marks on the lid — at hero size they're unmissable.

---

## The alternative worth considering

We now have **72 transparent, watermark-free cutouts of their actual machines**
in the brand kit. I can build these hero loops from those instead of generating
them:

| | AI video | Built from the cutouts |
|---|---|---|
| Product shown | invented, generic | **their real stock** |
| Brand accuracy | hallucinated logos | correct Dell / HP / Lenovo |
| Loop | needs ping-pong or 360° | perfect by construction |
| Cost / time | per generation, many rejects | free, minutes |
| Motion | true 3D rotation | float, drift, parallax, light sweep — not a real turn |
| Ceiling | very high when it lands | polished, but not a 360° |

A slow float with a drifting gradient backdrop and a moving specular sweep gets
most of the reference's feel, and the client sees the machine they actually rent.

**My suggestion:** let me build the cutout version first so you have a working
hero in the mockup today, and treat AI video as the upgrade if the client wants
a true rotation. Say the word and I'll do either.
