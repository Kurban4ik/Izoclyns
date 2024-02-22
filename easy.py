from turtle import *
from math import atan, degrees, cos, sin, e
global sos # size of square

sos = 15
arctg = lambda x: degrees(atan(x))
pensize(1)
l = 25
size = 250
screensize(size, size)
tracer(0)
def draw_dekart():
    up()
    goto(-size, 0)
    setheading(0)
    down()
    forward(2 * size)

    up()
    goto(0, -size)
    setheading(90)
    down()
    forward(2 * size)
    up()
draw_dekart()

up()
def f(x, y):
    try:
        return x + y
    except:
        return None
def draw_vec(x: int, y: int, tg: int):
    x_mid = x + sos // 2
    y_mid = y + sos // 2
    up()
    goto(x_mid, y_mid)
    deg = arctg(tg)
    setheading(deg)
    down()
    forward(sos // 4 * 3 - 2)
    color('red')
    forward(max(1, sos // 4 - 2))
    color('black')
    up()


for i in range(-size, size, sos):
    for j in range(-size, size, sos):
        if f(i / sos, j / sos) != None:
            draw_vec(i, j, f(i / sos, j / sos))
up()
ht()
done()