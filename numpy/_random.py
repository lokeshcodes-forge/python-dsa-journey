import numpy as np

print (np.random.rand())
print (np.random.rand(5))
print (np.random.rand(2,3))
print (np.random.randint(1,10))
print (np.random.choice([10,20,30,40]))
a = np.array([1,2,3,3,4,5])
print(a)
np.random.shuffle(a)
print (a)
np.random.seed(42)
print (np.random.seed(5))







