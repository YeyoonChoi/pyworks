#"안녕하세요!"를 3번 출력
#1 while 문
num = 1
while num <= 3:
    print("안녕하세요!")
    num = num + 1
print ("반복 종료!")

#2 for문
for x in range(3): #range(0, 3) - 0 1 2
    print("안녕하세요!")

# 구구단 - (3 X 1 = 3)
dan = int(input("단을 입력하세요: "))
for i in range(1, 10):
    # print(dan, "x", i, "=", dan*i)
    print(f"{dan} x {i} = {dan*i}")