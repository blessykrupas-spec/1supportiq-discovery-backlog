# Day 20 — Pure /ask request handler for the SupportIQ service

**Scenario:** SupportIQ serves its assistant behind a FastAPI `/ask` endpoint running in Docker; the pure business logic must be testable without the web framework.

## Your task
Implement two functions.

1. `classify_priority(text)` -> str: return `"P1"` if the (case-insensitive) text contains any of `urgent, outage, down, payment failed, cannot login`; else `"P2"` if it contains any of `error, failed, broken`; else `"P3"`.
2. `handle_ask(request)` -> dict: validate and route.
   - Not a dict -> `{'code':400,'error':'bad_request'}`.
   - `text` missing/blank -> `{'code':400,'error':'empty_text'}`.
   - `intent` not in `{order_status, refund, kb_search, escalate}` -> `{'code':400,'error':'unknown_intent'}`.
   - `order_status`: needs truthy `order_id`, else `{'code':422,'error':'missing_order_id'}`; else `{'code':200,'intent':'order_status','reply':'status requested for order <id>'}`.
   - `refund`: missing `order_id` -> 422 `missing_order_id`; `amount` not a positive number (bools are not numbers) -> `{'code':422,'error':'invalid_amount'}`; else reply `'refund of <amount rounded to 2> queued for order <id>'`.
   - `kb_search`: `{'code':200,'intent':'kb_search','reply':'searching kb for: <trimmed text>'}`.
   - `escalate`: `{'code':200,'intent':'escalate','priority':<classify_priority>,'reply':'ticket escalated'}`.
   Build each dict with keys in exactly the order shown.

**Example:** `handle_ask({'intent':'kb_search','text':'  reset password  '})` -> `{'code': 200, 'intent': 'kb_search', 'reply': 'searching kb for: reset password'}`.

---
Edit `day20/solution.py`, commit & push, then click **Run Test** in the platform.
