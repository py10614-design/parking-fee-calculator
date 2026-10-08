print("=== 주차 요금 계산기 ===")
minutes = int(input("주차 시간을 분 단위로 입력하세요: "))

if minutes <= 30:
    fee = 0
    message = "30분 이하는 무료입니다."
elif minutes <= 60:
    print("응 시간지나서 1000원이요")

elif minutes <= 120:
    fee = 2000
    message = "1시간 초과 ~ 2시간까지 2,000원입니다."
elif minutes <= 180:
    fee = 3000
    message = "2시간 초과 ~ 3시간까지 3,000원입니다."
else:
    extra_30min = (minutes - 180 + 29) // 30
    fee = 3000 + extra_30min * 1000
    message = "3시간 초과: 추가 30분마다 1,000원씩 부과됩니다."

print(f"주차 시간: {minutes}분")
print(message)
print(f"주차 요금: {fee}원")