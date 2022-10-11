n,m=[int(i) for i in input().split(" ")]
l=[int(x) for x in input().split(" ")]
a=set([int(x) for x in input().split(" ")])
b=set([int(x) for x in input().split(" ")])
res=0
for i in l:
    if i in a:
        res+=1
    if i in b:
        res-=1
print(res)