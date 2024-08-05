def max_arithmetic_sequence_count(n, arr):
    max_count = 0
    count_dict = {}
    for i in range(n):
        for j in range(i + 1, n):
            a_i, a_j = arr[i], arr[j]
            
            if (a_i + a_j) % 2 == 0:
                k = (a_i + a_j) // 2
                if k in count_dict:
                    count_dict[k] += 1
                else:
                    count_dict[k] = 1
                max_count = max(max_count, count_dict[k])

    return max_count
n = int(input().strip())
arr = list(map(int, input().strip().split()))

print(max_arithmetic_sequence_count(n, arr))