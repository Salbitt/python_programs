n = input('Enter a string :')
s = ""
for i in range(len(n)):
    if n[i]=='a' or n[i]=='A':
        s = s +'$'
    else:
        s = s + n[i]
print(s)
