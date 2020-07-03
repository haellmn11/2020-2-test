m = [[1, 2], [3, 4], [5, 6], [7, 8]]

transpose = [[row[i] for row in m] for i in range(len(m[0]))]

print("트랜스포즈를 컴프리헨션으로 만들어 그대로 출력")
print(transpose)
print()

print("트랜스포즈를 for문으로 출력")
for i in transpose:
    for j in i:
        print(j, end=' ')
    print()
