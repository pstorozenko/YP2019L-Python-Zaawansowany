import numpy as np

def approx_pi(n):
    x , y = np.random.rand(n), np.random.rand(n)
    return np.sum(x ** 2 + y ** 2 <= 1) / n * 4
