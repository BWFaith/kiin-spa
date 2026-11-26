# K'iin Spa & Lounge website

Pure HTML, CSS and JavaScript. No build step and no framework. Upload the whole folder to any host (Netlify, Vercel, cPanel, GitHub Pages, etc.) and open `index.html`.

## Pages (11)
index, about, services, massage-therapy, facials-skincare, hair-salon, nails, lashes-brows, gallery, booking, contact.
The **Services** menu has a dropdown that links to each service page (accordion on mobile).

## Files
- `css/style.css` - all styling (colours are CSS variables at the top).
- `js/main.js` - animations, hero doors, quote forms, gallery, chatbot.
- `js/config.js` - **the file you will edit most**: phone, owner email, EmailJS keys, prices, add-ons, time slots, TikTok videos.
- `assets/img/` - all images. Files named like `svc-massage.jpg` are placeholders (they say "Placeholder" on them). Replace each with your own photo using the **same file name** (or change the name in the HTML).
- `build.py` / `data.py` - optional. If you edit text or prices in `data.py` and run `python3 build.py`, every page and `config.js` regenerate. Not needed to host the site.

## 1. Make quote emails work (client + owner copy)
The booking and hero forms use EmailJS (free tier is fine). Each submission sends two emails: one to the owner and one to the client.
1. Create an account at emailjs.com and connect an email service (Gmail, Outlook, etc.).
2. Create one email template. In the template settings set **To email** to `{{to_email}}` and **Subject** to `{{subject}}`.
3. Template body example:
   ```
   Hello {{to_name}},
   Quote {{quote_id}} for {{client_name}} ({{client_email}}, {{client_phone}})
   Preferred: {{preferred_date}} at {{preferred_time}}, guests: {{guests}}
   {{{quote_html}}}
   Total: {{total}} ({{duration}})
   Notes: {{notes}}
   ```
4. Copy your Public Key, Service ID and Template ID into `js/config.js` (`emailjs` section) and set `business.ownerEmail`.
Until you do this the site runs in **demo mode** (forms work, but no email is sent, and the confirmation says so).

## 2. Video gallery with TikTok
1. Open one of your TikTok videos in a browser. The URL looks like `tiktok.com/@name/video/7312345678901234567`.
2. Copy the long number and paste it as `id` for a video in `js/config.js` (`videos`). Set `business.tiktok` to your profile link.
3. Swap `assets/img/video-1.jpg` etc. for a thumbnail from that video.
To use your own MP4 instead, put it in `assets/video/` and use `{type:"mp4", src:"assets/video/tour.mp4"}`.

## 3. Things to personalise
- **Prices, durations, add-ons** are sample values in `js/config.js`. Set `taxRate` (for example `0.07`) if you want tax shown in quotes.
- **Hours** are not published on the site (shown as "by appointment"). Add them in the footer, contact page and chatbot text.
- **Reviews** on the home page are placeholders. Replace with real ones from Facebook.
- **About page story and team** are placeholders. Replace with Eva's own words and photos.
- **Time slots** are in `config.js` (`slots`).

## Hero doors animation
The hero opens a pair of gilded doors on load, and on desktop closes and reopens them occasionally. A button lets visitors open or close them. The content always sits above the doors, so nothing is ever blocked. It respects "reduce motion" settings.
