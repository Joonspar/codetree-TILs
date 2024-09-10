a,b,c = map(int,input().split())

n = a*b*c

def func(n):
    if n < 10:
        return n
    return (n % 10) + func(n//10)

print(func(n))