x,y = map(int,input().split())
cnt = 0
for num in range(x,y+1):
    num = str(num)
    if num[0::] == num[::-1]:
        cnt += 1
print(cnt)