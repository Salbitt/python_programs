m1 = float(input('Enter the value of mass m1: '))
m2 = float(input('Enter the value of mass m2: '))
r = float(input('Enter the value of distance r: '))
g = 6.67*pow(10,-11)
f = (g*m1*m2)/r**2
print('Gravitational force between the two objects :',round(f,2))
