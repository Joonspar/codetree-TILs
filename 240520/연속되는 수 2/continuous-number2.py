n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
cnt = 1
arr2 = []
for i in range(1,n):
    if arr[i] == arr[i-1]:
        cnt += 1
    elif i == 0 or arr[i] != arr[i-1]: 
        arr2.append(cnt)
        cnt = 1
print(max(arr2))