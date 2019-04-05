import numpy as np

def clamp(x):
    return np.where(x < 0, 0, np.where(x > 1, 1, x))
