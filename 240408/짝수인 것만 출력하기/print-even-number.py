n = int(input())
li = list(map(int,input().split()))
l2 = []
for i in range(n):
    if li[i] % 2 == 0:
        l2.append(li[i])
print(*l2)