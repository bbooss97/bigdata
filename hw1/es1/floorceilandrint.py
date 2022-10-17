import numpy as np
np.set_printoptions(legacy='1.13')
m=np.array([float(x) for x in input().split(" ")])
print(np.floor(m))
print(np.ceil(m))
print(np.rint(m))