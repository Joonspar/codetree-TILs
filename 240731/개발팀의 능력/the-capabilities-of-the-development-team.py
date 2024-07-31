arr = list(map(int,input().split()))
min_diff = 1000
error = False
for i in range(5):
    for j in range(i+1,5):
        for k in range(5):
            if k != i and k != j:
                first = arr[i] + arr[j]
                second = arr[k]
                third = sum(arr) - first - second
                if first != second and first != third and second != third:
                    error = True
                    diff = max(first,second,third) - min(first,second,third)
                    min_diff = min(min_diff,diff)

if error:
    print(min_diff)
else:
    print(-1)