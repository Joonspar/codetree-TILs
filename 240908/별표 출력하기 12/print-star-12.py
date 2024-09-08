def print_star_pattern(n):
    # 각 줄을 출력합니다.
    for i in range(n):
        line = []
        for j in range(n):
            if (i + j) % n == 0:
                line.append('*')
            else:
                line.append(' ')
        print(' '.join(line))

# 입력을 받아 처리
n = int(input().strip())
print_star_pattern(n)