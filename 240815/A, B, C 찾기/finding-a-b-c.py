def find_abc(values):
    # 주어진 값들을 오름차순으로 정렬
    values.sort()
    
    # 가장 큰 값은 A + B + C
    ABC = values[-1]
    
    # 나머지 6개의 값 중 세 개는 두 수의 합(A + B, B + C, C + A)
    # 나머지 3개의 값은 A, B, C
    # 우리는 가장 작은 세 값 중 두 수의 차를 구해서 A, B, C를 찾아냅니다
    A = values[0]
    B = values[1]
    C = ABC - (A + B)
    
    return A, B, C

# 예제 입력
values = list(map(int, input().split()))

# A, B, C를 찾아서 출력
A, B, C = find_abc(values)
print(A, B, C)