from turtle import *

x = 0
y = 0
z = 0
w = 0
s = 0
pensize(10)
color("blue")
penup()

goto(-200, 50)
pendown()
while x < 4:
    forward(100)
    left(90)
    x = x + 1
penup()

goto(-50, 50)
color("black")
pendown()
while y < 4:
    forward(100)
    left(90)
    y = y + 1
penup()

goto(100, 50)
color("red")
pendown()
while z < 4:
    forward(100)
    left(90)
    z = z + 1
penup()

goto(-125, 0)
color("yellow")
pendown()
while w < 4:
    forward(100)
    left(90)
    w = w + 1
penup()

goto(25, 0)
color("green")
pendown()
while s < 4:
    forward(100)
    left(90)
    s = s + 1

done()