n,m=[int(i) for i in input().split()]

for i in range(m):
    if len(str(n))>1:
        if n%10==0:
            n=n//10
        else:
            n-=1
    else:
        n-=1
print(n)