# Litrix Technologies website

Static site served by GitHub Pages: index, terms, refunds and privacy pages. No build step.

## Message form

The contact section's form posts to `https://studio.litrixstudio.com/inquiry` (the Litrix Web
Studio app). Messages land in the studio's Inquiries page and the owner gets an email. The studio
accepts the form only from `https://litrixstudio.com` and `https://www.litrixstudio.com`, so the
form works once this site is served from that domain. After sending, visitors land on
`thanks.html`, or `inquiry-problem.html` if something was wrong. The hidden `company_website`
field is a spam trap and must stay empty and hidden.

## Hosting on Cloudflare (litrixstudio.com)

`wrangler.jsonc` serves the site from Cloudflare's free static hosting at `litrixstudio.com` and
`www.litrixstudio.com` (Cloudflare creates the DNS records and HTTPS certificate). `_headers` sets
the security headers, including a CSP that only lets the form post to the studio. `.assetsignore`
keeps the README and config out of the upload.

Deploy (PowerShell, on the PC, after the pull request is merged):

```powershell
cd C:\Users\chays\Projects\litrix-site
git switch main
git pull
corepack pnpm dlx wrangler@4 deploy
```
