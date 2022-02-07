n=int(input())
s=input()

f=''
j=0
k=0
for i in range(n):
    f+=list(set(s[j:(j*k)+1]))[0]
    j=(j*k)+1
    k+=1

print(f)