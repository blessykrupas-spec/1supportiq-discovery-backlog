def burndown_remaining(total_points, completed_per_day):
    """Return remaining points after each day (never below 0)."""
    raise NotImplementedError

def next_version(current, labels):
    """Return the next semver from merged-PR labels (breaking>feature>fix)."""
    raise NotImplementedError

def changelog_buckets(prs):
    """Bucket PR titles by label into Added/Changed/Fixed/Other."""
    raise NotImplementedError
