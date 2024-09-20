n, m = map(int, input().split())

# n * m 크기의 직사각형을 0으로 초기화
rects = [[0 for _ in range(m)] for _ in range(n)]

# 방향 (오른쪽, 아래, 왼쪽, 위)
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# 초기 위치와 방향 설정
x, y = 0, 0
dir_num = 0
current_char = 65  # 'A'의 ASCII 값

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

# 달팽이 모양으로 배열 채우기
for _ in range(n * m):
    rects[x][y] = current_char
    current_char += 1
    if current_char > 90:  # 'Z'의 ASCII 값은 90
        current_char = 65  # 다시 'A'로 돌아감
    
    # 다음 위치 계산
    nx, ny = x + dxs[dir_num], y + dys[dir_num]

    # 범위를 벗어나거나 이미 채워진 경우 방향 전환
    if not in_range(nx, ny) or rects[nx][ny] != 0:
        dir_num = (dir_num + 1) % 4
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

    # 다음 좌표로 이동
    x, y = nx, ny

# 결과 출력
for i in range(n):
    for j in range(m):
        print(chr(rects[i][j]), end=' ')
    print()