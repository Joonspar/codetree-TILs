arr = list(input())
ans = 0
l = len(arr)
for i in range(l):
    arr[i] = int(arr[i])
    ans += arr[i] * (2**(l-i-1))
ans *= 17
res = []
while True:
    if ans <= 1:
        res.append(ans)
        break
    res.append(ans%2)
    ans //= 2

for digit in res[::-1]:
    print(digit,end='')