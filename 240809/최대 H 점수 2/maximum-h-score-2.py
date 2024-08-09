n,l = map(int,input().split())
arr = list(map(int,input().split()))
ans = 0
for h in range(101):
    cnt = 0
    for k in range(n):
        for _ in range(l):
            arr[k] += l
    for j in range(n):
        if arr[j] >= h:
            cnt += 1
        if cnt == h:
            ans = max(cnt,h)
        arr[k] -= l
print(ans)