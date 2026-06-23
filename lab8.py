import numpy as np
import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
X = iris.data

k = 3

centroid = X[:k]

for _ in range(100):
    clusters = []

    for point in X:
        distance = [np.linalg.norm(point - c) for c in centroid]
        clusters.append(np.argmin(distance))

    clusters = np.array(clusters)

    new_centroid = np.array([
        X[clusters == i].mean(axis=0)
        for i in range(k)
    ])

    if np.all(centroid == new_centroid):
        break   

    centroid = new_centroid

print("centroid: ", centroid)
