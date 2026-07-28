# list는 python의 자료형 중 하나
# 여러 개의 값을 [대괄호]에 감싸서 순서대로 저장
# 나열된 값들은 자동으로 각자의 인덱스 번호를 순서대로 가지게 됨

temps = [35, 36, 37, 38]  # int 리스트
float_temps = [36.4, 36.5, 36.6, 36.7]  # float 리스트
machines = ["펌프", "압축기", "모터"]  # string 리스트

# 리스트는 자료형이 달라도 한 리스트에 담을 수 있음
mixed = ["펌프", 78, True]

# 리스트에 자동으로 순서 인덱스가 붙는다면?
print(temps[2])  # 37 > 인덱스로 해당 순서에 위치한 요소 뽑아내기 가능

# 리스트 안에 몇 개의 값이 담겼는지 모르지만 마지막 요소를 뽑고 싶다면?
print(temps[-1])  # 가장 마지막 요소 출력

# 빈 리스트
empty = []

# 리스트에 담긴 값의 갯수 세기
# len() 내장함수 사용
print(len(temps))  # 4
print(len(empty))  # 0

# 리스트의 담긴 값의 갯수 변수에 저장
temps_length = len(temps)  # 변수에 4라는 값이 할당
print(temps_length)  # 4

# =====================================
print("===========실습 1. 나만의 데이터 리스트 만들기 =========")

weather = [30, 27, 26, 32, 34]
print(weather)
print(len(weather))

today = []
print(len(today))

# ======================================
# 없는 인덱스 호출
# temps 리스트는 길이가 5
# print(temps[5])  # IndexError: list index out of range
# 인덱스 범위를 벗어나지 않도록 유의

# ========================================
print("=============== 실습 2. 인덱스로 값 꺼내기=========")
weather2 = [35, 30, 32, 34, 38, 34]
print(weather2[0])
print(weather2[2])
print(weather2[-1])

# =======================================
print("================ 실습 3. 인덱스로 꺼낸 값 계산하기 ===============")
first = weather2[0]
last = weather2[-1]
print(first + last)
print((first + last) / 2)

# 리스트의 자료형
print("=== 리스트의 자료형===")

# temps라는 리스트 자체
# print(f"temps: {temps}")
# print(type(temps): {type(temps)}) # <class 'list'>

# temps라는 리스트의 0번째 인덱스 요소
print(f"temps[0]: {temps[0]}")
# print(type(temps[6]))

# 다른 자료형의 값이 들어있는 리스트의 요소 타입
# float 값이 들어있는 float_temps 리스트의 0번째 요소
print(type(float_temps))  # <class 'float'>
print(type(machines[0]))  # <class 'string'>

# 퀴즈
# mixed = ["펌프", 78, True]

print(type(mixed[1]))  # <class 'int'>

# 리스트 슬라이싱
# 리스트명[시작:끝:간격]
# 시작, 끝, 간격 인덱스는 모두 생략 가능 (문자열과 동일)

# temps = [35, 36, 37, 38]
print(temps[1:3])  # [36, 37]
print(temps[1:2])  # [36]
print(temps[:2], temps[3:])  # [35, 36]
print(temps[:2], temps[3:])  # [35, 36] [38]
print(temps[::1])  # [35, 36, 37, 38]
print(temps[::3])  # [35, 38]
print(temps[100:999])  # [] > 슬라이싱은 없는 인덱슬르 넣으면 빈 값을 반환

# 인덱싱 vs 슬라이싱
# 인덱싱 temps[0]은 값 하나(35)
# temps[999]와 같이 없는 인덱스 사용 시 에러


# 슬라이싱 temps[0:2]은 리스트([35, 36])
# 슬라이싱은 영역을 잘라내는 역할이기 때문에 리스트를 반환하는 것
# temps[100:999] 에러 발생하지 않음
# 슬라이싱은 '있는 만큼만' 잘라주기 때문에 에러 발생하지 않음

