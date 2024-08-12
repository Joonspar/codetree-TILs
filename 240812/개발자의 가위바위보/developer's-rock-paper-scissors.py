n = int(input())
games = [
    list(map(int,input().split()))
    for _ in range(n)
]
wins = [0] * 6
for rsp in games:
    if (rsp[0] == 1 and rsp[1] == 3) or (rsp[0] == 2 and rsp[1] == 1) or (rsp[0] == 3 and rsp[1] == 2):
        wins[0] += 1
    elif (rsp[0] == 1 and rsp[1] == 2) or (rsp[0] == 2 and rsp[1] == 3) or (rsp[0] == 3 and rsp[1] == 1):
        wins[1] += 1
    elif (rsp[0] == 1 and rsp[1] == 2) or (rsp[0] == 2 and rsp[1] == 3) and (rsp[0] == 3 and rsp[1] == 1):
        wins[2] += 1         
    elif (rsp[0] == 1 and rsp[1] == 3) or (rsp[0] == 2 and rsp[1] == 1) and (rsp[0] == 3 and rsp[1] == 2):
        wins[3] += 1
    elif (rsp[0] == 1 and rsp[1] == 3) or (rsp[0] == 2 and rsp[1] == 1) and (rsp[0] == 3 and rsp[1] == 2):
        wins[4] += 1
    elif (rsp[0] == 1 and rsp[1] == 2) or (rsp[0] == 2 and rsp[1] == 3) and (rsp[0] == 3 and rsp[1] == 1):
        wins[5] += 1

print(max(wins))