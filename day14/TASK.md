# Day 14 — RAG answer assembly: inline citations and abstention gate

**Scenario:** SupportIQ's RAG assistant must answer only from retrieved KB chunks, cite each source, and abstain when retrieval is too weak to be trustworthy.

## Your task
A `chunk` is a dict `{"doc": str, "score": float, "text": str}`. Implement:

- `select_chunks(chunks, threshold)` — return the list of `doc` ids whose `score >= threshold`, ranked by `score` **descending** then `doc` **ascending**; empty list if none qualify.
- `build_answer(chunks, threshold)` — if the best chunk's score is **below** `threshold`, return exactly `"ABSTAIN: insufficient evidence"`. Otherwise concatenate the `text` of each qualifying chunk (in ranked order), each followed by a 1-based citation marker `"[n]"`, joined by single spaces.

**Example:**
```
chunks = [{"doc":"kb_ref","score":0.82,"text":"Refunds take 5 days."},
          {"doc":"kb_pol","score":0.61,"text":"Returns are allowed."}]
build_answer(chunks, 0.6)   -> 'Refunds take 5 days. [1] Returns are allowed. [2]'
select_chunks(chunks, 0.7)  -> ['kb_ref']
```


---
Edit `day14/solution.py`, commit & push, then click **Run Test** in the platform.
