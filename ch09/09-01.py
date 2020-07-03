import random
import math

def getarea(r):
    return math.pi * r * r

radius = round(random.random() * 10, 2)
print('원의 반지름:', radius)
print('원주율 pi:', round(math.pi, 4))
print('반지름 {}인 원의 면적은 {:.2f}'.format(radius, getarea(radius)))
