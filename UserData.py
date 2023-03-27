# This is a code to ask the user about his/her infromation

N = (input("Please enter your full name"))
A = int(input("Enter your current age"))
ZC = (input("Enter your zip code"))

strList = (N, A, ZC)
print(strList)

if A < 15:
   print("You are a middle schooler")
if A >= 18:
    print("You are an adult")
