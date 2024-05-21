digits = list(map(int, input()))
n = len(digits)

indicator = True
for i in range(n):
    if digits[i] == 0:
        digits[i] = 1
        indicator = False
        break

change = digits[-1]
for i in range(1, n):
    index = -1 -i
    change += pow(2,i)*digits[index]

if indicator:
    print(change -1 )
else:
    print(change)