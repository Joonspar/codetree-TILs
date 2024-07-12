n = int(input())
first = 2
second = 4
res = 1
for i in range(n-2):
    res = (first * second) % 100
    first = second
    second = res
print(res)