# ================================================================
print("===== 실습 4. 슬라이싱으로 구간 자르기 =====")
temperature = [17, 25, 20, 28, 27, 26, 24, 25, 24, 26]
print(temperature[:2])
print(temperature[-3:])
print(len(temperature[-3:]))

# =================================================================
print("========실습 5. 데이터를 두 구간으로 나누기 ==========")
hours = [5, 4, 3, 6, 42, 78, 56, 45, 21, 20, 24, 28]
first = hours[:6]
print(first)
second = hours[6:]
print(second)
print(len(first), len(second))

# ===================================================================

# 인덱스로 특정 값 바꾸기
# temps = [35, 36, 37, 38]

print("원본:", temps)
temps[2] = 999
print("2번 인덱스 값 변경 결과:", temps)

# in (존재 확인)
# machines = ["펌프", "압축기", "모터"]
print("펌프" in machines)  # True
print("펌프" not in machines)  # False

print("프레스" in machines)  # False

# =================================================================
print("=========실습 6. 값 찾아 바꾸기===========")

# 특정 값의 인덱스 찾기
# 리스트.index(찾고자하는값)
# machines = ["펌프", "압축기", "모터"]

i = machines.index("압축기")
print(i)  # 1

# .index() 메서드는 리스트에서 가장 처음 등장하는 인덱스만 반환
machines2 = ["펌프", "압축기", "모터", "압축기"]

i2 = machines.index("압축기")  # 1, 3번 인덱스 모두 값이 동일하지만
print(i2)  # 1 > 출력은 첫 번째로 찾은 1만 함

# =========================================================
temps = [24, 25, 36, 38, 240]
print("240" in temps)
i = temps.index(240)
temps[i] = 24
print(temps)
print("240" in temps)

# 리스트 값 추가
# .append(추가할값)
# 리스트의 가장 마지막에 값을 추가
# 리스트 원본이 수정 (재할당 필요 X)
nums = [1, 2, 3, 4, 5]

nums.append(999)
print(nums)

# 만약 원본 리스트와 특정 값을 추가한 리스트 둘 다 필요하다면
# 원본 리스트를 복사해서 리스트 수정 진행
# nums = [1, 2, 3, 4, 5] > 기존 리스트는 원본으로 둠
new_nums = nums  # 스스로의 메모리를 할당받지 않고, 메모리 주소만 복사
print(new_nums)  # [1, 2, 3, 4, 5, 999]

new_nums.append(111)
print("원본 nums 리스트:", nums)
# 기대 결과: [1, 2, 3, 4, 5, 999]
# 실제 결과: [1, 2, 3, 4, 5, 999, 111]
# 복사한 메모리 주소에 append를 했기 때문에 원본까지 영향을 받음

# 이를 해결하기 위해서 .copy()라는 메서드를 사용
# new_nums2는 새로운 메모리에 nums 배열을 새로 저장
new_nums2 = nums.copy()
new_nums.append(222)  # nums 배열에 영향을 미치지 않고 사용
print("원본 nums 리스트:", nums)
print("복사본 new_nums2에 222 append 결과:", new_nums2)

# .insert(위치, 값)
# 리스트에서 원하는 위치에 값을 삽입
# 원본 배열에서 바로 삽입
# 기존 배열에서 삭제는 되지 않고, 해당하는 인덱스 값이 삽입 (뒤에 요소들은 인덱스 +1)
nums.insert(3, 333)
print(nums)

# extend()
# 리스트 연결
# 다른 리스트의 값들을 "풀어서" 이어붙임
data = [1, 2, 3]
new_data = [7, 8, 9]
data.extend(new_data)
print(data)


# 함수의 반환 개념을 안 뒤에 확인할 내용
print(data.extend(new_data))
# 기대 결과:  [1, 2, 3, 7, 8, 9]
# 실제 결과: None
# extend() 메서드는 data라는 리스트를 "수정" 이를 반환하지 않음
# 반환값이 없어서 print를 할 값이 없는 것
print(data)  # [1, 2, 3, 7, 8, 9]

