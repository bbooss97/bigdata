n= int(input())
s1={int(x) for x in input().split()}
m=int(input())
s2={int(x) for x in input().split()}
print( len(s1.symmetric_difference(s2)))