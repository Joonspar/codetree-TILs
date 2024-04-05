cnt = 1
while cnt<=19:
    for i in range(1,20):
        for j in range(1,20):
            print("{} * {} = {}".format(i,j,i*j),end='')
            if j % 2 == 0:
                print()
            elif j == 19:
                print()
            elif j % 2 != 0:
                print(' /',end=' ')
        cnt += 1