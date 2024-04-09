n,m = map(int,input().split())

arr=[
    [0 for _ in range(m)]
    for _ in range(n)
]
a = 1
for i in range(n):
    for j in range(m):
        arr[i][j] = a
        print(a,end=' ')
        a += 1
    print()