import numpy as np
m1=np.array([int(x) for x in input().split()])
m2=np.array([int(x) for x in input().split()])
print(np.inner(m1,m2))
print(np.outer(m1,m2))
