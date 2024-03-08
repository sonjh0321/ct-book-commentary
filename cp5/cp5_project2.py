print("## X, Y 좌표의 사분면 위치 찾기 ##")
x = int(input("X축 좌표를 입력해주세요 : "))
y = int(input("Y축 좌표를 입력해주세요 : "))

if x > 0:
    if y > 0:
        print("1사분면")
    elif y < 0:
        print("4사분면")
    else:
        print("X축")
elif x < 0:
    if y > 0:
        print("2사분면")
    elif y < 0:
        print("3사분면")
    else:
        print("X축")
else:
    if y == 0:
        print("원점")
    else:
        print("Y축")
