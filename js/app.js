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

    var CART_KEY = 'MR2_CART';
    var LEGACY_CART_KEY = 'MR2_QUOTE';
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

    /* ---------------------------------------------------------- cart -- */
    /* Items are {k: product key, q: quantity, t: term}. An older
       build stored a flat array of keys, so read() migrates that shape rather
       than throwing the visitor's list away. */

    function readCart() {
        var raw = store(CART_KEY);
        if (!raw.length) {
            /* Carried over from when this was a quote list */
            var old = store(LEGACY_CART_KEY);
            if (old.length) raw = old;
        }
        if (!raw.length) return [];
        if (typeof raw[0] === 'string') {
            return raw.map(function (k) { return { k: k, q: 1, t: '' }; });
        }
        return raw.filter(function (i) { return i && i.k; });
    }

    function writeCart(items) {
        store(CART_KEY, items);
        paintCartCount();
    }

    function productByKey(k) {
        return (window.PRODUCTS || []).filter(function (p) { return p.key === k; })[0];
    }

    /* Prices read "RM140 / month"; the numeric value is carried separately as
       p.value, so fall back to parsing only if that is missing. */
    function monthlyValue(p) {
        if (!p) return 0;
        if (typeof p.value === 'number') return p.value;
        var m = String(p.price || '').replace(/,/g, '').match(/[\d.]+/);
        return m ? parseFloat(m[0]) : 0;
    }

    function money(n) {
        return 'RM' + n.toLocaleString('en-MY', { maximumFractionDigits: 0 });
    }

    function tileFor(key) {
        var plan = window.MR_PLAN_IMAGE || {};
        return 'img/tiles/' + (plan[key] || key) + '-1.webp';
    }

    function niceName(t) {
        var keep = /^(ssd|ram|hdd|sff|hp|pc|i3|i5|i7|gb|tb)$/i;
        return String(t).toLowerCase().split(' ').map(function (w) {
            return keep.test(w) ? w.toUpperCase() : w.charAt(0).toUpperCase() + w.slice(1);
        }).join(' ');
    }

    function paintCartCount() {
        var n = readCart().reduce(function (a, i) { return a + (i.q || 1); }, 0);
        document.querySelectorAll('[data-cart-count]').forEach(function (el) {
            el.textContent = n;
            el.hidden = n === 0;
        });
    }

    function addToCart(key, qty, term) {
        var items = readCart();
        var hit = items.filter(function (i) { return i.k === key; })[0];
        if (hit) {
            hit.q += qty || 1;
            if (term) hit.t = term;
        } else {
            items.push({ k: key, q: qty || 1, t: term || '' });
        }
        writeCart(items);
        renderCart();
        openCart();
    }

    /* --------------------------------------------------- cart drawer -- */

    function renderCart() {
        var body = document.querySelector('[data-cart-body]');
        var foot = document.querySelector('[data-cart-foot]');
        if (!body) return;

        var items = readCart();

        if (!items.length) {
            body.innerHTML =
                '<div class="cart-empty">' +
                '<p class="t-lead">Your cart is empty.</p>' +
                '<p class="t-body grey">Add the machines you need. Rentals bill monthly, ' +
                'hardware you buy outright bills once.</p>' +
                '<a class="pill" href="products.html">Browse equipment</a>' +
                '</div>';
            if (foot) foot.hidden = true;
            return;
        }

        /* Half the catalogue is rented monthly and half is sold outright, so
           the two can never be added into one figure. */
        var rent = 0, buy = 0;
        body.innerHTML = '<ul class="cart-list">' + items.map(function (it) {
            var p = productByKey(it.k);
            var line = monthlyValue(p) * it.q;
            var isRental = p && p.unit === 'month';
            if (isRental) { rent += line; } else { buy += line; }
            var name = p ? niceName(p.name) : it.k;
            return '<li class="cart-item" data-key="' + it.k + '">' +
                   '<span class="cart-item__media"><img src="' + tileFor(it.k) + '" alt="" loading="lazy" /></span>' +
                   '<span class="cart-item__main">' +
                     '<span class="cart-item__name">' + name + '</span>' +
                     '<span class="cart-item__term">' +
                       (isRental ? (it.t || 'Monthly rental') : 'One-off purchase') +
                     '</span>' +
                     '<span class="qty qty--sm">' +
                       '<button type="button" data-q="-1" aria-label="Fewer">&minus;</button>' +
                       '<span class="qty__n">' + it.q + '</span>' +
                       '<button type="button" data-q="1" aria-label="More">+</button>' +
                     '</span>' +
                   '</span>' +
                   '<span class="cart-item__side">' +
                     '<span class="cart-item__price">' + (p ? p.price : '') + '</span>' +
                     '<button class="cart-item__x" type="button" data-remove aria-label="Remove ' + name + '">&times;</button>' +
                   '</span>' +
                   '</li>';
        }).join('') + '</ul>';

        if (foot) {
            foot.hidden = false;
            var rows = [
                ['[data-sum-rent]', '[data-cart-rent]', rent, ' / month'],
                ['[data-sum-buy]', '[data-cart-buy]', buy, '']
            ];
            rows.forEach(function (r) {
                var wrap = foot.querySelector(r[0]);
                var val = foot.querySelector(r[1]);
                if (!wrap || !val) return;
                wrap.hidden = r[2] === 0;
                val.textContent = money(r[2]) + r[3];
            });
        }
    }

    var cartReturnFocus = null;

    function openCart() {
        var d = document.querySelector('[data-cart-drawer]');
        if (!d) return;
        cartReturnFocus = document.activeElement;
        d.hidden = false;
        /* Force a reflow so the browser registers the closed state before the
           class flips; requestAnimationFrame would do it too but is suspended
           in a backgrounded tab, which left the drawer stuck off-screen. */
        void d.offsetWidth;
        d.classList.add('is-open');
        document.body.classList.add('has-drawer');
        document.querySelectorAll('[data-open-cart]').forEach(function (b) {
            b.setAttribute('aria-expanded', 'true');
        });
        var first = d.querySelector('.cart__x');
        if (first) first.focus();
    }

    function closeCart() {
        var d = document.querySelector('[data-cart-drawer]');
        if (!d) return;
        d.classList.remove('is-open');
        document.body.classList.remove('has-drawer');
        document.querySelectorAll('[data-open-cart]').forEach(function (b) {
            b.setAttribute('aria-expanded', 'false');
        });
        /* wait out the slide before hiding, or it vanishes instead of leaving */
        window.setTimeout(function () {
            if (!d.classList.contains('is-open')) d.hidden = true;
        }, 320);
        if (cartReturnFocus && cartReturnFocus.focus) cartReturnFocus.focus();
    }

    function cartEvents() {
        document.addEventListener('click', function (e) {
            if (e.target.closest('[data-open-cart]')) {
                e.preventDefault();
                renderCart();
                openCart();
                return;
            }
            if (e.target.closest('[data-close-cart]')) { closeCart(); return; }

            var add = e.target.closest('[data-add-cart]');
            if (add && add.dataset.addCart) {
                e.preventDefault();
                var box = document.querySelector('[data-qty-value]');
                var chip = document.querySelector('.chip.is-active');
                addToCart(add.dataset.addCart,
                           Math.max(1, parseInt(box && box.value, 10) || 1),
                           chip ? chip.textContent.trim() : '');
                return;
            }

            var step = e.target.closest('.cart-item [data-q]');
            if (step) {
                var li = step.closest('.cart-item');
                var items = readCart();
                var row = items.filter(function (i) { return i.k === li.dataset.key; })[0];
                if (row) {
                    row.q += Number(step.dataset.q);
                    if (row.q < 1) items = items.filter(function (i) { return i.k !== row.k; });
                    writeCart(items);
                    renderCart();
                }
                return;
            }

            var rm = e.target.closest('.cart-item [data-remove]');
            if (rm) {
                var key = rm.closest('.cart-item').dataset.key;
                writeCart(readCart().filter(function (i) { return i.k !== key; }));
                renderCart();
                return;
            }

            if (e.target.closest('[data-clear-cart]')) {
                writeCart([]);
                renderCart();
            }
        });

        document.addEventListener('keydown', function (e) {
            if (e.key !== 'Escape') return;
            var d = document.querySelector('[data-cart-drawer]');
            if (d && d.classList.contains('is-open')) closeCart();
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
        paintCartCount();
        renderCart();
        cartEvents();
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
