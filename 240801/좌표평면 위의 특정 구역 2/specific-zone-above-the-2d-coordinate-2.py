n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
min_size = float('inf')  # 초기값을 무한대로 설정

for i in range(n):
    # 현재 제거할 점을 제외한 나머지 점들로 새로운 직사각형의 범위 계산
    remaining_points = [arr[j] for j in range(n) if j != i]

    # 남은 점들의 x와 y 값의 최소값과 최대값을 계산
    x_min = min(p[0] for p in remaining_points)
    x_max = max(p[0] for p in remaining_points)
    y_min = min(p[1] for p in remaining_points)
    y_max = max(p[1] for p in remaining_points)

    # 직사각형의 넓이를 계산
    width = x_max - x_min
    height = y_max - y_min
    size = width * height

    # 최소 넓이를 업데이트
    min_size = min(min_size, size)

print(min_size)