import math

def percentiles(latencies):
    """Return (p50, p95, p99) via nearest-rank, each round(x, 2); ValueError if empty."""
    raise NotImplementedError

def over_budget(latencies, budget_ms):
    """Return how many latencies are strictly greater than budget_ms."""
    raise NotImplementedError

def slowest_stage(stages):
    """Return the stage name with the highest mean latency (ties: name ascending)."""
    raise NotImplementedError
