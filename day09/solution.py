import math
from collections import Counter

CORPUS = [
    ("refund my payment please charge", "billing"),
    ("payment failed card charge declined", "billing"),
    ("where is my package shipping delay", "shipping"),
    ("package not delivered shipping late", "shipping"),
]

def tokenize(text):
    """Lowercase, split on non-alphanumeric characters; return list of tokens."""
    raise NotImplementedError

def tfidf(doc, corpus_texts):
    """Return {term: round(tf*idf, 4)} for terms in doc, terms sorted.
    tf = count/total_tokens; idf = log((1+N)/(1+df)) + 1 over corpus_texts."""
    raise NotImplementedError

def cosine(a, b):
    """Cosine similarity of two tf-idf dict vectors, round(.,4); 0.0 if either is empty."""
    raise NotImplementedError

def classify(doc, labeled_corpus):
    """Nearest-centroid-style: return the label of the corpus text with the highest
    cosine similarity to doc; break ties by the alphabetically smallest label."""
    raise NotImplementedError
