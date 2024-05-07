s = input()
arr = list(s)
for i in range(len(arr)):
    if arr[0] == arr[i]:
        arr[i] = arr[1]
    if arr[1] == arr[i]:
        arr[i] = arr[0]
a = ''.join(arr)
print(a)