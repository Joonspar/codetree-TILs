directions = {'E':0,'S':1,'W':2,'N':3}
n = int(input())
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
x , y = 0 , 0

for i in range(n):
    direction , distances = input().split()
    distances = int(distances)
    d = directions[direction]
    x += distances * dx[d]
    y += distances * dy[d]

print(x,y)