a, b = map(int, input().split())

remainder_count = {}
total_sum = 0

while a > 1:
    remainder = a % b
    if remainder in remainder_count:
        remainder_count[remainder] += 1
    else:
        remainder_count[remainder] = 1
    a //= b

for count in remainder_count.values():
    total_sum += count ** 2

print(total_sum)