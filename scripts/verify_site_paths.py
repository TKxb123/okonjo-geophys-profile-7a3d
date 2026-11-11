"""Verify that the site origin and base path agree with the repository setting."""

import sys

import yaml


def main():
    with open("_config.yml", "r", encoding="utf-8") as fh:
        cfg = yaml.safe_load(fh) or {}

    repo = str(cfg.get("repository") or "")
    owner, _, name = repo.partition("/")

    expected_url = "https://%s.github.io" % owner if owner else ""
    expected_base = "/%s" % name if name else ""

    url = str(cfg.get("url") or "").rstrip("/")
    base = str(cfg.get("baseurl") or "").rstrip("/")

    ok = True
    if expected_url and url != expected_url:
        print("url mismatch: got %r, expected %r" % (url, expected_url))
        ok = False
    if expected_base and base != expected_base:
        print("baseurl mismatch: got %r, expected %r" % (base, expected_base))
        ok = False

    if not ok:
        sys.exit(1)
    print("Site paths verified.")


if __name__ == "__main__":
    main()
