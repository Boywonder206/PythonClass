num = int(input("Enter Any Number"))
sum = list(range(1, num, 1))

WHO = 0
for help in sum:
    WHO = WHO + help
    counter = 2
    isprime = True
    while counter < help:
        if help % counter == 0:
            isprime = False
            break
        else:
            counter = counter + 1
    if isprime:
        print(help)

