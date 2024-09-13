n = int(input())
res = [0] * 101

segments = [
    list(map(int,input().split()))
    for _ in range(n)
]

for el1,el2 in segments:
    for i in range(el1,el2+1):
        res[i] += 1

print(max(res))