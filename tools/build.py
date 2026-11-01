# Builds the site pages (shared header, footer and page frames). Run: python tools/build.py
# Page text lives here and in content.py; legal page text lives in tools/legal/*.html.
import re, sys, os
sys.path.insert(0, os.path.dirname(__file__))
from content import *
OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

LOGO = '''<svg class="mark" width="34" height="34" viewBox="0 0 40 40" aria-hidden="true"><path d="M5 7 H13.5 L35 33 H26.5 Z" fill="#FF603B"/><path d="M26.5 7 H35 L25.2 18.9 L21 13.8 Z" fill="#FF603B"/><path d="M17.2 18.4 L21.4 23.5 L17.5 28.2 H24 L21.6 33 H5 Z" fill="#FF603B"/></svg>'''

NAV = [('/', 'Home'), ('/services', 'Services'), ('/work', 'Our Work'), ('/about', 'About'), ('/pricing', 'Pricing'), ('/contact', 'Contact')]

def header(active):
    links = '\n'.join(f'<a href="{h}"{" aria-current=\"page\"" if h == active else ""}>{t}</a>' for h, t in NAV)
    return f'''<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
<div class="wrap bar">
<a class="brand" href="/" aria-label="Litrix Technologies home">{LOGO}<span class="brand-name"><strong>Litrix</strong><small>TECHNOLOGIES</small></span></a>
<nav class="nav" aria-label="Main">
{links}
</nav>
<a class="btn btn-primary btn-sm hide-sm" href="/contact">Start a Project {ARROW}</a>
<details class="menu">
<summary><span class="sr-only">Menu</span><svg width="24" height="24" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></summary>
<nav class="menu-panel" aria-label="Main (mobile)">
{links}
<a class="btn btn-primary" href="/contact">Start a Project {ARROW}</a>
</nav>
</details>
</div>
</header>'''

FOOTER = f'''<footer class="site-footer">
<div class="wrap foot">
<div class="foot-brand">
<a class="brand" href="/" aria-label="Litrix Technologies home">{LOGO}<span class="brand-name"><strong>Litrix</strong><small>TECHNOLOGIES</small></span></a>
<p>Websites, automation and digital support for local businesses. Based in Snellville, Georgia.</p>
</div>
<nav aria-label="Site">
<h2>Site</h2>
<a href="/services">Services</a><a href="/work">Our Work</a><a href="/about">About</a><a href="/pricing">Pricing</a><a href="/contact">Contact</a>
</nav>
<nav aria-label="Policies">
<h2>Policies</h2>
<a href="/terms">Terms of service</a><a href="/refunds">Refunds and cancellations</a><a href="/privacy">Privacy policy</a>
</nav>
<div>
<h2>Contact</h2>
<a href="{TEL}">{PHONE}</a>
<p>Calls and texts welcome.</p>
</div>
</div>
<div class="wrap foot-base"><span>© 2026 Litrix Technologies · Snellville, Georgia</span></div>
</footer>'''

