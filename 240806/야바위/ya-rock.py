n = int(input())
games = [
    list(map(int,input().split()))
    for _ in range(n)
]
cnts = []
for i in range(3):
    cnt = 0
    cups = [0] * 3
    for tries in games:
        cups[i] = 1
        temp = cups[tries[0]-1]
        cups[tries[0]-1] = cups[tries[1]-1]
        cups[tries[1]-1] = temp
        if cups[tries[2]-1] == 1:
            cnt += 1
    cnts.append(cnt)
print(cnts.index(max(cnts))+1)