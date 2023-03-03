n = input('Enter a string :')
s = ""
for i in range(len(n)):
    if n[i]==' ':
        s+='-'
    else:
        s+=n[i]
print(s)
