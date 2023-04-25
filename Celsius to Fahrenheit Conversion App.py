import customtkinter as ctk
import math
def enter_clicked():
    print("")
    userName = entry.get()
    userName = int(userName)
    F = (userName) * (1.8) + 32
    F = str(F)
    strList = ["The value in Fahrenheit is", F]
    hey.configure(text='\n'.join(strList))



app = ctk.CTk()
app.title("Conversion")
app.geometry("800x700")


label = ctk.CTkLabel(app, text="Enter a number in Celsius ", font=ctk.CTkFont(size=20))
label.grid(row=0, column=0, padx=5, pady=5)

entry = ctk.CTkEntry(app, placeholder_text="Enter a valid number", font=ctk.CTkFont(size=20)
                     , width=200)
entry.grid(row=0, column=1, padx=5, pady=5)

btn = ctk.CTkButton(app, text="Enter", command= enter_clicked)
btn.grid(row=1, column=1, padx=5, pady=5)

hey = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
hey.grid(row=2, column=0, padx=5, pady=5)

app.mainloop()