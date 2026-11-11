# Day 09 — SupportIQ: Hand-Built TF-IDF Ticket Classifier

**Scenario:** SupportIQ's first-pass ticket classifier is a from-scratch TF-IDF model (no scikit-learn) that routes a ticket to the class of its most similar training example.

## Your task
Standard library only (`math`, `collections`). Implement:

- `tokenize(text)` -> `list[str]`: lowercase, split on any non-alphanumeric character.
- `tfidf(doc, corpus_texts)` -> `dict`: `{term: round(tf*idf, 4)}` for each term in `doc`, keys in sorted order. Use `tf = count / total_tokens` and `idf = log((1 + N) / (1 + df)) + 1` where `N = len(corpus_texts)` and `df` = number of corpus texts containing the term.
- `cosine(a, b)` -> `float`: cosine similarity of two tf-idf dict vectors, `round(x, 4)`; `0.0` if either vector is empty.
- `classify(doc, labeled_corpus)` -> `str`: `labeled_corpus` is a list of `(text, label)`; return the label of the text with the highest cosine similarity to `doc`, breaking ties by the alphabetically smallest label.

**Example:** `classify('refund my charge', corpus)` returns `'billing'` when the billing examples share the most weighted terms with the ticket.

---
Edit `day09/solution.py`, commit & push, then click **Run Test** in the platform.
