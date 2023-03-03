n = input('Enter a string : ')
num = int(input('Enter the index you want to remove: '))
s = n[0:num] + n[num+1:len(n)]
print('new string :',s)
