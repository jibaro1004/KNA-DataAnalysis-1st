# 산술연산자
# + - * / //(몫) %(나머지) **(거듭제곱)
print(3 + 5)  # 8
print(10 - 4)  # 6
print(4 * 5)  # 20
print(20 / 4)  # 5.0 (나눗셈 결과는 항상 float)
print(7 // 2)  # 3

print(7 % 3)  # 1 ( 7개의 음료수를 3봉투에 나눠담으면, 2봉투와 1개의 음료수가 나옴 )
print(2**5)  # 32 ( 2의 5제곱 )


# =======================================
# 연산 우선순위와 우선순위 지정
# **(거듭제곱) > *(곱하기) /(나누기) //(몫) % (나머지) > +(더하기) -(빼기)

print(2 + 8 * 3)  # 8*3 연산 후 그 결과를 2와 더함
print((2 + 8) * 3)  # 괄호 안의 연산을 먼저한 뒤 곱하기 계산

# =========================================
# 복합연산자

result = 3 * 5
print(result)  # 15

# +=: 기존 값에서 오른쪽 값을 더한 뒤 재할당
# -=: 기존 값에서 오른쪽 값을 뺀 뒤 재할당
# *=: 기존 값에서 오른쪽 값을 곱한 뒤 재할당
# /=: 기존 값에서 오른쪽 값을 나눈 뒤 재할당

result += 10  # 25
result -= 5  # 20
result *= 3  # 60
result /= 2  # 30.0

print(result)


print("안녕" + "하세요")  # 안녕하세요

# 만약 "안녕"과 "하세요" 사이에 공백을 1개 넣고 싶다면
# 방법 1) , 사용

# 방법 2) 안녕 뒤에 공백 추가

# 방법 3) 공백만 있는 문자열 더하기

print("안녕", "하세요")
print("안녕 " + "하세요")
print("안녕" + " " + "하세요")


# 문자열 곱하기
print("안녕" * 5)  # 안녕안녕안녕안녕안녕

# 문자열에 연산자를 사용할 경우 모두 이어져서 나옴


# ==================== 실습 02 =====================
x = 3
y = 5
z = 7
average = (z + x + y) / 3
width = x**2
boopi = y * 5 * 7
print(average)
print(width)
print(boopi)


a = 17
b = 5
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a**b)


# ==================================
print("=== 비교연산자 ===")

# <(미만), <(초과), <=(이하), >=(이상), ==(같다), !=(다르다)
# 비교 결과는 무조건 True or False (bool)
print(7 < 16)  # True
print(7 > 16)  # False
print(7 <= 7)  # True
print(7 >= 7)  # True
print(7 == 7)  # True
print(7 != 7)  # False

# 비교 연산자는 문자열 비교도 가능
print("hello" == "hello")  # True
print("정상" == "정상")  # True
print("정상" == "정상")  # True
print("정상" == "정상")  # True

# 1. 대소문자 구분
print("hello" == "Hello")  # False

# 2. 공백이 있어도 다르다고 판단
print("정상" == "정상")  # False

# 부정연산자 != (not)
print("hello" != "hello")  # True (두 값이 동일한데 !로 인해서 값이 반대로 출력됨)
print("hello" != "hello ")  # False
print("hello" != "Helllo")  # True (느낌표는 결과를 뒤집는다)

# 변수로 비교연산자 사용
num1 = 123
num2 = 456

print(num1 >= num2)  # False
print(
    "num1" >= "num2"
)  # TypeError: '>=' not supported between instances of 'int' and 'str'

# 변수에 문자열을 할당하고, 변수로 문자열 비교
hi = "안녕"
hello = hi  # print(hello) > 안녕
print("===변수 hello(안녕)와 변수 hi(안녕) 비교===")
print(hello == hi)  # True

# ====================================================================

# and / or / not - 논리연산자
# and: 둘 다 True 여야 True를 반환
# 첫 번째 조건이 False 라면 뒤에 조건은 확인 안함 -> 정답 확률이 높은 애를 앞에 배치함

print(5 == 5 and 7 == 7)  # True + True = True
print(5 == 7 and 7 == 7)  # False + True = False
print(5 == 5 and 7 != 7)  # True + False = False
# or: 하나라도 True라면 True 반환
# 위 코드는 가능하다면 7!= 7 and 5=5 순서로 작성

print(5 == 5 or 7 == 7)  # True + True = True
print(5 == 7 or 7 == 7)  #

print(7 == 7 or 5 == 5)

print(1004 == 1004)
print(8945 != 4546)
print(1 > 5)
print(5 < 8)
print(4 >= 3)
print(98754243324 <= 456)

print("===실습4==")
temp = 85
temp_ok = 60 <= temp and temp <= 90
print(temp_ok)

pressure = 5
pressure_ok = pressure <= 7 and 3 <= pressure
print(pressure_ok)

print(temp_ok and pressure_ok)

print("====실습5===")
stock = 100
print(stock)
stock += 50
print(stock)
stock -= 30
print(stock)
stock += 5
print(stock)

print("==== 실습6 설비 지표 계산 실전====")
All_stock = 500
Error_stock = 23
Error_percent = 500 / 23
print(Error_percent, "%")
print(f"{Error_percent}%")

Running_time = 21
All_time = 24
Running_rate = 21 / 24
print(Running_rate * 100, "%")


print("=====실습 7 시간 변환, 상자 포장 도전=====")

All_running_time = 500  # 숫자는 따옴표를 붙이지 않고, 그대로 사용
print(All_running_time // 60)  # 분을 시간으로 바꿀 때 //를 사용
print(All_running_time % 60)  # 분을 그대로 쓰기 위해서는 그대로 사용
