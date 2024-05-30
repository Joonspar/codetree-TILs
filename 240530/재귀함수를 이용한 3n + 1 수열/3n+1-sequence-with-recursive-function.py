n = int(input())
cnt = 0

def add(n, cnt):
    if n == 1:
        return cnt
    elif n % 2 == 1:
        cnt += 1
        return add(3 * n + 1, cnt)
    else:
        cnt += 1
        return add(n // 2, cnt)

print(add(n, cnt))