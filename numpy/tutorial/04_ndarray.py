import numpy as np

a = np.ndarray(shape=(2,2), dtype=float, order='F')

print(a)
print(type(a))
a = np.arange(12)
print(type(a))

a1 = np.array([[1,2],[3,4]])
np.pad(a1,((1,0),(1,0))) # (1,0),(1,0)  (上，下),(左,右)