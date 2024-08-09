from itertools import combinations

n, l = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0

for h in range(101): 
    for indices in combinations(range(n), l): 
        original = arr[:]  
        for idx in indices:
            arr[idx] += 1  
        cnt = sum(1 for x in arr if x >= h) 
        if cnt >= h:  
            ans = max(ans, h)  
        arr = original 

print(ans)