import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize
n = int(input())
ans = INT_MIN
coins = [
    list(map(int,input().split()))
    for _ in range(n)
]

for i in range(n):
    cnt = 0
    for j in range(n-2):
        cnt = coins[i][j] + coins[i][j+1] + coins[i][j+2]
    ans = max(ans,cnt)
print(ans)