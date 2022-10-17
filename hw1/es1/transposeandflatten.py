import numpy as np
r,c=[int(i) for i in input().split()]
matrix=[]
for i in range(r):
    matrix.append([int(i) for i in input().split()])
m=np.array(matrix)
print(m.transpose())
print(m.flatten())