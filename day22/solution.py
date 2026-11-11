
import math

def psi(baseline, current, eps=0.0001):
    # TODO: PSI = sum((c% - b%) * ln(c% / b%)) over bins, with an eps floor, round(.,2)
    raise NotImplementedError

def drift_alert(baseline, current, threshold):
    # TODO: True when PSI >= threshold
    raise NotImplementedError

def most_shifted_bin(baseline, current):
    # TODO: index of the bin with the largest absolute proportion change
    raise NotImplementedError
