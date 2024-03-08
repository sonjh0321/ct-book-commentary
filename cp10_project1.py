children = ['안나', '신후', '유나', '원준']

result1 = []
for i in children:
    for j in children:
        if i != j:
            result1.append((i, j))

result2 = [(i, j) for i in children for j in children if i != j]
print(result1)
print(result2)

