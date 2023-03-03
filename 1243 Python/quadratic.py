a = int(input('Enter value of a : '))
b = int(input('Enter value of b : '))
c = int(input('Enter value of c : '))
d = b**2 - 4*a*c
if d<0:
    print('Roots are imaginary')
elif d==0:
    print('Roots are real and equal')
    d = d**0.5
    x = (-b + d)/(2*a)
    print('Root : ',x)
else:
    print('Roots are real and unequal')
    d = d**0.5
    x1 = (-b +d)/(2*a)
    x2 = (-b -d)/(2*a)
    print('Root 1 : ',x1,' Root 2 : ',x2)
