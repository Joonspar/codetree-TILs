n = int(input())
cnt = 0
arr = input()
for i in range(n):
    if arr[i] == 'C':
        for j in range(i,n):
            if arr[j] == 'O':
                for k in range(j,n):
                    if arr[k] == 'W':
                        cnt += 1
print(cnt)