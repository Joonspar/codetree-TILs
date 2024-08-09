n,k = map(int,input().split())
arr = list(map(int,input().split()))
ans = 10000
max_num = 10000
for i in range(1,max_num+1):
    s = 0
    for j in range(1,n):
        if abs(arr[j] - arr[j-1]) > k:
            if arr[j] > arr[j-1]:
                arr[j] -= i
                s += i
            else:
                arr[j-1] += i
                s += i
    ans = min(ans,s)
print(ans)