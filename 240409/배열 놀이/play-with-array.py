n, q = map(int, input().split())
elements = list(map(int, input().split()))

for _ in range(q):
    query = input().split()
    if query[0] == '1':
        index = int(query[1]) - 1
        print(elements[index])
    elif query[0] == '2':
        value = int(query[1])
        index = -1
        for i in range(n):
            if elements[i] == value:
                index = i + 1
                break
        print(index)
    elif query[0] == '3':
        start = int(query[1]) - 1
        end = int(query[2])
        print(*elements[start:end])