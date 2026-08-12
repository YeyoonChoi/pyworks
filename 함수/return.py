# return이 있는 함수
# 제곱수 계산하는 함수
def square(x):
    return x * x

# 두 수의 합을 구하는 함수
def add(x, y):
    return x + y

# 원의 넓이를 계산하는 함수
def circle_area(r):
    return 3.14 * r * r

value = square(4) #호출
print(value)

value2 = add(10, 20)
print(value2)

c_area = circle_area(5)
print("원의 넓이:", c_area)

# 실습 2-1. 사각형 넓이 함수
def rect_area(x, y):
    return x * y

r_area = rect_area(3, 4)
print("사각형의 넓이 :", r_area)

# 실습 2-2. 절댓값 함수
def my_abs(n):
    if n<0:
        return -n
    return n

print(my_abs(10))