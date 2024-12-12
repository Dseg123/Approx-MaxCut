import numpy as np
import cvxpy as cp

def selectors(i, j, n):
    m1 = np.zeros(n)
    m2 = np.zeros(n)
    m1[i] = 1
    m2[j] = 1
    return (m1, m2)

def solve_sdp(A):
    n = len(A)
    X = cp.Variable((n, n), symmetric=True)
    constraints = [X >> 0]
    for i in range(n):
        m1, m2 = selectors(i, i, n)
        constraints += [m1 @ X @ m2 == 1]
   
    prob = cp.Problem(cp.Minimize(cp.trace(A @ X)),
                  constraints)

    prob.solve()

    eigenvalues, eigenvectors = np.linalg.eigh(X.value)

    # Discard eigenvalues that are very close to zero
    threshold = -100  # You can adjust this threshold
    non_zero_indices = eigenvalues > threshold

    Q = eigenvectors[:, non_zero_indices]

    return Q