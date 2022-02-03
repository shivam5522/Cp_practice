n,k,l,c,d,p,nl,np=[int(i) for i in input().split()]
total_soda=(k*l)
total_lime=c*d
 
soda=total_soda//nl
lime=total_lime
salt=p//np
print(min(soda,lime,salt)//n)