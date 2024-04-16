li = []
for _ in range(10):
    s = input()
    li.append(s)
cnt = 0
c = input()
for i in range(10):
    if li[i][-1] == c:
        cnt += 1
        if cnt >= 1:
            print(li[i])
if cnt == 0:
    print('None')