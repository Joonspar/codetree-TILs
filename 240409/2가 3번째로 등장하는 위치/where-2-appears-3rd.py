n = int(input())
li = list(map(int,input().split()))
cnt = 0

for i in li:
    if i == 2:
        cnt += 1
    elif cnt == 3:
        print(li.index(i))
        break