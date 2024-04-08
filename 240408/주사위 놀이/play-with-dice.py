li = list(map(int,input().split()))

for i in range(1,7):
    cnt = 0
    for elem in li:
        if elem == i:
            cnt += 1
    print("{} - {}".format(i,cnt))