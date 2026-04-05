# MiningAtlas

MiningAtlas is a public interactive Leaflet map for exploring global mining production, exports, and estimated market values by country and by mineral.

## Public site

- Temporary test URL: `https://mouth-counter-order-conclude.trycloudflare.com`
- Official GitHub Pages target: `https://hateynco.github.io/MiningAtlas/`

## Main files

- `index.html`: main HTML shell and styles
- `app.js`: client-side logic, map rendering, filters, rankings, and popups
- `mining_history.json.gz.b64.txt`: compressed historical dataset loaded directly by the frontend
- `build_historical_db.py`: rebuilds the historical dataset from BGS, USGS, and the local seed file
- `db.json`: local seed dataset kept for rebuilds and fallback
- `.github/workflows/deploy-pages.yml`: GitHub Pages deployment workflow

## Current features

- year selector from `1960` to `2025` when data exists
- collapsible left and right panels
- full map mode with edge search rails
- country popups on click
- production and export history by country and by mineral
- estimated production/export/domestic market values using USGS and World Bank price benchmarks
- global mode listing all tracked minerals for each country

## Update later

1. Update `index.html`, `app.js`, or `build_historical_db.py`.
2. Rebuild the dataset with `python build_historical_db.py` if the source data changes.
3. Commit and push to `main`.
4. GitHub Pages redeploys automatically.

## Notes

- Market values are interface-level estimates, not customs-certified trade values.
- Historical coverage before 1970 remains partial for some materials.
