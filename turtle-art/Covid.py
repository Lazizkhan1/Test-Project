import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor("black")
t.pencolor("white")
a = 0
b = 0

while True:
    t.forward(a)
    t.right(b)
    t.speed(50)
    a+=3
    b+=1
    if b ==175:
        break
    t.hideturtle()

turtle.done()