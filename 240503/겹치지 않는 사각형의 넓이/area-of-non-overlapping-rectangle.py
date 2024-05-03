OFFSET = 1000
A = [
    [0 for _ in range(2005)]
    for _ in range(2005)
]

# 직사각형을 입력받고 color로 표시하는 함수
def color(c):
    x1,y1,x2,y2 = map(lambda x: int(x)+OFFSET, input().split())

    for x in range(x1,x2):
        for y in range(y1,y2):
            A[x][y] = c

color(1)
color(2)
color(3)

answer = 0
for row in A:
    for elem in row:
        if elem in (1,2):
            answer += 1

print(answer)