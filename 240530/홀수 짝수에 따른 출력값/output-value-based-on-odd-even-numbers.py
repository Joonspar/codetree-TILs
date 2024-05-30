n = int(input())

def fn(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return n + fn(n-2)

print(fn(n))