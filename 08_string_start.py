# """ """ _ 여러 줄 문자열

notice = """설비 점검 안내
1. 전원 확인
2. 센서 점검"""

print(notice)
# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검
# 위와 같이 직접 작성한 줄바꿈이 반영되어 여러 줄로 출력함


# 설비 점검 안내
# 1. 전원 확인
# 2. 센서 점검
#
# 개발자가 보기 편한 방식으로 작성하면 생각과 다른 결과물이 나옴


# 작성하는 개발자가 보기 편한 방식으로 출력했을 때 문제
notice = """
설비 점검 안내
1. 전원 확인
2. 센서 점검
"""

# 탭
notice = """설비 점검 안내
    1. 전원 확인
2. 센서 점검 """

print(notice)
# 삼중 따옴표는 탭도 그대로 유지됨

# =================================
# 이스케이프 문자

# notice 이스케이프 사용해서 개선
notice = "설비 점검 안내\n1. 전원 확인\n2. 센서 점검"
print(notice)

tap = "이름\t 상태"
print(tap)
print("이름 상태")

backslash = "이름\\상태"
print(backslash)  # 이름\상태 > 첫 번째 \는 이스케이프 문자라는 것을 알리는 용도

quotes = "It's me"  # 감싸는 따옴표와 str 내부 따옴표의 종류가 같을 때는 \를 사용
print(quotes)

# 빈 문자열과 공백 문자열의 차이
# "" 따옴표로 깜싸졌지만 아무것도 작성되지 않았따면 "빈 문자열"
# 빈 문자열은 글자 수 0, 길이 0
# " " 따옴표 안에 공백 (스페이스바)이 있는 경우는 "공백 문자열"
# 공백(스페이스바)의 수 만큼 글자가 있고, 길이가 세어짐
# 빈 문자열과 공백 문자열은 컴퓨터에게 다른 값으로 인식됨

print("" == "  ")  # False


code = "pump_A"
state = "정상"
hours = 1200
day = "2006-07-16"

card = (
    "설비: "
    + code
    + "\n상태: "
    + state
    + "\n가동: "
    + str(hours)
    + "시간\n점검: "
    + day
)
print(card)


# =============================
# 인덱싱 - 위치 번호로 글자를 하나 꺼내기
# 문자열 [인덱스번호]
# 문자열의 첫 글자 인덱스는 0
print("=== 인덱싱 ===")

word = "PYTHON"
print(word[0], word[3], word[5])  # P H N

abc = "abcdefghijklmnopqrstuvwnyz"
# 자기 이름 출력하기 (성 빼고)
print(abc[7], abc[14], abc[13], abc[6], abc[9], abc[-6])  # olivia

# 음수 인덱스는 뒤에서부터 역순으로 순서 숫자가 붙음
# 주의사항은 음수 인덱스는 가장 마지막 글자가 -1부터 시작

# ==========================
print("=== 슬라이싱 ===")

# 슬라이싱 - 구간으로 잘라내기
# 문자열[시작:끝]
# 시작 인덱스 글자는 포함해서 출력
# 끝 인덱스 글자는 제외하고 출력

print("word[3:5] 결과:", word[3:5])  # HO
print("word[3:6] 결과:", word[3:6])  # HON
# 슬라이싱은 end가 포함되지 않고 출력하기 때문에 없는 인덱스인 6도 사용할 수 있음

print(word[1])  # 인덱싱은 정확하게 마지막 인덱스까지만 쓸 수 있고, 넘치면 Error

# 슬라이싱 - start 생략
# 처음부터 특정 인덱스까지 구간을 뽑아내고 싶을 때 사용
print(word[:4])  # print(word[0:4]와 동일한 동작)

# 슬라이싱 - end 생략
# 특정 인덱스부터 끝까지 구간을 뽑아내고 싶을 때 사용
print(word[2:])  # 2번 인덱스부터 끝까지 출력
# print(word[2:6])과 동일한 동작

