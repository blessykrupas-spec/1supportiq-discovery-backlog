
import hashlib

def in_canary(user_id, percent):
    # TODO: stable sha256 bucket of user_id in [0,100); True when bucket < percent
    raise NotImplementedError

def assign_variant(user_id, percent):
    # TODO: 'canary' or 'stable'
    raise NotImplementedError

def canary_share(user_ids, percent):
    # TODO: fraction of users routed to canary, round(.,2)
    raise NotImplementedError

def decide_release(canary_score, stable_score, margin):
    # TODO: promote / rollback / hold from the score margin
    raise NotImplementedError
