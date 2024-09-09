n = int(input()) 

def func(n):
    if n < 10:
        return n**2
    return (n % 10)**2 + func(n // 10)

print(func(n))