# 정리
# 오늘 꼭 알아야 하는 리스트 값 추가 메서드와 개념
# .append(추가할 값): 리스트의 가장 마지막에 값을 추가
# .insert(위치, 값): 첫번째 인자인 위치 인덱스에 값을 삽입
# .extend(합칠리스트): 두 리스트를 하나의 리스트로 합체
# 위 세 가지 메서드들은 원본 리스트 자체를 수정

# ==================================================
print("===========실습 7. 측정값 추가하기===========")
temps = []
temps.append(30)
print(temps)  # [30]
temps.insert(0, 28)
print(temps)  # [28, 30]
temps.extend([31, 32])
print(temps)  # [28, 30, 31, 32]

# ==================================================

# 리스트에서 요소 삭제
# .remove(값): 위치는 모르고 삭제할 "값"만 알 때 사용하는 요소 삭제 메서드
list1 = ["딸기", "사과", "수박", "배", "포도", "망고"]
list1.remove("수박")
print(list1)

# .pop(인덱스): 인덱스로 특정 요소를 삭제할 때 사용
# 삭제한 인덱스의 값을 반환
list1.pop(0)
print(list1)
print(list1.pop(2))  # 삭제한 인덱스 2번의 값을 출력

# 삭제도 하고, 삭제한 인덱스 값도 출력

# del: 인덱스로 리스트의 요소 삭제 (슬라이싱으로 영역 삭제 가능)
del list1[0]
print(list1)

del list1[:]
print(list1)  # [] > 빈 리스트가 됨

# del 건너뛰기
list2 = ["빨강", "노랑", "초록", "파랑", "남색"]
del list2[::2]  # "빨강", "초록", "남색"을 삭제하겠다는 의미
print(list2)  # ["노랑", "파랑", "보라"]

# 없는 인덱스로 삭제
# del list2[999] # IndexError: list assignment index out of range
del list2[100:300]  # 슬라이싱 할 값이 없기 때문에 그대로 유지 > Error 나지 않음
print(list2)

# ====================================
print("======= 실습 8. 잘못된 값 제거하기 =========")
hi_list = [25, 26, 24, 28, 26, 999]
hi_list.remove(999)
print(hi_list)
hi_list.pop(4)
print(hi_list)
del hi_list[0]

# 리스트 정렬하기
# 리스트.sort()
# 데이터를 정렬하는 친구
# 기본적으로 오름차순(작은 숫자부터 큰 숫자까지)
# 내림차순으로 정렬하고 싶은 경우에는 .sort(reverse=True)

n = [37, 2, 8, 109, 1004, -1, 22]
print("n 리스트 원본:", n)

# 오름차순 정렬
n.sort()  # 원본 리스트 수정
print("n 리스트 오름차순 정렬 결과:", n)

# 내림차순 정렬
n.sort(reverse=True)
print("n 리스트 내림차순 정렬 결과:", n)

# 리스트 순서 뒤집기
# .reverse()
# 값의 크기대로 정렬은 해주지 않음
# 뒤로 계속 쌓인 결과(최신)를 앞에서부터 보고싶을 때 사용

n.reverse()
print("n 리스트 순서 뒤집기 결과:", n)

f = ["텀블러", "일회용컵", "일회용컵", "텀블러", "텀블러", "일회용컵"]
print(f.count("일회용컵"))
print(f)  # 원본 배열에 변화 없음

# 특정 값의 위치 찾기
# .index(위치를 찾을 값)
# 리스트에서 가장 첫 위치만 찾아줌
print(f.index("일회용컵"))  # 1
print(f)  # 원본 배열에 변화 없음

# ================================================================
print("========= 실습 9. 정렬하고 탐색하기=============")
temp7 = [22, 24, 24, 26, 27, 28, 30]
temp7.sort()
print("temp 리스트 오름차순 정렬 결과:", temp7)
temp7.reverse()
print("temp 리스트 reverse로 뒤집어 출력:", temp7)
print(temp7.count(24))
print(temp7.index(24))
