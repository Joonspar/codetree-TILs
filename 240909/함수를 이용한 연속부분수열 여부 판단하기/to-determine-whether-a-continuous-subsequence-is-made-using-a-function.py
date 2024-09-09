n1,n2 = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def check(n):
    for i in range(n2):
        if A[i+n] != B[i]:
            return False
    return True

def is_sub():
    for i in range(n1):
        if check(i):
            return True
    return False

if is_sub():
    print('Yes')
else:
    print('No')