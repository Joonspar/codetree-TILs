import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize
ans = INT_MIN
n = int(input())
arr = [
    list(map(int,input().split())) for _ in range(n)
]

for i in range(n):
    cnt = 0
    for j in range(n-2):
        for k in range(n):
            for l in range(n-2):
                if i == k and abs(j-l) <= 2:
                    continue
                cnt = arr[i][j] + arr[i][j+1] + arr[i][j+2]
                cnt1 = arr[k][l] + arr[k][l+1] + arr[k][l+2]
                ans = max(ans,cnt+cnt1)
print(ans)