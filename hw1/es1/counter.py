from collections import Counter
n=int(input())
a=Counter(input().split())
op=int(input())
res=0
for i in range(op):
    inp=input().split()
    if inp[0] in a and a[inp[0]]>=1:
        res+=int(inp[1])
        a[inp[0]]-=1
print(res)