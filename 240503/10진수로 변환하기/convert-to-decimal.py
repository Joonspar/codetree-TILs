binary = input()
arr = []
for i in range(len(binary)):
    a = int(binary[i])
    arr.append(a)
num = 0

for i in range(5):
    num = num * 2 + arr[i]

print(num)