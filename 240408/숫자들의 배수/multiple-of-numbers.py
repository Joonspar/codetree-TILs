n = int(input())
cnt = 0
i = 1
while True:
    print(i*n,end=' ')
    i += 1
    if (i*n) % 5 == 0:
        cnt += 1
    elif cnt == 2:
        break