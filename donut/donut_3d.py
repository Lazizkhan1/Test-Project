from vpython import *
canvas(background= color.white)
donut = ring(radius=0.5, thickness=0.25, color=vector(400, 100, 1))
chocolate = ring(radius=0.55, thickness=0.25, color=vector(0.4, 0.2, 0))
rad = 0
while True:
    rate(10)
    donut.pos = vector(4*cos(rad), sin(rad), 0)
    chocolate.pos = vector(4*cos(rad), sin(rad), 0)
    rad = rad + 0.04