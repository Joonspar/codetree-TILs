A = input()
n = len(A)
cnt = 0
res = 0
for i in range(n-1,0,-1):
    if A[i] == ')' and A[i-1] == ')':
        cnt += 1
    elif A[i] == '(' and A[i-1] == '(':
        res += cnt
print(res)