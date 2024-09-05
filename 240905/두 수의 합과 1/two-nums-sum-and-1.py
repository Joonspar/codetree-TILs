num1 , num2 = map(int,input().split())
ans = num1 + num2
cnt = 0
ans = str(ans)
for elem in ans:
    if elem == '1':
        cnt += 1
print(cnt)