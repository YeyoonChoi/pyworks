# 딕셔너리 (dictionary) - 여러 개의 값을 저장
# 키(key)와 값(value)의 쌍(콜론으로 구분)
# 중괄호 - {} 사용
student = {
    "name": "한강", 
    "age": 21,
    "university" : "한국대학교"
    }

print(student)
print(type(student)) #<class 'dict'>

# 요소에 접근 (key로 검색)
print(student["name"])
print(student["age"])

# 요소 조회 (get(key))
print(student.get("university"))

# 요소 추가
student["major"] = "전자공학과"
print(student)

# 요소 수정
student["age"] = 25
print(student)

# 요소 삭제 - pop(key)
student.pop("major")

print(student.keys())
print(student.values())

# for문 사용
for key in student.keys():
    print(key, ':', student[key])