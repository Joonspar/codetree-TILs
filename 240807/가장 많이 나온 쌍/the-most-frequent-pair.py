n,m = map(int,input().split())
sections = [
    list(map(int,input().split()))
    for _ in range(m)
]
ans = 0
cnts = []
for i in range(m):
    cnt = 1
    for k in range(m):
        for j in range(k+1,m):
            if sections[k] == sections[j] or sections[k].reverse() == sections[j] or sections[k] == sections[j].reverse():
                cnt += 1
    cnts.append(cnt)
print(max(cnts))