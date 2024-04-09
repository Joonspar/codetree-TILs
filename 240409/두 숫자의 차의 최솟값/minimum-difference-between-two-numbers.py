n = int(input())
li = list(map(int,input().split()))

small = 100

for i in range(n):
    for j in range(i+1,n):
        dif = li[j] - li[i]
        if dif < small:
            small = dif
print(small)