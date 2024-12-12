import numpy as np

def get_cuts(Q, A, d, C=1):
    n = len(Q)

    eps = 1/(C * d * np.sqrt(np.log(d)))

    g = np.random.normal(0, 1, n)

    dots = [np.dot(Q[i, :], g) for i in range(n)]


    gw_cut = []
    for i in range(n):
        x = 1
        if dots[i] < 0:
            x = -1
        
        gw_cut.append(x)

    koth_cut = [z for z in gw_cut]

    for i in range(n):
        if np.abs(dots[i]) < eps:
            sum_B = 0
            sum_tot = 0
            for j in range(n):
                if A[i, j] != 0:
                    sum_tot += A[i, j]
                    if (dots[j]) * koth_cut[i] > eps:
                        sum_B += A[i, j]
            if 2 * sum_B - sum_tot > 0:
                koth_cut[i] = -koth_cut[i]

    return gw_cut, koth_cut
