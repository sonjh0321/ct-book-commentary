def check_pwd(password):
    if password == '1234':
        return True
    else:
        return False


while True:
    password = input("비밀번호 4자리를 입력하세요 : ")
    if check_pwd(password):
        print("정확한 비밀번호입니다!!!")
        break
    else:
        print("비밀번호가 틀렸습니다. 다시 시도하세요.")
