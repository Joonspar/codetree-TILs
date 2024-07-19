def check_winner(board):
    # 방향 벡터: (가로, 세로, 대각선 좌상-우하, 대각선 우상-좌하)
    directions = [(0, 1), (1, 0), (1, 1), (1, -1)]
    
    def in_bounds(x, y):
        return 0 <= x < 19 and 0 <= y < 19
    
    def get_middle_position(x, y, dx, dy):
        return x + 2*dx + 1, y + 2*dy + 1
    
    for x in range(19):
        for y in range(19):
            if board[x][y] != 0:
                for dx, dy in directions:
                    count = 1
                    nx, ny = x + dx, y + dy
                    while in_bounds(nx, ny) and board[nx][ny] == board[x][y]:
                        count += 1
                        if count == 5:
                            # 다섯 개가 연속된 경우
                            if in_bounds(nx + dx, ny + dy) and board[nx + dx][ny + dy] == board[x][y]:
                                break  # 여섯 개가 연속된 경우는 무시
                            mx, my = get_middle_position(x, y, dx, dy)
                            return board[x][y], (mx + 1, my + 1)
                        nx += dx
                        ny += dy
    return 0, None

# 바둑판 입력 받기
board = []
for _ in range(19):
    row = list(map(int, input().split()))
    board.append(row)

winner, position = check_winner(board)
print(winner)
if winner != 0:
    print(position[0]-1, position[1]-1)