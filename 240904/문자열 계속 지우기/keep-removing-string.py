# 변수 선언 및 입력:
A = input()
B = input()


# A에서 B를 찾습니다, 찾을 수 없을 때까지 반복합니다.
while A.find(B) != -1:
    start_pos = A.find(B)
    # start_pos부터 len(B)개의 문자를 지웁니다.
    A = A[:start_pos] + A[start_pos + len(B):]

print(A)