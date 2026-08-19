# 이차원 리스트 - 리스트 내부에 리스트를 포함한 자료구조
a = [
    [1, 2, 3], 
    [4, 5, 6]
    ]

print(a[0]) #첫째 행
print(a[1]) #둘째 행
print(a[0][0]) #1
print(a[0][1]) #2
print(a[0][2]) #3

# for문 출력
for row in a: 
    for x in row:
        print(x, end= " ")
        print()
