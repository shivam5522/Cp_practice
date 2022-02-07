for i in range(int(input())):
    temp=int(input())
    t=len(str(temp))
    d=int(list(set(str(temp)))[0])
    print((10*(d-1))+int((t/2)*(t+1)))