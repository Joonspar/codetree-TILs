s1 = input()
s2 = input()
arr1 = list(s1)
arr1.sort()
arr2 = list(s2)
arr2.sort()

if arr1 == arr2:
    print('Yes')
else:
    print('No')