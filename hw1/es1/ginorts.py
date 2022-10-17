from functools import cmp_to_key
s=input()
lower=[]
upper=[]
odd=[]
even=[]
for i in s:
    if i.islower():
        lower.append(i)
    elif i.isupper():
        upper.append(i)
    elif int(i)%2==0:
        even.append(i)
    else:
        odd.append(i)
lower.sort()
upper.sort()
odd.sort()
even.sort()
print("".join(lower+upper+odd+even))
