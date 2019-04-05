import numpy as np

def err(x, y):
    return np.mean(x == y)

def mse(x, y):
    return np.mean((x - y) * (x - y))

def rmse(x, y):
    return np.sqrt(np.sum((x - y) ** 2)) / x.shape[0]

def mad(x, y):
    return np.mean(np.abs(x - y))
