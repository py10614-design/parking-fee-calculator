while True:
    print("주문 금액을 입력해 주세요.")
    order = int(input(":"))

    if order >= 50000:
        print("무료배송 입니다.")
        break
    else:
        print("배송비는 5000원 입니다.")
        print(f"{50000 - order}원을 더 담으세요")

    print("조회가 끝났습니다.")

    