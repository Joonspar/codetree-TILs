x1_1, y1_1, x2_1, y2_1 = map(int, input().split())
x1_2, y1_2, x2_2, y2_2 = map(int, input().split())

first_x = x2_1 - x1_1
first_y = y2_1 - y1_1
first_area = first_x * first_y

second_x = x2_2 - x1_2
second_y = y2_2 - y2_1
second_area = second_x * second_y

if y2_1 > y2_2 or y1_1 < y2_1:
    print(first_area)
else:
    print(second_area)