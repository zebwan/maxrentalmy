# -*- coding: utf-8 -*-
"""
MAXRENTAL v2 — site copy.

Every fact here comes from maxrental.my, its WooCommerce store, or MMX
Solutions' rental agreement PDF. Reviews are their real published Google
reviews. Nothing is invented — see docs/BRAND.md.
"""

COMPANY = {
    "brand": "MAXRENTAL",
    "legal": "MMX Solutions Sdn Bhd",
    "reg": "200601022957 (742711-T)",
    "address": ["175, Jalan KIP 5,", "Taman Perindustrian KIP,",
                "52200 Kepong, Wilayah Persekutuan Kuala Lumpur"],
    "email": "info@mmxsolutions.com.my",
    "phone": "+6012-219 9211",
    "phone_href": "+60122199211",
    "support": "012-457 9211",
    "hours": "Monday to Friday, 9am to 6pm",
    "instagram": "https://www.instagram.com/maxrental.my/",
    "facebook": "https://www.facebook.com/maxrental.my/",
    "year": "2026",
}

NAV = [
    ("products.html", "Equipment"),
    ("short-term.html", "Rental plans"),
    ("services.html", "Services"),
    ("about.html", "About"),
    ("news.html", "Journal"),
]

HOME = {
    "title": "MAXRENTAL — Office IT rental in Malaysia",
    "description": (
        "Desktops and laptops for Malaysian offices from RM50 a month. Delivery, "
        "installation, warranty, insurance and support included. MMX Solutions "
        "Sdn Bhd, Kepong, since 2006."
    ),
    # The hero runs as a slideshow, the way the reference does: two product
    # films and one still, one message and one CTA each, 6s a slide.
    "hero_slides": [
        {
            "media": "video",
            "src": "video/hero-product.mp4",
            "src_tall": "video/hero-product-tall.mp4",
            "poster": "video/hero-poster.jpg",
            "poster_tall": "video/hero-poster-tall.jpg",
            "tone": "dark",
            "eyebrow": "Corporate IT rental",
            "h1": "Fit out the whole office from RM50 a desk.",
            "cta": "See rental plans",
            "href": "short-term.html",
        },
        {
            "media": "video",
            "src": "video/hero-turntable.mp4",
            "src_tall": "video/hero-turntable-tall.mp4",
            "poster": "video/hero-turntable-poster.jpg",
            "poster_tall": "video/hero-turntable-poster-tall.jpg",
            "tone": "light",
            "eyebrow": "Dell, HP and Lenovo",
            "h1": "Business machines, not consumer ones.",
            "cta": "Browse equipment",
            "href": "products.html",
        },
        {
            "media": "image",
            "src": "img/editorial/hero-fleet.jpg",
            "tone": "dark",
            "eyebrow": "Ten desks or two hundred",
            "h1": "Scale your fleet as fast as you hire.",
            "cta": "Talk to our team",
            "href": "contact.html",
        },
    ],

    # They are an authorised dealer for these — stated on their About page.
    "marquee_label": "Authorised dealer",
    # (name, file, render height in px). Heights are tuned per mark rather than
    # shared: a round mark and a long wordmark set to the same height look
    # nothing like the same size. Never recolour these — vendor brand rules.
    "marquee": [
        ("Dell", "dell.svg", 50),
        ("HP", "hp.svg", 44),
        ("Lenovo", "lenovo.svg", 27),
        ("Microsoft", "microsoft.svg", 36),
        ("Kaspersky", "kaspersky.svg", 27),
        ("Acronis", "acronis.svg", 27),
    ],

    "tabs_label": "What we rent",
    "tabs": [
        ("plans", "Rental plans"),
        ("laptops", "Laptops"),
        ("desktops", "Desktops"),
    ],

    "cats_head": "Browse by category",
    "cats": [
        ("products.html?c=long-term", "Long term", "img/stills/card-laptop-portrait.jpg"),
        ("products.html?c=short-term", "Short term", "img/stills/card-tower-portrait.jpg"),
        ("products.html?c=ref-laptop", "Refurbished", "img/stills/feature-laptop-square.jpg"),
    ],

    "featured_head": "Featured equipment",

    "statement": "Everything a desk needs, on one monthly line.",
    "statement_sub": (
        "Machine, monitor, licence, delivery, installation, warranty, insurance "
        "and support. One price, one invoice, no capital outlay."
    ),

    "band_head": "Twenty years of equipping offices",
    "band_copy": (
        "MMX Solutions has supplied and supported office IT in Malaysia since 2006. "
        "MAXRENTAL is our leasing scheme — built for businesses that would rather "
        "spread the cost than tie up capital."
    ),
    "band_cta": "About MMX Solutions",

    "trust": [
        ("Quick approval", "Most rentals approved the same working day."),
        ("Free delivery & installation", "Set up at your desks, no hidden charges."),
        ("Warranty & insurance", "Hardware cover for the whole rental term."),
        ("Remote & on-site support", "On-site within the Klang Valley."),
    ],

    "journal_head": "From the journal",
    "quotes_head": "What clients say",
}

