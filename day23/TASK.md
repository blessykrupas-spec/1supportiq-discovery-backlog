# Day 23 — Canary router and scorecard-driven promotion

**Scenario:** SupportIQ ships a new intent model to a hash-stable slice of users and promotes or rolls back based on a live scorecard.

## Your task
Implement four functions. Bucketing must be **stable**: `bucket = int(sha256(str(user_id)).hexdigest(), 16) % 100`.

1. `in_canary(user_id, percent)` -> bool: `True` when the user's bucket `< percent`.
2. `assign_variant(user_id, percent)` -> str: `"canary"` or `"stable"`.
3. `canary_share(user_ids, percent)` -> float: fraction of the list routed to canary, `round(., 2)`; empty list -> `0.0`.
4. `decide_release(canary_score, stable_score, margin)` -> str: let `diff = round(canary_score - stable_score, 4)`. Return `"promote"` if `diff >= margin`, `"rollback"` if `diff <= -margin`, else `"hold"`.

**Example:** `decide_release(0.94, 0.90, 0.02)` -> `'promote'`; `assign_variant('user-001', 0)` -> `'stable'`.

---
Edit `day23/solution.py`, commit & push, then click **Run Test** in the platform.
