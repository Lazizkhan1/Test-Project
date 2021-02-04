import turtle
colors = ['red', 'purple' , 'blue', 'green', 'orange', 'yellow']
t = turtle.Pen()
turtle.bgcolor('gray')
turtle.begin_fill()
t.speed(5)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
turtle.end_fill()
t.hideturtle()
turtle.done()