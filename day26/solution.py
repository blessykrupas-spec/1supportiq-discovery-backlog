import re

def authorize(role, action, resource):
    """Return True if `role` may perform `action` on `resource` (admin may do anything)."""
    raise NotImplementedError

def redact_pii(text):
    """Replace cards -> [CARD], phones -> [PHONE], emails -> [EMAIL]."""
    raise NotImplementedError

def has_injection(text):
    """Return True if `text` contains a known prompt-injection marker (case-insensitive)."""
    raise NotImplementedError
