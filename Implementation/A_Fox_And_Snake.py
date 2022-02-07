n,m=[int(i) for i in input().split()]

flag=True
f=[]

for row in range(n):
    if row%2==0:
        f.append('#'*m)
    else:
        if flag:
            f.append('.'*(m-1)+'#')
        else:
            f.append('#'+'.'*(m-1))
        flag=not(flag)

for i in f:
    print(i)
