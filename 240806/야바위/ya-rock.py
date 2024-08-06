n = int(input())
cnts = []
for i in range(n):
    a,b,c = map(int,input().split())
    cups = [0] * 3
    cups[i] = 1
    cnt = 0
    for j in range(n):
        temp = cups[a-1]
        cups[a-1] = cups[b-1]
        cups[b-1] = temp
        if cups[c-1] == 1:
            cnt += 1
    cnts.append(cnt)

print(cnts.index(max(cnts)))