a={int(x) for x in input().split()}
n=int(input())
for i in range(n):
    b={int(x) for x in input().split()}
    if not a.issuperset(b):
        print(False)
        break
print(True)