n1,n2 = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

def check(A,B):
    if A.find(B):
        return True
    else:
        return False

if check:
    print('Yes')
else:
    print('No')