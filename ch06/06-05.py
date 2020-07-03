fruits = ['apple', 'banana', 'grapes', 'pear']
prices = (1000, 500, 1200, 1500)

dic = dict(zip(fruits, prices))
print(dic)
print('\n')

for i, j in enumerate(dic.items()):
    print(i+1, j[0], '가격:', j[1])
