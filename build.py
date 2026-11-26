import json, os
from data import *

ICONS = {
 "lotus":"M12 20c-3-2-5-5-5-8 2 0 4 1 5 3 1-2 3-3 5-3 0 3-2 6-5 8zM12 15c-1-3-1-6 0-9 1 3 1 6 0 9z",
 "leaf":"M5 19c0-8 5-13 14-14 0 9-5 14-13 14M5 19c3-4 6-7 10-9",
 "sparkle":"M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8zM19 16l.7 1.8 1.8.7-1.8.7L19 21l-.7-1.8-1.8-.7 1.8-.7z",
 "scissors":"M6 4.5a2.5 2.5 0 100 5 2.5 2.5 0 000-5zM6 14.5a2.5 2.5 0 100 5 2.5 2.5 0 000-5zM8 8l12 10M8 16L20 6",
 "droplet":"M12 3s6 6.5 6 11a6 6 0 01-12 0c0-4.5 6-11 6-11z",
 "eye":"M2 12s4-7 10-7 10 7 10 7-4 7-10 7S2 12 2 12zM12 9a3 3 0 100 6 3 3 0 000-6z",
 "clock":"M12 3a9 9 0 100 18 9 9 0 000-18zM12 7v5l3 2",
 "shield":"M12 3l8 3v6c0 5-3.5 8-8 9-4.5-1-8-4-8-9V6zM9 12l2 2 4-4",
 "heart":"M12 20s-8-5-8-11a4.5 4.5 0 018-2.5A4.5 4.5 0 0120 9c0 6-8 11-8 11z",
 "gift":"M4 9h16v4H4zM5 13h14v7H5zM12 9v11M12 9c-2 0-4-1-4-3s3-2 4 3c1-5 4-5 4-3s-2 3-4 3",
 "phone":"M5 4h4l2 5-2.5 1.5a11 11 0 005 5L15 13l5 2v4a2 2 0 01-2 2A16 16 0 013 6a2 2 0 012-2z",
 "pin":"M12 21s7-6 7-11a7 7 0 10-14 0c0 5 7 11 7 11zM12 7.5a2.5 2.5 0 100 5 2.5 2.5 0 000-5z",
 "mail":"M3 6h18v12H3zM3 7l9 6 9-6",
 "check":"M5 12l5 5 9-10",
 "star":"M12 3l2.6 5.6 6.1.7-4.5 4.2 1.2 6L12 16.5l-5.4 3 1.2-6L3.3 9.3l6.1-.7z",
 "chev":"M6 9l6 6 6-6",
 "arrow":"M5 12h14M13 6l6 6-6 6",
 "stone":"M4 15c0-4 4-7 8-7s8 3 8 7-4 5-8 5-8-1-8-5z",
 "user":"M12 12a4 4 0 100-8 4 4 0 000 8zM4 21c0-4 4-6 8-6s8 2 8 6",
 "cal":"M4 6h16v14H4zM4 10h16M8 3v4M16 3v4",
 "chat":"M4 5h16v11H9l-5 4z",
 "close":"M6 6l12 12M18 6L6 18",
 "menu":"M4 7h16M4 12h16M4 17h16",
 "play":"M8 5l11 7-11 7z",
 "door":"M6 3h12v18H6zM15 12h.01M6 21h12",
 "fb":"M14 8h3V4h-3a4 4 0 00-4 4v3H7v4h3v6h4v-6h3l1-4h-4V8z",
 "tt":"M14 4v10a3 3 0 11-3-3M14 4c0 3 2 5 5 5",
 "couple":"M8 11a3 3 0 100-6 3 3 0 000 6zM16 11a3 3 0 100-6 3 3 0 000 6zM2 20c0-3 3-5 6-5s6 2 6 5M12 20c0-3 3-5 6-5s4 2 4 5",
}
def ic(n, cls="ic"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="{ICONS[n]}"/></svg>'

CAT = {c["id"]: c for c in CATS}
def frm(p): return min(i[4] for i in CAT[p]["items"])
PH = BIZ["phoneDisplay"]; TEL = "tel:" + BIZ["phone"]; SMS = "sms:" + BIZ["phone"]

def head(title, desc, page, extra=""):
    ld = '''<script type="application/ld+json">{"@context":"https://schema.org","@type":"HealthAndBeautyBusiness","name":"K'iin Spa & Lounge","description":"Full-service salon and spa in Plant City, Florida: massage therapy, facials, hair, nails, lashes and brows.","telephone":"+1-813-345-1049","address":{"@type":"PostalAddress","streetAddress":"119 S Collins St","addressLocality":"Plant City","addressRegion":"FL","addressCountry":"US"},"image":"assets/img/hero-bg.jpg","sameAs":["https://www.facebook.com/kiinspa.lounge"]}</script>'''
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{title}</title><meta name="description" content="{desc}"><meta name="theme-color" content="#241810">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:image" content="assets/img/hero-bg.jpg">
<link rel="icon" href="assets/img/favicon.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">{ld}{extra}
<script>document.documentElement.classList.add('js')</script></head>
<body data-page="{page}"><a class="skip" href="#main">Skip to content</a>'''

def header(active):
    sub = "".join(f'<a href="{c["page"]}"><span class="si">{ic(c["icon"])}</span><span><b>{c["nav"]}</b><small>From ${frm(c["id"])}</small></span></a>' for c in CATS)
    def a(p, label, k): return f'<a href="{p}"{" class=\"on\"" if active==k else ""}>{label}</a>'
    mob = "".join(f'<a href="{c["page"]}">{c["nav"]}</a>' for c in CATS)
    return f'''<header class="site-header"><div class="wrap hdr">
<a class="brand" href="index.html" aria-label="K'iin Spa &amp; Lounge, home"><img class="mk mk-l" src="assets/img/crest-light.png" alt="" width="34" height="40"><img class="mk mk-g" src="assets/img/crest-gold.png" alt="" width="34" height="40"><span class="bt"><b>K'iin</b><small>Spa &amp; Lounge</small></span></a>
<nav class="nav" id="nav" aria-label="Main">
{a("index.html","Home","home")}{a("about.html","About","about")}
<div class="has-sub{" on" if active=="services" else ""}"><a href="services.html" class="subtog">Services {ic("chev","ic chev")}</a>
<div class="sub"><div class="sub-in">{sub}<a class="sub-all" href="services.html">View full menu {ic("arrow")}</a></div></div>
<div class="msub">{mob}<a href="services.html">All services</a></div></div>
{a("gallery.html","Gallery","gallery")}{a("contact.html","Contact","contact")}
<a class="btn btn-primary mob-book" href="booking.html">Book now</a></nav>
<a class="btn btn-primary btn-sm hdr-cta" href="booking.html">Book now</a>
<button class="burger" aria-label="Open menu" aria-expanded="false" aria-controls="nav">{ic("menu")}</button>
</div></header><main id="main">'''

def footer():
    sv = "".join(f'<li><a href="{c["page"]}">{c["nav"]}</a></li>' for c in CATS)
    return f'''</main><footer class="site-footer"><div class="wrap">
<div class="f-top"><div class="f-brand"><img src="assets/img/logo-light.png" alt="K'iin Spa &amp; Lounge by Eva Vera" width="150" height="134" loading="lazy">
<p>A full-service salon and spa in downtown Plant City. Massage, skin, hair, nails and lashes, all in one calm place.</p>
<div class="soc"><a href="{BIZ["facebook"]}" aria-label="Facebook" target="_blank" rel="noopener">{ic("fb")}</a><a href="{BIZ["tiktok"]}" aria-label="TikTok" target="_blank" rel="noopener">{ic("tt")}</a><a href="{TEL}" aria-label="Call us">{ic("phone")}</a></div></div>
<div><h4>Explore</h4><ul><li><a href="index.html">Home</a></li><li><a href="about.html">About us</a></li><li><a href="services.html">All services</a></li><li><a href="gallery.html">Gallery</a></li><li><a href="booking.html">Book &amp; get a quote</a></li><li><a href="contact.html">Contact</a></li></ul></div>
<div><h4>Services</h4><ul>{sv}</ul></div>
<div><h4>Visit us</h4><address><a href="https://www.google.com/maps/search/?api=1&amp;query=119+S+Collins+St+Plant+City+FL" target="_blank" rel="noopener">119 S Collins St<br>Plant City, FL</a><br><a href="{TEL}">{PH}</a><br><span>By appointment. Call or book online.</span></address>
<a class="btn btn-ghost btn-sm" href="{BIZ["giftCardUrl"]}" target="_blank" rel="noopener">Buy a gift card</a></div></div>
<div class="f-bot"><span>&copy; <span id="yr">2026</span> K'iin Spa &amp; Lounge by Eva Vera. All rights reserved.</span><span><a href="contact.html">Privacy &amp; policies</a></span></div></div></footer>
<script src="https://cdn.jsdelivr.net/npm/@emailjs/browser@4/dist/email.min.js" defer></script>
<script src="js/config.js"></script><script src="js/main.js" defer></script></body></html>'''

def phero(title, sub, img, crumbs):
    cr = " / ".join(f'<a href="{h}">{t}</a>' if h else f'<span>{t}</span>' for t, h in crumbs)
    return f'''<section class="phero"><div class="phero-bg" data-parallax><img src="assets/img/{img}.jpg" alt=""></div><div class="phero-ov"></div>
<div class="wrap phero-in"><nav class="crumbs" aria-label="Breadcrumb">{cr}</nav><h1 data-reveal="mask">{title}</h1><p data-reveal="up" style="--d:.15s">{sub}</p></div></section>'''

def cta(title="Ready for your hour?", text="Build your quote in a minute and pick a time that suits you. You will get a copy by email.", img="cta-bg"):
    return f'''<section class="cta-band" style="--bg:url(assets/img/{img}.jpg)"><div class="wrap"><div data-reveal="up"><h2>{title}</h2><p>{text}</p></div>
<div class="cta-act" data-reveal="up" style="--d:.1s"><a class="btn btn-gold" href="booking.html">Book &amp; get a quote</a><a class="btn btn-ghost" href="{TEL}">Call {PH}</a></div></div></section>'''

def faq(items, title="Good questions"):
    d = "".join(f'<details><summary>{q}{ic("chev","ic chev")}</summary><p>{a}</p></details>' for q, a in items)
    return f'<section class="section"><div class="wrap narrow"><div class="sec-head center" data-reveal="up"><h2>{title}</h2></div><div class="faq" data-reveal="up">{d}</div></div></section>'

def svc_cards(cats=CATS, cls=""):
    out = ""
    for i, c in enumerate(cats):
        out += f'''<a class="svc-card" href="{c["page"]}" data-reveal="up" style="--d:{i*.08:.2f}s"><div class="svc-img"><img src="assets/img/{c["img"]}.jpg" alt="{c["name"]} at K'iin Spa" loading="lazy"><span class="from">From ${frm(c["id"])}</span></div>
<div class="svc-body"><span class="si">{ic(c["icon"])}</span><h3>{c["name"]}</h3><p>{c["short"]}</p><span class="more">Explore {ic("arrow")}</span></div></a>'''
    return f'<div class="svc-grid {cls}">{out}</div>'

def stars(n=5): return '<span class="stars" aria-label="5 out of 5 stars">' + ic("star", "ic st") * n + '</span>'

def ba(i, label_a="Before", label_b="After"):
    return f'''<div class="ba" data-ba><img src="assets/img/ba{i}-after.jpg" alt="After treatment (placeholder)" loading="lazy"><div class="ba-b"><img src="assets/img/ba{i}-before.jpg" alt="Before treatment (placeholder)" loading="lazy"></div>
<span class="ba-l ba-l1">{label_a}</span><span class="ba-l ba-l2">{label_b}</span><div class="ba-h"><span>{ic("chev","ic")}</span></div><input type="range" min="0" max="100" value="50" aria-label="Drag to compare before and after"></div>'''

def video_tiles(n=3):
    out = ""
    for i, v in enumerate(VIDEOS[:n]):
        out += f'''<button class="vid" data-video="{i}" aria-label="Play video: {v["title"]}"><img src="assets/img/{v["poster"]}.jpg" alt="" loading="lazy"><span class="play">{ic("play")}</span><span class="vt">{v["title"]}</span></button>'''
    return out

pages = {}

# ---------------- HOME ----------------
def hero_form():
    chips = "".join(f'<button type="button" class="qchip" data-cat="{c["id"]}">{ic(c["icon"])}<span>{c["name"]}</span></button>' for c in CATS)
    chips += f'<button type="button" class="qchip" data-cat="couples-pick">{ic("couple")}<span>Couples massage</span></button>'
    return f'''<div class="qf" id="heroQuote" aria-labelledby="qf-title"><div class="qf-head"><span class="qf-badge">Free quote</span><h2 id="qf-title">Get your quote in three steps</h2>
<div class="qf-prog" aria-hidden="true"><i></i><i></i><i></i></div></div>
<form novalidate>
<fieldset class="qs" data-s="1"><legend>What would you like?</legend><div class="qchips">{chips}</div><p class="qerr" role="alert"></p></fieldset>
<fieldset class="qs" data-s="2" hidden><legend>Choose your treatment and time</legend>
<label>Treatment<select name="svc" required></select></label>
<div class="row2"><label>Date<input type="date" name="date" required></label><label>Time<select name="time" required></select></label></div>
<label>Guests<select name="guests"><option>1</option><option>2</option><option>3</option><option>4</option></select></label><p class="qerr" role="alert"></p></fieldset>
<fieldset class="qs" data-s="3" hidden><legend>Where should we send it?</legend>
<label>Full name<input name="fullname" autocomplete="name" required></label>
<div class="row2"><label>Email<input type="email" name="email" autocomplete="email" required></label><label>Phone<input type="tel" name="phone" autocomplete="tel" required></label></div>
<div class="qest"><span>Estimated total</span><b data-est>$0</b></div><p class="qerr" role="alert"></p></fieldset>
<div class="qnav"><button type="button" class="btn btn-ghost btn-sm" data-back hidden>Back</button><button type="button" class="btn btn-gold" data-next>Continue</button></div>
</form><div class="qdone" hidden><span class="tick">{ic("check")}</span><h3>Your quote is on its way</h3><p>We have emailed a copy to you and to our team. Want to lock in your time?</p><a class="btn btn-gold" href="booking.html">Finish booking</a></div></div>'''

home = head("K'iin Spa & Lounge | Massage, Facials, Hair, Nails & Lashes in Plant City, FL",
  "K'iin Spa & Lounge is a full-service salon and spa in downtown Plant City, FL. Massage therapy, facials, hair, nails, lashes and brows. Get a free quote online.", "home") + header("home")
home += f'''<section class="hero" data-doors="closed" aria-label="Welcome to K'iin Spa and Lounge">
<div class="hero-bg" data-parallax="0.12"><img src="assets/img/hero-bg.jpg" alt="Guest relaxing on a massage table with a white towel and a flower" fetchpriority="high"></div><div class="hero-ov"></div>
<div class="doors" aria-hidden="true"><div class="door door-l"><i class="glass"></i><i class="handle"></i></div><div class="door door-r"><i class="glass"></i><i class="handle"></i></div><img class="door-crest" src="assets/img/crest-light.png" alt=""><div class="sweep"></div></div>
<canvas id="dust" aria-hidden="true"></canvas>
<div class="wrap hero-in"><div class="hero-copy"><p class="kick">Downtown Plant City, Florida</p>
<h1>Quiet hours,<br>beautifully kept.</h1>
<p class="lede">Massage therapy, facials, hair, nails and lashes together under one roof. Step through the door and let the day fall away.</p>
<div class="hero-act"><a class="btn btn-gold" href="booking.html">Book your visit</a><a class="btn btn-ghost" href="services.html">Explore services</a></div>
<ul class="hero-trust"><li>{ic("star")}<span><b>100%</b> recommend us on Facebook</span></li><li>{ic("gift")}<span>Gift cards available</span></li><li>{ic("phone")}<a href="{TEL}">{PH}</a></li></ul></div>
{hero_form()}</div>
<button class="doors-toggle" type="button" aria-pressed="false">{ic("door")}<span>Close the doors</span></button></section>

<div class="marquee" aria-hidden="true"><div class="mq-track">{"".join(f'<span>{c["name"]}</span>{ic("sparkle")}' for c in CATS*3)}</div></div>

<section class="section welcome"><div class="wrap split">
<div class="collage" data-reveal="up"><div class="arch a1"><img src="assets/img/about-1.jpg" alt="Spa treatment room" loading="lazy" data-parallax="0.06"></div><div class="arch a2"><img src="assets/img/about-2.jpg" alt="Spa details" loading="lazy"></div><div class="seal"><img src="assets/img/crest-gold.png" alt="" loading="lazy"></div></div>
<div class="txt"><p class="kick dk" data-reveal="up">Welcome to K'iin</p><h2 data-reveal="mask">A spa and salon that treats rest as the main event</h2>
<p data-reveal="up">K'iin Spa &amp; Lounge, by Eva Vera, is a full-service salon and spa on South Collins Street in Plant City. We bring massage, skin care, hair, nails and lash and brow work together so you can book one visit and leave looking and feeling taken care of.</p>
<p data-reveal="up">Our team listens first. Whether you are here for a deep-tissue session after a hard week, a color refresh, or a day with your best friend, we shape the appointment around you.</p>
<div class="stats" data-reveal="up"><div><b data-count="100" data-suffix="%">100%</b><span>recommend us on Facebook</span></div><div><b data-count="{len(CATS)}">{len(CATS)}</b><span>service studios under one roof</span></div><div><b data-count="{sum(len(c["items"]) for c in CATS)}" data-suffix="+">{sum(len(c["items"]) for c in CATS)}+</b><span>treatments on the menu</span></div></div>
<a class="btn btn-primary" href="about.html" data-reveal="up">Our story</a></div></div></section>

<section class="section soft"><div class="wrap"><div class="sec-head center"><p class="kick dk" data-reveal="up">The menu</p><h2 data-reveal="mask">Everything you need, in one place</h2><p data-reveal="up">Five studios, each led by specialists. Open any of them to see treatments, timing and prices.</p></div>
{svc_cards()}<div class="center mt" data-reveal="up"><a class="btn btn-ghost-d" href="services.html">See the full menu</a></div></div></section>

<section class="section dark packs"><div class="wrap"><div class="sec-head center"><p class="kick" data-reveal="up">Made for sharing</p><h2 data-reveal="mask">Spa days and special occasions</h2><p data-reveal="up">Not sure where to start? These combinations are our guests' favorites.</p></div>
<div class="pack-grid">
<article class="pack" data-reveal="up"><img src="assets/img/room-1.jpg" alt="Couples treatment room" loading="lazy"><div><span class="si">{ic("couple")}</span><h3>Couples retreat</h3><p>Two tables, one room, two therapists. Add a sparkling toast and a warm scalp treatment to make it an occasion.</p><a class="lnk" href="booking.html?service=couples">Quote this {ic("arrow")}</a></div></article>
<article class="pack" data-reveal="up" style="--d:.1s"><img src="assets/img/room-2.jpg" alt="Friends spa day" loading="lazy"><div><span class="si">{ic("heart")}</span><h3>Girls' day out</h3><p>Pedicures side by side, facials, blowouts and lashes. Bring the group and we will line up the schedule.</p><a class="lnk" href="booking.html?service=spapedi">Quote this {ic("arrow")}</a></div></article>
<article class="pack" data-reveal="up" style="--d:.2s"><img src="assets/img/gift.jpg" alt="Gift card" loading="lazy"><div><span class="si">{ic("gift")}</span><h3>Gift cards</h3><p>The easiest thoughtful gift. Send a digital gift card in a minute, for any amount.</p><a class="lnk" href="{BIZ["giftCardUrl"]}" target="_blank" rel="noopener">Buy a gift card {ic("arrow")}</a></div></article></div></div></section>

<section class="section"><div class="wrap"><div class="sec-head center"><p class="kick dk" data-reveal="up">Why guests return</p><h2 data-reveal="mask">Small details that add up</h2></div>
<div class="why">
{"".join(f'<div class="why-i" data-reveal="up" style="--d:{i*.07:.2f}s"><span class="si">{ic(a)}</span><h3>{b}</h3><p>{c}</p></div>' for i,(a,b,c) in enumerate([
("user","Licensed, caring specialists","Each studio is led by trained professionals who explain what they are doing and why."),
("shield","Spotless, sterilised, safe","Tools are cleaned between guests and linens are fresh for every visit."),
("lotus","Unrushed appointments","We build breathing room into the schedule so you never feel hurried."),
("sparkle","Everything under one roof","Hair, nails, lashes and massage in a single trip, back to back."),
("calendar" if False else "cal","Simple, transparent booking","Build your quote online, see the total, and choose a time that works."),
("heart","A welcome for everyone","Treatments tailored to every skin tone, hair texture and comfort level.")]))}
</div></div></section>

<section class="section soft visit"><div class="wrap"><div class="sec-head center"><p class="kick dk" data-reveal="up">Your visit</p><h2 data-reveal="mask">What a K'iin appointment feels like</h2></div>
<ol class="tl">
<li data-reveal="up"><h3>Book and get your quote</h3><p>Choose treatments, see the total instantly and pick a time. We email you a copy.</p></li>
<li data-reveal="up"><h3>Arrive and unwind</h3><p>Check in at South Collins Street. Settle in with something warm to drink.</p></li>
<li data-reveal="up"><h3>Consultation</h3><p>Your specialist talks through goals, preferences and anything to avoid.</p></li>
<li data-reveal="up"><h3>Your treatment</h3><p>Your hour, your pace. Phones away, shoulders down.</p></li>
<li data-reveal="up"><h3>Leave glowing</h3><p>Aftercare advice, and a rebooking at the front desk if you would like one.</p></li></ol></div></section>

<section class="section dark gal"><div class="wrap"><div class="sec-head center"><p class="kick" data-reveal="up">Proof, not promises</p><h2 data-reveal="mask">See the work</h2><p data-reveal="up">A look at the space and the results. Swap these placeholders for your own photos and videos.</p></div>
<div class="mosaic" data-reveal="up">
<button class="lb m1" data-full="assets/img/gallery-1.jpg" aria-label="Open photo"><img src="assets/img/gallery-1.jpg" alt="Gallery photo 1" loading="lazy"></button>
<button class="lb m2" data-full="assets/img/gallery-2.jpg" aria-label="Open photo"><img src="assets/img/gallery-2.jpg" alt="Gallery photo 2" loading="lazy"></button>
<div class="m3 vwrap">{video_tiles(1)}</div>
<button class="lb m4" data-full="assets/img/gallery-3.jpg" aria-label="Open photo"><img src="assets/img/gallery-3.jpg" alt="Gallery photo 3" loading="lazy"></button>
<button class="lb m5" data-full="assets/img/gallery-4.jpg" aria-label="Open photo"><img src="assets/img/gallery-4.jpg" alt="Gallery photo 4" loading="lazy"></button>
<button class="lb m6" data-full="assets/img/gallery-5.jpg" aria-label="Open photo"><img src="assets/img/gallery-5.jpg" alt="Gallery photo 5" loading="lazy"></button></div>
<div class="ba-row" data-reveal="up"><div><h3>Before and after</h3><p>Drag the handle to compare. Replace the images in the assets folder with your own client results.</p><a class="btn btn-ghost" href="gallery.html">Open the full gallery</a></div>{ba(1)}</div></div></section>

<section class="section testi"><div class="wrap"><div class="sec-head center"><p class="kick dk" data-reveal="up">Kind words</p><h2 data-reveal="mask">What guests say</h2><p data-reveal="up">Sample reviews shown as placeholders. Replace with real ones from your Facebook page.</p></div>
<div class="tslider" data-reveal="up"><div class="ttrack">
{"".join(f'<figure class="tcard">{stars()}<blockquote>{q}</blockquote><figcaption>{n}</figcaption></figure>' for q,n in [
("The calmest hour of my week. My therapist asked what I needed and then actually delivered it.","Guest review, massage"),
("My skin has never looked this good. She explained everything and did not push products.","Guest review, facial"),
("Came for a blowout, stayed for the lashes. Easy to book all of it in one trip.","Guest review, hair and lashes"),
("We did the couples massage for our anniversary and it was perfect from start to finish.","Guest review, couples"),
("Spotless, welcoming, and on time. Exactly what I want from a spa.","Guest review, nails")])}
</div><div class="tnav"><button aria-label="Previous review" data-t="-1">{ic("arrow")}</button><button aria-label="Next review" data-t="1">{ic("arrow")}</button></div></div></div></section>

<section class="section gift" style="--bg:url(assets/img/gift.jpg)"><div class="wrap gift-in"><div data-reveal="up"><span class="si">{ic("gift")}</span><h2>Give someone an hour to themselves</h2><p>Send a K'iin gift card by email in a few clicks. Perfect for birthdays, thank-yous and just-because.</p></div><a class="btn btn-gold" href="{BIZ["giftCardUrl"]}" target="_blank" rel="noopener" data-reveal="up">Buy a gift card</a></div></section>

<section class="section"><div class="wrap split rev"><div class="txt"><p class="kick dk" data-reveal="up">Find us</p><h2 data-reveal="mask">On South Collins Street, in the heart of Plant City</h2>
<ul class="contact-l" data-reveal="up"><li>{ic("pin")}<a href="https://www.google.com/maps/search/?api=1&amp;query=119+S+Collins+St+Plant+City+FL" target="_blank" rel="noopener">119 S Collins St, Plant City, FL</a></li><li>{ic("phone")}<a href="{TEL}">{PH}</a></li><li>{ic("clock")}<span>By appointment. Call for current hours.</span></li></ul>
<div class="hero-act" data-reveal="up"><a class="btn btn-primary" href="booking.html">Book online</a><a class="btn btn-ghost-d" href="contact.html">Contact us</a></div></div>
<div class="map" data-reveal="up"><iframe title="Map to K'iin Spa & Lounge" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="https://www.google.com/maps?q=119+S+Collins+St,+Plant+City,+FL&amp;output=embed"></iframe></div></div></section>

{faq([("Do I need an appointment?","Yes, we work by appointment so every guest gets unhurried time. Book online or call (813) 345-1049."),("How does the online quote work?","Choose your treatments and add-ons, and we show an instant estimate. When you confirm, a copy goes to your email and to our team, and we reach out to finalize your time."),("Can I combine services in one visit?","Yes. Many guests pair a massage with a facial, or hair with nails. Add them all in the booking tool and we will plan the sequence."),("Do you offer gift cards?","Yes. Gift cards are available online through our gift card page."),("What if I need to reschedule?","Call or message us as early as you can and we will find a new time.")], "Before you book")}
{cta()}'''
home += footer()
pages["index.html"] = home

# ---------------- SERVICES OVERVIEW ----------------
s = head("Services & Menu | K'iin Spa & Lounge, Plant City, FL", "Explore massage, facials, hair, nails, lashes and brows at K'iin Spa & Lounge in Plant City, FL. See treatments, timing and prices.", "services") + header("services")
s += phero("Our services", "Five studios, one calm address. Choose what you need today, or build a whole afternoon.", "svc-massage", [("Home","index.html"),("Services",None)])
s += '<section class="section"><div class="wrap"><div class="chooser" data-reveal="up"><span>I want to</span>' + "".join(f'<a href="#{c["id"]}">{t}</a>' for c, t in zip(CATS, ["unwind","glow","restyle","pamper my hands and feet","frame my eyes"])) + '</div></div></section>'
for i, c in enumerate(CATS):
    rows = "".join(f'<li><div><b>{n}</b><small>{d}</small></div><span class="mn">{m} min</span><span class="pr">${p}</span></li>' for _, n, d, m, p, _ in c["items"][:5])
    s += f'''<section class="section{" soft" if i%2 else ""} srow" id="{c["id"]}"><div class="wrap split{" rev" if i%2 else ""}">
<div class="srow-img arch" data-reveal="up"><img src="assets/img/{c["img"]}.jpg" alt="{c["name"]}" loading="lazy"></div>
<div class="txt"><span class="si" data-reveal="up">{ic(c["icon"])}</span><h2 data-reveal="mask">{c["name"]}</h2><p data-reveal="up">{c["intro"][0]}</p><ul class="menu" data-reveal="up">{rows}</ul>
<div class="hero-act" data-reveal="up"><a class="btn btn-primary" href="{c["page"]}">See all {c["nav"].lower()}</a><a class="btn btn-ghost-d" href="booking.html?cat={c["id"]}">Get a quote</a></div></div></div></section>'''
s += f'''<section class="section dark"><div class="wrap"><div class="sec-head center"><p class="kick" data-reveal="up">Make it yours</p><h2 data-reveal="mask">Add-ons for any visit</h2></div><div class="addons">{"".join(f'<div class="addon" data-reveal="up"><span>{n}</span><b>+${p}</b></div>' for _,n,p in ADDONS)}</div><p class="center small" data-reveal="up">Prices shown are starting guides and may vary by hair length, add-ons and specialist.</p></div></section>'''
s += faq([("Can I mix services from different studios?","Yes. Add anything from any studio in the booking tool and we will schedule them back to back."),("Are prices final?","They are our current menu prices. Hair length, extras and add-ons can change the total, and we confirm before your visit."),("Do you offer packages?","Yes, couples and group experiences. Ask us when you book."),("How do I pay?","Payment is handled at your visit. Ask us about accepted methods when we confirm.")], "Menu questions") + cta() + footer()
pages["services.html"] = s

# ---------------- SERVICE PAGES ----------------
for c in CATS:
    rel = [x for x in CATS if x["id"] != c["id"]][:3]
    rows = "".join(f'<li data-reveal="up"><div><b>{n}</b><small>{d}</small></div><span class="mn">{m} min</span><span class="pr">${p}{" /pair" if pr else ""}</span><a class="btn btn-ghost-d btn-sm" href="booking.html?service={i}" aria-label="Add {n} to quote">Add</a></li>' for i, n, d, m, p, pr in c["items"])
    ben = "".join(f'<div class="why-i" data-reveal="up" style="--d:{k*.07:.2f}s"><span class="si">{ic(a)}</span><h3>{b}</h3><p>{t}</p></div>' for k, (a, b, t) in enumerate(c["benefits"]))
    stp = "".join(f'<li data-reveal="up"><h3>{a}</h3><p>{b}</p></li>' for a, b in c["steps"])
    know = "".join(f'<li>{ic("check")}<span>{k}</span></li>' for k in c["know"])
    p = head(f'{c["name"]} in Plant City, FL | K\'iin Spa & Lounge', c["short"] + " Book online with an instant quote.", c["id"]) + header("services")
    p += phero(c["name"], c["tagline"], c["img"], [("Home","index.html"),("Services","services.html"),(c["name"],None)])
    p += f'''<section class="section"><div class="wrap split"><div class="collage two" data-reveal="up"><div class="arch a1"><img src="assets/img/{c["img"]}.jpg" alt="{c["name"]}" loading="lazy"></div><div class="arch a2"><img src="assets/img/{c["img2"]}.jpg" alt="{c["name"]} detail" loading="lazy"></div></div>
<div class="txt"><p class="kick dk" data-reveal="up">{c["hero"]}</p><h2 data-reveal="mask">{c["tagline"]}</h2><p data-reveal="up">{c["intro"][0]}</p><p data-reveal="up">{c["intro"][1]}</p>
<div class="hero-act" data-reveal="up"><a class="btn btn-primary" href="booking.html?cat={c["id"]}">Get a quote</a><a class="btn btn-ghost-d" href="{TEL}">Call {PH}</a></div></div></div></section>
<section class="section soft"><div class="wrap narrow"><div class="sec-head center"><p class="kick dk" data-reveal="up">The menu</p><h2 data-reveal="mask">Treatments and prices</h2><p data-reveal="up">Tap Add to start your quote with that treatment selected.</p></div><ul class="menu big">{rows}</ul></div></section>
<section class="section"><div class="wrap"><div class="sec-head center"><p class="kick dk" data-reveal="up">Why it helps</p><h2 data-reveal="mask">What you will notice</h2></div><div class="why four">{ben}</div></div></section>
<section class="section dark"><div class="wrap"><div class="sec-head center"><p class="kick" data-reveal="up">Your appointment</p><h2 data-reveal="mask">What to expect, step by step</h2></div><ol class="tl">{stp}</ol></div></section>
<section class="section"><div class="wrap split"><div class="txt"><p class="kick dk" data-reveal="up">Good to know</p><h2 data-reveal="mask">Preparing for your visit</h2><ul class="ticks" data-reveal="up">{know}</ul></div><div class="ba-col" data-reveal="up">{ba(1 if c["id"] in ("massage","facials","hair") else 2)}<p class="small">Placeholder results. Replace with your own before and after photos.</p></div></div></section>
{faq(c["faq"], c["name"] + " questions")}
<section class="section soft"><div class="wrap"><div class="sec-head center"><p class="kick dk" data-reveal="up">Pair it with</p><h2 data-reveal="mask">More from K'iin</h2></div>{svc_cards(rel)}</div></section>
{cta("Book your " + c["name"].lower().replace(" & "," and ") + " visit")}'''
    p += footer()
    pages[c["page"]] = p

# ---------------- ABOUT ----------------
a = head("About K'iin Spa & Lounge | Plant City, FL", "Meet K'iin Spa & Lounge by Eva Vera, a full-service salon and spa in downtown Plant City, Florida.", "about") + header("about")
a += phero("About K'iin", "A salon and spa built around unhurried time, honest advice and genuine care.", "about-1", [("Home","index.html"),("About",None)])
a += f'''<section class="section"><div class="wrap split"><div class="collage" data-reveal="up"><div class="arch a1"><img src="assets/img/about-1.jpg" alt="Inside K'iin Spa" loading="lazy"></div><div class="arch a2"><img src="assets/img/about-3.jpg" alt="Treatment detail" loading="lazy"></div><div class="seal"><img src="assets/img/crest-gold.png" alt="" loading="lazy"></div></div>
<div class="txt"><p class="kick dk" data-reveal="up">Our story</p><h2 data-reveal="mask">Created by Eva Vera for people who rarely stop</h2>
<p data-reveal="up">K'iin Spa &amp; Lounge was created by Eva Vera to give Plant City a place where care is done properly. The name is a nod to light and time, and that is the idea: a calm space where an hour belongs entirely to you.</p>
<p data-reveal="up">Over the years the studio has grown from a single service into a full salon and spa, with specialists in massage, skin, hair, nails and lashes. What has not changed is the standard: welcome warmly, listen carefully, work with skill and send you home better than you arrived.</p>
<p class="note" data-reveal="up">Owner tip: replace this story with Eva's own words, her training and the year K'iin opened.</p>
<a class="btn btn-primary" href="booking.html" data-reveal="up">Book with us</a></div></div></section>
<section class="section dark"><div class="wrap"><div class="sec-head center"><p class="kick" data-reveal="up">What we stand for</p><h2 data-reveal="mask">Our principles</h2></div><div class="why four">
{"".join(f'<div class="why-i" data-reveal="up" style="--d:{k*.07:.2f}s"><span class="si">{ic(i)}</span><h3>{t}</h3><p>{d}</p></div>' for k,(i,t,d) in enumerate([("clock","Time is the luxury","We never rush, so you never feel rushed."),("shield","Clean, always","Sterilised tools, fresh linens and a spotless space."),("heart","Care for everyone","Every guest, skin tone and hair texture, welcomed and understood."),("sparkle","Honest advice","Only what you need, explained plainly.")]))}</div></div></section>
<section class="section"><div class="wrap"><div class="sec-head center"><p class="kick dk" data-reveal="up">The team</p><h2 data-reveal="mask">The people behind the doors</h2><p data-reveal="up">Placeholder profiles. Replace the photos and names with your team.</p></div>
<div class="team">{"".join(f'<article class="member" data-reveal="up" style="--d:{k*.08:.2f}s"><div class="arch"><img src="assets/img/team-{k+1}.jpg" alt="{n}" loading="lazy"></div><h3>{n}</h3><span>{r}</span></article>' for k,(n,r) in enumerate([("Eva Vera","Founder and creative director"),("Your name here","Lead massage therapist"),("Your name here","Hair and beauty specialist")]))}</div></div></section>
<section class="section soft"><div class="wrap"><div class="stats big" data-reveal="up"><div><b data-count="100" data-suffix="%">100%</b><span>recommend us on Facebook</span></div><div><b data-count="{len(CATS)}">{len(CATS)}</b><span>studios under one roof</span></div><div><b data-count="{sum(len(c["items"]) for c in CATS)}" data-suffix="+">{sum(len(c["items"]) for c in CATS)}+</b><span>treatments</span></div></div></div></section>
{cta("Come and see the space", "Book a treatment or call us to arrange a visit.")}'''
a += footer(); pages["about.html"] = a

# ---------------- GALLERY ----------------
g = head("Gallery | K'iin Spa & Lounge, Plant City, FL", "Photos, before and after results and videos from K'iin Spa & Lounge in Plant City, FL.", "gallery") + header("gallery")
g += phero("Gallery", "The space, the work and the glow afterwards.", "gallery-1", [("Home","index.html"),("Gallery",None)])
cats = [("all","All"),("massage","Massage"),("facials","Facials"),("hair","Hair"),("nails","Nails"),("lashes","Lashes & Brows"),("space","The space")]
assign = ["massage","facials","hair","nails","lashes","space","massage","hair","space"]
gl = "".join(f'<button class="lb g-{["tall","wide","","","tall","","wide","",""][i]}" data-cat="{assign[i]}" data-full="assets/img/gallery-{i+1}.jpg" aria-label="Open photo {i+1}"><img src="assets/img/gallery-{i+1}.jpg" alt="Gallery photo {i+1}" loading="lazy"></button>' for i in range(9))
g += f'''<section class="section"><div class="wrap"><div class="filters" role="tablist" aria-label="Filter gallery">{"".join(f'<button class="{"on" if k=="all" else ""}" data-f="{k}">{t}</button>' for k,t in cats)}</div><div class="gal-grid" data-reveal="up">{gl}</div><p class="center small mt">Placeholder photos. Replace gallery-1.jpg to gallery-9.jpg in assets/img with your own.</p></div></section>
<section class="section soft"><div class="wrap"><div class="sec-head center"><p class="kick dk" data-reveal="up">Results</p><h2 data-reveal="mask">Before and after</h2><p data-reveal="up">Drag to compare.</p></div><div class="ba-pair" data-reveal="up">{ba(1)}{ba(2)}</div></div></section>
<section class="section dark"><div class="wrap"><div class="sec-head center"><p class="kick" data-reveal="up">Watch</p><h2 data-reveal="mask">Video gallery</h2><p data-reveal="up">Play our TikTok videos right here. Paste each video's ID into js/config.js (see the README).</p></div><div class="vgrid" data-reveal="up">{video_tiles(3)}</div>
<div class="center mt" data-reveal="up"><a class="btn btn-ghost" href="{BIZ["tiktok"]}" target="_blank" rel="noopener">Follow us on TikTok</a> <a class="btn btn-ghost" href="{BIZ["facebook"]}" target="_blank" rel="noopener">Follow us on Facebook</a></div></div></section>{cta()}'''
g += footer(); pages["gallery.html"] = g

# ---------------- BOOKING ----------------
b = head("Book & Get a Quote | K'iin Spa & Lounge, Plant City, FL", "Build your treatment quote, choose a date and book at K'iin Spa & Lounge in Plant City, FL. A copy is emailed to you instantly.", "booking") + header("booking")
b += phero("Book &amp; get your quote", "Choose treatments, watch your total update, and confirm. We email you a copy right away.", "svc-massage-2", [("Home","index.html"),("Book",None)])
b += f'''<section class="section book"><div class="wrap book-grid"><div class="bk" id="bk">
<ol class="steps" aria-label="Booking progress"><li class="on"><i>1</i><span>Treatments</span></li><li><i>2</i><span>Add-ons</span></li><li><i>3</i><span>Date &amp; time</span></li><li><i>4</i><span>Your details</span></li><li><i>5</i><span>Review</span></li></ol>
<form novalidate>
<fieldset class="bs" data-s="1"><legend>Choose your treatments</legend><div class="pick"></div></fieldset>
<fieldset class="bs" data-s="2" hidden><legend>Add a little extra</legend><div class="addpick"></div><div class="tipbox"><b>Gratuity (optional estimate)</b><div class="tips"><label><input type="radio" name="tip" value="0" checked><span>None</span></label><label><input type="radio" name="tip" value="15"><span>15%</span></label><label><input type="radio" name="tip" value="20"><span>20%</span></label><label><input type="radio" name="tip" value="25"><span>25%</span></label></div></div></fieldset>
<fieldset class="bs" data-s="3" hidden><legend>When would you like to come in?</legend><div class="row2"><label>Preferred date<input type="date" name="date" required></label><label>Preferred time<select name="time" required></select></label></div><div class="row2"><label>Number of guests<select name="guests"><option>1</option><option>2</option><option>3</option><option>4</option><option>5</option><option>6</option></select></label><label>Second choice (optional)<input type="date" name="date2"></label></div><label>Notes for your specialist<textarea name="notes" rows="3" placeholder="Allergies, pressure preference, special occasions"></textarea></label></fieldset>
<fieldset class="bs" data-s="4" hidden><legend>Where should we send your quote?</legend><label>Full name<input name="fullname" autocomplete="name" required></label><div class="row2"><label>Email<input type="email" name="email" autocomplete="email" required></label><label>Phone<input type="tel" name="phone" autocomplete="tel" required></label></div><label class="chk"><input type="checkbox" name="consent" required><span>I understand this is a quote request and that K'iin will confirm my appointment time.</span></label></fieldset>
<fieldset class="bs" data-s="5" hidden><legend>Review and confirm</legend><div class="review"></div></fieldset>
<p class="berr" role="alert"></p><div class="bnav"><button type="button" class="btn btn-ghost-d" data-back hidden>Back</button><button type="button" class="btn btn-primary" data-next>Continue</button></div></form></div>
<aside class="quote" aria-label="Your quote"><h2>Your quote</h2><ul class="ql"></ul><dl><div><dt>Subtotal</dt><dd data-sub>$0</dd></div><div class="tx"><dt>Tax</dt><dd data-tax>$0</dd></div><div class="tp"><dt>Gratuity</dt><dd data-tip>$0</dd></div><div class="tot"><dt>Estimated total</dt><dd data-tot>$0</dd></div></dl><p class="small"><span data-dur>0 min</span> of treatment time. Final pricing is confirmed by our team.</p><a class="btn btn-ghost-d btn-sm" href="{TEL}">Prefer to call? {PH}</a></aside></div>
<div class="done" id="bookDone" hidden><div class="done-in"><span class="tick">{ic("check")}</span><h2>Thank you, <span data-dn></span></h2><p>Your quote <b data-qid></b> has been sent to <b data-de></b>, and a copy has gone to our team. We will be in touch to confirm your time.</p><p class="demo" hidden>Demo mode: emails are not connected yet. See the README to switch on EmailJS.</p><div class="hero-act"><button class="btn btn-primary" onclick="window.print()">Print or save quote</button><a class="btn btn-ghost-d" href="index.html">Back to home</a></div></div></div></section>'''
b += footer(); pages["booking.html"] = b

# ---------------- CONTACT ----------------
ct = head("Contact | K'iin Spa & Lounge, Plant City, FL", "Call, message or visit K'iin Spa & Lounge at 119 S Collins St, Plant City, FL. Phone (813) 345-1049.", "contact") + header("contact")
ct += phero("Contact us", "Questions, special requests or a group booking? We would love to hear from you.", "about-2", [("Home","index.html"),("Contact",None)])
ct += f'''<section class="section"><div class="wrap"><div class="cards3">
<a class="icard" href="{TEL}" data-reveal="up"><span class="si">{ic("phone")}</span><h3>Call us</h3><p>{PH}</p></a>
<a class="icard" href="{SMS}" data-reveal="up" style="--d:.08s"><span class="si">{ic("chat")}</span><h3>Text or message</h3><p>Text us, or reach us on Facebook Messenger.</p></a>
<a class="icard" href="https://www.google.com/maps/search/?api=1&amp;query=119+S+Collins+St+Plant+City+FL" target="_blank" rel="noopener" data-reveal="up" style="--d:.16s"><span class="si">{ic("pin")}</span><h3>Visit</h3><p>119 S Collins St<br>Plant City, FL</p></a></div>
<div class="split mt2"><div class="txt"><h2 data-reveal="mask">Send us a message</h2><p data-reveal="up">Tell us what you are planning and we will reply by phone or email.</p>
<form class="cform" id="contactForm" novalidate data-reveal="up"><label>Full name<input name="fullname" required autocomplete="name"></label><div class="row2"><label>Email<input type="email" name="email" required autocomplete="email"></label><label>Phone<input type="tel" name="phone" autocomplete="tel"></label></div><label>How can we help?<textarea name="message" rows="5" required></textarea></label><p class="berr" role="alert"></p><button class="btn btn-primary" type="submit">Send message</button><p class="ok" hidden>Thank you. Your message has been sent and we will reply soon.</p></form></div>
<div class="map" data-reveal="up"><iframe title="Map to K'iin Spa & Lounge" loading="lazy" src="https://www.google.com/maps?q=119+S+Collins+St,+Plant+City,+FL&amp;output=embed"></iframe></div></div></div></section>
<section class="section soft"><div class="wrap narrow"><div class="sec-head center"><h2 data-reveal="mask">Visit and policies</h2></div><div class="pol" data-reveal="up"><div><h3>Hours</h3><p>By appointment. Call {PH} for current hours.</p></div><div><h3>Late arrivals</h3><p>Please arrive ten minutes early. Late arrivals may shorten your treatment so we can respect the next guest.</p></div><div><h3>Changes and cancellations</h3><p>Let us know as early as possible if your plans change so we can offer your time to someone else.</p></div><div><h3>Gift cards</h3><p>Available online through our gift card page.</p></div></div></div></section>
{faq([("Is there parking nearby?","Please check with us when booking and we will point you to the easiest spot."),("Can I bring a guest?","Yes for group bookings and couples treatments. Tell us your party size when you book."),("Do you take walk-ins?","We work by appointment. Call us and we will see what is available."),("Are products safe for sensitive skin?","Tell us about allergies when booking and we will choose accordingly.")], "Quick answers")}{cta()}'''
ct += footer(); pages["contact.html"] = ct

# ---------------- WRITE ----------------
for n, h in pages.items():
    open(n, "w", encoding="utf-8").write(h)

cfg = {"business": BIZ, "emailjs": {"publicKey": "YOUR_EMAILJS_PUBLIC_KEY", "serviceId": "YOUR_SERVICE_ID", "templateId": "YOUR_TEMPLATE_ID"},
       "taxRate": 0, "slots": SLOTS,
       "categories": [{"id": c["id"], "name": c["name"], "icon": c["icon"], "page": c["page"]} for c in CATS],
       "services": [{"id": i, "cat": c["id"], "name": n, "desc": d, "mins": m, "price": p, "pair": pr} for c in CATS for i, n, d, m, p, pr in c["items"]],
       "addons": [{"id": i, "name": n, "price": p} for i, n, p in ADDONS], "videos": VIDEOS}
open("js/config.js", "w", encoding="utf-8").write("/* ==== EDIT ME ====\n   Business details, EmailJS keys, prices, add-ons, time slots and TikTok videos live here. */\nwindow.KIIN = " + json.dumps(cfg, indent=2) + ";\n")
print(len(pages), "pages")
