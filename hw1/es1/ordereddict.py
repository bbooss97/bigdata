from collections import OrderedDict
n= int(input())
d=OrderedDict()
for i in range(n):
    inp=input().split()
    a=" ".join(inp[:-1])
    b=inp[-1]
    if a in d:
        d[a]+=int(b)
    else:
        d[a]=int(b)
for i in d:
    print(i,d[i])