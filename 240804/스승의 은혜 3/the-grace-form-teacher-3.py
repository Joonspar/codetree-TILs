n, b = map(int, input().split())
present = []
ship = []
for _ in range(n):
    a, c = map(int, input().split())
    present.append(a)
    ship.append(c)

count = [0] * n

for i in range(n):
    total = 0
    for j in range(n):
        if i == j:
            total += (present[j] // 2) + ship[j]
        else:
            total += present[j] + ship[j]
        
        if total <= b:
            count[i] += 1
        else:
            break  # 무게 제한을 넘으면 더 이상 계산할 필요 없음

print(max(count))