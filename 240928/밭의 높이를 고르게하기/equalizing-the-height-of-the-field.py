import sys
ans = sys.maxsize
n,h,t = map(int,input().split())
lands = list(map(int,input().split()))


for i in range(n-t+1):
    cost = 0
    for j in range(i,i+t):
        cost += abs(h-lands[j])
    ans = min(cost,ans)
print(ans)