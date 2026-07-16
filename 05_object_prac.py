count = 5
temp = 45
str = "풍력발전기"
is_ok = True
print(count, temp, str, is_ok)


print(type(count))
print(type(temp))
print(type(str))
print(type(is_ok))


print(type(100))  # 예상: int
print(type(100.0))  # 예상: float!
print(type("100"))  # 예상: str
print(type(is_ok))  # 예상 : bool

print(5 + 3)
print("5" + "3")
print("12" + "45")

print(3 > 2)
print(5 == 5)
print(type(3 > 2))

count = 3
print(type(count))
count = 3.0
print(type(count))
count = "3"
print(type(count))

device_temp = 3.4
check_count = 4.55
device_name = "배고픈 설비"
is_normal = False

print(5 > 3)


# ==== 실습 - 숫자 입력받아 계산하기 ====

birth_year = int(input("태어난 해를 입력하세요."))
age = 2026 - birth_year
print("나이", age, "세")


# < 여기서부터 07_input_실습실임>
# ==== 실습 - 입력값 비교해 출력하기 ====

temp = int(input("온도 1: "))
print("80초과?: ", temp > 80)
print("0 이상?", temp >= 0)

# ==== 실습 - 입력, 변환, 계산, 비교 출력 (종합) ====
score1 = int(input("점수1 : "))
print(score1 >= 60)
score2 = int(input("점수2: "))
print(score2 >= 60)
avg = (score1 + score2) / 2
print("60 이상?", avg >= 60)
