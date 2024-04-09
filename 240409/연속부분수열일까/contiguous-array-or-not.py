n1,n2 = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

if B in A:
    print('Yes')
else:
    print('No')