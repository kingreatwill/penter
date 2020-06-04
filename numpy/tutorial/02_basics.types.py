# https://numpy.org/doc/stable/user/basics.types.html
import numpy as np

a = np.int_([1, 2, 4])
print(a.dtype.name)
a = a.astype(float)
print(a)

d = np.dtype(int)
print(np.issubdtype(d, np.integer))
print(np.issubdtype(d, np.floating))
