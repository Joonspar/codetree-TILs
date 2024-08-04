def calculate_total_cost(selected_students, students, coupon_index):
    total_cost = 0
    for i in range(len(selected_students)):
        idx = selected_students[i]
        if idx == coupon_index:
            total_cost += (students[idx][0] // 2) + students[idx][1]  # 쿠폰 적용
        else:
            total_cost += students[idx][0] + students[idx][1]  # 쿠폰 미적용
    return total_cost

def max_students(N, B, students):
    # 학생을 선택할 수 있는 최대 수를 찾기 위해
    max_count = 0
    
    for coupon_index in range(N):
        # 쿠폰을 적용할 학생을 정하고, 나머지 학생들을 선택합니다.
        costs = []
        for i in range(N):
            if i != coupon_index:
                costs.append(students[i][0] + students[i][1])
        costs.sort()
        
        # 쿠폰을 적용한 학생의 비용을 별도로 처리
        coupon_cost = (students[coupon_index][0] // 2) + students[coupon_index][1]
        
        total_cost = coupon_cost
        count = 1  # 쿠폰 적용된 학생 포함
        
        # 비용이 예산 내에서 가능한 최대 학생 수를 계산
        for cost in costs:
            if total_cost + cost <= B:
                total_cost += cost
                count += 1
            else:
                break
        
        max_count = max(max_count, count)
    
    return max_count

# 입력 처리
import sys
input = sys.stdin.read
data = input().split()

N = int(data[0])
B = int(data[1])
students = [(int(data[2 + 2*i]), int(data[3 + 2*i])) for i in range(N)]

# 결과 계산 및 출력
print(max_students(N, B, students))