# 슬라이싱 - 전체 생략
print(word[:])  # print(word[0:6])와 동일한 동작
# :을 사용하고 start와 end를 모두 생략하면 모든 인덱스의 구간을 뽑아냄

# 슬라이싱 - 음수 인덱스 사용
print(word[-3:])  # HON
# 음수 인덱스 작성 시 그냥 그 인덱스부터 정방향으로 출력함
print(word[:-1])  # PYTHO
# 처음부터 -1(5)를 제외한 구간을 뽑아냄
# 역순 아님 주의
# 음수 인덱스 사용 시 컴퓨터가 알아서 정수 인덱스 찾아 치환해서 동작

# step으로 건너뛰기
# 문자열 [시작: 끝: 간격(step)]
print(word[0:6:2])  # PTO
# PYTHON 에서 첫 번째 글자는 명시했으니 거기서부터 출력
# step이 2이기 때문에 Y 띄고, T (두번째 점프) 출력
# H 띄고, O (두번째 점프) 출력
# N 띄고 끝
# 두 글자를 띄는게 아니라 두 번 띄는 것 (띈 그 자리 글자를 출력한다)

print(word[0:6:1])  # PYTHON

# start와 end를 생략하고 step만 입력 # PTO
print(word[::2])  # word 변수의 모든 글자를 두 칸씩 띄면서 출력

# 순서 뒤집기
print(word[::-1])  # NOHTYP
# step은 인덱스가 아니고, 음수 입력 시 문자열의 순서를 뒤집음

# 슬라이싱은 범위를 벗어나도 오류가 발생하지 않음
print("범위를 벗어난 슬라이싱", word[0:100])  # PYTHON을 정상 출력


print("==start:end로 구간 자르기==")
word2 = "PYTHON"
print(word2[0:3])
print(word2[2:5])

print("==start 생략==")
word3 = "temp_sensor"
print(word3[:4])

print("==end생략-끝까지==")
print(word3[5:])

print("== 음수 슬라이싱==")
word4 = "sensor_01"
print(word4[-2:])

print("실습 - step으로 건너뛰기")
word5 = "PYTHON"
print(word5[::2])

print("실습-문자열뒤집기")
print(word5[::-1])

# =======================
# len() - 문자열의 길이 반환
# len(문자열)

print("=== len () 활용 ===")
print(len("Hello World!"))  # 12 (공백자 모두 글자 취급)
print(len(""))  # 0 ( 빈 문자열은 0 출력)

var = "여러분~! 한 시간만 더 하면 됩니다! 조금만 더 힘을 내주세요 !"
print(len(var))  # 변수에 담긴 문자열의 길이 출력도 가능

print(len("이것도") - len("가능할까?"))
# len()은 int를 반환하기 때문에 연산 가능

print("abc 변수의 길이:", len(abc), " / 마지막 인덱스 번호:", len(abc) - 1)

# 음수 인덱스를 사용하지 않고 마지막 인덱스 문자를 뽑고 싶을 때
print(abc[len(abc) - 1])

phone_number = "01012345678"
print(len(phone_number))

# ==========================
print("====in 활용 ====")

# in - 특정 문자가 문자열에 포함되었는지 여부 확인
# "여부"를 확인하기 때문에 True 또는 False (bool) 으로 결과 반환

# 찾을문자열 in 문자열
print("고장" not in "설비 고장 발생")  # True
print("정상" not in "설비 고장 발생")  # False
print("설비에서 고장" not in "설비 고장 발생")  # False
print("설비에서 고장" not in "설비에서 고장이 났습니다.")  # False

# not in - in의 정반대 동작

print(" " in "설비 고장 발생")  # True
# 따옴표로 감싼 공백(스페이스바)는 정말 "한 글자"로 취급

# =============================================
print("=== count() ===")

# . count() - 문자열에 특정 글자의 수(int)를 반환
# 문자열.count("찾을 글자")
print("banana".count("a"))  # 3
print("010-1234-1234".count("-"))  # 2

print("실습-count로 갯수 세기")
print("a,b,c,d".count(","))

