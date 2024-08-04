n, b = map(int, input().split())
cost = []
for _ in range(n):
    a, c = map(int, input().split())
    cost.append([a,c])
count = [0] * n
cost.sort()
for i in range(n):
    total = 0
    for j in range(n):
        if i == j:
            total += (cost[j][0] // 2) + cost[j][1]
        else:
            total += cost[j][0] + cost[j][1]
        if total <= b:
            count[i] += 1
        else:
            break
print(max(count))