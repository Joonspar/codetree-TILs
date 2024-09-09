n = int(input())

def star(n):
    if n == 0:
        return
    else:
        star(n-1)
        print('*'*n)
star(n)