# ========================
print("=== find()===")
# 전달받은 글자가 "첫 번째"로 나오는 위치 인덱스 반환
# 찾는 글자가 없다면 -1을 반환
email = "hong@comapny.com"
print("hong@company.com")
at = email.find("@")  # @ 위치의 인덱스인 4가 할당
user_id = email[:at]  # hong 이라는 사용자의 아이디만 추출
print(user_id)

# SQE-00Q8이라는 설비의 SQE만 뽑아내기 (find와 슬라이싱 사용)
sqe = "SQE-00Q8"

sqe_index = sqe.find("-")
print(sqe_index)  # 3
sqe_fin = sqe[:sqe_index]  # sqe[0:3] > SQE
print(sqe_fin)  # SQE


# =========================
print("==== index() ====")

# 특정 문자열의 위치(인덱스 번호)를 반환
# 앞에서부터 가장 처음 나오는 인덱스 번호만 반환
# 찾는 문자열이 없으면 Error 발생

email = "jibaro@spreatics.com"
at = email.index("@")  # 5
print(email[0:at])  # jibaro
print(email[:at])  # 시작 번호가 0이라면 start 생략 가능
print(email[at:])  # 끝까지 출력하고 싶고, 뒤에 몇 글자가 있는지 모르니 생략
# 위처럼 시작하면 5번 인덱스부터 출력하기 때문에 @을 포함
print(email[at + 1 :])  # at+1을 하면 @을 포함하지 않고 출력

# find에서 했던 SQE 뽑아내기 실습 index 사용으로 바꾸기
print("===find에서 했던 SQE 뽑아내기 실습 index 사용으로 바꾸기")
sqe = "SQE-12345"
sqe_index = sqe.index("-")  # - 있으니 정상 동작
print(sqe_index)  # 3
sqe_fin = sqe[:sqe_index]  # sqe[0:3] > SQE
print(sqe_fin)  # SQE

# 만약에
# sqe_index = sqe.index("/") # / 없으니 Error 나고 중단


# ======================
print("=== count() ===")

# 문자열에서 특정 문자열의 갯수 세기

str = "a, b, c, d, e, a, a"

# a의 갯수 세기
print(str.count("a"))  # 3

# ,의 갯수 세기
print(str.count(","))  # 6

print(str.count(", "))  # 5 # count로 찾는 문자열과 완전히 동일해야 갯수를 셈

# ====================
print("=== startswith() ===")

# 특정 문자열로 시작하는지 검사
# True/False (불리언)

# EQP로 시작하는지 검사하기
print("EQP-001".startswith("EQP"))

# 변수 활용
eqp = "EQP"
print("EQP-001".startswith(eqp))
# 주의사항) 변수명은 따옴표 감싸기 금지 !!!!


# =====================
print("==== endswith() ====")

# 특정 문자열로 끝나는지 확인
# True / False 로 반환

str2 = "월요일입니다! 여러분은 할 수 있어요!"

print(str2.endswith("!"))  # True
print(str2.endswith("요!"))  # True
print(str2.endswith("음!"))  # False
print(str2.endswith("월요일입니다! 여러분은 할 수 있어요!"))  # True
print(str2.endswith(" 월요일입니다! 여러분은 할 수 있어요!"))  # False
print(str2.endswith(" 월요일입니다!           여러분은 할 수 있어요!"))  # False

# 실습 5. 시작과 끝 확인하기

str3 = "sensor_log.csv"
print(str3.startswith("sensor"))
print(str3.endswith(".csv"))

# =========================
print("=== 값은 객체다 ====")

print(type("잊어먹으면 안돼."))  # <class 'str'>
print(len("이렇게 썼죠??"))
# endswith와 len의 차이는?
# endswith는 .으로 연결
# .으로 연결하는 이런 도구들은 "메서드"
# 문자열이나 int, float처럼 특정 자료형(객체) 내부에 포함된 기능
# len은 . 사용 안함
# ()-> 함수
# len과 같이 개발자가 직접 선언하지 않은 기본 제공 함수 "내장함수"

