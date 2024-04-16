li = []
for _ in range(10):
    s = input()
    li.append(s)

c = input()
for i in range(10):
    if li[i][-1] == c:
        print(li[i])