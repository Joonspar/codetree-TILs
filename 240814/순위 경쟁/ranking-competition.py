n = int(input())
games = [
    list(input().split())
    for _ in range(n)
]
current_hall_of_fame = {"A", "B", "C"}  # 처음에는 A, B, C 모두가 명예의 전당에 올라감
cnta, cntb, cntc, fame = 0, 0, 0, 0

for game in games:
    game[1] = int(game[1])
    
    # 각 학생의 점수 변동
    if game[0] == 'A':
        cnta += game[1]
    elif game[0] == 'B':
        cntb += game[1]
    elif game[0] == 'C':
        cntc += game[1]
    
    # 현재 점수 확인
    max_score = max(cnta, cntb, cntc)
    
    # 현재 명예의 전당 조합 계산
    new_hall_of_fame = set()
    if cnta == max_score:
        new_hall_of_fame.add('A')
    if cntb == max_score:
        new_hall_of_fame.add('B')
    if cntc == max_score:
        new_hall_of_fame.add('C')
    
    # 명예의 전당 조합이 변경되었는지 확인
    if new_hall_of_fame != current_hall_of_fame:
        fame += 1
        current_hall_of_fame = new_hall_of_fame

# 결과 출력
print(fame)