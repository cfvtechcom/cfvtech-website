# cfvtech.com — static website

Static rebuild (Oct 2026) of the CFV Technologies website, replacing the ASP.NET MVC 5 app
that needed GoDaddy Windows hosting (C$25.28/month). Same look, FR + EN, free hosting.

## Layout

| Path | What |
|---|---|
| `docs/` | **The website.** Plain HTML/CSS/JS, deployable as-is (GitHub Pages serves this folder). |
| `docs/index.html`, `docs/carrieres.html` | French pages (default language) |
| `docs/en/index.html`, `docs/en/careers.html` | English pages |
| `docs/Home/Recruitment/` | Redirect so the old careers URL keeps working |
| `docs/assets/css/static.css` | The only CSS added on top of the original theme (layout fixes) |
| `tools/build.py` | Generates the 4 pages. **Edit texts here, then run it.** |

## Editing content

All texts (FR and EN) are in the `T` dictionary at the top of `tools/build.py`; client logos are in
`CLIENTS` / `CLIENT_NAMES`, certifications in `CERTS`. After a change:

```
python3 tools/build.py
```

To add a client logo: put the PNG in `docs/assets/images/`, add it to `CLIENTS` and `CLIENT_NAMES`, rebuild.

Preview locally: `cd docs && python3 -m http.server 8080`, then open http://localhost:8080.

## Differences from the old site (intentional)

- No contact form and no email addresses on the pages (spam). "Contact" menu item and
  "Savoir plus / Learn more" buttons removed, as they only led to the form.
- URLs: `/` (FR), `/en/` (EN), `/carrieres.html`, `/en/careers.html` instead of `?language=` and a cookie.
- HTTPS provided by the host.
- Service cards and careers boxes size to their content (fixed heights removed).

## Notes on the old site

- The source zip (`CFVTechnologiesMVC.zip`, last changed Feb–Dec 2022) is **older than what was deployed**:
  it lacks the Agropur, Cirque du Soleil and iA logos, the current banner images and header logo,
  and the contact-form email code. The deployed files (backup `cfvtech-httpdocs-backup-2026-10-15.zip`)
  and the live pages were used as the source of truth; texts come from the live site.
- No database was used; the identity/login code is the unused Visual Studio template.
- The deployed contact form sent mail through GoDaddy's relay (`relay-hosting.secureserver.net`); no credentials were stored.
