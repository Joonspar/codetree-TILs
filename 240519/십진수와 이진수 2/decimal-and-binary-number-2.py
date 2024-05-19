n = input()

arr = list(n)
for i in range(len(arr)):
    arr[i] = int(arr[i])
s = 0
for i in range(len(arr)-1,-1,-1):
    s += arr[i] * (2**(len(arr)-i-1))

s *= 17
arr2 = []
while s>=2:
    arr2.append(s%2)
    s //= 2
arr2.append(s)

print(*arr2[::-1],sep='')