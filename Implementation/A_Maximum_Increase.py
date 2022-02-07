n=int(input())
l=[int(i) for i in input().split()]
final=0
c=1
for i in range(n-1):
    if l[i+1]>l[i]:
        c+=1
    else:
        if final<c:
            final=c
        c=1
if final<c:
    final=c

print(final)