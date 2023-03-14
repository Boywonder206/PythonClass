#this code shows if the name is a pallendrome or not
def reverseString(str):
    counter = len(str) - 1
    rev = ""
    while counter >= 0:
        rev = reverseString + str[counter]
        counter = counter - 1

    return reverseString
def ispalindrome(str):
    rev = reverseString(str)
    if rev == str:
        return True
    else:
        return False

name = input("Enter a name")

if ispalindrome(name):
     print(f"Your name is a palindrome")
else:
     print(f"Your name is not a palindrome")






