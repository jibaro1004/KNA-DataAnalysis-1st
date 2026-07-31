# tuple: 값을 묶어주는 역할
# () 소괄호 안에 쉽표로 나누어서 여러가지 자료형의 값을 저장
# 그리고 마지막 값에는 꼭 ,를 붙여야 Python이 튜플로 인식을 함
# 짝지어진 값을 하나로 묶을 때 사용 가능한 자료형

sensor = ("모터온도", 78)  # 괄호 있고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))
# <class 'tuple'>

sensor = 78  # 괄호 없고, 끝에 쉼표 없음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))
# <class 'int'>

sensor = (78,)  # 괄호 있고, 끝에 쉼표 있음
print("sensor: ", sensor)
print("type(sensor): ", type(sensor))
# <class 'tuple'>

print("seonsor: ", sensor)
print("type(sensor): ", type(sensor))

# 요소 갯수
# 요소 2개 이상: 쉼표가 있다면 튜플
# 요소 1개: 쉼표 여부
# 요수 0개(빈 튜플): () 빈 괄호

# 튜플에서 많이 헷갈려하는 부분
# (1): int
# (1,): tuple

# (1, 2, 3,) -> 가장 마지막에 쉼표를 붙여서 튜플임을 명시
# (1, 2, 3) -> 튜플 맞음

# 튜플의 인덱스
print(sensor[0])  # 모터온도

# 튜플의 슬라이싱
s = ("a", "b", "c", "d", "e")
print(s[1:4])
# 슬라이싱한 결과는 소괄호에 감싸져 있음
# 튜플은 슬라이싱해도 튜플
print(type(s[1:4]))  # <class 'tuple'>

# 튜플 언패킹
# 튜플에 담긴 값을 변수로 한 번에 분리

# 복습) 복수의 변수 한 번에 선언
a, b, c = "a", "b", "c"
print(a)  # 문자열 a
print(b)  # 문자열 b
print(c)  # 문자열 c

unpacking(
    1,  # 변수 one
    2,  # 변수 two
    3,  # 변수 three
)

unpacking = one, two, three
# one, two, three 라는 알 수 없는 변수를
# unpacking 변수에 할당하겠다는 의미
# 동작 X

# one, two, three = unpacking  # Error 발생
# unpacking이라는 변수에 담긴 튜플 내부의 값들을
# 할당 연산자 왼쪽 one, two, three 변수에
# 풀어서 담는다는p
one, two, three, four = [11, 22, 33, 44]
print("one:", one)
print("two:", two)
print("three:", three)
print("four:", four)
# 가능 !

# 튜플의 언패킹은 변수의 개수와
# 튜플에 담긴 값의 개수가 동일해야 함

# 리스트 언패킹이 가능할까?
one, two, three, four = [1, 2, 3, 4]

# =======================================================================

tup = (
    "normal",
    "normal",
    "warning",
    "normal",
    "warning",
)

# 튜플의 길이
print(len(tup))  # 5

# 특정 값의 갯수 세기
print(tup.count("warning"))  # 2
print(tup.count("Warning"))  # 0

# 특정 값이 처음 나온 인덱스 찾기
print(tup.index("warning"))  # 2
# 찾고자 하는 값이 없으면 Error 발생 (원래 밑에는 Warning 이었음)
print(tup.index("warning"))  # ValueError: tuple.

# ========================================================

# 튜플 리스트
# 리스트 안에 튜플을 담은 것을 표현
# for문으로 리스트를 사용해서
# 리스트 내부의 튜플에 접근하고
# 튜플에 담긴 값을 사용할 수 있음

# 언패킹을 사용해서 접근한 튜플 내부의 값을
# 변수에 바로 할당해서 접근

hour_13 = [
    ("모터온도", 77),
    ("모터진동", 0.2),
    ("모터 압력", 91),
]

now = 0

for name, value in hour_13:
    now += 1
    print(now, "번째 반복")
    print("name:", name, "value", value)

# ========================================

temps_13 = [
    ("qox_001", 81),
    ("qox_002", 88),
    ("qox_003", 95),
    ("qox_004", 89),
]

warning = 90

for name, temp in temps_13:
    if temp >= warning:
        print("경고", name, "설비 온도 이상")

# 리스트 안의 튜플 갯수가 늘어나면
# for문에서 변수를 여러 개 작성하면 됨

tup_list = [
    ("일", "one", 1, "1"),
    ("이", "two", 2, "2"),
]

