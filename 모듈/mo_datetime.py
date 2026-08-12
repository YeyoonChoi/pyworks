# 날짜와 시간 모듈
# from 모듈 import 모듈
from datetime import datetime, date

# 현재 날짜와 시간
now = datetime.now()
print(now) #2026-08-10 21:45:40.436044

# 연 월 일
print(f"{now.year}년 {now.month}월 {now.day}일")

# 시 분 초
print(f"{now.hour} : {now.minute} : {now.second}")

# 오늘의 날짜
today = date.today()
print(today) #2026-08-10

# 광복절 (특정한 날짜)
the_day = date(2026, 8, 15)
print(the_day)

# D-day : date_diff.days
date_diff = the_day - today 
print("D-day:", date_diff.days)