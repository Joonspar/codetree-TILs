import sys
INT_MAX = sys.maxsize
ans = INT_MAX
n,s = map(int,input().split())
arr = list(map(int,input().split()))

for i in range(n):
    for j in range(n):
        res = 0
        if i == j:
            continue
        for k in range(n):
            if j == k or i == k:
                continue
            res += arr[k]
        res = abs(res-s)
        ans = min(res,ans)
print(ans)