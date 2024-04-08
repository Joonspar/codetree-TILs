n = int(input())
cnt = 0
i = 1
while cnt < 2:
    if (i*n) % 5 == 0:
        cnt += 1
    print(i*n,end=' ')
    i += 1