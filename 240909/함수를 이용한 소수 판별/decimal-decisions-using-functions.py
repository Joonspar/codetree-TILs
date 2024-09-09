a,b = map(int,input().split())
def func1(a,b):
    res = 0
    is_prime = False
    for i in range(a,b+1):
        for j in range(2,i):
            if i % j != 0:
                is_prime = True
            else:
                is_prime = False
                break
        if is_prime:
            res += i
    return res

print(func1(a,b))