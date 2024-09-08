n = int(input())

# 상단 패턴
for i in range(n):
    # 공백을 출력
    print(' ' * (n - i - 1), end='')
    # '*'을 출력 (마지막 공백을 제거)
    print('* ' * (i + 1),end='')
    print()

# 하단 패턴
for i in range(n - 2, -1, -1):
    # 공백을 출력
    print(' ' * (n - i - 1), end='')
    # '*'을 출력 (마지막 공백을 제거)
    print('* ' * (i + 1),end='')
    print()