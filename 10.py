import numpy as np
a = np.array([[1,2,3],[4,5,6]])
print("Shape :",a.shape)
print("Size :",a.size)
print("Dimension :",a.ndim)
print("Datatype :",a.dtype)
a = a.astype(float)
print(a.dtype)