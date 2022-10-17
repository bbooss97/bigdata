if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range(N):
        inp=input()
        inp=inp.split()
        command=inp[0]
        if command=="print":
            print(l)
        if command=="insert":
            index=int(inp[1])
            element=int(inp[2])
            l.insert(index,element)
        if command=="remove":
            element=int(inp[1])
            l.remove(element)
        if command=="sort":
            l.sort()
        if command=="pop":
            l.pop()
        if command=="reverse":
            l.reverse()
        if command=="append":
            element=int(inp[1])
            l.append(element)
    
