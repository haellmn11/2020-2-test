import turtle as t

side = int(input('변 길이: '))
cc = 360/5
t.color('black')

for i in range(60):
    for j in range(5):
        t.right(cc)
        t.fd(side)
    t.right(6)
