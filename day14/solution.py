
def select_chunks(chunks, threshold):
    """Return the doc ids of chunks whose score >= threshold, ranked by score
    descending then doc id ascending. Empty list if none qualify."""
    raise NotImplementedError

def build_answer(chunks, threshold):
    """Assemble a grounded answer with [n] citations, or abstain when the best
    chunk scores below threshold."""
    raise NotImplementedError
