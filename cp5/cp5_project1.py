print("## 안나와 신후의 가위, 바위, 보 게임 ##")
user1 = input("안나를 위한 가위, 바위, 보를 입력하세요 : ")
user2 = input("신후를 위한 가위, 바위, 보를 입력하세요 : ")

if user1 == '가위':
    if user2 == '가위':
        print("무승부")
    elif user2 == '바위':
        print("신후 승리")
    elif user2 == '보':
        print("안나 승리")
    else:
        print(f"신후 값 입력 오류 -> {user2}")
elif user1 == '바위':
    if user2 == '가위':
        print("안나 승리")
    elif user2 == '바위':
        print("무승부")
    elif user2 == '보':
        print("신후 승리")
    else:
        print(f"신후 값 입력 오류 -> {user2}")
elif user1 == '보':
    if user2 == '가위':
        print("신후 승리")
    elif user2 == '바위':
        print("안나 승리")
    elif user2 == '보':
        print("무승부")
    else:
        print(f"신후 값 입력 오류 -> {user2}")
else:
    print(f"안나 값 입력 오류 -> {user1}")


"""
원래는 위 코드가 정답이나, 이러한 코드는 매우 수준 낮은 코드이다. 뒤에 나오는 딕셔너리와 함수로 훨씬 짧게 구현할 수 있다.
"""
def rock_paper_scissors(player1_choice, player2_choice):
    rules = {
        '가위': '보',
        '바위': '가위',
        '보': '바위'
    }
    
    if rules.get(player1_choice) is None:
        return f"안나 값 입력 오류 -> {player1_choice}"
    elif rules.get(player2_choice) is None:
        return f"신후 값 입력 오류 -> {player2_choice}"

    if player1_choice == player2_choice:
        return '무승부'
    elif rules.get(player1_choice) == player2_choice:
        return '안나가 이겼습니다!'
    else:
        return '신후가 이겼습니다!'


player1_choice = input("안나를 위한 가위, 바위, 보를 입력하세요 : ")
player2_choice = input("신후를 위한 가위, 바위, 보를 입력하세요 : ")

result = rock_paper_scissors(player1_choice, player2_choice)
print(result)
