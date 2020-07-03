import random
a = [random.randrange(1,99) for i in range(10)]
print('리스트: ',a)

b = tuple(a)
print('튜플: ',b)

c = sorted(b)
print('튜플 정렬된 리스트: ',c)
print()

print('합: {} 항목수: {}'.format(sum(c),len(c)))
print('최대: {}, 최소: {}, 평균: {}'.format(max(c),min(c),sum(c)/len(c)))
