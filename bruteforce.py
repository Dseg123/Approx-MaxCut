import itertools
import numpy as np

def maxcut_bruteforce(graph):
    """
    Solve the Max-Cut problem using brute force for small graphs.
    `graph` is an adjacency matrix representing the graph.
    """
    # Number of vertices in the graph
    n = graph.shape[0]
    
    # All possible ways to split the set of vertices into two sets
    max_cut_value = 0
    best_partition = None
    
    # Generate all possible partitions into two sets
    for partition in itertools.product([0, 1], repeat=n):
        # Calculate the cut value (number of edges between the two sets)
        cut_value = 0
        for i in range(n):
            for j in range(i + 1, n):
                if partition[i] != partition[j]:
                    cut_value += graph[i, j]
        
        # Update max cut value and partition if we found a better one
        if cut_value > max_cut_value:
            max_cut_value = cut_value
            best_partition = partition
    
    return max_cut_value, best_partition
