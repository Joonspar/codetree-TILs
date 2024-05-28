n = int(input())
arr = list(map(int,input().split()))

for i in range(1,n):
    j = i-1
    k = arr[i]
    while j >= 0 and arr[j] > k:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = k

print(*arr)