n = int(input())
li = []
for _ in range(n):
    a = int(input())
    li.append(a)
ans = 0
cnt = 0
for i in range(n):
    if i == 0 or li[i-1] == li[i]:
        cnt += 1
    else:
        ans = max(cnt,ans)
print(ans)