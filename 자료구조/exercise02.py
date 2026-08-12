# 리스트

fruit = "grape"  #문자열을 저장하는 변수
print(fruit)

fruits = ["grape", "apple", "strawberry"] #리스트
print(fruits)

# 순서 - 앞: 0 1 2, 뒤 : -1 -2 -3
print(fruits[1]) #apple
print(fruits[-2]) #apple

# 요소 추가 함수 - append()
fruits.append("kiwi")
print(fruits)

# 요소 삭제 - remove()
fruits.remove("strawberry")
print(fruits)

# 요소 수정
fruits[1] = "banana"
print(fruits)

# 전체 요소 출력
for f in fruits:
    print(f)

# 숫자 리스트 만들기
num = []  # 빈 리스트
num.append(10)
num.append(20)
num.append(30)
print(num) # [10, 20, 30]

# 20을 삭제
num.remove(20)
print(num)

# 실습 8-1. 장바구니 관리
cart = []
cart.append("우유")
cart.append("빵")
cart.append("계란")
# cart.remove("빵")
cart.pop() # 맨 뒤 삭제
print(cart) #['우유', '빵']

# 커피, 과자
# cart.append("커피")
# extend(리스트)
cart.extend(["커피","과자"])

print(cart)  # ['우유', '계란']

# 전체 요소 출력
for c in cart:
    print(c, end=" ") #원래 for in 쓰면 줄바꿈인데 줄바꿈 하지 말고 옆으로 한 칸 띠어서 가라