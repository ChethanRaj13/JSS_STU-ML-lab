import numpy as np
from sklearn.datasets import load_iris

def pca():
    iris = load_iris()
    X = iris.data

    X_mean = X - np.mean(X,axis=0)

    cov_matrix = np.cov(X_mean.T)

    eigen_values , eigen_vectors = np.linalg.eig(cov_matrix)

    idx = np.argsort(eigen_values)[::-1]
    eigen_vectors = eigen_vectors[:,idx]

    components = eigen_vectors[:,:2]

    X_pca = np.dot(X_mean,components)

    print("PCA Transformed data:")
    print(X_pca[:5])

def lda():
    iris = load_iris()
    X = iris.data
    y = iris.target

    n_features = X.shape[1]

    mean_overall = np.mean(X,axis=0)

    SW = np.zeros((n_features,n_features))
    SB = np.zeros((n_features,n_features))

    for c in np.unique(y):
        X_c = X[y==c]

        mean_c = np.mean(X_c,axis=0)

        SW += (X_c - mean_c).T.dot(X_c - mean_c)

        n_c = X_c.shape[0]

        mean_diff = (mean_c-mean_overall).reshape(n_features,1)

        SB += n_c * mean_diff.dot(mean_diff.T)

        eigen_value , eigen_vector = np.linalg.eig(
            np.linalg.inv(SW).dot(SB)
        )

        idx = np.argsort(abs(eigen_value))[::-1]
        eigen_vector = eigen_vector[:,idx]

        W = eigen_vector[:,:2]

        X_lda = np.dot(X,W)

        print("LDA Transformed data:")

        print(X_lda[:5])

lda()