def size(n,m):
    for _ in range(n):
        print(m*'1')
h,w = map(int,input().split())
size(h,w)