# Their real published Google reviews (54 reviews, rated Excellent).
REVIEWS = [
    ("Mimi Mardiana",
     "Excellent service. The rental process was smooth and the equipment provided "
     "was in great condition. The team was responsive and helpful throughout.",
     "Rental"),
    ("Sukumaran Narmitha",
     "MMX Solutions has been a great help for me and my company in finding the "
     "rental laptops we needed. They were very helpful with every query we had.",
     "Laptop rental"),
    ("Navin Navin",
     "Good and fast service. Been using MMX for a year now and it has been a good "
     "experience. Keep up the good work.",
     "Long term rental"),
    ("Xin Yeh Chen",
     "Good renting experience. Fast, easy and secure. Easy to communicate and fast "
     "approval.",
     "Rental"),
    ("Edmond Lang",
     "Good service, speedy communication. Provide good Mac rental service.",
     "MacBook rental"),
    ("Yuen Sook Ying",
     "Great service and reasonable prices. Very satisfied with the overall "
     "experience.",
     "Rental"),
]

# Their seven real blog posts.
JOURNAL = [
    ("Guide", "Why renting IT equipment is the smarter choice for Malaysian SMEs",
     "img/editorial/journal-1.jpg"),
    ("Guide", "How different businesses benefit from IT equipment rental",
     "img/editorial/journal-2.jpg"),
    ("Tips", "How to choose the right laptop specs for your business tasks",
     "img/editorial/journal-3.jpg"),
]

PLANS = {
    "short-term": {
        "title": "Short Term Rental Plan — MAXRENTAL",
        "description": "Desktop and laptop rental from RM100 a month on 1 to 12 month terms.",
        "h1": "Short term rental",
        "lead": "One to twelve months. For projects, cover, seasonal teams and trials.",
        "terms": "1 / 3 / 6 / 9 / 12 month terms",
        "desktop": [
            ("Basic", "RM100", "Intel i5-6th Gen · 8GB RAM · 128GB SSD · Win10 Pro · 22\" monitor"),
            ("Mid range", "RM140", "Intel i5-8th Gen · 16GB RAM · 256GB SSD · Win11 Pro · 22\" monitor"),
            ("Advanced", "RM180", "Intel i7-8th Gen · 16GB RAM · 512GB SSD · Win11 Pro · 22\" monitor"),
        ],
        "laptop": [
            ("Basic", "RM100", "Intel i5-6th Gen · 8GB RAM · 128GB SSD · Win10 Pro · 14\" display"),
            ("Mid range", "RM140", "Intel i5-8th Gen · 16GB RAM · 256GB SSD · Win11 Pro · 14\" display"),
            ("Advanced", "RM180", "Intel i7-8th Gen · 16GB RAM · 512GB SSD · Win11 Pro · 14\" display"),
        ],
        "other": "long-term.html",
        "other_label": "Long term rental",
    },
    "long-term": {
        "title": "Long Term Rental Plan — MAXRENTAL",
        "description": "Desktop and laptop rental from RM50 a month on 24 or 36 month terms.",
        "h1": "Long term rental",
        "lead": "Twenty-four or thirty-six months. The lowest monthly rate we offer.",
        "terms": "24 / 36 month terms",
        "desktop": [
            ("Basic", "RM50", "Intel i5-6th Gen · 8GB RAM · 128GB SSD · Win10 Pro · 22\" monitor"),
            ("Mid range", "RM70", "Intel i5-8th Gen · 16GB RAM · 256GB SSD · Win11 Pro · 22\" monitor"),
            ("Advanced", "RM90", "Intel i7-8th Gen · 16GB RAM · 512GB SSD · Win11 Pro · 22\" monitor"),
        ],
        "laptop": [
            ("Basic", "RM50", "Intel i5-6th Gen · 8GB RAM · 128GB SSD · Win10 Pro · 14\" display"),
            ("Mid range", "RM70", "Intel i5-8th Gen · 16GB RAM · 256GB SSD · Win11 Pro · 14\" display"),
            ("Advanced", "RM90", "Intel i7-8th Gen · 16GB RAM · 512GB SSD · Win11 Pro · 14\" display"),
        ],
        "other": "short-term.html",
        "other_label": "Short term rental",
    },
}

