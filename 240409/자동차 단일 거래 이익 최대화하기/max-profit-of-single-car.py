n = int(input())

lst = list(map(int, input().split()))
dp = [0] * n

for i in range(n-1):
    dp[i] = max(lst[i:]) - lst[i]

print(max(dp))