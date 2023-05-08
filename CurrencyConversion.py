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
def CAD_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 1.36
    translation = str(translation)
    hey = str(hey)
    CADList = ["Your amount in dollars is", hey, "but your amount in CAD is", translation]
    response.configure(text='\n'.join(CADList))
def swissFranc_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 0.89
    translation = str(translation)
    hey = str(hey)
    CHFList = ["Your amount in dollars is", hey, "but your amount in Swiss franc is", translation]
    response.configure(text='\n'.join(CHFList))
def CNH_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 6.93
    translation = str(translation)
    hey = str(hey)
    CNHList = ["Your amount in dollars is", hey, "but your amount in chinese renminbi is", translation]
    response.configure(text='\n'.join(CNHList))
def HongKong_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 7.85
    translation = str(translation)
    hey = str(hey)
    HKDList = ["Your amount in dollars is", hey, "but your amount in Hong Kong Dollars is", translation]
    response.configure(text='\n'.join(HKDList))
def NZD_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 1.61
    translation = str(translation)
    hey = str(hey)
    NZDList = ["Your amount in dollars is", hey, "but your amount in New Zealand Dollars is", translation]
    response.configure(text='\n'.join(NZDList))
def Mexico_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 17.98
    translation = str(translation)
    hey = str(hey)
    MPList = ["Your amount in dollars is", hey, "but your amount in Mexican Peso is", translation]
    response.configure(text='\n'.join(MPList))
def ZAR_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 18.46
    translation = str(translation)
    hey = str(hey)
    ZARList = ["Your amount in dollars is", hey, "but your amount in South Africian Rand is", translation]
    response.configure(text='\n'.join(ZARList))
def KD_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 0.31
    translation = str(translation)
    hey = str(hey)
    KDList = ["Your amount in dollars is", hey, "but your amount in Brazilian Reals is", translation]
    response.configure(text='\n'.join(KDList))
def BR_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 5
    translation = str(translation)
    hey = str(hey)
    BRList = ["Your amount in dollars is", hey, "but your amount in Brazilian Reals is", translation]
    response.configure(text='\n'.join(BRList))
def RR_clicked():
    print("")
    hey = textbox.get()
    hey = int(hey)
    translation = (hey) * 77.72
    translation = str(translation)
    hey = str(hey)
    RRList = ["Your amount in dollars is", hey, "but your amount in Russian Rubles is", translation]
    response.configure(text='\n'.join(RRList))

app = ctk.CTk()
app.title("Dollars to any currency")
app.geometry("1500x700")

label = ctk.CTkLabel(app, text="Enter an amount in dollars", font=ctk.CTkFont(size=20))
label.grid(row=0, column=0)

textbox = ctk.CTkEntry(app, placeholder_text="Enter a valid number", font=ctk.CTkFont(size=20), width=200)
textbox.grid(row=0, column=1)

Rupeebutton = ctk.CTkButton(app, text="Rupee", font=ctk.CTkFont(size=20), command=Rupee_clicked)
Rupeebutton.grid(row=2, column=0, pady=5)

PoundButton = ctk.CTkButton(app, text="Pound", command=Pound_clicked, font=ctk.CTkFont(size=20))
PoundButton.grid(row=3, column=0, pady=5)

Yenbutton = ctk.CTkButton(app, text="Yen", command=Yen_clicked, font=ctk.CTkFont(size=20))
Yenbutton.grid(row=4, column=0, pady=5)

AustralianButton = ctk.CTkButton(app, text="AUD", command=AUD_clicked, font=ctk.CTkFont(size=20))
AustralianButton.grid(row=5, column=0, pady=5)

Eurobutton = ctk.CTkButton(app, text="Euro", command=Euro_clicked, font=ctk.CTkFont(size=20))
Eurobutton.grid(row=6, column=0, pady=5)

CADbutton = ctk.CTkButton(app, text="CAD", command=CAD_clicked, font=ctk.CTkFont(size=20))
CADbutton.grid(row=7, column=0, pady=5)

swissfrancbutton = ctk.CTkButton(app, text="Swiss franc", command=swissFranc_clicked, font=ctk.CTkFont(size=20))
swissfrancbutton.grid(row=8, column=0, pady=5)

Chinesebutton = ctk.CTkButton(app, text="CNH", command=CNH_clicked, font=ctk.CTkFont(size=20))
Chinesebutton.grid(row=9, column=0, pady=5)

HongKongbutton = ctk.CTkButton(app, text="HKD", command=HongKong_clicked, font=ctk.CTkFont(size=20))
HongKongbutton.grid(row=10, column=0, pady=5)

NewZealandbutton = ctk.CTkButton(app, text="NZD", command=NZD_clicked, font=ctk.CTkFont(size=20))
NewZealandbutton.grid(row=2, column=1, pady=5)

Mexicobutton = ctk.CTkButton(app, text="Mexican Peso", command=Mexico_clicked, font=ctk.CTkFont(size=20))
Mexicobutton.grid(row=3, column=1, pady=5)

ZARbutton = ctk.CTkButton(app, text="ZAR", command=ZAR_clicked, font=ctk.CTkFont(size=20))
ZARbutton.grid(row=4, column=1, pady=5)

Kuwaitbutton = ctk.CTkButton(app, text="Kuwait Dinars", command=KD_clicked, font=ctk.CTkFont(size=20))
Kuwaitbutton.grid(row=5, column=1, pady=5)

BRbutton = ctk.CTkButton(app, text="Brazilian Reals", command=BR_clicked, font=ctk.CTkFont(size=20))
BRbutton.grid(row=6, column=1, pady=5)

RRbutton = ctk.CTkButton(app, text="Russian Rubles", command=RR_clicked, font=ctk.CTkFont(size=20))
RRbutton.grid(row=7, column=1, pady=5)

label = ctk.CTkLabel(app, text="Click another currency for us to convert", font=ctk.CTkFont(size=20))
label.grid(row=1, column=0)

response = ctk.CTkLabel(app, text="", font=ctk.CTkFont(size=20))
response.grid(row=11, column=0)

app.mainloop()