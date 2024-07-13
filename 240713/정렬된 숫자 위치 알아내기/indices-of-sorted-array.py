def find_new_positions(N, sequence):
    # 원래 수열의 각 원소와 위치를 저장
    indexed_sequence = [(value, index) for index, value in enumerate(sequence)]
    
    # 수열을 값 기준으로 정렬
    indexed_sequence.sort()
    
    # 정렬된 수열에서 원래 수열의 각 원소의 새로운 위치를 저장할 리스트
    new_positions = [0] * N
    
    # 정렬된 수열의 각 원소에 대해 원래 위치를 찾아 새로운 위치를 기록
    for new_index, (value, original_index) in enumerate(indexed_sequence):
        new_positions[original_index] = new_index + 1  # 위치는 1부터 시작
    
    return new_positions

# 입력
N = int(input())
sequence = list(map(int, input().split()))

# 새로운 위치 찾기
new_positions = find_new_positions(N, sequence)

# 출력
print(" ".join(map(str, new_positions)))