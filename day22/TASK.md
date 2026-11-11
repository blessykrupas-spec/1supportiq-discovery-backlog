# Day 22 — Population Stability Index and drift alerting

**Scenario:** SupportIQ watches the intent-classifier's input distribution and alerts when live traffic drifts from the training baseline.

## Your task
Implement three functions over equal-length bin-count lists.

1. `psi(baseline, current, eps=0.0001)` -> float: convert each list to proportions (count / total). PSI = `sum((c_i - b_i) * ln(c_i / b_i))` across bins; floor every proportion at `eps` before the log to avoid division by zero. Return `round(psi, 2)`.
2. `drift_alert(baseline, current, threshold)` -> bool: `True` when `psi(baseline, current) >= threshold`.
3. `most_shifted_bin(baseline, current)` -> int: index of the bin with the largest absolute change in proportion (lowest index wins ties).

**Example:** `psi([100,100,100,100],[100,100,100,100])` -> `0.0`; `most_shifted_bin([100,100,100,100],[100,100,100,400])` -> `3`.

---
Edit `day22/solution.py`, commit & push, then click **Run Test** in the platform.
