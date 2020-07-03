data = [ [1, 2, 3],
         [4, 5, 6],
         [7, 8, 9] ]

row,col = [], [0] * len(data[0])

for i in data:
    row.append(sum(i))
    for r, c in enumerate(i):
        col[r] += c

print('각 행의 합: ', row)
print('각 열의 합: ', col)