# for문에서도 언패킹 할 때는 무조건 튜플의 값 갯수와
# for문의 변수 갯수 통일
# 통일하지 않을 경우 Error 발생
for kor_str, eng_str, num, num_str in tup_list:
    print("kor_str:", kor_str, "eng_str", eng_str, "num:", num, "num_str:", num_str)

# ===================================================

# 튜플 리스트 정렬
# sorted ()를 사용하여
# 튜플의 특정 값 기준으로 리스트를 정렬

temps_13 = [
    (81, "qox_001"),
    (88, "qox_002"),
    (95, "qox_003"),
    (89, "qox_004"),
]

# sorted()는 원본 배열을 수정하지 않고
# 새 리트를 반환해줌
hot = sorted(temps_13, reverse=True)
print(hot)
print("원본: ", temps_13)  # 정렬 적용 X

# ================================================
print("=== 실습 1. 센서를 튜플로 묶고 꺼내기 ===")
s1 = ("모터온도", 78)
print(s1)  # ('모터온도', 78)
print(s1[0])  # 모터온도
print(s1[1])  # 78
name, value = s1  # 언패킹
print(name, value)  # 모터온도 78

# ========================================================

print("=== 실습 2. 튜플 리스트를 반복 처리하기 ===")
sensors = [
    ("모터온도", 78),
    ("회전속도", 1750),
    ("펌프압력", 95),
    ("유량", 42),
]
for name, value in sensors:
    print(name, value)
limit = 90
for name, value in sensors:
    if value > limit:
        print(name, "경고")  # 회전속도 경고 / 펌프압력 경고

# =================================================
print("=== 실습 3. 중첩 튜플로 센서 위치 관리하기 ===")
sensors = [
    ("모터온도", 78, (3, 5)),
    ("베어링진동", 0.5, (7, 2)),
    ("펌프압력", 95, (4, 8)),
]
for name, value, pos in sensors:
    x, y = pos
    print(name, "위치:", x, y)
for name, value, pos in sensors:
    x, y = pos
    if x <= 5:
        print(name, "1구역")  # 모터온도 / 펌프압력

# ===============================================
# set
# 자동 중복 제거
# 순서가 없음
# 형태가 중괄호로 감쌈

# 빈 set 만들기
empty_list = []  # 빈 리스트
print(type(empty_list))  # <class dict>
# 빈 중괄호는 딕셔너리라는 다른 자료형으로 생성

# 빈 셋은 무조건 set() 내장함수를 사용
real_empty_set = set()
print(type(real_empty_set))  # <class 'set'>

# 값을 포함한 셋 만들기
logs = ["S01", "S02", "S01", "S03", "S01"]

# 리스트를 {}에 감쌀 경우
# TypeError: cannot use 'list' as a set element
# unique = {logs}

# set() 사용
unique = set(logs)
print(type(unique)) # <class 'set'>
print(unique) # {'S01', 'S02', 'S03'}
# unique 셋에는 기존 중복되었던 S01이 한 번만 들어감
# 지금은 길이가 짧아서 순서대로 정렬된 것처럼 보이지만
# 셋은 순서가 없는 값의 묶음
print(unique[0]) # TypeError
# set에서 인덱스 사용 시 Error 발생

# set에 바로 여러 값을 작성
unique = {"S01", "S02", "S01", "S03", "S01"}
print(type(unique)) # <class 'set'>
print(unique) # {'S01','S02', 'S03'}

# set을 사용해서
# 리스트에 들어있는 고유한 종류의 수를 알 수 있음
print(len(unique)) # 3

empty_tuple = ()  # 빈 튜플
print(type(empty_tuple))

# 복수의 값을 중괄호에 감싸서 작성

# =====================================

# 셋에 값 추가하기
# .add(추가할값)
# 이미 있는 값을 추가할 경우 무시

alerts = {"S01", 'S02"}

# 경고 상태인 S03이 추가될 경우
# .add()를 사용해서 추가
alerts.add("S03")
print(alerts)


# S01에서 또 경고가 발생
# 이미 S01은 경고가 발생한 적이 있고
# alerts라는 셋에는 경고가 발생한 센서만 저장하고 싶음
# 횟수 상관없이
# 이럴 때 set을 쓰면 편리함
alerts.add("S01")
print(alerts) # {'S02', 'S03', 'S01'}
# S01이라는 값을 또 넣어도 무시하고 한 번만 저장
# 그래서 독립적인 값을 저장하기에는 아주 편리함