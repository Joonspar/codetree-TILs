t,a,b = map(int,input().split())
S = []
N = []
for i in range(t):
    alpha,state = input().split()
    state = int(state)
    if alpha == 'S':
        S.append(state)
    elif alpha == 'N':
        N.append(state)
S.sort()
N.sort()
s1 = 0
n1 = 0
cnt = 0
for k in range(a,b+1):
    while s1 < len(S) -1 and abs(k-S[s1]) > abs(k-S[s1+1]):
        s1 += 1
    d1 = abs(k-S[s1])

    while n1 < len(N) -1 and abs(k-N[n1]) > abs(k-N[n1+1]):
        n1 += 1
    d2 = abs(k-N[n1])

    if d1 <= d2:
        cnt += 1

print(cnt)