n = int(input())

def stars(n):
    if n == 0:
        return
    print('*'*n,end=' ')
    stars(n-1)
    print('*'*n,end=' ')

stars(n)