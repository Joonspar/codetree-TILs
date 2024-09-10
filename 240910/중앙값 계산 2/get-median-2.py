n = int(input())
nums = list(map(int,input().split()))
nums.sort()
l = n // 2
print(*nums[:l+1])