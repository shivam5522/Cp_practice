n=int(input())
l=[int(i) for i in input().split()]
f=[0 for i in range(n)]
for i in range(len(l)):
    f[l[i]-1]=i+1
print(*f)