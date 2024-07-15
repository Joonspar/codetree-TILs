n = int(input())
current = n * 10
arr = [0] * 2000
for i in range(n):
    x, s = input().split()
    x = int(x)
    if s == 'R':
        for j in range(current+1, current + x +1 ):
            arr[j] += 1
        current += x
    elif s == 'L':
        for j in range(current, current - x, -1):
            arr[j] += 1
        current -= x

cnt = 0
for i in range(len(arr)):
    if arr[i] >= 2:
        cnt += 1
print(cnt)