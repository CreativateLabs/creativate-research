[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17501847.svg)](https://doi.org/10.5281/zenodo.17501847)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![Paper PDF](https://img.shields.io/badge/Paper-Typst%20PDF-blue)](https://github.com/CreativateLabs/creativate-research/releases)

> **Neural Enterprise Network (NEN)** — a cluster-based architecture for organizational decision intelligence  
> with explainability and uncertainty built in.  
>
> This repository provides the open-research components of the NEN framework:
> - Scientific outline and architecture figure
> - Evaluation toolkit (MAE, SMAPE, ECE, CRPS)
> - Reproducible Typst paper build pipeline
>
> ⚠️ *Production implementations remain proprietary; this release only covers open scientific artifacts.*

---
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

![CI](https://github.com/CreativateLabs/creativate-research/actions/workflows/ci.yml/badge.svg)](https://github.com/CreativateLabs/creativate-research/actions)

### 📖 How to cite

If you use this work, please cite:

> Bornhäußer, L. (2025). *Neural Enterprise Network (NEN): Open Evaluation & Paper Assets* (v0.1). Zenodo.  
> https://doi.org/10.5281/zenodo.17501847

---

