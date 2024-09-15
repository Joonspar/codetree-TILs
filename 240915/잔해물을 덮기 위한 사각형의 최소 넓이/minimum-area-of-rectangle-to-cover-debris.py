OFFSET = 1000
first = list(map(int,input().split()))
second = list(map(int,input().split()))

rects = [
    [0 for _ in range(2000)]
    for _ in range(2000)
]

for i in range(first[0]+OFFSET,first[2]+OFFSET):
    for j in range(first[1]+OFFSET,first[3]+OFFSET):
        rects[i][j] = 1
for i in range(second[0]+OFFSET,second[2]+OFFSET):
    for j in range(second[1]+OFFSET,second[3]+OFFSET):
        rects[i][j] = 0
cntc = 0
cntr = 0
for li in rects:
    if 1 in li:
        cntc += 1
    a = li.count(1)
    cntr = max(cntr,a)

print(cntr*cntc)