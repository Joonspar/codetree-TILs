n = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
cnt = 0
for i in range(n):
    if A[i] in B:
        cnt += 1
if cnt == n:
    print('Yes')
else:
    print('No')