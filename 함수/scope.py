# 변수의 유효 범위
def click_a():
    x = 0  #지역(local) 변수
    x = x + 1
    print("x =", x)

click_a() # x=1
click_a() # x=1
click_a() # x=1

quantity = 2 # 전역변수
def get_price():
    price = 1000 * quantity #price-지역변수
    print(f"{quantity}개에 {price}원입니다.")

get_price()
print(quantity) #2
# print(price) # 이미 소멸한 변수이므로 오류 발생

# 값이 유지되는 변수
x = 0 # 전역변수
def click_b():
    global x #global을 붙이면 지역변수가 전역변수화 함
    x = x + 1
    print("x =", x)

click_b() # x = 1
click_b() # x = 2
click_b() # x = 3
