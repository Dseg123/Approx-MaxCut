import numpy as np

def evaluate_cut(A, cut):
    tot = 0
    for i in range(len(cut)):
        for j in range(len(cut)):
            if A[i, j] == 1:
                tot += (cut[i] != cut[j])
    return tot/2