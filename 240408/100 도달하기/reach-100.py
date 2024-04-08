n = int(input())

li = [1,n]
while True:
    if li[-1] > 100:
        break
    li.append(li[-2]+li[-1])
print(*li)