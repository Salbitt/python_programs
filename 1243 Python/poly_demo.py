print('Enter the polynomial coefficients (ax3 + bx2 + cx + d) :')
coeff=[]
for i in range(0,4):
    coeff.append(int(input()))
x = int(input('Enter the value of x : '))
sum = 0
for i in range(0,4):
    sum+=(coeff[i]*(x**(3-i)))

print(sum)
