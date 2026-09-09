# Smart Indoor Space Webpage

Files:
- `index.html` — the responsive project webpage
- `assets/architecture.svg` — project architecture visual
- `qr_code.png` — QR code
- `site_url.txt` — URL encoded by the QR
- `generate_qr.py` — regenerates the QR after you publish the site

## Publish with GitHub Pages
1. Create a GitHub repository, e.g. `smart-indoor-space`.
2. Upload all files while keeping the same folder structure.
3. In GitHub: Settings → Pages → deploy from the `main` branch.
4. GitHub will give you a public URL.
5. Replace the URL in `site_url.txt` with that public URL.
6. Run `python generate_qr.py`.
7. Upload the new `qr_code.png` to the repository.

The brochure/content is kept generic about the cloud provider, so you can use your final choice later.
