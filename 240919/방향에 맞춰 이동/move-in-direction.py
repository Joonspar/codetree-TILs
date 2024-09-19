# 상하좌우로 움직임.
# x,y = 1,5
# dir_num = 2 

# (1,5)에 위치하고 있고 , 방향번호가 2여서 서쪽으로 한 칸 이동 == > x - 1
# 방향 번호를 if로 묶고 nx,ny에 저장 
# if dir_num == 0:
#     nx,ny = x+1,y
#     ...
# dx,dy = [1,0,-1,0] , [0,-1,0,1]
# nx,ny = x+dx[dir_num] , y+dy[dir_num]

n = int(input())
nx , ny = 0,0
for i in range(n):
    direct,dist = input().split()
    dist = int(dist)
    if direct == 'N':
        nx , ny = nx , ny + dist 
    elif direct == 'E':
        nx , ny = nx + dist , ny
    elif direct == 'S':
        nx , ny = nx , ny - dist
    elif direct == 'W':
        nx , ny = nx - dist, ny 
    
print(nx,ny)