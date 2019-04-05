import numpy as np
np.random.seed(123)
x = np.round(np.random.normal(size=20), 2)

# 1
print(x[((-2 <= x) & (x <= -1)) | ((1 < x) & (x < 2))])

# 2
print(np.sum(x < 0) / x.shape[0])
print((x < 0).mean())

# 3
print(np.abs(x).mean())

# 4
print(x[np.argmax(np.abs(x))])

# 5
print(x[np.argmax(np.abs(x - 2))])

# 6
print(np.abs(x) - np.floor(np.abs(x)))

# 7
# print(['nieujemny' if el >= 0 else 'ujemny' for el in x])
print(np.where(x >= 0, 'nieujemny', 'ujemny'))

# 8
# print(['maly' if el < 1 else 'duzy' if el > 1 else 'sredni' for el in x])
print(np.where(x < 1, 'maly', np.where(x > 1, 'duzy', 'sredni')))
