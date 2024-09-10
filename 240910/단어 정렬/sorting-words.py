n = int(input())
li = []
for _ in range(n):
    li.append(input())

li.sort()
for elem in li:
    print(elem)