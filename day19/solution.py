
CPU_RATE_PER_VCPU_HR = 0.04048
MEM_RATE_PER_GB_HR = 0.004445

def fargate_task_cost(vcpu, mem_gb, duration_sec):
    # TODO: compute (vcpu*CPU_RATE + mem_gb*MEM_RATE) * hours, rounded to 2 decimals
    raise NotImplementedError

def validate_task_def(td):
    # TODO: return a sorted list of error codes for an invalid Fargate task definition
    raise NotImplementedError

def resolve_secret_env(env, secrets):
    # TODO: resolve secretsmanager:// references against the secrets store
    raise NotImplementedError
