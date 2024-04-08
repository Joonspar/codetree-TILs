cnt = [0] * 4
for i in range(3):
    a,b = input().split()
    if a == 'Y' and int(b) >= 37:
        cnt[0] += 1
    elif a == 'N' and int(b) >= 37:
        cnt[1] += 1
    elif a == 'Y' and int(b) < 37:
        cnt[2] += 1
    elif a == 'N' and int(b) < 37:
        cnt[3] += 1    
print(*cnt,end=' ')
if cnt[0] >= 2:
    print('E')