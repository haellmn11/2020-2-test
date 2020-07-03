import random
cels = [random.randrange(1,100) for i in range(10)]

fahr = list(map(lambda c: c * 9/5 + 32, cels))

print('섭씨 온도: ', cels)
print('화씨 온도: ', fahr)

for a, b in zip(cels, fahr):
    print('섭씨 온도 {} => 화씨 {}'.format(a, b))
