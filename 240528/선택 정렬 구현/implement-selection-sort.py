n = int(input())
arr = list(map(int,input().split()))
small = 100
for i in range(n):
    small = i
    for j in range(i+1,n):
        if arr[j] < arr[small]:
            small = j
    tmp = arr[i]
    arr[i] = arr[small]
    arr[small] = tmp
print(*arr)