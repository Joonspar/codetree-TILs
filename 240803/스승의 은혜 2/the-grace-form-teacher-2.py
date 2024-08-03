n,b = map(int,input().split())
cnt = 0
p = []
for _ in range(n):
    price = int(input())
    p.append(price)

for i in range(n):
    total = 0
    cnt = 1
    for j in range(n):
        if i == j:
            p[i] = p[i] // 2
        total += p[j]
        if total <= b:
            cnt += 1
        else:
            p[i] *= 2
            break
print(cnt)