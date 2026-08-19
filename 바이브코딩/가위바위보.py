import random

choices = ["가위", "바위", "보"]

user_choice = input("가위, 바위, 보 중 하나를 입력하세요: ")

if user_choice not in choices:
    print("잘못 입력했습니다.")
else:
    computer_choice = random.choice(choices)

    print(f"사용자: {user_choice}")
    print(f"컴퓨터: {computer_choice}")

    # 두 선택이 같으면 무승부입니다.
    if user_choice == computer_choice:
        print("비겼습니다!")

    # 아래 세 가지 경우에는 사용자가 이깁니다.
    elif (
        (user_choice == "가위" and computer_choice == "보")
        or (user_choice == "바위" and computer_choice == "가위")
        or (user_choice == "보" and computer_choice == "바위")
    ):
        print("사용자가 이겼습니다!")

    # 나머지 경우에는 컴퓨터가 이깁니다.
    else:
        print("컴퓨터가 이겼습니다!")