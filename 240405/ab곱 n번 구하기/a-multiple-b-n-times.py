test = int(input())

for i in range(test):
    total = 1
    a,b = map(int,input().split())
    for j in range(a,b+1):
        total *= j
    print(total)