# Page bodies for the Litrix site. Real business facts only come from the existing site.
PHONE = '(470) 632-6701'
TEL = 'tel:+14706326701'

ARROW = '<svg class="i" width="16" height="16" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17 17 7M8 7h9v9"/></svg>'
RIGHT = '<svg class="i" width="18" height="18" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
CHECK = '<svg class="i" width="16" height="16" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"/></svg>'

ICONS = {
 'monitor': '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>',
 'spark': '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/>',
 'layers': '<path d="m12 3 9 5-9 5-9-5 9-5Z"/><path d="m3 13 9 5 9-5"/>',
 'shield': '<path d="M12 3 4 6v6c0 4.5 3.4 8.2 8 9 4.6-.8 8-4.5 8-9V6l-8-3Z"/>',
 'wrench': '<path d="M14.7 6.3a4 4 0 0 0-5.4 5.2L3 17.8V21h3.2l6.3-6.3a4 4 0 0 0 5.2-5.4l-2.6 2.6-2.4-.6-.6-2.4 2.8-2.6Z"/>',
 'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 'pin': '<path d="M12 21s7-6.2 7-12a7 7 0 0 0-14 0c0 5.8 7 12 7 12Z"/><circle cx="12" cy="9" r="2.5"/>',
 'phone': '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2z"/>',
 'chat': '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 21l1.9-5.4A8 8 0 1 1 21 12Z"/>',
 'compass': '<circle cx="12" cy="12" r="9"/><path d="m15.5 8.5-2 5-5 2 2-5 5-2Z"/>',
 'doc': '<path d="M14 3H6v18h12V7l-4-4Z"/><path d="M14 3v4h4M9 13h6M9 17h6"/>',
 'pen': '<path d="m4 20 4-1 11-11-3-3L5 16l-1 4Z"/>',
 'folder': '<path d="M3 6h6l2 2h10v11H3V6Z"/>',
 'flag': '<path d="M5 21V4h11l-2 4 2 4H5"/>',
}
def icon(name, size=26):
    return f'<svg class="ic" width="{size}" height="{size}" viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</svg>'

def eyebrow(t): return f'<p class="eyebrow"><span class="rule" aria-hidden="true"></span>{t}</p>'

CTA_BAND = f'''<section class="cta-band" aria-labelledby="cta-title">
<div class="wrap cta-inner">
<div><h2 id="cta-title">Ready to build something great?</h2><p>Tell us about your business. We reply within one business day.</p></div>
<a class="btn btn-primary" href="/contact">Start a Project {ARROW}</a>
</div>
</section>'''

SERVICES = [
 ('monitor','Web Design &amp; Development','Fast, modern websites that work on every phone, with tap-to-call, a contact form and your service area. Live within a week of getting your content, and yours to keep.','web'),
 ('wrench','Website Maintenance &amp; Hosting','Monthly care: hosting and domain renewal managed, updates and backups, uptime checks, form tests and quick edits when your hours or services change.','care'),
 ('spark','AI Assistants &amp; Automation','Save time on repetitive work with smart tools, like instant replies to new inquiries or simple workflows that connect the apps you already use. Scoped and quoted for your business.','automation'),
 ('layers','Branding, Graphics &amp; UI/UX','A consistent look across your website, social profiles and printed pieces, plus a review link and QR code so happy customers can leave a review in seconds.','brand'),
 ('shield','IT Support &amp; Security','Help setting up and fixing Wi-Fi, devices, TVs and streaming at home. Ask us about your business setup and we will tell you plainly what we can take on.','it'),
 ('chart','Google Business Profile &amp; More','We set up or clean up your Google Business Profile, link it to your site and keep it current. Something else in mind? Ask, and we will quote it before any work starts.','more'),
]
