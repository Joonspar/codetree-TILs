# 입력 받기
N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

# x 좌표별로 y 좌표들을 모은다
x_points = {}
# y 좌표별로 x 좌표들을 모은다
y_points = {}

for x, y in points:
    if x not in x_points:
        x_points[x] = []
    if y not in y_points:
        y_points[y] = []
    x_points[x].append(y)
    y_points[y].append(x)

max_area = 0

# x축에 평행한 변을 기준으로 삼각형의 넓이 계산
for x in x_points:
    ys = sorted(x_points[x])
    for i in range(len(ys)):
        for j in range(i + 1, len(ys)):
            y1, y2 = ys[i], ys[j]
            height = y2 - y1
            # y축에 평행한 변을 찾아야 함
            for y in (y1, y2):
                if y in y_points:
                    xs = y_points[y]
                    for x_other in xs:
                        if x_other != x:
                            base = abs(x_other - x)
                            area = base * height
                            if area > max_area:
                                max_area = area

# 결과 출력 (최대 넓이에 2를 곱한 값)
print(max_area)