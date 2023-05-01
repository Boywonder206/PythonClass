#this program tels us what the left over variable is
from math import sqrt

user = str(input("Select a value you want us to calculate. 'a' is a leg, 'b' is also a leg, 'c' is the hypotenuse "))

if user == 'a':
    w = int(input("Enter the hypotenuse"))
    y = int(input("Enter a value for one side"))
    a = sqrt(w**2-y**2)
    print(a)

if user == 'b':
    z = int(input("Enter a hypotenuse"))
    g = int(input("Enter a value for one side"))
    r = sqrt(z**2-g**2)
    print(r)

if user == 'c':
    h = int(input("Enter a value for one side"))
    k = int(input("Enter a value for another side"))
    q = sqrt(k**2+h**2)
    print(q)