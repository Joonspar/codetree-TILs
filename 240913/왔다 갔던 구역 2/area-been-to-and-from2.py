n = int(input())
res = [0] * 2000
cur = 1001
for _ in range(n):
    dis,dire = input().split()
    dis = int(dis)
    if dire == 'R':
        for i in range(cur,cur+dis+1):
            res[i] += 1
            cur += dis
    else:
        for i in range(cur,cur-dis-1,-1):
            res[i] += 1
            cur -= dis
cnt = 0
for i in range(len(res)):
    if res[i] >= 2:
        cnt += 1
print(cnt+1)