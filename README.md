# creativate-research

Public research repo for Creativate AI Studio.

## What’s inside
- 📦 `oss-eval/` — Open-source evaluation toolkit (`evalkit`) with tests.
- 📝 `papers/` — Typst paper stub (CI builds PDFs on tag).
- 📊 `datasets/` — Synthetic dataset tracked with **DVC**.
- 📚 `docs/` — `mkdocs` site (deploy via GitHub Pages).
- ⚙️ CI: tests + docs build + Typst PDF build on release tags.

## Quickstart
```bash
# Eval toolkit
cd oss-eval
pip install -e .
evalkit --help
pytest -q

# Docs local preview
cd ..
pip install mkdocs
mkdocs serve  # http://127.0.0.1:8000

# DVC basics
pip install dvc
dvc init
# (configure a remote later, e.g. 'dvc remote add -d origin s3://…')
```

## Releasing
1. Bump version.
2. Create a tag like `v0.1.0` and push.
3. CI builds PDF and attaches as release asset; Zenodo (if connected) mints a DOI.
