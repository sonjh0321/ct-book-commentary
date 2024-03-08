count = int(input("입력하는 학생 수가 총 몇명인가요? : "))
print('학생의 이름과 취미를 차례대로 입력하세요!')

num = 1
all_student = []
habit = set()

while num <= count:
    print(f"{num} 번째 학생 ====")
    name = input("* 이름 : ")
    student_habit = input("* 취미 : ")
    all_student.append(name)
    habit.add(student_habit)
    num += 1

print(f" == 전체 학생 리스트 정보 : {all_student}")
print(f" == 전체 취미 세트 정보 : {habit}")
