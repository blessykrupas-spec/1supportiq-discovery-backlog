class OrderNotFoundError(Exception):
    pass

def lookup_order(orders, order_id):
    raise NotImplementedError

def describe_order(orders, order_id):
    raise NotImplementedError

def raises_not_found(orders, order_id):
    raise NotImplementedError

def _raise_value():
    try:
        lookup_order([], '')
    except ValueError:
        return True
    except NotImplementedError:
        return False
    return False
