n = int(input())
rect = [
    list(map(int,input().split()))
    for _ in range(n)
]
ans = 0
for i in range(n-2):
    for l in range(n-2):
        cnt = 0
        for j in range(i,i+3):
            for k in range(l,l+3):
                if rect[j][k] == 1:
                    cnt += 1
        ans = max(ans,cnt)
print(ans)