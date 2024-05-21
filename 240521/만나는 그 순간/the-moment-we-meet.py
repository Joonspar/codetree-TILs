n,m = map(int,input().split())
cur = 0
arr = [0] * 1
brr = [0] * 1
cnta = 0
cntb = 0
for _ in range(n):
    direction , distance = input().split()
    distance = int(distance)
    if direction == 'L':
        for _ in range(distance):
            cnta -= 1
            arr.append(cnta)
    else:
        for _ in range(distance):
            cnta += 1
            arr.append(cnta)
for _ in range(m):
    direction , distance = input().split()
    distance = int(distance)
    if direction == 'L':
        for _ in range(distance):
            cntb -= 1
            brr.append(cntb)
    else:
        for _ in range(distance):
            cntb += 1
            brr.append(cntb)
for i in range(1,len(arr)):
    if arr[i] == brr[i]:
        ans = i
        break
print(ans)