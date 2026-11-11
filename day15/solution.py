
ALLOWED = {"lookup_order", "search_kb", "create_escalation"}
WRITE = {"create_escalation"}
REQUIRED = {
    "lookup_order": ["order_id"],
    "search_kb": ["query"],
    "create_escalation": ["ticket_id", "reason"],
}

def dispatch(tool, args, approved=False):
    """Guarded MCP dispatcher: allow-list, argument validation, write-approval gate.
    Return 'DENY: unknown tool' / 'DENY: invalid arguments' /
    'DENY: approval required' / 'ALLOW: <tool>'."""
    raise NotImplementedError
