
import math

def cosine_similarity(a, b):
    """Cosine similarity of two equal-length vectors, rounded to 2 decimals.
    Returns 0.0 if either vector has zero magnitude."""
    raise NotImplementedError

def top_k_docs(query_vec, docs, k):
    """docs: {doc_id: vector}. Return the k doc_ids most similar to query_vec,
    sorted by similarity descending, ties broken by doc_id ascending."""
    raise NotImplementedError
