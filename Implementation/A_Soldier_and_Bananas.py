import math
k,n,w=[int(i) for i in input().split()]

s=(w/2)*(2*k+((w-1)*k))

if s-n>0:
    print(int(s-n))
else:
    print(0)