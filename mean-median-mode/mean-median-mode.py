import numpy as np
from collections import Counter

def mean_median_mode(x):
    """
    Compute mean, median, and mode.
    """
    x=np.array(x)
    mean=float(np.mean(x))
    median = float(np.median(x))

    result = Counter(x)
    max_1 = 0
    mode= None
    for i, j in result.items():
        if j>max_1:
            max_1 = j
            mode = i

    return mean, median, mode

    

   
    