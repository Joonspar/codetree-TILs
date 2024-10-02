n,b = map(int,input().split())
prices = [int(input()) for _ in range(n)]
ans = 0
prices.sort()
for i in range(n):
    s = 0
    cnt = 0
    for j in range(n):
        if i == j:
            s += int(prices[j] / 2)
        else:
            s += prices[j]
        if s <= b:
            cnt += 1
        else:
            break
    ans = max(ans,cnt)
print(ans)