def page(fname, title, desc, active, body, noindex=False, script=False):
    robots = '<meta name="robots" content="noindex">\n' if noindex else ''
    js = '<script src="/form.js" defer></script>\n' if script else ''
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{robots}<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="theme-color" content="#0B0D10">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&amp;family=Manrope:wght@600;700;800&amp;display=swap">
<link rel="stylesheet" href="/styles.css">
{js}</head>
<body>
{header(active)}
<main id="main">
{body}
</main>
{FOOTER}
</body>
</html>
'''
    open(os.path.join(OUT, fname), 'w').write(html)

WAVES = '''<svg class="waves" viewBox="0 0 800 600" aria-hidden="true" preserveAspectRatio="xMidYMid slice">
<defs>
<linearGradient id="wg" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF603B" stop-opacity="0"/><stop offset=".45" stop-color="#FF603B" stop-opacity=".9"/><stop offset="1" stop-color="#FFB08F" stop-opacity=".15"/></linearGradient>
<radialGradient id="glow" cx=".62" cy=".5" r=".5"><stop offset="0" stop-color="#FF603B" stop-opacity=".28"/><stop offset="1" stop-color="#FF603B" stop-opacity="0"/></radialGradient>
</defs>
<rect width="800" height="600" fill="url(#glow)"/>
''' + '\n'.join(
    f'<path d="M-50 {470 - i*9} C 180 {520 - i*16}, 330 {150 + i*6}, 520 {230 + i*4} S 760 {40 + i*11}, 860 {80 + i*7}" fill="none" stroke="url(#wg)" stroke-width="{1.4 if i % 4 else 2.2}" opacity="{0.25 + (i % 7) * 0.09:.2f}"/>'
    for i in range(26)) + '\n</svg>'

def card_service(icon_name, title, text, href='/services'):
    return f'''<a class="card card-link" href="{href}">
{icon(icon_name)}
<h3>{title}</h3>
<p>{text}</p>
<span class="card-arrow" aria-hidden="true">{RIGHT}</span>
</a>'''

# ---------- Home ----------
home = f'''<section class="hero">
{WAVES}
<div class="wrap hero-inner">
{eyebrow("Litrix Technologies")}
<h1>Technology that moves your business <em>forward.</em></h1>
<p class="lede">We design modern websites, build intelligent automations, and create digital solutions that help your business work smarter and stand out.</p>
<div class="actions">
<a class="btn btn-primary" href="/contact">Start a Project {ARROW}</a>
<a class="btn btn-ghost" href="/work">Explore Our Work {RIGHT}</a>
</div>
</div>
<div class="wrap">
<ul class="strip" aria-label="What we do">
<li>{icon("monitor")}<span>Websites &amp; Digital Experiences</span></li>
<li>{icon("spark")}<span>Automation &amp; AI Solutions</span></li>
<li>{icon("layers")}<span>Branding &amp; UI/UX Design</span></li>
<li>{icon("shield")}<span>IT Support &amp; Security</span></li>
</ul>
</div>
</section>

<section class="section" aria-labelledby="svc-title">
<div class="wrap">
<div class="split-head">
<div>{eyebrow("Our services")}<h2 id="svc-title" class="display">End-to-end digital <em>solutions.</em></h2></div>
<div><p class="muted">From fast, phone-friendly websites to smart automation, we provide the technology, design and support to help your business grow.</p><a class="text-link" href="/services">View All Services {RIGHT}</a></div>
</div>
<div class="grid grid-3">
{card_service("monitor","Web Design &amp; Development","Modern, fast and responsive websites that make your phone ring.")}
{card_service("spark","AI Assistants &amp; Automation","Save time and cut repetitive work with smart, practical tools.")}
{card_service("layers","Branding &amp; UI/UX Design","A consistent, professional look your customers recognize and trust.")}
</div>
</div>
</section>

<section class="section section-alt" aria-labelledby="work-title">
<div class="wrap">
<div class="split-head">
<div>{eyebrow("Featured work")}<h2 id="work-title" class="display">Selected projects.</h2></div>
<div><p class="muted">Real projects will appear here once they are live and the client has said yes to sharing them.</p><a class="text-link" href="/work">About our work {RIGHT}</a></div>
</div>
<div class="grid grid-3">
<div class="card placeholder"><span class="tag">Coming soon</span><h3>Your project could be first</h3><p>We are taking on our first three clients at founding prices.</p><a class="text-link" href="/pricing">See founding prices {RIGHT}</a></div>
<div class="card placeholder"><span class="tag">In progress</span><h3>Client websites in progress</h3><p>We only show work with the client's permission, after launch.</p></div>
<div class="card placeholder"><span class="tag">How we work</span><h3>See the process</h3><p>From first chat to launch in a few clear steps.</p><a class="text-link" href="#process">How it works {RIGHT}</a></div>
</div>
</div>
</section>

