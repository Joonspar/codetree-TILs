arr1 = list(map(int,input().split()))
s = 0
cnt = 0
for elem in arr1:
    if elem >= 250:
        break
    s += elem
    cnt += 1
print(s, round(s/cnt,1))