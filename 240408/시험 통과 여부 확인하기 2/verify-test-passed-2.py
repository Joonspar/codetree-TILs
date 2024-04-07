test = int(input())
cnt = 0
for i in range(test):
    total = 0
    a,b,c,d = map(int,input().split())
    total = (a+b+c+d)/4
    if total >= 60:
        print('pass')
        cnt += 1
    else:
        print('fail')
    
print(cnt)