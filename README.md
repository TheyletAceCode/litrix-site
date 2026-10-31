# Litrix Technologies website

Static site served by GitHub Pages: index, terms, refunds and privacy pages. No build step.

## Message form

The contact section's form posts to `https://studio.litrixstudio.com/inquiry` (the Litrix Web
Studio app). Messages land in the studio's Inquiries page and the owner gets an email. The studio
accepts the form only from `https://litrixstudio.com` and `https://www.litrixstudio.com`, so the
form works once this site is served from that domain. After sending, visitors land on
`thanks.html`, or `inquiry-problem.html` if something was wrong. The hidden `company_website`
field is a spam trap and must stay empty and hidden.
