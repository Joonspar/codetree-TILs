n,k = map(int,input().split())
arr = [0] * 10000
# arr2 = []
for i in range(n):
    state,point = input().split()
    state = int(state)
    arr[state] = point
max_cnt = 0
for i in range(1,n-k+2):
    res = 0
    for j in range(i,i+k+1):
        if arr[j] == 'G':
            res += 1
        elif arr[j] == 'H':
            res += 2
    max_cnt = max(max_cnt,res)
print(max_cnt)