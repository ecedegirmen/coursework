# HTML Build Automation | Coursework

[Research portfolio](https://github.com/ecedegirmen/research-portfolio) · [Repository directory](https://github.com/ecedegirmen/research-portfolio/blob/main/docs/repository-directory.md)

**Context:** Course activity in build automation and GitHub Actions  
**Tools:** Python, HTML, GitHub Actions

This repository contains a small build script that inserts an Eastern Time timestamp into an HTML template.

## Files

| File | Purpose |
| --- | --- |
| [build.py](build.py) | Replaces the timestamp placeholder and writes the generated page |
| [index.html](index.html) | Source HTML template |
| [.github/workflows](.github/workflows/) | Automation and spell-check workflow definitions |

## Build locally

From the repository root, with Python 3.9 or newer and an available time-zone database:

```bash
python3 build.py
```

The generated page is written to `out/index.html`. This is a course exercise in automated builds; the original activity files are retained.
