n=input()
f=''
for i in range(len(n)):
    if 9-int(n[i])<int(n[i]):
        if 9-int(n[i])==0 and i==0:
            f+=str(n[i])
        else:
            f+=str(9-int(n[i]))
    else:
        f+=n[i]
print(int(f))