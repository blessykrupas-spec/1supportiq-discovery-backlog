# Day 17 — AWS security-group reachability and internet-exposure check

**Scenario:** SupportIQ runs on AWS behind security groups; before deploy you must check which traffic a group admits and flag any ports exposed to the whole internet.

## Your task
A security-group `rule` is a dict `{"from_port": int, "to_port": int, "cidr": str}` (an inbound allow rule). Implement (standard library only — do CIDR matching by hand with integer/bit math; no `ipaddress`/`boto3`):

- `is_allowed(rules, port, source_ip)` — return `True` if **any** rule's inclusive port range contains `port` **and** `source_ip` (a dotted IPv4 string) falls inside that rule's CIDR block.
- `open_to_internet(rules)` — return the **sorted list of distinct ports** reachable from `0.0.0.0/0` (the group's internet-facing exposure).

**Example:**
```
rules = [{"from_port":443,"to_port":443,"cidr":"0.0.0.0/0"},
         {"from_port":22, "to_port":22, "cidr":"10.0.0.0/8"}]
is_allowed(rules, 22, "10.1.2.3")   -> True
is_allowed(rules, 22, "203.0.113.5")-> False
open_to_internet(rules)             -> [443]
```


---
Edit `day17/solution.py`, commit & push, then click **Run Test** in the platform.
