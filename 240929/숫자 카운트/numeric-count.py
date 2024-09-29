n = int(input())
nums = [
    list(map(int,input().split()))
    for _ in range(n)
]
cnt = 0
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if i == j or j == k or i == k:
                continue
            correct = True
            for question , cnt1 , cnt2 in nums:
                x = question // 100
                y = question % 100 // 10
                z = question % 10
                res1 = 0
                res2 = 0
                if x == i:
                    res1 += 1
                if y == j:
                    res1 += 1
                if z == k:
                    res1 += 1
                if x == j or x == k:
                    res2 += 1
                if y == i or y == k:
                    res2 += 1
                if z == i or z == j:
                    res2 += 1
                
                if res1 != cnt1 or res2 != cnt2:
                    correct = False
                    break
            if correct:
                cnt += 1
print(cnt)