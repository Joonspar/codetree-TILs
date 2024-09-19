mapper = {
    'N': 0,
    'E': 1,
    'S': 2,
    'W': 3
}

x, y = 0, 0
dxs = [-1, 0, 1, 0]  # N, E, S, W 방향에 대한 x 변화량
dys = [0, 1, 0, -1]  # N, E, S, W 방향에 대한 y 변화량
time = 0
n = int(input())

for _ in range(n):
    direct, dist = input().split()
    dist = int(dist)
    direct = mapper[direct]
    # 현재 좌표를 dist 만큼 이동
    for _ in range(dist):
        x += dxs[direct]
        y += dys[direct]
        time += 1
        # (0, 0)에 도착하면 시간 출력 후 종료
        if x == 0 and y == 0:
            print(time)
            exit()

# 루프가 끝나도 (0, 0)에 도달하지 못했다면 -1 출력
print(-1)