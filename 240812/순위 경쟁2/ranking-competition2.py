n = int(input())
games = [
    list(input().split())
    for _ in range(n)
]
cnta , cntb , fame = 0,0,0
current_hall_of_fame = {"A", "B"}

for game in games:
    game[1] = int(game[1])
    if game[0] == 'A':
        cnta += game[1]

    elif game[0] == 'B':
        cntb += game[1]
    
    if cnta > cntb:
        new_hall_of_fame = {"A"}
    elif cntb > cnta:
        new_hall_of_fame = {"B"}
    else:
        new_hall_of_fame = {"A", "B"}
    
    if new_hall_of_fame != current_hall_of_fame:
        fame += 1
        current_hall_of_fame = new_hall_of_fame
print(fame)