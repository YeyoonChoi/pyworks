# 중첩 for(nested for)
# 5행 5열
for i in range(1, 6):
    for j in range(1, 6):
        print("가", end='')
    print()  # 줄바꿈
print("------------------")
for i in range(5):
    for j in range(5):
        print("*", end='')
    print()  # 줄바꿈



# 구구단 전체 출력
for i in range (2, 10):
    for j in range (1, 10):
        print(f"{i} x {j} = {i*j}")
    print()

for i in range(1, 6):
    for j in range(1, i+1):
        print("*", end='')
    print()  # 줄바꿈
print("------------------")


for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end="")
    
    for j in range(i):
        print("*", end="")
    
    print()