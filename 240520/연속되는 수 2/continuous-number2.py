n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
cnt = 1
arr2 = []
for i in range(n):
    if i == 0 or arr[i] == arr[i-1]:
        cnt += 1
    else:
        arr2.append(cnt)
        cnt = 1
print(max(arr2))