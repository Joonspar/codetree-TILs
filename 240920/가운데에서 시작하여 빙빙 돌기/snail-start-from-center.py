n = int(input())

# n * n 크기의 정사각형을 0으로 초기화
rects = [[0 for _ in range(n)] for _ in range(n)]

# 방향 (오른쪽, 위, 왼쪽, 아래)
dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

# 시작 위치 (가운데)
x, y = n // 2, n // 2
dir_num = 0  # 오른쪽 방향부터 시작
rects[x][y] = 1  # 처음 숫자는 1

# 2부터 n*n까지 숫자를 채워넣기
for i in range(2, n * n + 1):
    # 현재 방향으로 이동할 다음 위치 계산
    nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    # 배열의 범위를 벗어나거나 이미 숫자가 채워져 있으면 방향 전환
    if nx < 0 or nx >= n or ny < 0 or ny >= n or rects[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4  # 오른쪽, 위, 왼쪽, 아래 순으로 전환
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
    
    # 다음 좌표로 이동하고 숫자 채우기
    x, y = nx, ny
    rects[x][y] = i

# 결과 출력
for row in rects:
    print(' '.join(map(str, row)))