from itertools import permutations

# 입력 받기
N = int(input())
conditions = [input().split() for _ in range(N)]

# 가능한 모든 1부터 9까지의 세자리 수 생성
possible_numbers = list(permutations(range(1, 10), 3))

# 조건을 만족하는지 확인하는 함수
def check_condition(number, guess, count1, count2):
    count_1 = 0
    count_2 = 0
    for i in range(3):
        if number[i] == guess[i]:
            count_1 += 1
        elif guess[i] in number:
            count_2 += 1
    return count_1 == count1 and count_2 == count2

# 가능한 수의 개수를 세기
valid_count = 0

for number in possible_numbers:
    valid = True
    for condition in conditions:
        guess = tuple(map(int, condition[0]))
        count1 = int(condition[1])
        count2 = int(condition[2])
        if not check_condition(number, guess, count1, count2):
            valid = False
            break
    if valid:
        valid_count += 1

# 결과 출력
print(valid_count)