n1 = int(input('Enter first number: '))
n2 = int(input('Enter second number: '))
print('Even numbers from,',n1,' to ',n2)
for i in range(n1,n2):
    if i%2==0:
        print(i)
if n2%2==0:
    print(n2)
