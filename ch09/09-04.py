import turtle as t

cc = 360/5
side = 100
t.color('black')

for i in range(60):
    for j in range(5):
        t.right(cc)
        t.fd(side)
    t.right(6)
