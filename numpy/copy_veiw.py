import numpy as np

print("===== COPY =====")

a = np.array([1,2,3,4])

b = a.copy()

print("Original:", a)
print("Copy:", b)

b[0] = 100

print("After changing copy")
print("Original:", a)
print("Copy:", b)

print("\n===== VIEW =====")

x = np.array([10,20,30,40])

y = x.view()

print("Original:", x)
print("View:", y)

y[0] = 999

print("After changing view")
print("Original:", x)
print("View:", y)

print("\n===== MEMORY CHECK =====")

print(a.base)
print(b.base)

print(x.base)
print(y.base)