import turtle as a
import math
wn=a.Screen()
wn.setup(width=7680, height=4320)
wn.title('Lazizkhan')

def rectangle(color):
    a.begin_fill()
    a.fillcolor(color)
    for i in range(2):
        a.forward(400)
        a.rt(90)
        a.fd(100)
        a.rt(90)
    a.end_fill()



a.up()
a.goto(0,-300)
a.down()
a.goto(0,300)
rectangle('blue')
a.up()
a.goto(400,200)
a.down()
a.rt(90)
def rectangle(color):
    a.begin_fill()
    a.fillcolor(color)
    for i in range(2):
        a.forward(10)
        a.rt(90)
        a.fd(400)
        a.rt(90)
    a.end_fill()
rectangle('red')
a.fd(100)
a.rt(90)
a.fd(400)
a.lt(90)
a.color('black','red')
a.begin_fill()
a.fd(10)
a.lt(90)
a.fd(400)
a.lt(90)
a.fd(10)
a.end_fill()
a.rt(180)
a.fd(10)
a.color('black','green')
a.begin_fill()
for i in range(2):
    a.fd(100)
    a.rt(90)
    a.fd(400)
    a.rt(90)
a.end_fill()
a.up()
a.lt(180)
a.fd(200)
a.lt(90)
a.fd(370)
a.down()


a.color('black','white')
a.begin_fill()
for i in range(360):
    a.fd(0.4)
    a.lt(1)
a.end_fill()
a.lt(180)
a.fd(10)
a.rt(180)
a.color('blue','blue')
a.begin_fill()
for i in range(360):
    a.fd(0.4)
    a.lt(1)
a.end_fill()
a.color('black')
a.lt(180)
a.up()
a.fd(50)
a.rt(90)
a.fd(10)
a.lt(90)
a.down()

a.color('white','white')
a.begin_fill()

for i in range (3):
    a.lt(72)
    a.fd(15)
    for i in range(4):
        a.rt(144)
        a.fd(15)
    a.lt(144)
    a.up()
    a.fd(20)
    a.down()
a.end_fill()

a.rt(90)
a.up()
a.fd(20)
a.rt(90)
a.fd(80)
a.rt(180)
a.color('white','white')
a.begin_fill()

for i in range (4):
    a.lt(72)
    a.fd(15)
    for i in range(4):
        a.rt(144)
        a.fd(15)
    a.lt(144)
    a.up()
    a.fd(20)
    a.down()
a.end_fill()

a.rt(90)
a.up()
a.fd(20)
a.rt(90)
a.fd(100)
a.rt(180)

a.color('white','white')
a.begin_fill()
for i in range(5):
    a.lt(72)
    a.fd(15)
    for i in range(4):
        a.rt(144)
        a.fd(15)
    a.lt(144)
    a.up()
    a.fd(20)
    a.down()
a.end_fill()

a.up()
a.rt(180)
a.fd(150)
a.lt(90)
a.fd(540)
a.color('black')
a.down()
a.color('black','black')
a.begin_fill()
for i in range(2):
    for i in range(2):
        a.rt(90)
        a.fd(6)
        a.rt(90)
        a.fd(600)
a.end_fill()
a.hideturtle()
a.done()
