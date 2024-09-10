n = int(input())
li = list(map(int,input().split()))

for i in range(n):
    for j in range(i,n):
        if li[i] >= li[j]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
print(*li)

for i in range(n):
    for j in range(i,n):
        if li[i] < li[j]:
            temp = li[i]
            li[i] = li[j]
            li[j] = temp
print(*li)