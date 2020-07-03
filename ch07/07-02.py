def getinterest(money, rate, year):
    return money * ((1 + rate)) ** year

total = getinterest(300000, 0.05, 2)
print('예금 원금: 300000')
print('2년 총액: {0:.2f}'.format(total))

total = getinterest(300000, 0.05, 4)
print('4년 총액: {0:.2f}'.format(total))

total = getinterest(300000, 0.05, 6)
print('6년 총액: {0:.2f}'.format(total))

total = getinterest(300000, 0.05, 8)
print('8년 총액: {0:.2f}'.format(total))

