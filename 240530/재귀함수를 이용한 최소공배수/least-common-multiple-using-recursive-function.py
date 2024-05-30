n = int(input())
arr = list(map(int,input().split()))
s = 1
for i in range(n):
    if s % arr[i] == 0:
        s = s
    else:
        s *= arr[i]
print(s)