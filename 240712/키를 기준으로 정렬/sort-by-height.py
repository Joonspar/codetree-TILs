class Height:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = int(height)
        self.weight = int(weight)

n = int(input())
arr = [list(input().split()) for _ in range(n)]
people = [Height(name, height, weight) for name, height, weight in arr]

people.sort(key = lambda x: x.height)

for elem in people:
    print(elem.name, elem.height, elem.weight)