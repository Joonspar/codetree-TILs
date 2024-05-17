n = int(input())
arr = list(map(float,input().split()))

s = sum(arr)
res = round(s/n,1)
if res >= 4.0:
    print(res)
    print('Perfect')
elif res >= 3.0:
    print(res)
    print('Good')
elif res < 3.0:
    print(res)
    print('Poor')