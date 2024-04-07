a = list(map(int,input().split()))
li = []
for i in range(len(a)):
    if a[i] != 0:
        li.append(a[i])
    else:
        break
print(*li[::-1])