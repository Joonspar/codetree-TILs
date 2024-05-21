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
max_length = max(len(A), len(B))

# A와 B의 경로를 동일한 길이로 맞추기 위해 부족한 부분은 마지막 위치로 채움
A += [A[-1]] * (max_length - len(A))
B += [B[-1]] * (max_length - len(B))

# 만남 횟수 계산
for i in range(1, max_length):
    if A[i-1] != B[i-1] and A[i] == B[i]:
        res += 1

print(res)