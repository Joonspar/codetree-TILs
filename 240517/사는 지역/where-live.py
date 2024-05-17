class info:
    def __init__(self, name, street, loc):
        self.name = name
        self.street = street
        self.loc = loc

k = int(input())

array = []
for _ in range(k):
    n, s, l = map(str, input().split())
    array.append(info(n, s, l))

idx = 0
for i in range(1, k):
    if array[idx].name < array[i].name: # 저장한 이름을 비교해보며 해당 이름이 더 뒤의 순서일경우 idx 변경
        idx = i

print(f"name {array[idx].name}")
print(f"addr {array[idx].street}")
print(f"city {array[idx].loc}")