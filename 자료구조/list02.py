# 리스트의 연산
score = [80, 70, 90, 75]

#  개수 - len(리스트)
count = len(score)
print("개수: ", count) #4

# 합계 - sum(리스트)
# total = score[0] + score[1] + score[2] + score[3]
total = sum(score)
print("합계: ", total) #315

# 평균 = 합계 / 개수
average = total / count
print("평균: ", average)

# 최대값 - max(리스트)
max_val = max(score)
print("최고 점수: ", max_val)

# 최소값 - min(리스트)
min_val = min(score)
print("최저 점수: ", min_val)

# score = [80, 70, 90, 75]
# 평균 이상인 점수만 골라 출력하기
for s in score:
    if s >= average:
        print(s)