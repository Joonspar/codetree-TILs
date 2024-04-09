arr = [
    list(map(int,input().split()))
    for _ in range(4)
]
t = 0
for i in range(4):
    for j in range(i+1):
        t += arr[i][j]
print(t)