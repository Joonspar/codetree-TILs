n = int(input())

def func(n):
    if n == 0:
        return
    func(n-1)
    print(n,end=' ')

def func2(n):
    if n == 0:
        return
    print(n,end=' ')
    func2(n-1)

func(n)
print()
func2(n)