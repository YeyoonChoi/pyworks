# 입력 처리 - input()
name = "우영우"
age = 31
print(type(age)) #int
"""
print("이름을 입력하세요: ")
name = input()
"""
"""
name = input("이름 입력: ")
age = int(input("나이 입력: "))

print(type(age))  #int - 예)31
print("이름: ",name)

# 출력1
print("나이: " + str(age))  #+를 사용할 때는 같은 문자 형식으로 연결해야 됨

# 출력2
print("나이:",age)

# 출력3
print("나이: {age}")
"""

# 사각형의 넓이 계산
# 넓이(area) = 가로(w) * 세로(h)
# 입력받은 숫자는 문자열이므로 숫자로 변환해야 함
# float(문자) -> 실수형으로 변환

w = float(input("가로: "))
h = float(input("세로: "))

area = w * h
print("사각형의 넓이: ", area)
