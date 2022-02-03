for r in range(1,6):
    temp=input().split()
    if '1' in temp:
        cords=[r,temp.index('1')+1]
        break

total=abs(cords[0]-3)+abs(cords[1]-3)
print(total)