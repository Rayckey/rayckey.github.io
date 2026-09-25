# Rocky Wang — personal website

Personal homepage for Weiqi (Rocky) Wang, a UCLA Ph.D. graduate in robotics.
Configured for https://rayckey.github.io/.

## Deployment

In **Settings → Pages**, set the source to **GitHub Actions**. The deployment
workflow builds the research pages and publishes the website files.

Pushes to `main` publish automatically. To publish manually, open
**Actions → Deploy personal website → Run workflow** and select `main`.

The homepage and assets also live at the repository root, alongside `.nojekyll`,
so GitHub's default branch publishing serves the same website if it runs.

The full SUN video should be committed through Git; it exceeds the browser's
per-file upload limit. No Git LFS or website framework is required.

## Preview and edit

Run `python3 scripts/serve.py` and open http://localhost:8765/.

- `index.html`: introduction, projects, experience, and publications.
- `styles.css`: blue theme and responsive layout.
- `site.js`: video controls, email copying, and navigation.
- `scripts/build_pages.py`: research case-study source and asset-version links.
- `scripts/build_resume.py`: optional PDF regeneration; requires ReportLab and Liberation Sans.
- `assets/`: portrait, original research media, fonts, and prepared resume.

After changing styles, the favicon, or research page source, run
`python3 scripts/build_pages.py`. The deployment workflow runs this automatically.
The portrait uses its original 3:4 proportions and scales without cropping.
