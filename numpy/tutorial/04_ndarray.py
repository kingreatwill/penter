import numpy as np

a = np.ndarray(shape=(2,2), dtype=float, order='F')

print(a)
print(type(a))
a = np.arange(12)
print(type(a))