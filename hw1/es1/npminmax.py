import numpy as np
n,m=[int(i) for i in input().split()]
m1=[]
for i in range(n):
    m1.append([int(i) for i in input().split()])
m1=np.array(m1)
print(np.max(np.min(m1,axis=1)))