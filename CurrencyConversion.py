import customtkinter as ctk
import math


def Rupee_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 82.03
    translation = str(translation)
    hey = str(hey)
    strList = ["Your amount in dollars is", hey, "but your amount in rupees is", translation]
    response.configure(text='\n'.join(strList))


def Pound_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 0.81
    translation = str(translation)
    hey = str(hey)
    PoundList = ["Your amount in dollars is", hey, "but your amount in pounds is", translation]
    response.configure(text='\n'.join(PoundList))


def Yen_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 133.57
    translation = str(translation)
    hey = str(hey)
    YenList = ["Your amount in dollars is", hey, "but your amount in Yen is", translation]
    response.configure(text='\n'.join(YenList))


def AUD_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 1.51
    translation = str(translation)
    hey = str(hey)
    AUDList = ["Your amount in dollars is", hey, "but your amount in AUD is", translation]
    response.configure(text='\n'.join(AUDList))


def Euro_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 0.91
    translation = str(translation)
    hey = str(hey)
    EuroList = ["Your amount in dollars is", hey, "but your amount in Euros is", translation]
    response.configure(text='\n'.join(EuroList))

app = ctk.CTk()
app.title("Dollars to any currency")
app.geometry("1500x700")

label = ctk.CTkLabel(app, text="Enter an amount in dollars", font=ctk.CTkFont(size=20))
label.grid(row=0, column=0, padx=5, pady=5)

textbox = ctk.CTkEntry(app, placeholder_text="Enter a valid number", font=ctk.CTkFont(size=20), width=200)
textbox.grid(row=0, column=1, padx=5, pady=5)

Rupeebutton = ctk.CTkButton(app, text="Rupee", font=ctk.CTkFont(size=20), command=Rupee_clicked)
Rupeebutton.grid(row=1, column=1, padx=5, pady=5)

PoundButton = ctk.CTkButton(app, text="Pound", command=Pound_clicked, font=ctk.CTkFont(size=20))
PoundButton.grid(row=1, column=3, padx=5, pady=5)

Yenbutton = ctk.CTkButton(app, text="Yen", command=Yen_clicked, font=ctk.CTkFont(size=20))
Yenbutton.grid(row=1, column=3, padx=5, pady=5)

AustralianButton = ctk.CTkButton(app, text="AUD", command=AUD_clicked, font=ctk.CTkFont(size=20))
AustralianButton.grid(row=1, column=4, padx=5, pady=5)

Eurobutton = ctk.CTkButton(app, text="Euro", command=Euro_clicked, font=ctk.CTkFont(size=20))
Eurobutton.grid(row=1, column=2, padx=5, pady=5)

label = ctk.CTkLabel(app, text="Click another currency for us to convert", font=ctk.CTkFont(size=20))
label.grid(row=1, column=0, padx=5, pady=5)

response = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
response.grid(row=2, column=0, padx=5, pady=5)

app.mainloop()