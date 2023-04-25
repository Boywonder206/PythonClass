import customtkinter as ctk
import random

num = random.randint(1, 10)
Amount = 0
guess = 0

def enter_clicked():
    global guess
    print("")
    guess = entry.get()
    guess = int(guess)
    if guess == num:
        label = ctk.CTkLabel(app, text="You guessed the number right")
        label.grid(row=2, column=0)
        SHANTI.configure(text="You guessed way too many times")
    elif guess < num:
        label = ctk.CTkLabel(app, text="Too low, guess again")
        label.grid(row=2, column=0)
        Amount = Amount + 1
    if guess > num:
        label = ctk.CTkLabel(app, text="Too High, guess again")
        label.grid(row=2, column=0)
        Amount = Amount + 1

    if Amount >= 3:
        SHANTI.configure(text="You guessed way too many times")




app = ctk.CTk()
app.title("RockPaperScissorsShoot")
app.geometry("800x700")

OM = ctk.CTkLabel(app, text="Guess a number from 1 to 10", font=ctk.CTkFont(size=20))
OM.grid(row=0, column=0, padx=5, pady=5)

entry = ctk.CTkEntry(app, placeholder_text="Enter a valid number", font=ctk.CTkFont(size=20)
                     , width=200)
entry.grid(row=0, column=1, padx=5, pady=5)

SHANTI = ctk.CTkLabel(app, text="")
SHANTI.grid(row=3, column=0)

btn = ctk.CTkButton(app, text="Enter", command=enter_clicked)
btn.grid(row=1, column=1, padx=5, pady=5)




app.mainloop()