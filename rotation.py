import turtle

forw = 1

turt = turtle. Turtle()
turt.speed(90)

while True:
    turt.forward(forw)
    turt.left(120)
    turt.left(1)
    forw += 1

turtle.done()