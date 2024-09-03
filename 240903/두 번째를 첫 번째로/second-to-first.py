li = list(input())
n = len(li)

for i in range(2,n):
    if li[i] == li[1]:
        li[i] = li[0]
li[1] = li[0]
print(*li,sep='')