n=int(input())
s=set()
toAdd=[int(i) for i in input().split()]
for i in toAdd:
    s.add(i)
N=int(input())
for i in range(N):
    inp=input().split()
    command=inp[0]
    if command=="pop":
        s.pop()
    elif command=="remove":
        if int(inp[1])in s:
            s.remove(int(inp[1]))
    elif command=="discard":
        s.discard(int(inp[1]))
print(sum(s))