# "str".startswith("s")
# 123.startswith(1)
# .으로 사용하는 메서드들은 특정 자료형(객체 타입)마다 다름
# int 자료형의 객체에는 startswith라는 메서드가 없음 (결국 문자는 되지만, 숫자는 startswith 메서드가 없음)

# print(len(123))  # len 내장함수는 길이를 반환하기 때문에 int 자료형은 사용 불가

# =============
# 재할당 복습

num = 1
num = num + 1  # 2
num += 1  # 3
# += 은 복합할당연산자
# 원래 내 자신의 값에 다음 오는 연산자와 값을 적용해서 재할당

# ================
print("=== .upper() ===")

str4 = "abcdefg"
print(str4)  # abcdefg

str4.upper  # ABCDEFG > 반환은 대문자인데, 값에 재할당은 X
print(str4)  # abcdefg > 기존 str4의 값인 소문자를 그대로 출력


# 앞으로 계속 대문자로 변환한 값을 사용하고 싶다면
# 변수에 재할당
# 변수 재할당에서 변수 스스로를 부르는 것이 가능
# 재할당에서 변수 스스로 값을 부르려면 무조건 "재할당"이어야 함

str4 = str4.upper()

# 최초 변수 할당 시에는 저장된 값이 없어서
# 변수 스스로 값을 불러와 할당 불가능
# str5 = str5.upper()

# =======================
print("========= 실습 1. 대문자로 바꾸기 ===========")

B = "WARNING"
big = B.upper()
print(big)

# =======================
print("========= 실습 2. 소문자로 바꾸기 ===========")

s = "WARNING"
small = s.lower()
print(small)

# ================================================================
user_name = "kim chul soo"

# capitalize는 문자열의 첫 글자만 대문자로 변환
print(user_name.capitalize())  # Kim chul soo

# title은 띄어쓰기 기준으로 각 단어의 첫 글자들을 모두 대문자로 변환
print(user_name.title())  # Kim Chul Soo

# '를 사용한 경우 다른 단어로 인식
print("i'm full".title())  # I'M Full
print("i'm full".title())  # I'M Full

# ================================================================
print("=======실습 5 대문자인지 소문자인지 검사하기======")

hi = "ABC"
print(hi.isupper())
hi2 = "abc"
print(hi2.islower())
hi3 = "Abc"
print(hi3.isupper())

# ================================================================
print("======== 실습 6. 파일명 규칙 한 번에 점검하기 ==========")
silsup = "Sensor_LOG.CSV"
low = silsup.lower()
print(low.startswith("sensor"))
print(low.endswith(".csv"))

# ================================================================
print("==== .strip() ====")

# 공백제거
# .strip(): 앞과 뒤의 모든 공백 제거 (중간 띄어쓰기는 그대로 유지)
# .lstrip(): left(왼쪽) 공백만 제거
# .rstrip(): right(오른쪽) 공백만 제거

raw = "     정상      "
print(raw.strip())  # "정상"
print(raw.lstrip())  # "정상         "
print(raw.rstrip())  # "            정상"

# 문자열의 가운데 공백은  strip으로 지우지 못함
print("         정          상".strip())  # wjd

print(raw)  # "     정상      "
# strip은 재할당이나 새 변수에 할당하지 않는 이상 휘발

# strip으로 문자 제거
str5 = "===정상==="
print(str5.strip("="))  # 정상
# 인자로 전달한 양 끝의 =이 모두 지워짐

str6 = "=정상=========="
print(str6.strip("="))  # 정상
# 갯수 상관 없이 인자로 전달한 문자를 무조건 삭제
print(str6.strip("=  "))  #  정상
# strip 자체가 공백을 지우는 것이기 때문에
# 공백 상관없이 양 끝의 해당 문자열 삭제

str7 = "==정==상===="
print(str7.strip("="))  # 정==상
# 글자 중간에 있는 문자열은 건드리지 않음

