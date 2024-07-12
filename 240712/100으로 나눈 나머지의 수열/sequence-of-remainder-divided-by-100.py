n = int(input())
first = 2
second = 4
res = 1
if n == 1:
    print(2)
elif n == 2:
    print(4)
else:    
    for i in range(n-2):
        res = (first * second) % 100
        first = second
        second = res
    print(res)