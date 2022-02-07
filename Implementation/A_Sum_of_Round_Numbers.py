for i in range(int(input())):
    n=int(input())
    l=len(str(n))
    if l==1 or str(n).count('0')==l-1:
        print(1)
        print(n)
    else:
        count=l-str(n).count('0')
        temp=str(n)
        final=[]
        print(count)
        i=0
        while(count!=0):
            if temp[i]!='0':
                final.append(temp[i]+'0'*(l-i-1))
                count-=1
                i+=1
            else:
                i+=1
        print(*final)
