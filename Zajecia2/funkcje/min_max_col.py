import numpy as np

def min_max_col(X):
    return np.vstack((X.min(axis = 0), X.max(axis = 0)))