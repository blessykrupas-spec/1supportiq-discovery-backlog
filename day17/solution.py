
def is_allowed(rules, port, source_ip):
    """rules: list of {'from_port','to_port','cidr'} inbound allow rules.
    Return True if a rule admits (port, source_ip)."""
    raise NotImplementedError

def open_to_internet(rules):
    """Return the sorted list of distinct ports reachable from 0.0.0.0/0."""
    raise NotImplementedError
