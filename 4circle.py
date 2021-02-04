import turtle

tur=turtle.Turtle()

scr=turtle.Screen()

scr.bgcolor('black')

#tur.pencolor('white')

x=30

y=0

Color =['red', 'purple', 'blue', 'green']

tur.speed(0)

tur.penup()

#tur.goto(0,200)

tur.pendown()



while True:

	tur.circle(x)

	tur.pencolor(Color[y%len(Color)])

	

	tur.forward(x)

	tur.right(90)

	x +=1

	y +=1

	if y==100:

		break

		

turtle.done()

