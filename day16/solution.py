
import re

def prf1(y_true, y_pred):
    """Precision, recall, F1 for binary labels (positive class = 1), each rounded
    to 2 decimals, returned as a tuple."""
    raise NotImplementedError

def is_blocked(text, banned):
    """Guardrail: True if text contains a banned term, an email, or a run of
    10+ digits."""
    raise NotImplementedError
