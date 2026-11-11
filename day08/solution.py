BATCH = [
    {"id": 1, "category": "billing",  "order_id": "A1", "ts": 1000},
    {"id": 2, "category": "shipping", "order_id": None, "ts": 1100},
    {"id": 3, "category": None,       "order_id": "A3", "ts": 1200},
    {"id": 4, "category": "billing",  "order_id": "",   "ts": 1250},
]

OLD_ROWS = [
    {"id": 1, "category": "billing", "order_id": "A1", "priority": 3},
    {"id": 2, "category": "billing", "order_id": "A2", "priority": 4},
]
NEW_ROWS = [
    {"id": 3, "category": "billing", "priority": 3, "sentiment": "neg"},
    {"id": 4, "category": "billing", "priority": 5, "sentiment": "pos"},
]

def null_rate(rows, field):
    """Fraction of rows whose `field` is None or empty string, round(.,2)."""
    raise NotImplementedError

def is_fresh(rows, now_ts, max_age_sec):
    """True if (now_ts - latest row ts) <= max_age_sec; False on empty input."""
    raise NotImplementedError

def schema_drift(old_rows, new_rows):
    """Return (sorted added keys, sorted removed keys) between two row-sets."""
    raise NotImplementedError
