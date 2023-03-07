counter = 1
x1 = 0
x2 = 1
next = 0
counter = 1
print(x1)
print(x2)
while counter <= 100:
    next = x1 + x2
    x1 = x2
    x2 = next
    counter = counter + 1
    print(next)