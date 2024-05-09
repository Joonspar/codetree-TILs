# arr = [1,5,2,6,8]
# res = 0

# for i in range(5):
#     arr[i] *= 2
#     s = 0
#     for j in range(4):
#         s += abs(arr[j] - arr[j+1])
#     res = max(res,s)
#     arr[i] //= 2
# print(res)

n = int(input())
arr = list(map(int,input().split()))
res = []
for i in range(n):
    s = 0
    for j in range(n):
        s += arr[j]*abs(j-i)
    res.append(s)
print(min(res))