# 두 직사각형의 좌표를 입력받음
x1_1, y1_1, x2_1, y2_1 = map(int, input().split())
x1_2, y1_2, x2_2, y2_2 = map(int, input().split())

# 겹치는 부분의 좌표를 구함
overlap_x1 = max(x1_1, x1_2)
overlap_y1 = max(y1_1, y1_2)
overlap_x2 = min(x2_1, x2_2)
overlap_y2 = min(y2_1, y2_2)

# 첫 번째 직사각형의 전체 넓이 계산
first_area = (x2_1 - x1_1) * (y2_1 - y1_1)

# 겹치는 부분의 넓이 계산
if overlap_x1 < overlap_x2 and overlap_y1 < overlap_y2:
    overlap_area = (overlap_x2 - overlap_x1) * (overlap_y2 - overlap_y1)
else:
    overlap_area = 0

# 첫 번째 직사각형의 남은 부분의 넓이 계산
remaining_area = first_area - overlap_area

# 최소 직사각형의 넓이 구하기
# 남아 있는 부분을 포함하는 최소 직사각형의 범위
min_x = min(x1_1, x2_1)
max_x = max(x2_1, x1_2)
min_y = min(y1_1, y2_1)
max_y = max(y2_1, y1_2)

# 최소 직사각형의 넓이 계산
min_width = max_x - min_x
min_height = max_y - min_y

# 결과 출력
min_area = min_width * min_height
print(min_area)