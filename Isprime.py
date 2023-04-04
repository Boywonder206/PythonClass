
def isprimeFunction (number):
    isprime = True
    counter = 2
    while counter < number:
        if number % counter == 0:
            isprime = False
            break
        else:
            counter = counter + 1

    return isprime

if __name__ == "__main__":
    num = int(input("Enter Any Number"))
    if isprimeFunction(num):
        print("This is a prime number")
    else:
        print("This number is not prime")