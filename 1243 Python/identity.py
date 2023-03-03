m = int(input('Enter the number of rows and columns : '))
l=[]
for i in range(m):
    l1=[]
    for j in range(m):
        if i==j:
            l1.append(1)
        else:
            l1.append(0)
    l.append(l1)

for i in range(m):
    for j in range(m):
        print(l[i][j],end=" ")
    print()
