print("지금부터 달리기 시합을 시작하겠습니다.")
people_number = int(input("달리기 선수가 몇 명인가요? "))

result = [input("지금 들어온 선수 이름을 입력하세요 : ") for i in range(people_number)]

print("달리기 시합 결과!\n")
for i, j in enumerate(result):
    print(f"{i+1} 등 {j}")

print("\n수고 많았습니다. 여러분!!")