import time


def debt(money, debtcount):
    if debtcount == 0:
        print(f"{nickname}는(은) 패배했습니다. 돈이 없죠")
        print("하지만 다시 시작할 수 있습니다.")
        print(".")
        time.sleep(1)
        print()
        print("바로 빚을 지는 것 입니다")
        print("제가 500000원을 빌려줄게요.")
        money += 500000
        debtcount += 1

    elif debtcount == 1:
        print(f"{nickname}는(은) 패배했습니다. 돈이 없죠")
        print("하지만... 왜죠?")
        print("저는 분명 돈을 빌려줬습니다.")
        print("이번이 마지막입니다. 100만원을 빌려줄게요.")
        money += 1000000
        debtcount += 1

    elif debtcount == 2:
        print()
        print(f" 또 오셨군요;{nickname};")
        print("이젠 대가 없이 빌려주지 않겠습니다.")
        print(".")
        time.sleep(1)
        print(".")
        print("대가가 무엇이냐고요?")
        print("바로 당신의 몸입니다.")
        print("일단 당신의 '간'을 가져가겠습니다.")
        time.sleep(0.3)
        print("뭐 300만원을 줄게요.")
        time.sleep(0.1)
        print("10번안에 다시 350만원을 갚지 못하면 당신의 몸은 제 것이 됩니다.")
        money += 3000000
        debtcount += 1

    return money, debtcount