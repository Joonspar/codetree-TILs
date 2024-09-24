import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize
ans = INT_MIN

n = int(input())
board = [
    list(map(int,input().split()))
    for _ in range(n)
]

for i in range(n):
    for j in range(n-2):
        res = board[i][j] + board[i][j+1] + board[i][j+2]
    ans = max(ans,res)
print(ans)