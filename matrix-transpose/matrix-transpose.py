import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    A=np.array(A)
    rows, columns=A.shape
    transpose = np.zeros((columns, rows), dtype=A.dtype)
    for i in range(rows):
        for j in range(columns):
            transpose[j][i]=A[i][j]

    return transpose
            
