class Student:
    def __init__(self, height, weight, index):
        self.height = int(height)
        self.weight = int(weight)
        self.index = index

# 입력 받기
n = int(input().strip())
students = []

for i in range(n):
    height, weight = map(int, input().strip().split())
    students.append(Student(height, weight, i + 1))

# 정렬하기: 키가 큰 순, 키가 같으면 몸무게 큰 순, 둘 다 같으면 번호 작은 순
students.sort(key=lambda x: (-x.height, -x.weight, x.index))

# 결과 출력
for student in students:
    print(student.height, student.weight, student.index)