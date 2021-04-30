import math

def is_equal(a,b,eps=1e-5):
    diff = math.fabs(a-b)
    rel_err1 = math.fabs(diff/a)
    rel_err2 = math.fabs(diff/b)
    if rel_err1 < eps and rel_err2 < eps:
        return True
    else:
        return False
