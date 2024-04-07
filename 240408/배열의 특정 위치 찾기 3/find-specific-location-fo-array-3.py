n = list(map(int,input().split()))
total = 0
for i in range(len(n)):
    if n[i] == 0:
        total = n[i-1] + n[i-2] + n[i-3]
        break
print(total)