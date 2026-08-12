# 회원 정보 - member
member = {
    "name" : "최예윤",
    "age" : 26,
    "city" : "서울"
}

print(member)

member["age"] += 1
print(f"{member['name']}님은 {member['city']}에 사는 {member['age']}살입니다.")