n,b = map(int,input().split())
prices = [int(input()) for _ in range(n)]
ans = 0

for i in range(n):
    s = 0
    cnt = 0
    for j in range(n):
        if i == j:
            s += int(prices[j] / 2)
        s += prices[j]
        cnt += 1
        if s > b:
            break
    ans = max(ans,cnt)
print(ans)