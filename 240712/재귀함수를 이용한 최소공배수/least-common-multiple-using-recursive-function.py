import math

def lcm(a, b):
    return a * b // math.gcd(a, b)

def find_lcm_recursive(numbers, n):
    if n == 1:
        return numbers[0]
    else:
        return lcm(numbers[n-1], find_lcm_recursive(numbers, n-1))

# 입력 받기
n = int(input().strip())
numbers = list(map(int, input().strip().split()))

# 최소공배수 계산
result = find_lcm_recursive(numbers, n)
print(result)