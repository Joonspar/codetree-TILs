n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_distance_squared = float('inf')  # 초기값을 무한대로 설정

# 모든 점 쌍에 대해 거리 제곱 계산
for i in range(n):
    for j in range(i + 1, n):
        x1, y1 = points[i]
        x2, y2 = points[j]
        distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
        min_distance_squared = min(min_distance_squared, distance_squared)

print(min_distance_squared)