PLAN_INCLUDES = [
    "Quick approval",
    "Free delivery and installation",
    "Hardware warranty and insurance",
    "Remote and on-site support and maintenance",
]

ADDONS = [
    ("RAM upgrade, 8GB to 16GB", "RM21.20"),
    ("Microsoft Office Home & Business 2024", "RM53.00"),
    ("Kaspersky Endpoint antivirus", "RM10.60"),
]

SERVICES = {
    "title": "Services — MAXRENTAL",
    "description": "PC sales, IT support and backup solutions from MMX Solutions.",
    "h1": "More than rentals",
    "lead": "Three services that sit around the hardware, for clients renting from us and for those who aren't.",
    "items": [
        ("PC Sales",
         "Brand-new and refurbished laptops and desktops from Dell, HP and Lenovo. "
         "Tell us team size, workload and budget and we come back with a shortlist.",
         ["New and refurbished options", "Custom spec matching", "Bulk order discounts",
          "Warranty and support", "Fast delivery"]),
        ("IT Support",
         "Remote troubleshooting first, an on-site technician when it's needed. "
         "Covers all rented equipment and basic network configuration.",
         ["Remote troubleshooting", "On-site visits", "Hardware diagnosis",
          "Software assistance", "Device replacement"]),
        ("Backup Solutions",
         "When a rental term ends, your data shouldn't end with it. We move your "
         "files to an external drive or to cloud storage before the kit comes back.",
         ["Data assessment", "External drive transfer", "Cloud backup",
          "Multi-device consolidation", "Secure erasure on request"]),
    ],
}

ABOUT = {
    "title": "About — MMX Solutions Sdn Bhd",
    "description": "MMX Solutions has supplied and supported office IT in Malaysia since 2006.",
    "h1": "Since 2006, keeping Malaysian offices running on hardware they never had to buy.",
    "body": [
        "MMX Solutions Sdn Bhd was incorporated in 2006 under Mewamax Sdn Bhd, who had "
        "been supplying multifunction printers since 1997. The company started in IT "
        "support services and moved into trading, leasing and renting computers in 2018.",
        "In 2019 it became an authorised dealer for Dell, HP and Lenovo, and added IT "
        "support and backup solutions. In 2022 a corporate restructuring made MMX "
        "Solutions an associate company of Mewamax, and MAXRENTAL launched as a "
        "dedicated rental scheme for offices that wanted flexible, reliable equipment "
        "without the capital outlay.",
        "Our mission is to provide reliable, efficient computer leasing with maximum "
        "customer satisfaction. Our vision is to establish MAXRENTAL as a nationally "
        "recognised brand and the premier provider in computer leasing.",
    ],
    "timeline": [
        ("2006", "Incorporated under Mewamax, focusing on IT support services."),
        ("2018", "Moved into trading, leasing and renting computers."),
        ("2019", "Authorised dealer for Dell, HP and Lenovo. Added IT support and backup."),
        ("2022", "Became an associate company of Mewamax. Launched MAXRENTAL."),
        ("2024", "Continued growth, helping more businesses access reliable IT."),
    ],
}

