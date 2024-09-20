import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize
ans = INT_MIN
n = int(input())
li = list(map(int,input().split()))

for i in range(n):
    s = 0
    for j in range(i+2,n):
        s = li[i] + li[j]
        ans = max(s,ans)
print(ans)