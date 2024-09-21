import sys
INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize
ans = INT_MIN
n,k = map(int,input().split())
li = list(map(int,input().split()))
for i in range(n-k+1):
    s = 0
    for j in range(i,i+k):
        s += li[j]
    ans = max(ans,s)
print(ans)