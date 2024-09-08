n = int(input())
ans = n-2
arr = [
    ['*' for _ in range(n)]
    for _ in range(n)
]

for li in arr[1:n-1]:
    for i in range(1,n-1):
        li[i:n-1] = ' '

for li in arr:
    print(*li)