n,m = map(int,input().split())
sections = [
    list(map(int,input().split()))
    for _ in range(m)
]
ans = 0
cnts = []
for i in range(1,n+1):
    for j in range(1,n+1):
        cnt = 0
        for k in range(m):
            if i in sections[k] and j in sections[k]:
                cnt += 1
        ans = max(cnt,ans)
print(ans)