CONTACT = {
    "title": "Contact — MAXRENTAL",
    "description": "Talk to MMX Solutions about IT rental, PC sales, support or backup.",
    "h1": "Tell us what the desks need.",
    "lead": "Team size, what the machines are for, and how long you need them. We'll come back with options.",
    "topics": ["Rental enquiry", "PC sales", "IT support", "Backup solutions", "Billing", "Something else"],
}

LEGAL = {
    "terms": {
        "title": "Terms & Conditions — MAXRENTAL",
        "description": "General terms and conditions of the MMX Solutions rental agreement.",
        "h1": "Terms & conditions",
        "blocks": [
            ("Rental agreement",
             "This agreement governs the rental of computer equipment from MMX Solutions "
             "Sdn Bhd [Registration No. 200601022957 (742711-T)], a private limited company "
             "incorporated in Malaysia with its principal business address at No. 175, Jalan "
             "KIP 5, Taman Perindustrian KIP, Kepong, 52200 Kuala Lumpur."),
            ("Rental term and renewal",
             "Equipment is rented for a fixed initial period as agreed. On expiry the "
             "agreement is deemed renewed for a further one-month term on the same terms, "
             "unless either party gives written notice before the period ends."),
            ("Warranty and service",
             "During the rental term we provide warranty services for hardware, operating "
             "system, monitor and the parts and software supplied with the package. Services "
             "are delivered mainly through remote support; on-site support may incur charges "
             "where the problem was caused primarily by the customer. Service hours are "
             "Monday to Friday, 9am to 6pm, excluding public holidays."),
            ("Loss, damage and insurance",
             "We cover loss and damage caused by natural disaster and theft, including fire, "
             "flood, traffic accidents and break-ins, in line with our insurance policy. A "
             "complete police report is required to start a claim. Loss and damage caused by "
             "human error or negligence are excluded, including water spillage, dropping the "
             "equipment, submersion, mishandling or improper use."),
            ("Ownership",
             "The equipment remains our property throughout the rental period. On expiry or "
             "termination it must be returned in its original condition; reasonable wear and "
             "tear on the exterior is acceptable."),
            ("Payment",
             "Fees are payable at the rate and in the manner specified at order confirmation, "
             "within the credit term stated on the invoice. Overdue amounts carry interest at "
             "1.5% per month. Fees may be adjusted in response to changes in government "
             "legislation, including the implementation or revision of SST or GST."),
            ("Deposit",
             "A deposit or advance payment is payable before or on delivery; the amount is "
             "stated at order confirmation. It is refunded on completion of the term and "
             "return of the equipment in acceptable condition, provided nothing is outstanding."),
            ("Early termination",
             "If you terminate before the end of the initial or current subsequent period, "
             "all amounts due to the date of termination become payable, together with the "
             "remaining rental charges for the unexpired portion."),
            ("Governing law",
             "This agreement is governed by and construed in accordance with the laws of "
             "Malaysia."),
        ],
    },
    "privacy": {
        "title": "Privacy Policy — MAXRENTAL",
        "description": "How MMX Solutions Sdn Bhd handles the information you give us.",
        "h1": "Privacy policy",
        "blocks": [
            ("Overview",
             "MMX Solutions Sdn Bhd respects the privacy of everyone who uses this site. "
             "This page explains what we collect, why, and how it is handled."),
            ("What we collect",
             "The information you give us: name, company, email address, phone number, "
             "delivery address and the details of any enquiry, quotation or rental order. "
             "We also collect basic technical information such as browser type and pages "
             "visited, which helps us keep the site working."),
            ("How we use it",
             "To respond to enquiries, prepare quotations, process and deliver rental "
             "orders, provide support during the rental term and meet our obligations "
             "under the rental agreement. We do not sell it."),
            ("Sharing",
             "Only where it is needed to deliver the service, for example with our delivery "
             "and technical teams, or where we are required to by law."),
            ("Your data on rented equipment",
             "You are responsible for the security of your own information on rented "
             "equipment. Before a rental ends we can transfer your files to an external "
             "drive or to cloud storage, and erase the device on request."),
            ("Contact",
             "For any question about this policy, email info@mmxsolutions.com.my or call "
             "+6012-219 9211."),
        ],
    },
}
