n,k = map(int,input().split())
cnt = [0] * n
for i in range(k):
    a,b = map(int,input().split())
    for i in range(a-1,b):
        cnt[i] += 1
    
print(max(cnt))