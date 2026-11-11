
_TYPES = {"string": str, "int": int, "float": (int, float), "bool": bool, "list": list, "dict": dict}

def validate_payload(payload, schema):
    # TODO: return sorted 'missing:<f>' and 'type:<f>' errors against the contract
    raise NotImplementedError

def detect_breaking_changes(old, new):
    # TODO: return sorted removed/type_changed/now_required/added_required findings
    raise NotImplementedError
