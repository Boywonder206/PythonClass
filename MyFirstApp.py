import customtkinter as ctk

app = ctk.CTk()
app.title("MYFIRSTAPP")
app.geometry("500x300")

label = ctk.CTkLabel(app, text="Name: ")
label.grid(row=0, column=0)

entry = ctk.CTkEntry(app, placeholder_text="Enter ur name")
entry.grid(row=0, column=1)

app.mainloop()