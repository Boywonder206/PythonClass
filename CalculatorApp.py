import customtkinter as ctk

currentText = "0"
num = 0
op = ""
def addText(str):
    global currentText

    if float(currentText) == 0 and str != '.' not in currentText:
        currentText = ""
        currentText = currentText + str
    elif str == '.' and '.' in currentText:
        currentText = currentText
    else:
        currentText = currentText + str
    updateText()
def preformOperation():
    global currentText
    global num
    global op
    currentNum = float(currentText)

    if op == '+':
        result = num + currentNum
        currentText = str(result)
    elif op == '-':
        result = num - currentNum
        currentText = str(result)
    elif op == 'X':
        result = num * currentNum
        currentText = str(result)
    elif op == '/':
        if currentNum == 0:
            currentText = "0"
        else:
            result = num / currentNum
            currentText = str(result)
    num = float(currentText)
    updateText()


def operation(str):
    global currentText
    global op
    global num

    if op == "":
        num = float(currentText)
        currentText = "0"
    else:
       preformOperation()

    if str != '=':
        op = str
        currentText = "0"
    else:
        op = ""
        return
def updateText():
    global currentText
    if len(currentText) > 12:
        currentText = currentText[:12]
    calcLabel.configure(text=currentText)
def CE():
    global currentText
    global num
    global op
    currentText = "0"
    num = 0
    op = ""
    updateText()
def C():
    global currentText
    currentText = "0"
    updateText()
def Back():
    global currentText
    currentText = currentText[0:len(currentText)-1]
    if len(currentText) == 0:
        currentText = "0"
    updateText()
def Plus_Minus():
    global currentText
    if currentText == "0":
        return
    if '-' in currentText:
        currentText = currentText.replace('-', '')
    else:
        currentText = '-' + currentText
    updateText()



app = ctk.CTk()
app.geometry("350x500")
app.title("Calculator")
calcframe = ctk.CTkFrame(app, width=340, height=70 ,fg_color="white")
calcframe.grid(row=0, column=0, padx=5, pady=5)

calcLabel = ctk.CTkLabel(calcframe, text="0", fg_color="white", width=340, height=50, font=ctk.CTkFont(size=50), anchor="e")
calcLabel.grid(row=0, column=0, padx=2, pady=2)

btnframe = ctk.CTkFrame(app,width=340, height=400,bg_color="white" ,fg_color="white")
btnframe.grid(row=1, column=0, padx=5, pady=5)


btnCE = ctk.CTkButton( btnframe, text="CE",width=75, height=65 ,font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", command=CE)
btnCE.grid(row=0, column=0, padx=5, pady=5)
btnC = ctk.CTkButton(btnframe, text="C", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65, command=C)
btnC.grid(row=0, column=1, padx=5, pady=5)
btnbackspace = ctk.CTkButton(btnframe, text="<--", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65, command=Back)
btnbackspace.grid(row=0, column=2, padx=5, pady=5)
btndivide = ctk.CTkButton(btnframe, text="/", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65, command=lambda : operation('/'))
btndivide.grid(row=0, column=3, padx=5, pady=5)

btn7 = ctk.CTkButton(btnframe, text="7", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65, command=lambda : addText("7"))
btn7.grid(row=1, column=0, padx=5, pady=5)
btn8 = ctk.CTkButton(btnframe, text="8", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65, command=lambda : addText("8"))
btn8.grid(row=1, column=1, padx=5, pady=5)
btn9 = ctk.CTkButton(btnframe, text="9", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65, command=lambda : addText("9"))
btn9.grid(row=1, column=2, padx=5, pady=5)
btnmultiply = ctk.CTkButton(btnframe, text="X", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65, command= lambda : operation('X'))
btnmultiply.grid(row=1, column=3, padx=5, pady=5)

btn4 = ctk.CTkButton(btnframe, text="4", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65, command=lambda : addText("4"))
btn4.grid(row=2, column=0, padx=5, pady=5)
btn5 = ctk.CTkButton(btnframe, text="5", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65, command=lambda : addText("5"))
btn5.grid(row=2, column=1, padx=5, pady=5)
btn6 = ctk.CTkButton(btnframe, text="6", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65, command=lambda : addText("6"))
btn6.grid(row=2, column=2, padx=5, pady=5)
btnsubtract = ctk.CTkButton(btnframe, text="----", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65, command=lambda : operation('-'))
btnsubtract.grid(row=2, column=3, padx=5, pady=5)

btn1 = ctk.CTkButton(btnframe, text="1", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65, command=lambda : addText("1"))
btn1.grid(row=3, column=0, padx=5, pady=5)
btn2 = ctk.CTkButton(btnframe, text="2", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65, command=lambda : addText("2"))
btn2.grid(row=3, column=1, padx=5, pady=5)
btn3 = ctk.CTkButton(btnframe, text="3", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65, command=lambda : addText("3"))
btn3.grid(row=3, column=2, padx=5, pady=5)
btnaddition = ctk.CTkButton(btnframe, text="+", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65, command=lambda : operation('+'))
btnaddition.grid(row=3, column=3, padx=5, pady=5)

btnopposite = ctk.CTkButton(btnframe, text="+/-", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65, command=Plus_Minus)
btnopposite.grid(row=4, column=0, padx=5, pady=5)
btn0 = ctk.CTkButton(btnframe, text="0", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65, command=lambda : addText("0"))
btn0.grid(row=4, column=1, padx=5, pady=5)
btndecimal = ctk.CTkButton(btnframe, text=".", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="blue", width=75, height=65, command=lambda : addText("."))
btndecimal.grid(row=4, column=2, padx=5, pady=5)
btnequalsign = ctk.CTkButton(btnframe, text="=", font=ctk.CTkFont(size=20),bg_color="white" ,fg_color="red", width=75, height=65, command=lambda : operation('='))
btnequalsign.grid(row=4, column=3, padx=5, pady=5)




app.mainloop()