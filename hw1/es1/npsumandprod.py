import numpy as np
n,m=[int(i) for i in input().split()]
m1=[]
for i in range(n):
    m1.append([int(i) for i in input().split()])
m1=np.array(m1)
print(np.prod(np.sum(m1,axis=0)))