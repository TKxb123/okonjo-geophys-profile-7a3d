# Academic profile starter

A small Jekyll site that the Wrayburn group uses for personal profile pages.

## Layout
- `_config.yml` holds the site identity, the Pages origin (`url`) and the repository
  path prefix (`baseurl`).
- `index.md` is the front page.
- `_pages/` holds secondary pages (about, publications, cv).
- `scripts/verify_site_paths.py` runs inside the deploy workflow and rejects builds
  whose `url` / `baseurl` do not agree with the `repository` setting.

## Publication feed
The publications page renders the machine-readable feed that is published to the
group's site-assets Cloud Storage bucket. Asset lookups use exact object paths, so
the feed must be written to the live root key agreed in the publishing request.
