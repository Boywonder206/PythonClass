from turtle import *
x = 0
pendown()
pensize(1)
color("red", "yellow")
begin_fill()
while x < 5:
    forward(200)
    left(72)
    x = x + 1

end_fill()
penup()
x = 0

goto(-100, -100)
pendown()
while x < 3:
    forward(100)
    left(120)
    x = x + 1

end_fill()
done()