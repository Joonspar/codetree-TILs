n = int(input())
games = [
    list(input().split())
    for _ in range(n)
]
cnta , cntb , fame = 0,0,0

for game in games:
    game[1] = int(game[1])
    if game[0] == 'A':
        cnta += game[1]
        fame += 1
    elif game[0] == 'B':
        cntb += game[1]

print(fame)