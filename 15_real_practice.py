# =====================================================================
# 종합 실습 1. 설비 종합 모니터링 리포트
# 요구사항 자세히는 practice_guide.md 참고
# =====================================================================

sensors = [
    ("컨베이어_01", 78, 2.1),
    ("용접기_02", 92, 5.4),
    ("절단기_03", 85, 3.2),
    ("건조로_04", 101, 6.8),
    ("냉각탑_05", 67, 1.5),
    ("도장부스_06", 88, 4.1),
    ("성형기_07", 90, 2.9),
]
# (설비명, 온도, 진동)

# 판정 기준
#   온도 > 90 또는 진동 > 5.0  > "위험"
#   온도 >= 80 또는 진동 >= 3.0 > "주의"
#   그 외                      > "정상"

# TODO 1. 각 설비 상태 판정해서 번호 붙여 한 줄씩 출력 (for + enumerate + if/elif/else)

for num, (name, temp, vibration) in enumerate(sensors):
    if temp > 90 or vibration > 5.0:
        status = "위험 🚨"
    elif temp >= 80 or vibration >= 3.0:
        status = "주의 ⚠️"
    else:
        status = "정상 ✅"

    print(f"{num}.{name} | 온도 {temp}℃ | 진동 {vibration}mm/s {status}")

# TODO 2. 정상 / 주의 / 위험 각각 몇 대인지 세서 출력 ()
total_normal = 0
total_cation = 0
total_danger = 0

for num, (name, temp, vibration) in enumerate(sensors, start=1):
    if temp > 90 or vibration > 5.0:
        total_danger += 1
    elif temp >= 80 or vibration >= 3.0:
        total_cation += 1
    else:
        total_normal += 1

print(f"총 설비:", "{len(sensors)}대")
print(f"정상: {total_normal} / 주의: {total_cation} / 위험: {total_danger}")

# TODO 3. 이상 설비(주의 + 위험) 비율 % 출력 (round)

abnormal = total_cation + total_danger
ratio = round(abnormal / len(sensors) * 100, 1)
print(f"이상 설비 비율: {ratio}%")

# TODO 4. 전체 평균 온도 출력 (round)
temp_sum = 0
for name, temp, vibration in sensors:
    temp_sum += temp
avg_temp = round(temp_sum / len(sensors) * 100, 1)
print(f"센서 평균 온도: {avg_temp}℃")

# TODO 5. 온도 가장 높은 설비 이름 + 온도 출력 (반복문으로 직접 찾기)
max_name = ""
max_temp = 0

for name, temp, vibration in sensors:
    if temp > max_temp:
        max_temp = temp
        max_name = name

print(f"최고 온도 설비: {max_name} ({max_temp}℃)")

# TODO 6. "위험" 설비 이름만 모아서 정렬해 리스트로 출력 (.append() + .sort())
danger_list = []

for name, temp, vibration in sensors:
    if temp > 90 or vibration > 5.0:
        danger_list.append(name)

danger_list.sort()

print(f"위험 설비 목록: {danger_list}")

# 도전) 위험 1대라도 있으면 "⚠ 즉시 점검 요망", 없으면 "✅ 전 설비 안정"
