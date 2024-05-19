n = int(input())
current = 100
arr = [0] * 200
for i in range(n):
    x,s = input().split()
    x = int(x)
    if s == 'R':
        for j in range(current,current+x):
            arr[j] += 1
        current += x
    elif s == 'L':
        for j in range(current,current+(-1)*abs(x),-1):
            arr[j] += 1
        current += (-1)*abs(x)
cnt = 0
# print(*arr)
for i in range(len(arr)):
    if arr[i] >= 2:
        cnt += 1
print(cnt)