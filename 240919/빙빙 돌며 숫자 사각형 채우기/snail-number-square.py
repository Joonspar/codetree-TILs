# 회전을 하는 경우
# 1 . 격자를 벗어나면 시계 방향으로 바꾼다.
# 2. 이미 그 칸에 숫자가 넣어져있으면 시계방향으로 회전.

n,m = map(int,input().split())
rects = [
    [0 for _ in range(m)]
    for _ in range(n)
]
dxs , dys = [0,1,0,-1] , [1,0,-1,0]
x , y = 0,0
dir_num = 0
rects[x][y] = 1
def in_range(x,y):
    return 0<= x < n and 0<= y < m

for i in range(2,n*m+1):
    nx,ny = x + dxs[dir_num] , y + dys[dir_num]

    if not in_range(nx,ny) or rects[nx][ny] != 0:
        dir_num = (dir_num+1) % 4

    x, y = x + dxs[dir_num] , y + dys[dir_num]
    rects[x][y] = i

for i in range(n):
    for j in range(m):
        print(rects[i][j],end=' ')
    print()