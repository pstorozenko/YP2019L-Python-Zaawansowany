def standarize(X):
    return (X - X.mean(axis = 0)) / X.std(axis = 0)