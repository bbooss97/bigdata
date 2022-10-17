import numpy as np
n=int(input())
m1=[]
for i in range(n):
    m1.append([float(i) for i in input().split()])
m1=np.array(m1)
print(np.around(np.linalg.det(m1),decimals=2))