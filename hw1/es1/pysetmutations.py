n= int(input())
s1={int(x) for x in input().split()}
m=int(input())
for i in range(m):
    imp=input().split()
    command=imp[0]
    s2={int(x) for x in input().split()}
    if command=="intersection_update":
        s1.intersection_update(s2)
    elif command=="update":
        s1.update(s2)
    elif command=="symmetric_difference_update":
        s1.symmetric_difference_update(s2)
    elif command=="difference_update":
        s1.difference_update(s2)
print(sum(s1))