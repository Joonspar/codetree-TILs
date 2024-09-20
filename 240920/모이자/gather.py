n = int(input())
li = list(map(int,input().split()))
ans = 10000

for i in range(n):
    s = 0
    for j in range(n):
        if i != j:
            s += li[j] * abs(j-i)
    ans = min(ans,s)
print(ans)