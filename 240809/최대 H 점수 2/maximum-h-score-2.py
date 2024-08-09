def calculate_h_score(arr):
    arr.sort(reverse=True)
    h_score = 0
    for i in range(1, len(arr) + 1):
        if arr[i-1] >= i:
            h_score = i
        else:
            break
    return h_score

def max_h_score_after_operations(n, l, arr):
    arr.sort(reverse=True)
    max_h = calculate_h_score(arr)
    
    if l == 0:
        return max_h
    
    for _ in range(l):
        # 현재 배열에서 증가시키면 가장 효과적인 원소 선택
        for i in range(n):
            if arr[i] > arr[-1]: # 가장 작은 원소는 증가해도 H 점수에 영향 없음
                arr[i] += 1
                break
        max_h = max(max_h, calculate_h_score(arr))
    
    return max_h

# 입력 처리
n, l = map(int, input().split())
arr = list(map(int, input().split()))

# 최대 H 점수 계산
result = max_h_score_after_operations(n, l, arr)
print(result)