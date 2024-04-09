n = int(input())
li = list(map(int,input().split()))
cnt = 0
result = 0
for idx,el in enumerate(li):
    if el == 2:
        cnt += 1
        if cnt == 3:
            result = idx

print(result+1)