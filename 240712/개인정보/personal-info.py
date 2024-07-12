class People:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = int(height)
        self.weight = float(weight)

# 키 기준으로 내림차순

students = []

for i in range(5):
    name, height, weight = list(input().split())
    students.append(People(name,height,weight))

students.sort(key = lambda x: x.name)
print('name')
for elem in students:
    print(elem.name, elem.height, elem.weight)
print()

students.sort(key = lambda x: -x.height)
print('height')
for elem in students:
    print(elem.name, elem.height, elem.weight)