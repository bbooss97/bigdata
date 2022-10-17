nSubjects,nStudents=[int(x)for x in input().split()]
subjects=[]
for i in range(nStudents):
    subjects.append([float(x) for x in input().split()])
sGrades=zip(*subjects)
for i in sGrades:
    print(sum(i)/nStudents)