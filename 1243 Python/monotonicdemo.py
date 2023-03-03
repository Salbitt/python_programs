arr = []
print('Enter elements of array: ')
for i in range(0,5):
    arr.append(int(input()))
ar1 = arr.copy()
ar2 = arr.copy()
ar1.sort()
ar2.sort(reverse = True)

if ar1==arr or ar2==arr:
    print(arr,'is monotonic')
else:
    print(arr,' is not monotonic')
