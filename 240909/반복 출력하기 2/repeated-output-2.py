n = int(input())

def func(n):
    if n == 0:
        return
    else:
        func(n-1)
        print('HelloWorld')
func(n)