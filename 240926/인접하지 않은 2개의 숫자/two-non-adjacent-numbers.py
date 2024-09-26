import sys
INT_MIN = -sys.maxsize
ans = INT_MIN
n = int(input())
li = list(map(int,input().split()))


for i in range(n):
    res = 0
    for j in range(i+1,n-1):
        res = li[i] + li[j+1]
        ans = max(ans,res)
print(ans)