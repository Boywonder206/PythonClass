username = input("Enter Your Name")
password = input("Enter Your Password")
numberOfCharacters = len(password)
while numberOfCharacters < 8:
    print("The password is invalid. Please enter a password with at least 8 characters long")
    password = input("Enter Your Password")
    numberOfCharcters = len(password)
HiddenPassword = '*' * len(password)

print(f"Hello {username} your password is {HiddenPassword}")
revealPassword = input("Do you want to see your password")
if revealPassword == 'y':
    print(f"your password is {password}")