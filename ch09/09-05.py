import turtle as t
import random as r

t.screensize(800,500)
tshs=['arrow','circle','turtle','square','triangle','classic']
han=['화살','원','거북이','사각형','삼각형','전통']
cols=['red','blue','green','purple','magenta','black',
      'gray','yellow','cyan','orange','aqua']

for i in range(20):
    x=r.randint(-300, 300)
    y=r.randint(-200, 200)
    tsh=r.randrange(len(tshs))

    t.begin_fill()
    t.circle(r.randint(3,50),360)
    t.end_fill()
    t.write(han[tsh])
    
    t.shape(tshs[tsh])
    t.up()
    t.goto(x,y)
    t.down()
    t.color('black',r.choice(cols))
