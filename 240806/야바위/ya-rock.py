n = int(input())
cups = [0] * n
ans = 0
for i in range(3):
    a, b, c = map(int,input().split())
    cups[i] = 1
    cnt = 0
    for j in range(n):
        temp = cups[a-1]
        cups[a-1] = cups[b-1]
        cups[b-1] = temp
        if cups[c-1] == 1:
            cnt += 1
    ans = max(cnt,ans)
    cups[i] -= 1

print(ans)