n = int(input())
heights = []
for _ in range(n):
    heights.append(int(input()))

heights.sort()
min_cost = float('inf')
max_gap = 17

# 구간의 시작 높이를 정합니다.
for start in range(0, 84):  # 0부터 83까지 시도 (최대 높이가 100이므로)
    end = start + max_gap
    cost = 0
    for h in heights:
        if h < start:
            cost += (start - h) ** 2
        elif h > end:
            cost += (h - end) ** 2
    min_cost = min(min_cost, cost)

print(min_cost)