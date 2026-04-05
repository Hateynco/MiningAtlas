# MiningAtlas

MiningAtlas is a public static Leaflet map for exploring mining production by country.
It is already shareable from the public repository through a CDN URL:

`https://cdn.jsdelivr.net/gh/Hateynco/MiningAtlas@main/index.html`

## Repository contents

- `index.html`: static frontend map and ranking UI
- `pages-gzip/db.json.gz.b64.part001.txt` and `pages-gzip/db.json.gz.b64.part002.txt`: compressed data payload loaded directly by the frontend
- `.github/workflows/deploy-pages.yml`: optional GitHub Pages deployment workflow kept in the repo

## Update later

1. Update your local `index.html` and source data.
2. Rebuild the compressed payload parts if the dataset changes.
3. Push to `main`.
4. The CDN URL serves the latest files after refresh and GitHub Pages can also be used later if desired.
