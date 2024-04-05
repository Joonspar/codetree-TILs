a,b = map(int,input().split())

for i in range(1,10):
    for j in range(b,a-1,-2):
        print("{} * {} = {}".format(j,i,i*j),end='')
        if j > 2:
            print(" /", end=" ")
    print()