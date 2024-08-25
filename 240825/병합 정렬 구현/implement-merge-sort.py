def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    
    while i < len(left):
        sorted_arr.append(left[i])
        i += 1
    
    while j < len(right):
        sorted_arr.append(right[j])
        j += 1
    
    return sorted_arr

n = int(input())
arr = list(map(int, input().split()))

sorted_arr = merge_sort(arr)

print(" ".join(map(str, sorted_arr)))