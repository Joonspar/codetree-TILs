n,m,k = map(int,input().split())
arr = [
    list(map(int,input().split()))
    for _ in range(n)
]
for i in range(n):
    for j in range(k):