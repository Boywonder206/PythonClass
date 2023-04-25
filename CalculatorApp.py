import customtkinter as ctk

app = ctk.CTk()
app.geometry("350x500")
app.title("Calculator")
calcframe = ctk.CTkFrame(app, width=340, height=70 ,fg_color="white")
calcframe.grid(row=0, column=0, padx=5, pady=5)

calcLabel = ctk.CTkLabel(calcframe, text="0", fg_color="white", width=340, height=50, font=ctk.CTkFont(size=50), anchor="e")
calcLabel.grid(row=0, column=0, padx=2, pady=2)

btnframe = ctk.CTkFrame(app,width=340, height=400,bg_color="white" ,fg_color="white")
btnframe.grid(row=1, column=0, padx=5, pady=5)



btnCE = ctk.CTkButton( btnframe, text="CE",width=75, height=65 ,font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red")
btnCE.grid(row=0, column=0, padx=5, pady=5)
btnC = ctk.CTkButton(btnframe, text="C", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65)
btnC.grid(row=0, column=1, padx=5, pady=5)
btnbackspace = ctk.CTkButton(btnframe, text="<--", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65)
btnbackspace.grid(row=0, column=2, padx=5, pady=5)
btndivide = ctk.CTkButton(btnframe, text="/", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65)
btndivide.grid(row=0, column=3, padx=5, pady=5)

btn7 = ctk.CTkButton(btnframe, text="7", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65)
btn7.grid(row=1, column=0, padx=5, pady=5)
btn8 = ctk.CTkButton(btnframe, text="8", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65)
btn8.grid(row=1, column=1, padx=5, pady=5)
btn9 = ctk.CTkButton(btnframe, text="9", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65)
btn9.grid(row=1, column=2, padx=5, pady=5)
btnmultiply = ctk.CTkButton(btnframe, text="X", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65)
btnmultiply.grid(row=1, column=3, padx=5, pady=5)

btn4 = ctk.CTkButton(btnframe, text="4", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65)
btn4.grid(row=2, column=0, padx=5, pady=5)
btn5 = ctk.CTkButton(btnframe, text="5", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65)
btn5.grid(row=2, column=1, padx=5, pady=5)
btn6 = ctk.CTkButton(btnframe, text="6", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65)
btn6.grid(row=2, column=2, padx=5, pady=5)
btnsubtract = ctk.CTkButton(btnframe, text="-", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65)
btnsubtract.grid(row=2, column=3, padx=5, pady=5)

btn1 = ctk.CTkButton(btnframe, text="1", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65)
btn1.grid(row=3, column=0, padx=5, pady=5)
btn2 = ctk.CTkButton(btnframe, text="2", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65)
btn2.grid(row=3, column=1, padx=5, pady=5)
btn3 = ctk.CTkButton(btnframe, text="3", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65)
btn3.grid(row=3, column=2, padx=5, pady=5)
btnaddition = ctk.CTkButton(btnframe, text="+", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65)
btnaddition.grid(row=3, column=3, padx=5, pady=5)

btnopposite = ctk.CTkButton(btnframe, text="+/-", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65)
btnopposite.grid(row=4, column=0, padx=5, pady=5)
btn0 = ctk.CTkButton(btnframe, text="0", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65)
btn0.grid(row=4, column=1, padx=5, pady=5)
btndecimal = ctk.CTkButton(btnframe, text=".", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65)
btndecimal.grid(row=4, column=2, padx=5, pady=5)
btnequalsign = ctk.CTkButton(btnframe, text="=", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65)
btnequalsign.grid(row=4, column=3, padx=5, pady=5)




app.mainloop()