raw = "    NORMAL     "
step1 = raw.strip()  # 'NORMAL'
clean = raw.strip().lower()  #'normal'
print(clean)

# ===============================
print("==== 체이닝 ====")

raw = "      NORMAL     "
# 체이닝 X
step1 = raw.strip()  # "NORMAL"
step2 = step1.lower()  # "normal"

# 체이닝 X, 기존 변수에 재할당
raw = raw.strip()
raw = raw.lower()

# 체이닝 O -> 이걸 가장 자주 사용함
chain = raw.strip().lower()  # "normal"

# 기존 변수에 재할당도 가능 -> 이걸 가장 자주 사용함
raw = raw.strip().lower()

# 변수에 할당하지 않고 사용 가능
print(raw.strip())

# ===================================================

print("=======실습11.결과를 변수에 다시 저장하기=========")
str = "           Warning         "
str = str.strip()

print("[" + str + "]")
str = str.strip().lower()
print("[" + str + "]")

# strip() 메서드에 인자로 들어가는 문자열은 완전히 동일하지 않아도 전부 삭제가 됨

str8 = "aaaaab 이렇게? cd"
print(str8.strip("abcd"))  # " 이렇게? "
print(str8.strip("abcd "))  # "이렇게?"
print(str8.strip("bc"))  # "aaaaab 이렇게? cd"
print(str8.strip("ab)"))  # " 이렇게? cd"

# ==================================================
print("=== replace() ===")

# 특정 문자열을 제거하거나 치환할 때 사용
# .replace("바꾸고싶은문자열", "바꿀문자열")
# 제거할 때는 인자의 두 번째를 ""(빈 문자열)로 작성
print("정 상 가 동".replace(" ", ""))  # 정상가동 (중간 공백 제거)
print("    정             상 가  동".replace(" ", ""))
# 정 상 가 동 (공백이 2칸 붙어 있는 경우만 제거)
# " 정 상 가 동"

# 글자 치환
print("고장".replace("고장", "fault"))  # fault
print("고장".replace("고", "fault"))  # fault장

# 단어 치환
str9 = "설비 정상 가동"
print(str9.replace("정상", "점검"))  # 설비 점검 가동

# replace() 체이닝
num = "    010-1234-1234   "
num = num.replace(" ", "").replace("-", "")  # 01012341234

# ===================================================
print("=== split() ===")
# 문자열 자르기
# 결과는 대괄호에 감싸진 "리스트" 자료형
# 리스트는 순서가 있기 때문에
# 왼쪽에서부터 0으로 시작하는 인덱스가 자동 생성

drinks = "에스프레소 아메리카노 카페라떼"
print(drinks.split())  # 인자를 보내지 않음
# ['에스프레스', '아메리카노', '카페라떼']
# "띄어쓰기"를 기준으로 나뉘어진 세 개의 문자열을 대괄호에 감싸서 반환함

# 구분자를 특정하고 싶은 경우
fruits = "딸기,거봉,키위,사쿠란보"
print(fruits.split(","))  # 문자열 콤마를 기준으로 분할
# ['딸기', '거봉', '키위', '사쿠란보']

fruits2 = "딸기, 거봉, 키위, 사쿠란보"
print(fruits2.split(", "))  # 문자열 콤마+ 공백 1칸을 기준으로 분할
# ['딸기', '거봉', '키위', '사쿠란보'] > 공백 그대로 유지

# 리스트의 인덱스
fruits_list = fruits.split(",")
print(fruits_list)  # ['딸기', '거봉', '키위', '사쿠란보']

# 거봉만 출력하기
# 출력하고자 하는 요소의 인덱스를 대괄호로 감싸서 호출
print(fruits_list[1])  # 거봉
print(fruits_list[3])  # 사쿠란보
print(fruits_list[-1])  # 사쿠란보 > 음수 인덱스가 있으므로 작동함

# split 횟수 제한
num = "010-1234-1234"
# ["010", "1234-1234"]
print(num.split("-", 1))

