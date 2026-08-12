# 사용자 정의 함수
# 함수 정의 및 호출
def greet():
    print("안녕하세요!")

def greet_n(name):
    print(f"{name}님 안녕하세요!")

def info(name, age):
    print(f"{name}님은 {age}살입니다.")


greet() # 호출
greet_n("성희")
greet_n("대원")

info("박성희", 25)
info("최예윤", 27)

