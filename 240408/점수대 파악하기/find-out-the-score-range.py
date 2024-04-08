li = list(map(int,input().split()))
cnt = 0
for j in range(10,0,-1):
    cnt = 0
    for i in li:
        if i == 0:
            break
        elif (i//10) == j:
            cnt += 1
    print("{} - {}".format(j*10,cnt))