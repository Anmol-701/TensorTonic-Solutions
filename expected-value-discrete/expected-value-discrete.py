import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """

    x = np.array(x)
    p = np.array(p)

    # Check length
    if len(x) != len(p):
        raise ValueError("x and p must have the same length")

    # Check probabilities range
    if np.any(p < 0) or np.any(p > 1):
        raise ValueError("Probabilities must be between 0 and 1")

    # Check if probabilities sum to 1
    if not np.isclose(np.sum(p), 1):
        raise ValueError("Probabilities must sum to 1")

    # Expected value formula
    expected_value = np.sum(x * p)

    return float(expected_value)