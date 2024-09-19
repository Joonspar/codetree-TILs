n,m = map(int,input().split())
x,y = 0,0
rects = [
    [0 for _ in range(m)]
    for _ in range(n)
]
dir_num = 1
dys,dxs = [1,0,-1,0] , [0,1,0,-1] 
def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

rects[x][y] = 1
for i in range(2,n*m+1):
    nx,ny = x + dxs[dir_num] , y + dys[dir_num]
    if not in_range(nx,ny) or rects[nx][ny] != 0:
        dir_num = (dir_num-1) % 4
    x, y = x + dxs[dir_num] , y + dys[dir_num]
    rects[x][y] = i

for i in range(n):
    for j in range(m):
        print(rects[i][j],end=' ')
    print()