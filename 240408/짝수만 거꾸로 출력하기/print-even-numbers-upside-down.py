n = int(input())
li = []
li2 = []
for i in range(n):
    li.append(int(input()))

for i in range(len(li)):
    if li[i] % 2 == 0:
        li2.append(li[i])
print(*li[::-1])