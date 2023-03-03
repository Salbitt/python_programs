import array as a
arr = a.array('b',[1,3,5,7,9,11])

sum = 0

for i in range(0,len(arr)):
    sum+=arr[i]

print('Sum of array:',sum)
