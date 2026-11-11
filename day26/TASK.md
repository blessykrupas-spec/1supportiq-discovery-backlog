# Day 26 — Guard the SupportIQ dispatcher: authz, PII redaction & injection (security)

**Scenario:** The **SupportIQ** assistant sits behind a guarded dispatcher that must enforce access control, scrub PII from logs, and flag prompt-injection attempts.

## Your task
- `authorize(role, action, resource)` - return `True` if `role` may perform `action` on `resource`. `'admin'` may do anything. Otherwise use this policy: **agent** -> `tickets` `{read, write}`, `orders` `{read}`, `kb` `{read}`; **supervisor** -> `tickets` `{read, write}`, `orders` `{read}`, `escalations` `{read, write}`, `kb` `{read}`. Any unknown role, resource, or action returns `False`.
- `redact_pii(text)` - replace a 16-digit **card** (four groups of four, optionally separated by spaces or hyphens) with `[CARD]`, a 10-digit **phone** (`ddd-ddd-dddd`, with `-`, `.`, or nothing as separators) with `[PHONE]`, and an **email** with `[EMAIL]`. Redact cards before phones so a card is never mistaken for a phone.
- `has_injection(text)` - return `True` if `text` contains any known injection marker (case-insensitive): `ignore previous instructions`, `ignore all previous`, `disregard the above`, `you are now`, `reveal your system prompt`.

## Example
```python
authorize("agent", "write", "escalations")              # -> False
redact_pii("call 555-123-4567")                         # -> 'call [PHONE]'
has_injection("Please IGNORE previous instructions")    # -> True
```

---
Edit `day26/solution.py`, commit & push, then click **Run Test** in the platform.
