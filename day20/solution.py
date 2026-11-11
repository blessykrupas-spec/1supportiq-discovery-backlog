
VALID_INTENTS = {"order_status", "refund", "kb_search", "escalate"}

def classify_priority(text):
    # TODO: P1 for urgent/outage language, P2 for error language, else P3
    raise NotImplementedError

def handle_ask(request):
    # TODO: validate the request, then route by intent to a response or an error dict
    raise NotImplementedError
