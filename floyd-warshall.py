from math import inf
import numpy as np


def floydWarshall (graph):
    a = graphToMatrix(graph)
    size =a.shape[0] #size of single row or single column
    for k in range(0,size):
        for i in range(0,size):
            for j in range(0,size):
                if i == j or i==k or j==k:
                    continue
                else:
                    a[i,j] = min(a[i,j],a[i,k]+a[k,j])
    print (a)


def graphToMatrix(graph):
    node = sorted(graph.keys())
    keyIndex = {key: i for i, key in enumerate(node)} #this is a variable that makes a dictionary by making a loop; to say that ex: A -> 0, B -> 1, C -> 2 & so on
    size = len(graph) #size of single row, or single column
    a0 = np.full((size,size),np.inf)
    for edge in graph:
        b =graph[edge]
        for directedEdge in b:
            i = keyIndex[edge]
            j = keyIndex[directedEdge]
            a0[i][j] = b[directedEdge]
        np.fill_diagonal(a0, 0)
    return (a0)

graph = {
     'A': {'B':2,'D':3},
     'B': {'A':3,'C':2},
     'C': {'D':4},
     'D': {'A':-2,'B':6}
}

floydWarshall(graph)