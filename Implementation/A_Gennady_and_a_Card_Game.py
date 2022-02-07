n=input()

l=[i for i in input().split()]
c=0

for i in l:
    if i[0]==n[0] or i[1]==n[1]:
        c+=1

if c>0:
    print('YES')
else:
    print('NO')