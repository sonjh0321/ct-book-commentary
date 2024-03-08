def multiple(num):
    for i in range(1, 10):
        print(f"{num} * {i} = {num*i}")


for n in range(1, 10):
    print(f"--- {n} 단 ---")
    multiple(n)
