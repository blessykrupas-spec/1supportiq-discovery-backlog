
_RANK = {"low": 1, "medium": 2, "high": 3, "critical": 4}

def find_unpinned(deps):
    # TODO: return sorted names of deps missing an exact version or a hash list
    raise NotImplementedError

def scan_vulnerable(sbom, advisories):
    # TODO: return sorted 'name==version' for components whose version is advised vulnerable
    raise NotImplementedError

def severity_gate(findings, min_severity):
    # TODO: return True if any finding meets/exceeds the min severity
    raise NotImplementedError
