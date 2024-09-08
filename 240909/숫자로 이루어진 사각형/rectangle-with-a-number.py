n = int(input())

def rect(n):
    num = 1
    arr = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]
    for i in range(n):
        for j in range(n):
            arr[i][j] = num
            if num < 9:
                num += 1
            else:
                 num = 1
    for elem in arr:
        print(*elem)
rect(n)