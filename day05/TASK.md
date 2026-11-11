# Day 05 — Validate SupportIQ tickets against a data contract

**Scenario:** Tickets stream into SupportIQ from many channels; a data contract decides which ones are trustworthy and which get quarantined for review.

## Your task
Implement `validate_tickets(tickets, contract)`.

- `tickets` is a list of dicts. Each should carry an `id`.
- `contract` is a dict: `{"required": [field names], "category": [allowed values], "priority": [allowed values]}`.
- A ticket is **valid** when: every field in `required` is present and non-empty; its `category` is in the allowed list; and its `priority` is in the allowed list. Otherwise it is **quarantined**.
- Return a tuple `(valid_ids, quarantined_ids)` where each is a **sorted** list of the `id` values. A ticket with no `id` (or an empty one) is quarantined under the id `"<no-id>"`.

Also implement `is_valid(ticket, contract)` returning a bool for a single ticket (used by the above).

## Example
```python
contract = {'required': ['id','category','priority'],
            'category': ['billing','technical'], 'priority': ['low','high']}
tickets = [{'id':'T1','category':'billing','priority':'high'},
           {'id':'T2','category':'spam','priority':'low'}]
validate_tickets(tickets, contract)  # -> (['T1'], ['T2'])
```


---
Edit `day05/solution.py`, commit & push, then click **Run Test** in the platform.
