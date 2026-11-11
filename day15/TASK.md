# Day 15 — MCP guarded dispatcher: allow-list, arg validation, approval gate

**Scenario:** SupportIQ's MCP agent can call three tools; a guarded dispatcher must block unknown tools, reject malformed arguments, and require human approval before any write.

## Your task
Implement `dispatch(tool, args, approved=False)` returning a decision string. `args` is a dict. Apply these checks **in order**:

1. If `tool` is not one of `lookup_order`, `search_kb`, `create_escalation` -> return `"DENY: unknown tool"`.
2. Each tool's required args must be present and be **non-empty strings** (after stripping whitespace), else `"DENY: invalid arguments"`. Required args: `lookup_order` -> `order_id`; `search_kb` -> `query`; `create_escalation` -> `ticket_id` and `reason`.
3. `create_escalation` is a **write** tool and requires `approved=True`, else `"DENY: approval required"`.
4. Otherwise return `"ALLOW: " + tool`.

**Example:**
```
dispatch("lookup_order", {"order_id": "A1"})                                  -> 'ALLOW: lookup_order'
dispatch("create_escalation", {"ticket_id":"T1","reason":"angry"})            -> 'DENY: approval required'
dispatch("create_escalation", {"ticket_id":"T1","reason":"angry"}, True)      -> 'ALLOW: create_escalation'
```


---
Edit `day15/solution.py`, commit & push, then click **Run Test** in the platform.
