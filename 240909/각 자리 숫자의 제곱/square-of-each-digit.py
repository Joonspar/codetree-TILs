n = int(input())

def sqr(n):
    if n < 10:
        return n**2
    else:
        return sqr(n//10) + (n%10)**2 

print(sqr(n))