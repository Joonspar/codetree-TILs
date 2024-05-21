n,m = map(int,input().split())
cnta = 0
cntb = 0
A = [0] * 1
B = [0] * 1
for _ in range(n):
    distance , direction = input().split()
    distance = int(distance)
    if direction == 'L':
        for _ in range(distance):
            cnta -= 1
            A.append(cnta)
    else:
        for _ in range(distance):
            cnta += 1
            A.append(cnta)
for _ in range(m):
    distance , direction = input().split()
    distance = int(distance)
    if direction == 'L':
        for _ in range(distance):
            cntb -= 1
            B.append(cntb)
    else:
        for _ in range(distance):
            cntb += 1
            B.append(cntb)
res = 0
for i in range(len(A)):
    if A[i-1] == B[i-1] and A[i] == B[i]:
        res += 1
print(res+1)