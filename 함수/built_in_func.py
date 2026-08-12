# 내장 함수 - 파이썬에서 제공되는 함수
a = [1, 3, 5, 1]

print(sum(a)) #10
print(len(a)) #4
print(min(a)) #1

# 반올림 - round()
b = 352.567
print(round(b)) #353
print(round(b, 1)) # 352.6
print(round(b, 2)) # 352.57 (소수 둘째)
print(round(b, -1)) # 350.0 (일의 자리)
print(round(b, -2)) # 400.0 (십의 자리)

# 절대값 - abs(x)
print(abs(8)) #8
print(abs(-8)) #8

# 직접 만든 절대값 함수
def my_abs(x):
    if x >= 0:
        return x
    else: 
        return -(x)

print(my_abs(-8)) #8
