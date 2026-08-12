# 반복문 - for
# range(시작값, 종료값, 증감값) - 실제 종료값은(종료값-1)
print(range(5)) # range(0, 5)
print(list(range(5)))
print(list(range(1, 6)))

# 1부터 5까지 출력
for i in range(1, 6, 1):
    print(i)
print("반복을 종료합니다.")

# 1부터 5까지의 합계
'''
total = 0
for i in range(1, 6, 1):
    total = total + i
print("합계: ", total)
'''

total = 0
for i in [1, 2, 3, 4, 5]:
    total = total + i
print("합계: ", total)