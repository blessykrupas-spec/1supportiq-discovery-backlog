# Day 29 — SupportIQ release ops: burndown & semver from PR labels (product team)

**Scenario:** Your team runs the **SupportIQ** capstone like a product: you track the sprint burndown and cut releases from the labels on merged pull requests.

## Your task
- `burndown_remaining(total_points, completed_per_day)` - return the list of story points remaining after each day, subtracting that day's completed points. Remaining never drops below `0`.
- `next_version(current, labels)` - `current` is a semver `'major.minor.patch'`. From the merged-PR `labels`, apply the **highest-impact** bump: `'breaking'` bumps major and resets minor and patch to 0; else `'feature'` bumps minor and resets patch; else `'fix'` bumps patch; else the version is unchanged. Return the new version string.
- `changelog_buckets(prs)` - `prs` is a list of `{'title', 'label'}` dicts. Bucket each title (in input order) by label: `feature` -> `Added`, `fix` -> `Fixed`, `breaking` -> `Changed`, anything else -> `Other`. Return a dict with exactly the four keys in the order `Added`, `Changed`, `Fixed`, `Other`.

## Example
```python
burndown_remaining(20, [5, 3, 7])              # -> [15, 12, 5]
next_version("1.4.2", ["feature", "fix"])      # -> '1.5.0'
```

---
Edit `day29/solution.py`, commit & push, then click **Run Test** in the platform.