# ===================================
print("======실습 3. 쉼표 기준으로 나누기=====")
alphabet = "a,b,c,d"
print(alphabet.split(","))

# ===================================
print("=== join()---")
# 리스트를 하나의 문자열로 합침
# "구분자".join(리스트)
# 모든 요소가 합쳐져서 하나의 문자열로 반환

fruits_list = ["딸기", "거봉", "키위", "사쿠란보"]

print("-".join(fruits_list))  # "딸기-거봉-키위-사쿠란보"
print(",".join(fruits_list))  # "딸기,거봉,키위,사쿠란보"
print(", ".join(fruits_list))  # "딸기, 거봉, 키위, 사쿠란보"

# ==================================
print("======실습5.리스트 합치기=======")
date_list = ["2025", "01", "15"]
print("-".join(date_list))

# ========= 방법 1. 실습 python을 pyThon 으로 출력하기 =================
word = "python"
print(word.replace("thon", "Thon"))

# ========= 방법 2. 슬라이싱 + T만 upper 사용 ==========================
print(word[:2] + word[2].upper() + word[3:])

# ========= 방법 3. 인덱싱으로 글자 하나씩 연결 =========================
print(word[0] + word[1] + word[3].upper() + word[4] + word[5])

# ==========================================
print("=== print 함수의 sep, end ====")

print("2026", "07", "27")  # 2026 07 27 (기본적으로는 공백 1칸)

# sep 속성을 사용하면 구분을 공백이 아닌 특정 문자열로 가능
print("2026", "07", "27", sep="사랑해")  # 2026사랑해07사랑해27
# 공백 대신 sep 속성에 전달한 문자열이 삽입되어 이어짐

print("안녕", "하세")  # 안녕하세
print("안녕", "하세", end="요")  # 안녕 하세요
# end 속성 사용 시 출력문 마지막에 해당 문자열이 붙어 삽입

# print("안녕", "하세", end="요", "ㅎㅎ") # end 속성 뒤에 또 인자

# print 함수 + 사용 시 sep과 end
print("안녕" + "하세", end="요" + "이렇게?!")

# 기본적으로 print문에는 sep으로 공백 한 칸,
# end로 /n(줄바꿈)이 적용되어 있음

print("========실습 7. 구분자 통째로 바꾸기========")
raw = "2026/07/27"
parts = raw.split("/")
print("-".join(parts))

print("========실습 8. CSV 한 줄에서 값 꺼내 정리하기============")
t = "1,NORMAL,25.3"
parts = t.split(",")
status = parts[1].strip().lower()
print(status)

# ===================================================
print("====실습 1.f-string 으로 변수 끼워 출력하기====")
name = "온도기"
temp = 25
print(f"설비{name}, 온도 {temp}도")

# ===================================================
print("=== f- string ===")

name = "PUMP_A"
temp = 36

# 설비 PUMP_A, 온도 36도
# print("설비 " + name + ", 온도 " + str(temp))

# f-string
print(f"설비 {name}, 온도 {temp}도")

# f- string 연산
hour = 12

# 우리는 하루에 8시간 수업을 듣고, 이는 480분입니다.
print(f"우리는 하루에 {hour}시간 수업을 듣고, 이는 {hour * 60}분입니다.")

# ==================================================
print("===== 실습 2. f-string 안에서 계산하기=====")

score1 = 99
score2 = 96
score3 = 98

print(f"평균점수는 {(score1 + score2 + score3)/3} 입니다.")

# ==================================================
print("===== 실습 3. 소수점 자릿수 지정하기 =====")
value = 87.456
print(f"{value:.1f}")
print(f"{value:.2f}")

# ==================================================
print("==== 실습 4. 센서 로그 한 줄 정리 리포트 만들기 ====")
raw = "5, sensor_2, WARNING, 0.78912"
parts = raw.strip().split(",")
sid = parts[1].strip()
status = parts[2].strip().lower()
value = float(parts[3].strip())
print(f"[센서{sid}] 상태 {status}, 측정값 {value:.2f}")
