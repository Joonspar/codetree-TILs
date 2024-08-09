n = int(input())
sections = [
    list(input().split())
    for _ in range(n)
]
cnt = 0
for i in range(n):
    extra = 101
    for j in range(i+1,n):
        sections[i][0] = int(sections[i][0])
        sections[j][0] = int(sections[j][0])
        if sections[i][0] == sections[j][0]:
            if sections[i][1] != sections[j][1]:
                cnt += 1
                sections[i][1] = sections[j][1]
                break
            sections[j][0] += extra
            extra += 10
print(cnt)