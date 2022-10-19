from collections import namedtuple
n=int(input())
columns=input().split()
Student=namedtuple('Student',columns)
students=[]
for i in range(n):
    a,b,c,d=input().split()
    students.append(Student(a,b,c,d))
res=0
for i in students:
    res+=int(i.MARKS)
print(res/n)