# Day 13 — pgvector KB search: cosine similarity and top-k retrieval

**Scenario:** SupportIQ stores each KB article as a pgvector embedding; to answer a ticket you must find the closest articles to the question's embedding using cosine similarity.

## Your task
Implement two functions (standard library only — compute cosine similarity by hand with `math`):

- `cosine_similarity(a, b)` — given two equal-length numeric vectors, return their cosine similarity as a float **rounded to 2 decimals** (`round(x, 2)`). If either vector has zero magnitude, return `0.0`.
- `top_k_docs(query_vec, docs, k)` — `docs` is a dict mapping `doc_id -> vector`. Return a list of the `k` `doc_id`s whose vectors are most similar to `query_vec`, sorted by similarity **descending**, with ties broken by `doc_id` **ascending**.

**Example:**
```
cosine_similarity([1, 0, 0], [1, 1, 0])          -> 0.71
top_k_docs([1, 0, 0],
           {"kb1": [1,0,0], "kb2": [0,1,0], "kb3": [1,1,0]}, 2)  -> ['kb1', 'kb3']
```


---
Edit `day13/solution.py`, commit & push, then click **Run Test** in the platform.
