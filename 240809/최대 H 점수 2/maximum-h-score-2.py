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
    
    # L번만큼 반복하면서 가장 낮은 값 중 선택하여 증가시키는 전략
    for _ in range(l):
        arr.sort()
        for i in range(n):
            if arr[i] + 1 >= max_h + 1:
                arr[i] += 1
                break
        max_h = max(max_h, calculate_h_score(arr))
    
    return max_h

# 입력 처리
n,l = map(int,input().split())
arr = list(map(int,input().split()))
result = max_h_score_after_operations(n, l, arr)
print(result)