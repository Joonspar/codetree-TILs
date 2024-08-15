n = int(input())
sections = [
    list(map(int,input().split()))
    for _ in range(n)
]
max_line = 10000
for i in range(n):
    cnts = []
    for j in range(n):
        if i == j:
            continue
        x,y = sections[j]
        for k in range(x,y+1):
            cnts.append(k)
    res = max(cnts) - min(cnts)
    max_line = min(max_line,res)
print(max_line)