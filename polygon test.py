# program to create a polyogn using turtle

from turtle import *

def square(length):
    i = 0
    while i < 4:
        forward (length)
        left(90)
        i = i + 1
def polygon(length, sides):
    if sides < 3:
        return
    i = 0
    while i < sides:
        forward(length)
        left(360/sides)
        i = i + 1
sides = int(input("Enter number of sides"))
length = int(input("Enter a length for the polygon"))
polygon(length, sides)
done()