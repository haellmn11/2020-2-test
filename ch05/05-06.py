m = [[1,2], [3,4], [5,6], [7,8]]

print('원 행렬(m) 출력:')
for i in m:
    print(*i)
print()

print('전치 행렬 출력:')
for j in range(len(m[0])):
    for i in range(len(m)):
        print(m[i][j], end = ' ')
    print()
