arr = [0] * 200
n = int(input())

for i in range(n):
    x1,x2 = map(int,input().split())
    for j in range(x1,x2):
        arr[j] += 1
print(max(arr))