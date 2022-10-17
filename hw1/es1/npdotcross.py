import numpy as np
n=int(input())
m1=[]
m2=[]
for i in range(n):
    m1.append([int(i) for i in input().split()])
for i in range(n):
    m2.append([int(i) for i in input().split()])
m1=np.array(m1)
m2=np.array(m2)
print(m1@m2)