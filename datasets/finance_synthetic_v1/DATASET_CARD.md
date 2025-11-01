

# Dataset Card — Finance Synthetic v1

**Motivation**: Synthetic, non-identifiable time series for OPEX-style forecasting and calibration tests.  
**Composition**: multivariate monthly series (36–120 steps), signals include turnover, OPEX components, external indices.  
**Generation**: programmatic synthesis with controlled noise and regime shifts; parameters withheld.  
**Intended use**: benchmarking MAE/SMAPE and ECE/CRPS with cluster vs. per-domain baselines.  
**Licensing**: CC-BY-4.0 for the *schema*; no real-world data included.  
**Notes**: Use `oss-eval` loaders for repeatable splits; seeds set in examples.
