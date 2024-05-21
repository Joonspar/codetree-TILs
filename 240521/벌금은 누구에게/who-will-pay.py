n , m , k =map(int,input().split())
num = []
for i in range(m):
    a = int(input())
    num.append(a)
    if num.count(a) == k:
        print(a)
        break
    
else:
    print(-1)