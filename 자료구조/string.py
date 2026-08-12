# 문자열 - string
# 인덱싱 - 1개 추출, 슬라이싱 - 여러개 추출
# s = ['s', 'k', 'y']
s = "python"
print(s[0])
print(s[0:2]) #py
print(s[:3]) #pyt
print(s[2:]) #thon
print(s[:-1]) #pytho

# split(구분기호) - 문자열을 리스트로 변환
fruit = "banana,grape,apple"
fruit_list = fruit.split(',')
print(fruit_list)  # ['banana,grape,apple']
print(fruit_list[0])

# replace() - 문자 수정(대체)
msg = "Hello, World"
print(msg)

msg = msg.replace("World", "Korea")
print(msg)

# strip() - 공백 제거
msg2 = "  hi, jun"
msg2 = msg2.strip()
print(msg2)

# 실습 9-1. 이메일 아이디 추출
mail = "user@naver.com"
mail = mail.split("@")
print(mail)

print("아이디: ", mail[0])
print("도메인: ", mail[1])
