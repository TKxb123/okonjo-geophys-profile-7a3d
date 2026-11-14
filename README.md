# Nerissa Okonjo-Bailey — Academic Profile

Personal academic profile site for Dr. Nerissa Okonjo-Bailey, built from the Wrayburn group starter kit.

## Layout
- `_config.yml` holds the site identity, the Pages origin (`url`) and the repository path prefix (`baseurl`).
- `index.md` is the front page.
- `_pages/` holds secondary pages (about, publications, cv).
- `scripts/verify_site_paths.py` runs inside the deploy workflow and rejects builds whose `url` / `baseurl` do not agree with the `repository` setting.

## Publication feed
The publications page renders the machine-readable feed that is published to the group's site-assets Cloud Storage bucket.
