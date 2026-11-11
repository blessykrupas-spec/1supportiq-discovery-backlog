def final_answer(chain):
    """Return the text after the last '####' marker, stripped (or the whole chain)."""
    raise NotImplementedError

def majority_vote(chains):
    """Return the most common final answer across chains (ties: answer ascending)."""
    raise NotImplementedError

def validate_output(obj, schema):
    """Return True if obj is a dict matching the schema exactly (keys and types)."""
    raise NotImplementedError
