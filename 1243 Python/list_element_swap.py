l =[1,2,3,4,5,6,7]
l1 = l.copy()
n1 = int(input('Enter position 1: '))
n2 = int(input('Enter position 2: '))
temp = l[n1-1]
l[n1-1] = l[n2-1]
l[n2-1] = temp

print('List before element swap:',l1)
print('List after element swap:',l)
