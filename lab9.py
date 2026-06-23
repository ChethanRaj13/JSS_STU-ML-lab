import numpy as np
from sklearn.datasets import load_iris

X = load_iris().data[:10,:2]

cluster = [[i] for i in range(len(X))]

print(cluster)

while len(cluster) > 1:

    min_dist = float('inf')
    c1,c2 = 0,0

    for i in range(len(cluster)):
        for j in range(i+1, len(cluster)):

            dist = min(
                np.linalg.norm(X[p1]-X[p2])
                for p1 in cluster[i]
                for p2 in cluster[j]
            )

            if dist < min_dist:
                min_dist = dist
                c1,c2 = i,j
    
    cluster[c1].extend(cluster[c2])
    del cluster[c2]
    print(cluster, "minimum distance: ", min_dist)