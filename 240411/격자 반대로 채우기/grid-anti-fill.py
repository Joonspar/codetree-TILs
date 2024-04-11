n = int(input())

arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]

cnt = 1
for col in range(n-1,-1,-1):
    if col % 2 == 0:
        for row in range(n):
            arr[row][col] = cnt
            cnt += 1
    else:
        for row in range(n-1,-1,-1):
            arr[row][col] = cnt
            cnt += 1

for i in arr:
    for j in i:
        print(j,end=' ')
    print()