# Day 21 — Supply-chain gate: pinning, SBOM scan, severity policy

**Scenario:** SupportIQ's release pipeline refuses to ship unless dependencies are hash-pinned and the SBOM is clear of blocked-severity vulnerabilities.

## Your task
Implement three functions.

1. `find_unpinned(deps)` -> list: each dep is `{'name','version','hashes'}`. A dep is *unpinned* if its `version` is empty/absent **or** its `hashes` list is empty/absent. Return the **sorted** list of offending names.
2. `scan_vulnerable(sbom, advisories)` -> list: `sbom` is a list of `{'name','version'}`; `advisories` maps a name to a list of vulnerable version strings. Return the **sorted** list of `"<name>==<version>"` for components whose exact version is listed as vulnerable.
3. `severity_gate(findings, min_severity)` -> bool: severities rank `low < medium < high < critical`. Return `True` (block the release) if any finding's severity is **>=** `min_severity`, else `False`.

**Example:** `scan_vulnerable([{'name':'requests','version':'2.19.0'}], {'requests':['2.19.0']})` -> `['requests==2.19.0']`; `severity_gate([{'id':'V2','severity':'high'}], 'high')` -> `True`.

---
Edit `day21/solution.py`, commit & push, then click **Run Test** in the platform.
