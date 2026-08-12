# 산술 연산자

n1 = 7  #대입연산자('=')
n2 = 2

print(n1+n2, n1-n2, n1*n2)
print(n1/n2) # 나누기
print(n1 // n2) #나눗셈 
print(n1%n2) #나머지
print(n1 ** n2) #거듭제곱

count = 10
count += 2  # count = count + 2
print(count) #12

count -= 2  # count = count - 2
print(count) #10

count *= 2 # count = count * 2
print(count) #20

count /= 2 # count = count / 2
print(count) #10.0 (나누기는 실수로 출력됨)

#비교, 논리 연산자
a = 3
b = 4

print(a > b) #False
print(a < b) #True
print(a == b) #False
print(a != b) #True

#논리 연산자 - and, or, not
result = (a < b) and (a == b)
print(result) # T and F, False

result = (a < b) or (a == b)
print(result) # T or F, True

result = not (a != b) # not T -> False
print(result)


# 실습 8-1. 몫과 나머지 계산하기
bread = 30
people = 4

# 계산(연산)
share = bread // people # 몫
remain = bread % people  # 나머지

#출력
print("한사람 몫:", share, "개")
print(f"한사람 몫: {share}개")
print("남는 빵:", remain, "개")
print(f"남는 빵: {remain}개")
