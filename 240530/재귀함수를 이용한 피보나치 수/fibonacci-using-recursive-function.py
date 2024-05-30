n = int(input())

def fn(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
    return fn(n-1) + fn(n-2)

print(fn(n))