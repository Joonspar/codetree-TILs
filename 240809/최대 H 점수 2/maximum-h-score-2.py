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
    max_h = calculate_h_score(arr)
    
    if l == 0:
        return max_h
    
    for i in range(n):
        modified_arr = arr[:]
        modified_arr[i] += 1
        max_h = max(max_h, calculate_h_score(modified_arr))
    
    return max_h

# 입력 처리
n, l = map(int, input().split())
arr = list(map(int, input().split()))

# 최대 H 점수 계산
result = max_h_score_after_operations(n, l, arr)
print(result)