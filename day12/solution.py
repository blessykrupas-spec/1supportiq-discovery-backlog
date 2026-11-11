import json

SCHEMA = {"category": "str", "priority": "int", "escalate": "bool"}

GOOD = '{"category": "billing", "priority": 4, "escalate": true}'
BAD_TYPE = '{"category": "billing", "priority": "high", "escalate": true}'
MISSING = '{"category": "billing", "escalate": true}'
MALFORMED = '{"category": "billing", "priority": 4,'

def parse_json(text):
    """Return the parsed dict, or None if text is not valid JSON or not an object."""
    raise NotImplementedError

def validate_output(text, schema):
    """Parse text; if invalid JSON/object return ['invalid_json']. Otherwise return a
    sorted list with 'missing:<field>' for absent fields and 'type:<field>' for wrong
    types. schema maps field -> one of 'str','int','float','bool','list'
    (bool is NOT a valid int/float)."""
    raise NotImplementedError

def backoff_schedule(base, factor, retries, cap):
    """Return [round(min(cap, base*factor**i), 2) for i in range(retries)]."""
    raise NotImplementedError
