# 바라보고있는 방향을 기준으로 회전
# x = 1 , y = 5 북쪽으로 바라봄
# == > x = 2 , y = 5
# dir_num = ??
# 시계 방향 90도 회전을 구현...
# dir_num = (dir_num + 1) % 4
# dx = [1,-1,0,0]
# dy = [0,0,-1,1]

x , y = 0,0
dir_num = 3
dx = [1,0,-1,0]
dy = [0,-1,0,1]
commend = list(input())
n = len(commend)

for i in range(n):
    if commend[i] == 'L':
        dir_num = (dir_num -1) % 4
    elif commend[i] =='R':
        dir_num = (dir_num + 1) % 4
    elif commend[i] == 'F':
        x , y = x + dx[dir_num] ,y + dy[dir_num]
print(x,y)