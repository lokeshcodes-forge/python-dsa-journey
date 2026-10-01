import numpy as np
a=np.array([
    [1,2,3],
    [4,5,6]
])
print("original array")
print(a)

b= a.ravel()
print("\nravel:")
print (b)
b[0]=100
print("\nafter changing b")
print("b=")
print(b)
print("\noriginal array a")
print(a)