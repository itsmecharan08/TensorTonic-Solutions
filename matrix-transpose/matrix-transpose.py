import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    i = len(A)
    j = len(A[0])

    a = [[0] * i for _ in range(j)]

    for k in range(i):
        for m in range(j):
            a[m][k] = A[k][m]

    return np.asarray(a)