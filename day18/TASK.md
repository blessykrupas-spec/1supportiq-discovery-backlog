# Day 18 — Terraform dependency graph: topological apply order and cycle detection

**Scenario:** SupportIQ's `supportiq` Terraform project declares resources that depend on one another; Terraform must apply them in dependency order and reject any configuration with a dependency cycle.

## Your task
`deps` is a dict mapping each resource name to the list of resource names it **depends on** (those must be created first). Implement (standard library only):

- `apply_order(deps)` — return a valid apply order with every dependency appearing **before** the resources that depend on it. Use Kahn's topological sort and break ties by resource **name ascending** for a deterministic order. Return `[]` if the graph contains a cycle.
- `has_cycle(deps)` — return `True` if the graph cannot be fully ordered, else `False`.

**Example:**
```
deps = {"aws_instance.web": ["aws_subnet.main"],
        "aws_subnet.main":  ["aws_vpc.main"],
        "aws_vpc.main":     []}
apply_order(deps) -> ['aws_vpc.main', 'aws_subnet.main', 'aws_instance.web']
has_cycle({"a": ["b"], "b": ["a"]}) -> True
```


---
Edit `day18/solution.py`, commit & push, then click **Run Test** in the platform.
