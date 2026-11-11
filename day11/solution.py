CANDIDATE = {"f1": 0.86, "latency_ms": 180.0}
PROD = {"f1": 0.83, "latency_ms": 150.0}

SCORE_ROWS = [
    {"id": 1, "score": 0.91},
    {"id": 2, "score": 0.40},
    {"id": 3, "score": 0.70},
    {"id": 4, "score": 0.69},
]

def should_promote(candidate, prod, metric, min_delta):
    """True iff candidate[metric] >= prod[metric] + min_delta (False if metric missing)."""
    raise NotImplementedError

def passes_gates(candidate, gates):
    """gates maps metric -> (op, value) with op in {'min','max'}. Return True iff every
    gate holds: 'min' needs value >= bound, 'max' needs value <= bound. Missing metric fails."""
    raise NotImplementedError

def batch_predict(rows, threshold):
    """Return the sorted list of row ids whose score >= threshold."""
    raise NotImplementedError
