li = list(map(int,input().split()))

for i in range(len(li)):
    if li[i] == 0:
        break
    elif li[i] % 2 == 0:
        print(li[i] // 2,end=' ')
    else:
        print(li[i]+3, end=' ')