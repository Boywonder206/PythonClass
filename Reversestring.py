# code to reverse any sting
def reverseString(str):
    counter = len(str) - 1
    reverseString = ""
    while counter >= 0:
        reverseString = reverseString + str[counter]
        counter = counter - 1

    return reverseString

name = input("Enter your userneame:")
print(f" Your username spelled backwards is {reverseString(name)}")