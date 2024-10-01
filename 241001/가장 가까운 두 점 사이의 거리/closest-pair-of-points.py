import sys
ans = sys.maxsize
n = int(input())
points = [
    list(map(int,input().split()))
    for _ in range(n)
]

for i in range(n):
    for j in range(i+1,n):
        dist = (abs(points[j][0] - points[i][0]) ** 2 + abs(points[j][1] - points[i][1]) ** 2)
        ans = min(dist,ans)
print(ans)