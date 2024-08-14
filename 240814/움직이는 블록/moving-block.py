# 변수 선언 및 입력:
n = int(input())
blocks = [
    int(input())
    for _ in range(n)
]

# 전체 블럭 수를 셉니다.
sum_of_blocks = sum(blocks)

# 평균 블럭 수 보다 더 큰 블럭에 대해서만
# 그 차이만큼 옮겨주면 됩니다.
avg = sum_of_blocks // n
ans = 0
for block_num in blocks:
    if block_num > avg:
        ans += block_num - avg

print(ans)