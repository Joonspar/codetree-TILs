n = int(input())
li = list(map(int,input().split()))
li2 = []
for i in range(len(li)):
    if li[i] % 2 == 0:
        li2.append(li[i])
print(*li2[::-1])