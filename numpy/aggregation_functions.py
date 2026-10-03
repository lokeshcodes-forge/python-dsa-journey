import numpy as np 
a = np.array([
    [10,20,30],
    [40,50,60]

])
print(np.sum(a))
print(np.mean(a))
print(np.min(a))
print(np.max(a))
print(np.std(a))
print(np.var(a))
print(np.argmax(a))
print(np.argmin(a))

print(np.sum(a,axis=0))
print(np.sum(a,axis=1))


print(np .mean(a,axis=0))
print(np.mean(a,axis=1))

