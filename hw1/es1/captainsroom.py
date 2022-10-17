k=int(input())
dict={}
els=[int(x) for x in input().split()]
for el in els:
    if el in dict:
        dict[el]+=1
    else:
        dict[el]=1
for i in dict:
    if dict[i]==1:
        print(i)
        break