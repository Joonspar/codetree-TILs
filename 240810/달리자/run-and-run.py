def minimum_total_distance(n, A, B):
    total_distance = 0
    carry = 0  # 현재 집에서 다음 집으로 이동해야 할 인원

    for i in range(n):
        carry += A[i] - B[i]  # 현재 집에서 남거나 부족한 인원 계산
        total_distance += abs(carry)  # 그 인원이 이동해야 하는 거리를 누적합으로 계산

    return total_distance

# 입력
n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 출력
print(minimum_total_distance(n, A, B))