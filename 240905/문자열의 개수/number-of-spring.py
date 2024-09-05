li = []
while True:
    a = input()
    if a == '0':
        break
    li.append(a)

print(len(li))
for i in range(len(li)):
    if i % 2 == 0:
        print(li[i])