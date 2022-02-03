c=0
for i in range(int(input())):
    if '+' in input():
        c+=1
    else:
        c-=1
print(c)