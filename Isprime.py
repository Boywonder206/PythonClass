num = int(input("Enter Any Number"))
counter = 2
isprime = True
while counter < num:
    if num % counter == 0:
         isprime = False
         break
    else:
        counter = counter + 1
if isprime:
    print("This is a prime number!")
else:
    print("This is not a Prime number")