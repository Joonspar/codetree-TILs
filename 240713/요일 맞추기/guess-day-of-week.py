# 입력 값을 받습니다.
input_str = input().strip()
m1, d1, m2, d2 = map(int, input_str.split())

# 각 월의 일수를 정의합니다.
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# 기준 날짜인 2011년 1월 1일의 요일을 설정합니다. (월요일)
reference_weekday = 0  # 0: 월요일, 1: 화요일, ..., 6: 일요일

# 기준 날짜와 목표 날짜 사이의 일 수를 계산합니다.
def calculate_days_between_dates(m1, d1, m2, d2):
    # 같은 달인 경우
    if m1 == m2:
        return d2 - d1

    # 다른 달인 경우
    days = days_in_month[m1 - 1] - d1  # 첫 달의 남은 일수
    for month in range(m1, m2 - 1):
        days += days_in_month[month]
    days += d2  # 마지막 달의 일수 추가
    return days

days_difference = calculate_days_between_dates(m1, d1, m2, d2)

# 기준 날짜의 요일에서 일 수 차이만큼 이동하여 목표 날짜의 요일을 계산합니다.
target_weekday = (reference_weekday + days_difference) % 7

# 요일 목록을 정의합니다.
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# 목표 날짜의 요일을 출력합니다.
print(weekdays[target_weekday])