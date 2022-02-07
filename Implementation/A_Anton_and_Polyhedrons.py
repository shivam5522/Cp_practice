c=0
d={'Tetrahedron':4,'Cube':6,'Octahedron':8,"Dodecahedron":12,'Icosahedron':20}
for tc in range(int(input())):
    n=input()
    c+=d[n]
print(c)