
def apply_order(deps):
    """Return a valid Terraform apply order (dependencies first), ties broken by
    name ascending; [] if the graph has a cycle."""
    raise NotImplementedError

def has_cycle(deps):
    """Return True if the resource dependency graph cannot be fully ordered."""
    raise NotImplementedError
