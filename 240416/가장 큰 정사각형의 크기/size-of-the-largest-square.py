n,m = map(int,input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]
for i in range(m):
    li = list(map(int,input().split()))
    arr.append(li)

print(arr)