import sqlite3

TICKETS_A = [
    {"id": 1, "text": "refund please",      "category": "billing",   "order_id": "A1",  "priority": 3},
    {"id": 2, "text": "where is my order",  "category": "shipping",  "order_id": "A2",  "priority": 2},
    {"id": 3, "text": "double charge",      "category": "billing",   "order_id": None,  "priority": 5},
    {"id": 4, "text": "late delivery",      "category": "shipping",  "order_id": "A4",  "priority": 1},
    {"id": 5, "text": "app keeps crashing", "category": "technical", "order_id": None,  "priority": 4},
]

TICKETS_B = [
    {"id": 10, "text": "wrong item",     "category": "shipping", "order_id": "B1", "priority": 2},
    {"id": 11, "text": "card declined",  "category": "billing",  "order_id": "",   "priority": 4},
    {"id": 12, "text": "invoice wrong",  "category": "billing",  "order_id": "B3", "priority": 4},
    {"id": 13, "text": "package stuck",  "category": "shipping", "order_id": "B4", "priority": 5},
]

def category_features(tickets):
    """Return sorted list of (category, ticket_count, round(avg_priority,2),
    high_priority_count) using a SQL GROUP BY over an in-memory sqlite table."""
    raise NotImplementedError

def failing_billing_rows(tickets):
    """Data test: return the number of 'billing' tickets whose order_id is
    NULL or an empty string."""
    raise NotImplementedError
