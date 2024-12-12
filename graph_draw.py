import numpy as np

def get_graph(n, d):
    arr = [i for i in range(n)]
    degrees = np.zeros(n)
    A = np.zeros((n, n))
    for i in range(n-1):
        already = np.sum(A[i, :])
        if d - already <= 0:
            continue
        inds = np.random.choice(arr[i+1:], size = int(d - already), replace = False)
        for j in inds:
            if degrees[i] < d and degrees[j] < d:
                A[i, j] = 1
                A[j, i] = 1
                degrees[i] += 1
                degrees[j] += 1
    
    return A

def get_random_graph(n, d):
    p = (d)/(n - 1)
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            z = np.random.rand() < p
            A[i, j] = z
            A[j, i] = z
    
    return A

    
        