<section class="section" id="process" aria-labelledby="process-title">
<div class="wrap">
{eyebrow("How it works")}
<h2 id="process-title" class="display">From first chat to <em>launch.</em></h2>
<ol class="flow">
<li>{icon("compass")}<strong>Discover</strong><span>Look through our services and pricing.</span></li>
<li>{icon("chat")}<strong>Talk</strong><span>Send a message or call. The first chat is free.</span></li>
<li>{icon("doc")}<strong>Plan</strong><span>Get a clear written scope and price before any work starts.</span></li>
<li>{icon("pen")}<strong>Build</strong><span>See a working draft within 7 business days of getting your content.</span></li>
<li>{icon("flag")}<strong>Launch</strong><span>Go live, and it's yours. Optional monthly care after that.</span></li>
</ol>
</div>
</section>

{CTA_BAND}'''
page('index.html', 'Litrix Technologies | Technology that moves your business forward', 'Litrix Technologies designs modern websites, builds smart automations and supports local businesses in Snellville and east metro Atlanta.', '/', home)

# ---------- Services ----------
svc_cards = '\n'.join(f'''<article class="card" id="{sid}">
{icon(ic)}
<h2>{t}</h2>
<p>{d}</p>
</article>''' for ic, t, d, sid in SERVICES)
services = f'''<section class="page-hero">
{WAVES}
<div class="wrap">
{eyebrow("Services")}
<h1>Our Services</h1>
<p class="lede">Practical digital solutions to help your business grow, run more smoothly and stand out.</p>
</div>
</section>
<section class="section">
<div class="wrap">
<div class="grid grid-3 services">
{svc_cards}
</div>
<p class="note">Every job is quoted in writing before work starts. We don't promise rankings or a number of calls. We promise work that does what we agreed, on time, that you own. See <a href="/pricing">pricing</a>.</p>
</div>
</section>
{CTA_BAND}'''
page('services.html', 'Services | Litrix Technologies', 'Web design, website care and hosting, automation, branding, IT help and Google Business Profile setup from Litrix Technologies.', '/services', services)

# ---------- Work ----------
work = f'''<section class="page-hero">
{WAVES}
<div class="wrap">
{eyebrow("Our work")}
<h1>Work we're <em>proud of.</em></h1>
<p class="lede">We are a new studio, and we only show real projects, with the client's permission, once they are live.</p>
</div>
</section>
<section class="section">
<div class="wrap">
<div class="empty">
<h2>Our first projects are on the way</h2>
<p>Client websites are in progress now. Each one will appear here as a short story: the business, what they needed, what we built, and how it's going.</p>
<div class="actions">
<a class="btn btn-primary" href="/contact">Be one of our first clients {ARROW}</a>
<a class="btn btn-ghost" href="/pricing">See founding prices {RIGHT}</a>
</div>
</div>
</div>
</section>
{CTA_BAND}'''
page('work.html', 'Our Work | Litrix Technologies', 'Projects by Litrix Technologies. Real client work appears here once it is live and shared with permission.', '/work', work)

# ---------- About ----------
about = f'''<section class="page-hero">
{WAVES}
<div class="wrap">
{eyebrow("About")}
<h1>Local, and <em>reachable.</em></h1>
<p class="lede">Litrix Technologies is a small technology business based in Snellville, Georgia, serving Snellville, Lithonia, Stone Mountain and nearby.</p>
</div>
</section>
<section class="section">
<div class="wrap grid grid-2 about">
<div>
<h2 class="display-sm">How we work</h2>
<p>Plain answers, fair prices and real follow-through. You'll always know what we're doing and what it costs before we start.</p>
<p>We also help homeowners set up and fix home Wi-Fi, TVs and streaming, and new devices. Those jobs are quoted up front, before any work begins.</p>
</div>
<ul class="values">
<li>{CHECK}<span><strong>Quoted first.</strong> A written price and scope before any work.</span></li>
<li>{CHECK}<span><strong>Yours to keep.</strong> Once paid, your site's content and design are yours.</span></li>
<li>{CHECK}<span><strong>No tricks.</strong> No promises of rankings or call counts. Work that does what we agreed.</span></li>
<li>{CHECK}<span><strong>Close by.</strong> A local number you can call or text.</span></li>
</ul>
</div>
</section>
{CTA_BAND}'''
page('about.html', 'About | Litrix Technologies', 'Litrix Technologies is a small technology business in Snellville, Georgia, serving Snellville, Lithonia, Stone Mountain and nearby.', '/about', about)

# ---------- Pricing ----------
def plan(name, blurb, price, was, unit, items, featured=False, cta='Choose', href='/contact'):
    feat = ' featured' if featured else ''
    badge = '<span class="badge">Most popular</span>' if featured else ''
    was_html = f'<s aria-label="was {was}">{was}</s>' if was else ''
    unit_html = f'<span>{unit}</span>' if unit else ''
    lis = ''.join(f'<li>{CHECK}<span>{x}</span></li>' for x in items)
    btn = 'btn-primary' if featured else 'btn-light'
    return f'''<article class="card plan{feat}">{badge}
