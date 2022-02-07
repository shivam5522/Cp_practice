m=0
max=0
for i in range(int(input())):
    p,q=[int(i) for i in input().split()]
    m+=q-p
    if m>max:
        max=m
print(max)
 