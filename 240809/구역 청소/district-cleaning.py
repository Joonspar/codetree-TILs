a,b = map(int,input().split())
c,d = map(int,input().split())
cnt = [0] * 100

for i in range(a,b+1):
    cnt[i] += 1
for i in range(c,d+1):
    cnt[i] += 1
new_list = [x for x in cnt if x>=1]
print(len(new_list)-1)