<h3>{name}</h3><p class="muted">{blurb}</p>
<p class="price"><strong>{price}</strong>{was_html}{unit_html}</p>
<a class="btn {btn}" href="{href}">{cta}</a>
<ul class="checks">{lis}</ul>
</article>'''
pricing = f'''<section class="page-hero">
{WAVES}
<div class="wrap">
{eyebrow("Pricing")}
<h1>Simple, flexible <em>pricing.</em></h1>
<p class="lede">Founding prices for our first three clients. Half to start, half at launch. All prices in US dollars.</p>
</div>
</section>
<section class="section" aria-labelledby="builds">
<div class="wrap">
<h2 id="builds" class="display-sm">Website builds</h2>
<div class="grid grid-3 plans">
{plan("Starter","Great for getting started.","$450","$750","",["One page: services, service area, reviews","Tap-to-call and a contact form","Google Business Profile link-up","One round of revisions"],cta="Choose Starter")}
{plan("Business","A complete site for a growing business.","$900","$1,400","",["Up to 5 pages: home, services, about, gallery, contact","Quote-request form","Google Business Profile tune-up","Two rounds of revisions"],featured=True,cta="Choose Business")}
{plan("Custom","Tailored to your needs.","Quote","","",["Custom scope and features","Automation and integrations","Written quote before work starts"],cta="Request a Quote")}
</div>
<h2 class="display-sm care-title">Ongoing care</h2>
<div class="grid grid-2 plans">
{plan("Care plan: Basic","Keep your site healthy.","$49","","a month",["Hosting and domain renewal managed","Monthly updates and backups","Uptime checks and a form test","Up to 30 minutes of edits a month"],cta="Ask about Basic")}
{plan("Care plan: Plus","More help, every month.","$99","","a month",["Everything in Basic","Up to 90 minutes of edits a month","A one-page monthly report","Quarterly Google profile updates"],cta="Ask about Plus")}
</div>
<p class="note">Care plans are month to month and start the month after launch. Cancel any time. Extra work beyond the plan is $60 an hour, always quoted before we start. We don't promise rankings or a number of calls. We promise a site that works, on time, that you own. See our <a href="/refunds">refund and cancellation policy</a>.</p>
</div>
</section>
{CTA_BAND}'''
page('pricing.html', 'Pricing | Litrix Technologies', 'Website builds from $450 and care plans from $49 a month. Founding prices for our first three clients.', '/pricing', pricing)

# ---------- Contact ----------
contact = f'''<section class="page-hero">
{WAVES}
<div class="wrap">
{eyebrow("Contact")}
<h1>Start a <em>project.</em></h1>
<p class="lede">Tell us about your business. We'll reply within one business day with two or three specific ideas.</p>
</div>
</section>
<section class="section">
<div class="wrap grid contact-grid">
<form class="card inquiry" action="https://studio.litrixstudio.com/inquiry" method="post" aria-labelledby="form-title" data-inquiry>
<h2 id="form-title">Send a message</h2>
<div class="field-row">
<label>Your name<input name="name" autocomplete="name" required maxlength="120"></label>
<label>Email<input name="email" type="email" autocomplete="email" required maxlength="254"></label>
</div>
<div class="field-row">
<label><span>Phone <span class="optional">(optional)</span></span><input name="phone" type="tel" autocomplete="tel" maxlength="40" pattern="[0-9+().\\s\\-]*"></label>
<label><span>Business name <span class="optional">(optional)</span></span><input name="business" autocomplete="organization" maxlength="160"></label>
</div>
<label>How can we help?<textarea name="message" rows="6" required maxlength="4000"></textarea></label>
<div class="hp" aria-hidden="true"><label>Leave this empty<input name="company_website" tabindex="-1" autocomplete="off"></label></div>
<p class="form-note">We use your details only to reply to you. See our <a href="/privacy">privacy policy</a>.</p>
<p class="form-status" role="status" aria-live="polite" data-status></p>
<button class="btn btn-primary" type="submit">Send message {ARROW}</button>
</form>
<aside class="contact-side">
<div class="card">
{icon("phone")}
<h2>Call or text</h2>
<p><a class="phone-big" href="{TEL}">{PHONE}</a></p>
<p class="muted">Calls and texts welcome.</p>
</div>
<div class="card">
{icon("pin")}
<h2>Where we are</h2>
<p class="muted">Based in Snellville, Georgia. Serving Snellville, Lithonia, Stone Mountain and nearby.</p>
</div>
</aside>
</div>
</section>'''
page('contact.html', 'Contact | Litrix Technologies', 'Start a project with Litrix Technologies. Send a message or call (470) 632-6701.', '/contact', contact, script=True)

# ---------- Thanks / problem / 404 ----------
def simple(fname, title, desc, h1, html, noindex=True):
    page(fname, title, desc, '', f'''<section class="page-hero short">
{WAVES}
<div class="wrap">
<h1>{h1}</h1>
{html}
</div>
</section>''', noindex=noindex)
simple('thanks.html','Message sent | Litrix Technologies','Your message to Litrix Technologies was sent.','Thanks, your message is <em>on its way.</em>',
 f'<p class="lede">We reply within one business day. If it\'s urgent, call or text <a href="{TEL}">{PHONE}</a>.</p><div class="actions"><a class="btn btn-primary" href="/">Back to the home page</a></div>')
simple('inquiry-problem.html','Message not sent | Litrix Technologies','Your message to Litrix Technologies could not be sent.','Your message <em>wasn\'t sent.</em>',
 f'<p class="lede">Something about the form didn\'t go through. This can happen if a field was left empty or was too long, or if several messages were sent in a short time.</p><div class="actions"><a class="btn btn-primary" href="/contact">Try again</a><a class="btn btn-ghost" href="{TEL}">Call {PHONE}</a></div>')
simple('404.html','Page not found | Litrix Technologies',"This page doesn't exist.",'Page <em>not found.</em>',
 f'<p class="lede">That page doesn\'t exist.</p><div class="actions"><a class="btn btn-primary" href="/">Go to the home page</a><a class="btn btn-ghost" href="{TEL}">Call {PHONE}</a></div>')

# ---------- Legal pages: keep their text, new frame ----------
for f, title, desc in [('privacy','Privacy policy','Privacy policy for Litrix Technologies.'),('terms','Terms of service','Terms of service for Litrix Technologies.'),('refunds','Refunds and cancellations','Refund and cancellation policy for Litrix Technologies.')]:
    src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'legal', f + '.html')).read()
    inner = re.search(r'<main class="policy">\s*<div class="wrap">(.*?)</div>\s*</main>', src, re.S).group(1)
    inner = inner.replace('href="index.html#contact"', 'href="/contact"').replace('href="privacy.html"', 'href="/privacy"').replace('href="terms.html"', 'href="/terms"').replace('href="refunds.html"', 'href="/refunds"').replace('href="index.html"', 'href="/"')
    page(f + '.html', f'{title} | Litrix Technologies', desc, '', f'<section class="section policy"><div class="wrap">{inner}</div></section>')
print('built')
