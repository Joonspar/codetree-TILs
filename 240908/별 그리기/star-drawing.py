n = int(input())

# 윗부분 (중앙 포함)
for i in range(n):
    # 앞에 들어가는 공백: n - i - 1
    print(" " * (n - i - 1), end='')
    # 별의 개수: 2*i + 1
    print("*" * (2 * i + 1))

# 아랫부분
for i in range(n - 1):
    # 앞에 들어가는 공백: i + 1
    print(" " * (i + 1), end='')
    # 별의 개수: 2*(n-i-2) + 1
    print("*" * (2 * (n - i - 2) + 1))