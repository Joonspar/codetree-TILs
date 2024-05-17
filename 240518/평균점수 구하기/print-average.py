arr = list(map(float,input().split()))

s = sum(arr)
res = round(s/len(arr),1)
print(res)