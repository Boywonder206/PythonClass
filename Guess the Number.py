import random

num = random.randint(1, 9)
print("num")
Amount = 0
guess = False
while not guess:
    userNum = int(input("Guess the number between 1 and 9"))
    if userNum == num:
        print("You guessed the number right")
        break
    elif userNum < num:
        print("Too Low")
    else:
        print("Too High!")
        Amount = Amount + 1

    if Amount == 2:
        print("Too Many Guess!")
        print("You Lost")
        break
