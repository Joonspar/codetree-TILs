def rotate_string(s):
    L = len(s)
    for i in range(L):
        print(s)
        s = s[-1] + s[:-1]  # 문자열을 오른쪽으로 한 글자 밀기

# 입력 예제
input_string = input()

# 함수 호출
rotate_string(input_string)
print(input_string)