# Day 04 — Audit the SupportIQ requirements lock

**Scenario:** Before shipping SupportIQ you must prove every dependency is pinned, so the build is reproducible across machines.

## Your task
Implement three module-level functions over `lines` (a list of raw requirements-file lines).

1. `parse_requirement(line)` — strip the line. Return `None` for a blank line or a comment (starts with `#`). Otherwise return a tuple `(name, operator, version)` where `operator` is one of `==`, `>=`, `<=`. If the line has a name but no recognised operator, return `(name, '', '')`.

2. `find_unpinned(lines)` — return a sorted list of package names that are **not** pinned with `==` (including bare names with no operator). Blanks and comments are ignored.

3. `resolve_versions(lines)` — return a sorted list of `(name, version)` tuples for every `==`-pinned package.

## Example
```python
lines = ['flask==2.0.1', 'requests>=2.0', '# tooling', '', 'rich']
find_unpinned(lines)     # -> ['requests', 'rich']
resolve_versions(lines)  # -> [('flask', '2.0.1')]
```


---
Edit `day04/solution.py`, commit & push, then click **Run Test** in the platform.
