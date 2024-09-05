def rotate_string(s):
    # 문자열 s를 오른쪽으로 한 칸 밀기
    return s[-1] + s[:-1]

def find_minimum_rotation(A, B):
    n = len(A)
    rotated_A = A
    
    for i in range(1, n+1):
        rotated_A = rotate_string(rotated_A)  # 문자열을 한 칸씩 우측으로 밀기
        if rotated_A == B:
            return i  # 같아지는 순간의 n을 반환
    
    return -1  # 끝까지 같아지지 않으면 -1 반환

# 입력 받기
A = input().strip()
B = input().strip()

# 결과 출력
print(find_minimum_rotation(A, B))