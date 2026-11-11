SAMPLE_RUNS = [
    {"run_id": 1, "params": {"C": 0.1}, "metrics": {"f1": 0.71, "loss": 0.44}},
    {"run_id": 2, "params": {"C": 1.0}, "metrics": {"f1": 0.83, "loss": 0.30}},
    {"run_id": 3, "params": {"C": 2.0}, "metrics": {"f1": 0.83, "loss": 0.25}},
    {"run_id": 4, "params": {"C": 5.0}, "metrics": {"loss": 0.22}},
]

def record_run(store, params, metrics):
    """Append a run (run_id = len(store)+1) with copies of params/metrics; return run_id."""
    raise NotImplementedError

def best_run(store, metric, mode="max"):
    """Return run_id of the run optimizing `metric` (mode 'max' or 'min'),
    breaking ties by smallest run_id. Return -1 if no run has the metric."""
    raise NotImplementedError

def get_metric(store, run_id, metric):
    """Return round(metric value, 2) for run_id, or None if the run is absent."""
    raise NotImplementedError
