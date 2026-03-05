import math
def log_transform(values):
    """
    Apply the log1p transformation to each value.
    """
    # Write code here
    # for i in range(values):
    #     m.log(1+value[i])

    result = [math.log1p(v) for v in values]
    return result
    