import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
checkpoints = []

# 입력 데이터 처리
idx = 1
for i in range(n):
    x = int(data[idx])
    y = int(data[idx + 1])
    checkpoints.append((x, y))
    idx += 2

# 택시 거리 계산 함수
def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# 기본 경로의 총 거리 계산
total_distance = 0
for i in range(1, n):
    total_distance += manhattan_distance(checkpoints[i-1], checkpoints[i])

# 체크포인트 하나를 건너뛰었을 때의 최소 거리 계산
min_distance = total_distance
for i in range(1, n-1):
    skip_distance = total_distance
    skip_distance -= manhattan_distance(checkpoints[i-1], checkpoints[i])
    skip_distance -= manhattan_distance(checkpoints[i], checkpoints[i+1])
    skip_distance += manhattan_distance(checkpoints[i-1], checkpoints[i+1])
    if skip_distance < min_distance:
        min_distance = skip_distance

# 결과 출력
print(min_distance)