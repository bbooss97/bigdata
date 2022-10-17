import numpy as np
n,m,p=[int(i) for i in input().split()]
m1=[]
m2=[]
for i in range(n):
    m1.append([int(i) for i in input().split()])
for i in range(m):
    m2.append([int(i) for i in input().split()])
print(np.concatenate([np.array(m1),np.array(m2)],axis=0))