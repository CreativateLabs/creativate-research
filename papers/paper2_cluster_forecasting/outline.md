
# Outline — Paper 2: "Cluster-Governed Forecasting for Financial Planning under Uncertainty"
**Repository:** creativate-research  
**Version:** v0.2.0  
**Timestamp (UTC):** '"$(date -u +"%Y-%m-%d %H:%M:%SZ")"'  
**Authors:** Leonardo Bornhäußer, Tuna (R&D Lead), Creativate Research Group  
**DOI:** _to be filled after Zenodo release_

## 1 | Motivation & Objective
While Paper 1 defined the Neural Enterprise Network (NEN) architecture, this work validates it in **enterprise financial forecasting**.  
We demonstrate how a **cluster-governed model** improves accuracy, stability, and decision trust vs. siloed per-department models.

**Key Problem:** Traditional financial ML systems ignore organizational interdependencies (e.g., headcount → OPEX → cashflow).  
Our approach clusters these domains, sharing latent representations while maintaining domain accountability.

## 2 | Methodology – Clustered Forecasting Approach
| Layer | Description |
|---|---|
| **Architecture** | Subgraph of NEN restricted to Finance (+ linked Ops & HR signals). |
| **Data** | Synthetic & anonymized enterprise dataset (v2) ≈ 10k rows, monthly cadence. |
| **Model Variants** | ① Per-domain baseline ② Cluster-shared NEN ③ Ensemble baseline. |
| **Targets** | OPEX, CAPEX, Headcount, Revenue growth. |
| **Toolkit** | `oss-eval` (MAE, SMAPE, ECE, CRPS, Pinball). |

Equation (placeholder):  \(\hat{y}_t^{(d)} = f_{\theta_d}(x_t^{(d)}, z_t^{(c)}) + \epsilon_t\).

## 3 | Experimental Design
- Baseline: XGBoost / LSTM per domain  
- NEN Cluster: Finance+HR+Ops joint training  
- Split: 80/20 temporal; horizon=3 months  
- Metrics: MAE, SMAPE, Pinball, ECE, CRPS  
- XAI: SHAP stability + 95% band coverage curves

## 4 | Results (Planned)
| Model | MAE ↓ | SMAPE ↓ | ECE ↓ | CRPS ↓ | Interpretability |
|---|:--:|:--:|:--:|:--:|:--:|
| Per-domain |  |  |  |  | Limited |
| Clustered NEN |  |  |  |  | High |
| Cluster + Gov. |  |  |  |  | High |

Expected: ≥10% MAE/SMAPE drop, ~30% ECE drop.

## 5 | Discussion
- Accuracy ↔ explainability trade-offs  
- Budget risk from mis-calibration  
- Governance benefits (traceability, accountability)

## 6 | Figures & Artifacts
- Fig.1: Finance Cluster Network topology  
- Fig.2: Error distribution vs. uncertainty interval  
- Fig.3: Calibration curve (pred vs obs)  
- Dataset: `datasets/finance_synthetic_v2/` (CC-BY)  
- Notebook: `examples/finance_cluster_demo.ipynb`

## 7 | Relation to Paper 1
Quantitative evidence for NEN; extends `oss-eval` with probabilistic metrics & a Finance dataset.

## 8 | Publication Plan
| Venue | Type | Target | Status |
|---|---|---|---|
| AI in Finance @ NeurIPS | Workshop | 4 pages | Draft Nov → Submit Dec |
| IEEE Trans. Eng. Mgmt | Journal | ~10 pages | Submit Q1 2026 |
| Zenodo | Preprint | v0.2.0 | DOI Nov 2025 |

## 9 | Next Steps (Tuna – R&D Lead)
1. Pipeline under `internal/ablations/cluster_forecasting/`  
2. Synthetic dataset v2 + dataset card  
3. Add Pinball & CRPS to `oss-eval`  
4. Produce first plots (Fig.2, Fig.3)  
5. Write Methods/Results in Typst  
6. Tag v0.2.0 → Zenodo DOI
