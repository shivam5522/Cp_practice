for num in range(int(input())):
    l=input()
    c=0
    final=[]
    for i in range(len(l)):
        if l[i]=='1':
            final.append(i)
    for i in range(len(final)-1):
        c+=final[i+1]-final[i]-1

    print(c)