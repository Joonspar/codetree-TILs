def split_and_print(numbers):
    # 모든 숫자를 하나의 문자열로 합치기
    combined = ''.join(numbers)
    
    # 5개씩 출력
    for i in range(0, len(combined), 5):
        print(combined[i:i+5])

# 입력 받기
n = int(input())  # 문자열 개수
numbers = input().split()  # 공백으로 나눠진 숫자들

split_and_print(numbers)