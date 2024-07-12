class Person:
    def __init__(self,name,height,weight):
        self.name = name
        self.height = int(height)
        self.weight = int(weight)

n = int(input())
students = []
for i in range(5):
    name, height, weight = list(input().split())
    students.append(Person(name,height,weight))

students.sort(key = lambda x:(x.height,-x.weight))

for elem in students:
    print(elem.name, elem.height, elem.weight)