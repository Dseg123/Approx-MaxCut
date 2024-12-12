import numpy as np
import cvxpy as cp

def selectors(i, j, n):
    m1 = np.zeros(n)
    m2 = np.zeros(n)
    m1[i] = 1
    m2[j] = 1
    return (m1, m2)

def solve_sdp(A):
    rho = -0.686
    n = len(A)

    adj = []
    for i in range(n):
        adj_verts = []
        for j in range(n):
            if A[i, j] == 1:
                adj_verts.append(j)
        adj.append(adj_verts)

    X = cp.Variable((n, n), symmetric=True)
    constraints = [X >> 0]
    for i in range(n):
        m1, m2 = selectors(i, i, n)
        constraints += [m1 @ X @ m2 == 1]

    # a = [[1, 1, 1], [1, -1, -1], [-1, -1, 1], [-1, 1, -1]]
    # for i in range(n):
    #     for j in range(n):
    #         for k in range(n):
    #             if i == j or j == k or i == k:
    #                 continue
                
    #             mi, mj = selectors(i, j, n)
    #             mj, mk = selectors(j, k, n)
    #             for z in a:
    #                 constraints += [z[0] * mi @ X @ mj + z[1] * mj @ X @ mk + z[2] * mi @ X @ mk <= 1]

    for i in range(n):
        adj_verts = adj[i]
        for j in adj_verts:
            mi, mj = selectors(i, j, n)
            constraints += [mi @ X @ mj >= rho - 0.02]
            constraints += [mi @ X @ mj <= rho + 0.02]



    for i in range(n):
        print(i)
        adj_verts = adj[i]
        for j in adj_verts:
            for k in adj_verts:
                if j == k:
                    continue


                mi, mj = selectors(i, j, n)
                mj, mk = selectors(j, k, n)
                constraints += [mi @ X @ mj + mj @ X @ mk + mi @ X @ mk >= -1]
                
   
    prob = cp.Problem(cp.Minimize(cp.trace(A @ X)),
                  constraints)

    prob.solve()

    eigenvalues, eigenvectors = np.linalg.eigh(X.value)

    # Discard eigenvalues that are very close to zero
    threshold = -100  # You can adjust this threshold
    non_zero_indices = eigenvalues > threshold

    Q = eigenvectors[:, non_zero_indices]

    return Q