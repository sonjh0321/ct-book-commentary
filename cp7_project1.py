print("5명의 평가 점수를 입력하세요! (100점 만점)")

max_score = 0
min_score = 101
count = 0
result = []
while count < 5:
    user_input = int(input("점수 입력 : "))
    result.append(user_input)
    if user_input > max_score:
        max_score = user_input
    if user_input < min_score:
        min_score = user_input
    count += 1

print("\n##총 입력 점수##")
for i in result:
    print(f"{i} 점")

print("\n##제거 대상 점수##")
print(f"- 최고 점수 : {max_score}")
print(f"- 최저 점수 : {min_score}")
result.remove(max_score)
result.remove(min_score)

print("\n##최종 입력 점수##")
total = 0
average = 0
for i in result:
    print(f"{i} 점")
    total += i
average = total / 3

print("__________________")
print(f"- 총점 {total} 점")
print(f"- 평균 {round(average, 2)}")
