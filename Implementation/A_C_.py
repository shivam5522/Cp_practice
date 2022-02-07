for i in range(int(input())):
    a,b,n=[int(i) for i in input().split()]
    c=0
    while (n>=max(a,b)):
        if n-a<n-b:
            b+=a
        else:
            a+=b
        c+=1
    print(c)