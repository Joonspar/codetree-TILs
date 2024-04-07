n = int(input())

subject = list(map(float,input().split()))

total = round(sum(subject)/n,1)
print(total)

if total >= 4.0:
    print('Perfect')
elif total>= 3.0:
    print('Good')
else:
    print('Poor')