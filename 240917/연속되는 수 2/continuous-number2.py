n = int(input())
li = []
for _ in range(n):
    a = int(input())
    li.append(a)
ans = 1
cnt = 1
for i in range(n):
    if li[i-1] == li[i]:
        cnt += 1
    else:
        ans = max(cnt,ans)
print(ans)