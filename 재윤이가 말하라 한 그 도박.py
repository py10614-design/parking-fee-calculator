import random
import time

from debt import debt
import countdown

# 변수 선언
money = 100000
probability = 0
turn = 1
betting_money = 0
a = 0
debtcount = 0

#여기까지 변수 선언


nickname = input("닉네임을 입력해주세요: ")
print(f"{nickname}님 안녕하세요.")
print()
print("재윤이가 요청한 게임을 시작합니다.")
print(f"현재 당신의 게임 머니는 {money}원 입니다.")
print()
print()

print("== 시작하시겠습니까? [yes or no] ==")
start = input(": ").strip().lower()

if start == "yes":
    countdown.set_turn_count(0)

    while True:
        if money <= 0:
            money, debtcount = debt(money, debtcount)
            if debtcount < 3:
                countdown.set_turn_count(0)
                print(f"남은 턴: {countdown.get_countdown()}턴")
                continue
            elif money <= 0:
                print("당신은 더 이상 진행할 수 없습니다.")
                break
            else:
                countdown.set_turn_count(10)

        print()
        print(f"{turn}번째 턴 입니다")

        if debtcount >= 3 and countdown.get_countdown() <= 0:
            countdown.reset_countdown()

        if debtcount >= 2:
            print(f"남은 턴: {countdown.get_countdown()}턴")

        print(f"현재 잔고: {money}원")

        while True:
            try:
                betting_money = int(input("돈 얼마나 걸꺼야? : "))
                break
            except ValueError:
                print("숫자로 입력해 주세요.")

        print(f"건 돈: {betting_money}")
        print()
        print()

        if betting_money <= 0:
            print("야 하기 싫어?")

        elif betting_money > money:
            print("너 돈 없잔아")

        else:
            print("돈 따는 중.")
            for i in range(3):
                time.sleep(0.5)
                print(".")

            probability = random.randint(0, 9)

            if probability < 5:
                money = money - betting_money
                print(f"{betting_money}원을 잃었습니다.")
            else:
                a = random.randint(1, 7)

                if a < 3:
                    reward = betting_money * 1
                    money = money + reward
                    print(f"{reward}원을 얻었습니다.")
                elif a < 5:
                    reward = betting_money * 2
                    money = money + reward
                    print(f"{reward}원을 얻었습니다.")
                elif a < 6:
                    reward = betting_money * 3
                    money = money + reward
                    print(f"{reward}원을 얻었습니다.")
                else:
                    reward = betting_money * 5
                    money = money + reward
                    print(f"{reward}원을 얻었습니다.")

            print()
            print(f"현재 잔고: {money}원")

            print("더 하시겠습니까? [yes or no]")
            skip = input(": ").strip().lower()

            if skip == "no":
                break

            countdown.decrease_turn()
            turn += 1

print("당신의 잔고는...")
print(f"{money}원 입니다.")