n=int(input())
for i in range(n):
    input()
    a={int(x) for x in input().split()}
    input()
    b={int(x) for x in input().split()}
    print(a.issubset(b))