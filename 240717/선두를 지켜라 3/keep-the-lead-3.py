def find_leader_changes(n, m, movements_a, movements_b):
    MAX_T = 1000000
    pos_a, pos_b = [0] * (MAX_T + 1), [0] * (MAX_T + 1)

    # 기록 A의 위치
    time_a = 1
    for v, t in movements_a:
        for _ in range(t):
            pos_a[time_a] = pos_a[time_a - 1] + v
            time_a += 1

    # 기록 B의 위치
    time_b = 1
    for v, t in movements_b:
        for _ in range(t):
            pos_b[time_b] = pos_b[time_b - 1] + v
            time_b += 1

    # A와 B 중 더 앞서 있는 경우를 확인합니다.
    leader, ans = 0, 0
    for i in range(1, time_a):
        if pos_a[i] > pos_b[i]:
            if leader != 1:
                ans += 1
                leader = 1
        elif pos_b[i] > pos_a[i]:
            if leader != 2:
                ans += 1
                leader = 2
        else:
            if leader != 3:
                ans += 1
                leader = 3

    return ans

# 입력
n, m = map(int, input().split())
movements_a = [tuple(map(int, input().split())) for _ in range(n)]
movements_b = [tuple(map(int, input().split())) for _ in range(m)]

# 명예의 전당 변경 횟수 계산
result = find_leader_changes(n, m, movements_a, movements_b)
print(result)