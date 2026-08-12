# 함수 예제
def message() :
    return "Good Luck!"

msg = message()
print(msg)

# 사각형의 면적 계산 함수
def area(w, h):
    return w * h

# 삼각형의 면적 계산 함수
def triangle (s, h):
    return s * h / 2

# 구구단 출력
def gugudan(dan) :
    for i in range(1, 10): 
        print(f"{dan} x {i} = {dan*i}")

# 응원 메시지
msg = message()
print(msg)

# 사각형의 면적 : 가로(w) x 세로(h)
area = area (4,3)
print("사각형의 면적:", area)

# 삼각형의 면적 : 가로(s) * 세로(h) / 2
tri_area = triangle (4,3)
print("삼각형의 면적:", tri_area)

# 구구단 함수 호출
gugudan(5) 
gugudan(7)