# 칼렌더(calendar) 모듈 사용

import calendar

# 2026 달력 출력
# calendar.prcal(2026)

calendar.prmonth(2026, 8)

# 요일 이름 출력
print(calendar.day_name[0]) #Monday
print(calendar.day_name[6]) #Sunday
print(calendar.day_name[ : ])

# 특정 날짜의 요일
day_of_week = calendar.weekday(2025, 12, 25)
print(day_of_week)
print(calendar.day_name[day_of_week])
calendar.prmonth(2025, 12)