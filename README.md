# MiningAtlas

MiningAtlas is a public static Leaflet map for exploring mining production by country.
The published site is designed for GitHub Pages and rebuilds its `db.json` payload from compressed text parts stored in the repository.

## Files

- `index.html`: static frontend map and ranking UI
- `.github/workflows/deploy-pages.yml`: GitHub Pages deployment workflow
- `pages-gzip/db.json.gz.b64.part001.txt` and `pages-gzip/db.json.gz.b64.part002.txt`: compressed data payload used to rebuild `db.json` during deployment

## Update later

1. Update your local `db.json` and `index.html`.
2. Regenerate the compressed payload parts if the data changes.
3. Push to `main`.
4. GitHub Pages redeploys automatically.

Expected public URL:
`https://hateynco.github.io/MiningAtlas/`
