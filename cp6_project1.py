print("## 안나와 신후의 가위, 바위, 보 게임 ##")
print("삼선승제로 세판 먼저 이기는 사람이 승리!!")
print("-------------------------------")
win1 = 0
win2 = 0

while win1 < 3 and win2 < 3:
    user1 = input("안나를 위한 가위, 바위, 보를 입력하세요 : ")
    user2 = input("신후를 위한 가위, 바위, 보를 입력하세요 : ")
    if user1 == '가위':
        if user2 == '가위':
            print("무승부")
        elif user2 == '바위':
            print("신후 승리")
            win2 += 1
        elif user2 == '보':
            print("안나 승리")
            win1 += 1
        else:
            print(f"신후 값 입력 오류 -> {user2}")
    elif user1 == '바위':
        if user2 == '가위':
            print("안나 승리")
            win1 += 1
        elif user2 == '바위':
            print("무승부")
        elif user2 == '보':
            print("신후 승리")
            win2 += 1
        else:
            print(f"신후 값 입력 오류 -> {user2}")
    elif user1 == '보':
        if user2 == '가위':
            print("신후 승리")
            win2 += 1
        elif user2 == '바위':
            print("안나 승리")
            win1 += 1
        elif user2 == '보':
            print("무승부")
        else:
            print(f"신후 값 입력 오류 -> {user2}")
    else:
        print(f"안나 값 입력 오류 -> {user1}")
    print(f"안나 {win1} : 신후 {win2}")

if win2 < win1:
    print("안나 3선승! 최종 승리")
else:
    print("신후 3선승! 최종 승리")