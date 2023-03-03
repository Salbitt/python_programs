l =[12,23,34,22,67,83,55,81]
print('Series:',l)
print('Prime numbers:')
for i in range(0,len(l)):
    flag = True
    
    for j in range(2,l[i]):
        if l[i]%j==0 and l[i]!=2:
                flag = False
                break
    if flag:
            print(l[i])
