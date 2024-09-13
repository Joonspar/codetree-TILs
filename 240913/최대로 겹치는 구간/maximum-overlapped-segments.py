n = int(input())
res = [0] * 202
segment = [
    list(map(int,input().split()))
    for _ in range(n)
]

for el1,el2 in segment:
    for i in range(el1,el2):
        res[i] += 1

print(max(res))