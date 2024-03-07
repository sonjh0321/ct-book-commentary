star = "*"
print(f"1개 {star}")
print(f"1개 {star}")
print(f"2개 {star*2}")
print(f"3개 {star*3}")
print(f"5개 {star*5}")
print(f"8개 {star*8}")

"""
아래는 하드코어 버전
"""
fibo_len = int(input("몇 번째 피보나치 수열까지 출력할까요?"))
counter = 1
before_counter = 1
print(f"1개 {star}")
print(f"1개 {star}")

for i in range(fibo_len-2):
    counter, before_counter = counter + before_counter, counter
    print(f"{counter}개 {star*counter}")
