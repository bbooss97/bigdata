import numpy as np

n,m=[int(i) for i in input().split()]
m1=[]
for i in range(n):
    m1.append([int(i) for i in input().split()])
m1=np.array(m1)
print(m1.mean(axis=1))
print(m1.var(axis=0))
print(m1.std(axis=None))