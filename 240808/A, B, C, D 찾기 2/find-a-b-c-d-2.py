def getResult(idx):

    # 1. 기저조건
    if len(temp) >= 1:
        sum_temp = sum(temp)
        if sum_temp not in dict_check:
            dict_check[sum_temp] = 1
        else:
            dict_check[sum_temp] += 1

    # 2. 백트래킹
    for i in range(idx, 4):
        temp.append(temp_arr[i])
        getResult(i+1)
        temp.pop()

def check(dict_c, dict_a):

    # 1. 딕셔너리 비교
    for check in dict_c:
        
        # 1.1
        if check not in dict_a:
            return False

        # 1.2
        if dict_c[check] != dict_a[check]:
            return False
    
    return True
    
# 입력
import sys
input = sys.stdin.readline

arr = list(map(int,input().split()))

# 계산1: 조건 딕셔너리
dict_arr = {}
for ele in arr:
    if ele not in dict_arr:
        dict_arr[ele] = 1
    else:
        dict_arr[ele] += 1

# 계산2 및 출력
# : a+b+c+d <= 40
# : 가능한 답은 유일 
for a in range(1, 37+1):
    for b in range(1, 37+1):
        for c in range(1, 37+1):
            for d in range(1, 37+1):
                
                # 1. 체크 딕셔너리 생성(백트래킹_오름차순)
                dict_check = {}
                temp_arr = [a,b,c,d]

                temp = []
                getResult(0)

                # 2. 딕셔너리 비교
                if check(dict_check, dict_arr):
                    print(a,b,c,d)
                    quit()