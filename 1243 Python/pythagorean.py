
h = int(input('Enter the higher limit : '))

print('Pythagorean triplets in range 1 to',h)
for i in range(1,h+1):
    for j in range(i,h+1):
        sq = i**2 + j**2
        sq = sq**0.5
        n = int(sq)
        if sq-n==0.0 and sq in range(1,h+1):
            print(i,j,n)
