n = int(input())
cnt = n
for i in range(1,n+1):
    for j in range(1,cnt+1):
        print("{} * {} = {}".format(i,j,i*j),end='')
        if j != (n-i+1):
            print(' /',end=' ')
    cnt -= 1
    print()