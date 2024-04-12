n,m = tuple(map(int,input().split()))

arr=[
    [0 for _ in range(n)]
    for _ in range(n)
]
k = 1
for _ in range(m):
    r,c = map(int,input().split())
    arr[r-1][c-1] = k
    k += 1

for row in arr:
    for ele in row:
        print(ele,end=' ')
    print()