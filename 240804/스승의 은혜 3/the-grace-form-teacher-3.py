n, b = map(int, input().split())
cost = []
for _ in range(n):
    a, c = map(int, input().split())
    cost.append([a,c])
count = []
cost = sorted(cost,key = lambda x: sum(x))
for i in range(n):
    total = 0
    cnt = 0
    for j in range(n):
        if i == j:
            total += (cost[j][0] // 2) + cost[j][1]
        else:
            total += cost[j][0] + cost[j][1]
        if total <= b:
            cnt += 1
        else:
            count.append(cnt)
            break
print(max(count))