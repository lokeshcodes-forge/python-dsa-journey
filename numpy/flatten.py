import numpy as np 
a = np.array([
    [1,2,3],
    [4,5,6]
])

print("original:")
print(a)

b = a.flatten()
print("\nFlatten:,")
print(b)

b[0]=100
print("\nafter changing b:")
print("b =",b)

print("\na=")
print(a)