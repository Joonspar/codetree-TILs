# 회전 , 방향 이동
# 북쪽으로 향하고있음. 
# 시계 방향 회전 L, 반대 방향 R
dx,dy = [1,-1,0,0] , [0,0,-1,1]
commands = input()
x,y = 0,0
dirn = 3

for i in range(len(commands)):
    if commands[i] == 'L':
        if dirn == 0:
            dirn = 3 
        elif dirn == 1:
            dirn = 2
        elif dirn == 2:
            dirn = 0
        else:
            dirn = 1
    elif commands[i] == 'R':
        if dirn == 0:
            dirn = 2
        elif dirn == 1:
            dirn = 3
        elif drin == 2:
            dirn = 1
        else:
            dirn = 0
    elif commands[i] == 'F':
        x = x + dx[dirn]
        y = y + dy[dirn]

print(x,y)