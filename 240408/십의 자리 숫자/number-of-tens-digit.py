# 입력 받기
numbers = list(map(int, input().split()))

# 각 십의 자리의 숫자를 저장할 딕셔너리 생성
count = {}

# 0이 나올 때까지 입력된 수의 십의 자리 수 카운트
for num in numbers:
    if num == 0:
        break
    tens_digit = num // 10
    if tens_digit in count:
        count[tens_digit] += 1
    else:
        count[tens_digit] = 1

# 결과 출력
for i in range(1, 10):
    print(f"{i} - {count.get(i, 0)}")