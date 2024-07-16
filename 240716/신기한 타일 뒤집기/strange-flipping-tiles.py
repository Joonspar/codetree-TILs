n = int(input())

arr = [0] * 100000
current = n * 100

for i in range(n):
    x , directions = input().split()
    x = int(x)
    if directions == 'L':
        for j in range(current, current - x, -1):
            arr[j] = 'W'
        current -= x
    elif directions == 'R':
        for j in range(current+1,current+x):
            arr[j] = 'B'
        current += x

cntb = 0
cntw = 0


for i in range(len(arr)):
    if arr[i] == 'W':
        cntw += 1
    elif arr[i] == 'B':
        cntb += 1

print(cntw, cntb)