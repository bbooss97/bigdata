if __name__ == '__main__':
    inp=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        inp.append([name,score])
    dictionary = sorted({v for k,v in inp})
    second_lowest = dictionary[1]
    res=[]
    for i in inp:
        if i[1] == second_lowest:
            res.append(i[0])
    res=sorted(res)
    for i in res:
        print(i)
    
