l= [12,34,5,3,2,3,12,3,4,12,34]
n = 12

lc = l.copy()#copying list
lc.reverse()#reversing list
print('Original list:',l)
print('Reversed list:',lc)
print('No of times',n,'appears in list:',l.count(n))
print('First occurence of',n,':',l.index(n))
l.insert(0,1)
l.pop(1)
l.remove(3)
l.sort()
print('Modified list:',l)
l.clear()
print('Final list:',l)
