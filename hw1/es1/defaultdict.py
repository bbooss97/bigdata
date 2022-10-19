from collections import defaultdict
n,m=[int(i) for i in input().split()]
a=defaultdict(list)
b=defaultdict(list)

for i in range(1,n+1):
    a[input()].append(i)

for i in range(1,m+1):
    b[input()].append(i)

for i in b:
    if i in a:
        print(*a[i])
    else:
        print(-1)
