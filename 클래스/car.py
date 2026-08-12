# 클래스 - 사물(객체)을 코드로 만든 것
class Car:
    # 생성자(constructor)
    def __init__(self, color, model, wheel):
        self.color = color
        self.model = model
        self.wheel = wheel

    def drive(self):
        print(f"{self.color} {self.model}가 달립니다.")

# 객체(인스턴스) 생성
car = Car("검정색", "Sonata", 4)
print(car) #<__main__.Car object at 0x0000026F235A4440>

car.drive() # 메서드 호출