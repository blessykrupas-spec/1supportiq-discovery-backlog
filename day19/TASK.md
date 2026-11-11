# Day 19 — Fargate task economics and secret resolution

**Scenario:** SupportIQ's ticket-triage API runs as an ECS Fargate service backed by RDS, with DB credentials injected from Secrets Manager.

## Your task
Implement three pure functions.

1. `fargate_task_cost(vcpu, mem_gb, duration_sec)` -> float: On-demand Fargate is billed at **$0.04048 per vCPU-hour** and **$0.004445 per GB-hour**. Return the task's cost as `round(cost, 2)`.
2. `validate_task_def(td)` -> list: Return a **sorted** list of error codes for a task definition dict. Rules: append `"cpu_invalid"` if `td['cpu']` is not a valid Fargate CPU size (256, 512, 1024, 2048, 4096); else `"memory_invalid"` if `td['memory']` is not a legal memory value for that CPU (legal memory MiB per CPU: 256 -> {512,1024,2048}; 512 -> {1024,2048,3072,4096}; 1024 -> 2048..8192 step 1024; 2048 -> 4096..16384 step 1024; 4096 -> 8192..30720 step 1024); `"missing_execution_role"` if `executionRoleArn` is absent/empty; and `"image_not_pinned:<container-name>"` for every container whose `image` has no tag/digest or ends with `:latest`.
3. `resolve_secret_env(env, secrets)` -> dict: `env` is a list of `{'name','value'}`. If a value starts with `secretsmanager://<arn>#<key>`, replace it with `secrets[arn][key]` (use `"MISSING"` when the arn or key is absent, or when no `#key` is present); otherwise keep the value. Return a dict keyed by name, inserted in **sorted name order**.

**Example:** `fargate_task_cost(1, 4, 86400)` -> `1.4`; `resolve_secret_env([{'name':'DB_URL','value':'secretsmanager://arn:db#url'}], {'arn:db':{'url':'postgres://rds/supportiq'}})` -> `{'DB_URL': 'postgres://rds/supportiq'}`.

---
Edit `day19/solution.py`, commit & push, then click **Run Test** in the platform.
