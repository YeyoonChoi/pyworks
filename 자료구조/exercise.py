# 실습 7-1. 성적통계
score = [88, 92, 79, 95, 60]

count = len(score)
total = sum(score)
print("합계: ", total)
average = total / count
print("평균: ", average)
max_value = max(score)
print("최고점: ", max_value)
min_value = min(score)
print("최저점: ", min_value)

# 요소 전체 출력
for s in score:
    if s >= average:
        print(s)