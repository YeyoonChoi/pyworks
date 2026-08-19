import random

# 1. 가위, 바위, 보 항목 정의 (0: 가위, 1: 바위, 2: 보)
choices = ["가위", "바위", "보"]

print("=== 가위바위보 게임을 시작합니다 ===")
user_input = input("가위, 바위, 보 중 하나를 입력하세요: ").strip()

# 사용자 입력 유효성 검사
if user_input not in choices:
    print("잘못된 입력입니다. '가위', '바위', '보' 중에서 입력해 주세요.")
else:
    # 2. 컴퓨터의 무작위 선택
    computer_choice = random.choice(choices)

    print(f"\n사용자: {user_input}")
    print(f"컴퓨터: {computer_choice}\n")

    # 3. 승부 판정 로직
    # [경우 1] 사용자 = 컴퓨터 : 비긴 경우
    if user_input == computer_choice:
        print("결과: 비겼습니다! 🤝")

    # [경우 2] 사용자가 이기는 경우 3가지 정의
    # - 가위 vs 보
    # - 바위 vs 가위
    # - 보 vs 바위
    elif (
        (user_input == "가위" and computer_choice == "보")
        or (user_input == "바위" and computer_choice == "가위")
        or (user_input == "보" and computer_choice == "바위")
    ):
        print("결과: 당신이 이겼습니다! 🎉")

    # [경우 3] 비기지도 않고 이기지도 않은 경우 : 컴퓨터가 이긴 경우
    else:
        print("결과: 컴퓨터가 이겼습니다! 🤖")