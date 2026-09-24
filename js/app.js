/* ==========================================================================
   MAXRENTAL v2 — interactions
   The reference runs Framer's Motion for simple opacity reveals and nothing
   heavier: no scroll-scrub, no pinning, no smooth-scroll hijack. This matches
   that restraint in plain JS, so the page stays fast and the browser keeps
   its native scrolling.
   ========================================================================== */

(function () {
    'use strict';

    /* Mark the document so reveal styles only apply when JS is alive — without
       this a failed script would leave the page parked at opacity 0. */
    document.documentElement.classList.add('js');

    var CART_KEY = 'MR2_QUOTE';
    var FAV_KEY = 'MR2_FAVS';

    function store(key, value) {
        try {
            if (arguments.length > 1) {
                localStorage.setItem(key, JSON.stringify(value));
                return value;
            }
            return JSON.parse(localStorage.getItem(key)) || [];
        } catch (e) {
            return [];
        }
    }

    /* ------------------------------------------------------- reveals --- */

    function reveals() {
        var items = [].slice.call(document.querySelectorAll('.reveal'));
        if (!items.length) return;

        if (!('IntersectionObserver' in window)) {
            items.forEach(function (el) { el.classList.add('is-in'); });
            return;
        }

        var io = new IntersectionObserver(function (entries) {
            entries.forEach(function (entry) {
                if (!entry.isIntersecting) return;
                var el = entry.target;
                var delay = Number(el.dataset.revealDelay || 0);
                window.setTimeout(function () { el.classList.add('is-in'); }, delay);
                io.unobserve(el);
            });
        }, { rootMargin: '0px 0px -8% 0px', threshold: 0.08 });

        items.forEach(function (el) { io.observe(el); });

        /* Anything already on screen at load reveals immediately, so the first
           painted frame is never blank. */
        window.requestAnimationFrame(function () {
            items.forEach(function (el) {
                var r = el.getBoundingClientRect();
                if (r.top < window.innerHeight * 0.92) {
                    el.classList.add('is-in');
                    io.unobserve(el);
                }
            });
        });
    }

    /* -------------------------------------------------------- header --- */

    function header() {
        var el = document.querySelector('.header');
        if (!el) return;
        function onScroll() {
            el.classList.toggle('is-stuck', window.scrollY > 8);
        }
        onScroll();
        window.addEventListener('scroll', onScroll, { passive: true });
    }

    function mobileNav() {
        var btn = document.querySelector('.nav-toggle');
        var nav = document.querySelector('.nav');
        if (!btn || !nav) return;

        btn.addEventListener('click', function () {
            var open = nav.classList.toggle('is-open');
            btn.setAttribute('aria-expanded', open ? 'true' : 'false');
            btn.textContent = open ? 'Close' : 'Menu';
        });

        nav.addEventListener('click', function (e) {
            if (e.target.tagName !== 'A') return;
            nav.classList.remove('is-open');
            btn.setAttribute('aria-expanded', 'false');
            btn.textContent = 'Menu';
        });
    }

    /* ---------------------------------------------------------- tabs --- */

    function tabs() {
        document.querySelectorAll('[data-tabs]').forEach(function (group) {
            var buttons = [].slice.call(group.querySelectorAll('[data-tab]'));
            var panels = [].slice.call(
                document.querySelectorAll('[data-tab-panel][data-tabs-for="' + group.dataset.tabs + '"]')
            );
            if (!buttons.length || !panels.length) return;

            buttons.forEach(function (btn) {
                btn.addEventListener('click', function () {
                    buttons.forEach(function (b) {
                        b.setAttribute('aria-selected', b === btn ? 'true' : 'false');
                    });
                    panels.forEach(function (p) {
                        p.hidden = p.dataset.tabPanel !== btn.dataset.tab;
                    });
                });
            });
        });
    }

    /* ------------------------------------------------------ quote list -- */

    function quoteCount() {
        var items = store(CART_KEY);
        document.querySelectorAll('[data-quote-count]').forEach(function (el) {
            el.textContent = items.length ? '(' + items.length + ')' : '';
        });
    }

    function quoteButtons() {
        document.addEventListener('click', function (e) {
            var btn = e.target.closest('[data-add-quote]');
            if (!btn) return;
            e.preventDefault();

            var key = btn.dataset.addQuote;
            var items = store(CART_KEY);
            if (items.indexOf(key) === -1) {
                items.push(key);
                store(CART_KEY, items);
                btn.textContent = 'Added to quote';
            } else {
                btn.textContent = 'Already on quote';
            }
            quoteCount();
            window.setTimeout(function () {
                btn.textContent = btn.dataset.label || 'Add to quote';
            }, 1800);
        });
    }

    /* ----------------------------------------------------- favourites --- */

    function favourites() {
        function paint() {
            var favs = store(FAV_KEY);
            document.querySelectorAll('[data-fav]').forEach(function (btn) {
                var on = favs.indexOf(btn.dataset.fav) !== -1;
                btn.setAttribute('aria-pressed', on ? 'true' : 'false');
                btn.textContent = on ? '♥' : '♡';
            });
        }

        document.addEventListener('click', function (e) {
            var btn = e.target.closest('[data-fav]');
            if (!btn) return;
            e.preventDefault();
            var key = btn.dataset.fav;
            var favs = store(FAV_KEY);
            var i = favs.indexOf(key);
            if (i === -1) { favs.push(key); } else { favs.splice(i, 1); }
            store(FAV_KEY, favs);
            paint();
        });

        paint();
    }

    /* --------------------------------------------------------- filter --- */

    function filter() {
        var select = document.querySelector('[data-filter]');
        if (!select) return;

        function apply() {
            var value = select.value;
            document.querySelectorAll('[data-collection]').forEach(function (el) {
                el.hidden = value !== 'all' && el.dataset.collection !== value;
            });
            var shown = document.querySelectorAll('[data-collection]:not([hidden])').length;
            var empty = document.querySelector('[data-filter-empty]');
            if (empty) empty.hidden = shown !== 0;
        }

        select.addEventListener('change', apply);
        apply();
    }

    /* ----------------------------------------------------- hero slides -- */
    /* A slideshow of product films and one still, like the reference: 6s a
       slide, a hairline indicator that fills over the dwell, click to jump.
       Timing is wall-clock rather than rAF because a backgrounded tab
       suspends rAF and freezes CSS transitions — on return we resync instead
       of drifting. */

    var HERO_MS = 3400;

    function heroSlides() {
        var hero = document.querySelector('[data-hero]');
        if (!hero) return;

        var slides = [].slice.call(hero.querySelectorAll('.hero__slide'));
        var dots = [].slice.call(hero.querySelectorAll('.hero__dot'));
        var dotRow = hero.querySelector('.hero__dots');
        if (slides.length < 2) { loadMedia(slides[0], true); return; }

        var index = 0;
        var timer = null;
        var still = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

        /* `play` is false when we are only warming the next slide. Warming must
           not start playback: the clip would run to its end off-screen and the
           slide would arrive showing its last frame instead of its first. */
        function loadMedia(slide, play) {
            if (!slide) return;
            var v = slide.querySelector('video');
            if (!v) return;

            var tall = window.matchMedia('(max-width: 720px)').matches;
            var src = v.getAttribute(tall ? 'data-tall' : 'data-wide');
            var poster = v.getAttribute(tall ? 'data-tall-poster' : 'data-wide-poster');
            if (poster) v.setAttribute('poster', poster);
            if (src && v.getAttribute('src') !== src) {
                v.setAttribute('src', src);
                v.load();
            }
            if (!play) return;

            try { v.currentTime = 0; } catch (e) { /* not seekable yet */ }
            var p = v.play();
            if (p && typeof p.catch === 'function') {
                p.catch(function () { /* the poster is a real frame */ });
            }
        }

        function paintDots() {
            dots.forEach(function (d, i) {
                var on = i === index;
                d.classList.toggle('is-active', on);
                d.setAttribute('aria-selected', on ? 'true' : 'false');
                var fill = d.querySelector('.hero__dot-fill');
                if (!fill) return;
                /* restart the fill from zero without animating backwards */
                fill.style.transition = 'none';
                fill.style.width = '0';
                if (on && !still) {
                    void fill.offsetWidth;
                    fill.style.transition = 'width ' + HERO_MS + 'ms linear';
                    fill.style.width = '100%';
                } else if (on) {
                    fill.style.width = '100%';
                }
            });
            if (dotRow) {
                dotRow.setAttribute(
                    'data-tone',
                    slides[index].classList.contains('hero__slide--light') ? 'light' : 'dark'
                );
            }
        }

        function show(next) {
            index = (next + slides.length) % slides.length;
            slides.forEach(function (s, i) {
                var on = i === index;
                s.classList.toggle('is-active', on);
                s.setAttribute('aria-hidden', on ? 'false' : 'true');
                var v = s.querySelector('video');
                if (v && !on && typeof v.pause === 'function') v.pause();
            });
            loadMedia(slides[index], true);
            /* warm the next slide's file only — no playback, see loadMedia */
            loadMedia(slides[(index + 1) % slides.length], false);
            paintDots();
        }

        function schedule() {
            window.clearTimeout(timer);
            if (still) return;
            timer = window.setTimeout(function () { show(index + 1); schedule(); }, HERO_MS);
        }

        dots.forEach(function (d) {
            d.addEventListener('click', function () {
                show(Number(d.dataset.goto) || 0);
                schedule();
            });
        });

        /* A hidden tab freezes the fill mid-way; repaint and restart on return
           so the indicator never sits at a stale width. */
        document.addEventListener('visibilitychange', function () {
            if (document.hidden) { window.clearTimeout(timer); return; }
            paintDots();
            schedule();
        });

        show(0);
        schedule();
    }

    /* -------------------------------------------------------- marquee -- */
    /* The strip must never show a gap. One set of logos is usually narrower
       than the viewport, so translating by a fixed -50% exposes empty space at
       the wrap. Instead: clone the set until the run comfortably overflows,
       then shift by exactly one set's width — the frame it lands on is
       identical to the one it left. Speed is held constant in px/s rather than
       by a fixed duration, so a wider strip does not scroll faster. */

    var MARQUEE_PX_PER_SEC = 58;

    function marquee() {
        var track = document.querySelector('.marquee__track');
        if (!track) return;
        var first = track.querySelector('.marquee__set');
        if (!first) return;

        function layout() {
            /* start from a single set each time so repeated calls don't stack */
            track.querySelectorAll('.marquee__set').forEach(function (el, i) {
                if (i > 0) el.remove();
            });

            var setWidth = first.getBoundingClientRect().width;
            if (!setWidth) return;

            var need = Math.ceil(window.innerWidth / setWidth) + 1;
            for (var i = 1; i < need; i++) {
                track.appendChild(first.cloneNode(true));
            }

            track.style.setProperty('--marquee-shift', setWidth + 'px');
            track.style.setProperty('--marquee-dur', (setWidth / MARQUEE_PX_PER_SEC) + 's');
        }

        layout();

        /* SVGs can lay out at zero width before they decode */
        window.addEventListener('load', layout);

        var t;
        window.addEventListener('resize', function () {
            window.clearTimeout(t);
            t = window.setTimeout(layout, 180);
        });
    }

    /* ---------------------------------------------------------- start --- */

    function init() {
        reveals();
        header();
        mobileNav();
        tabs();
        quoteCount();
        quoteButtons();
        favourites();
        filter();
        heroSlides();
        marquee();
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
