n = list(map(int,input().split()))
total = 0
cnt = 0
for i in range(len(n)):
    if n[i] == 0:
        break
    elif n[i] % 2 == 0:
        total += n[i]
        cnt += 1
print(cnt, total)