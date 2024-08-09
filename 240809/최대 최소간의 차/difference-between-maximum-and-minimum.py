n,k = map(int,input().split())
arr = list(map(int,input().split()))
ans = 10000
max_num = 10000
for i in range(1,k):
    cost = 1
    for j in range(1,n):
        if abs(arr[j] - arr[j-1]) > k:
            if arr[j] > arr[j-1]:
                arr[j] -= i
                cost += i
            else:
                arr[j-1] += i
                cost += i
    ans = min(ans,cost)
print(ans)