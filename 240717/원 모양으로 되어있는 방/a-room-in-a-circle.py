def min_total_distance(N, people):
    # 각 방에서 출발하는 경우에 대해 총 이동 거리를 저장할 리스트
    total_distances = [0] * N

    # 각 방에서 출발하는 경우의 총 이동 거리 계산
    for start in range(N):
        total_distance = 0
        for i in range(N):
            distance = (i - start + N) % N
            total_distance += distance * people[i]
        total_distances[start] = total_distance

    # 최솟값을 찾아 출력
    return min(total_distances)

# 입력 처리
N = int(input().strip())
people = [int(input().strip()) for _ in range(N)]

# 최소 이동 거리 계산
result = min_total_distance(N, people)
print(result)