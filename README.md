# Litrix Technologies website (litrixstudio.com)

Static site, no build step needed to serve it. Design: the owner's approved A + C hybrid concept
(dark minimal tech, editorial accents). Tokens: #0B0D10 background, #1D2026 surface, #FF603B accent,
#F5F5F2 text, #9299A3 muted; Manrope for headings, Inter for text.

Pages: home, services, work, about, pricing, contact, thanks, inquiry-problem, 404, privacy,
terms, refunds. Cloudflare serves `/services` from `services.html` (and redirects `.html` URLs).

## Editing

The pages share a header, footer and frame, so they are generated:

```bash
python tools/build.py
```

Page text is in `tools/build.py` and `tools/content.py`; legal page text is in `tools/legal/*.html`.
`styles.css`, `form.js`, `_headers` and `favicon.svg` are edited directly. Never add made-up
projects, testimonials, results or prices: the Work page shows real client work only, with
permission.

## Message form

The contact page's form posts to `https://studio.litrixstudio.com/inquiry` (Litrix Web Studio).
With JavaScript, `form.js` sends it in the background (`Accept: application/json`) and shows the
result on the page; without it, the browser posts normally and lands on `/thanks` or
`/inquiry-problem`. Messages land on the studio's Inquiries page and the owner gets an email.
The studio accepts the form only from `https://litrixstudio.com` and `https://www.litrixstudio.com`.
The hidden `company_website` field is a spam trap and must stay empty and hidden. See the studio's
docs/INQUIRIES.md.

## Hosting on Cloudflare

`wrangler.jsonc` serves the site from Cloudflare's free static hosting at `litrixstudio.com` and
`www.litrixstudio.com`. `_headers` sets the security headers; its CSP allows scripts from this site
only and lets the form talk only to the studio. `.assetsignore` keeps the README, tools and config
out of the upload.

Deploy (PowerShell, on the PC, after the pull request is merged):

```powershell
cd C:\Users\chays\Projects\litrix-site
git switch main
git pull
corepack pnpm dlx wrangler@4 deploy
```
