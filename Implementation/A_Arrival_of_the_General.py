no=int(input())
l=[int(i) for i in input().split()]
m=l.index(max(l))
maxi=max(l)
dist = m
l.remove(maxi)
l.insert(0,maxi)
z=l[::-1]
n=z.index(min(z))
dist+=n
print(dist)