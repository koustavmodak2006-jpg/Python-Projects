from tkinter import *
from random import choice,shuffle
from datetime import datetime
import json
from tkinter import messagebox
import pyperclip

screen = Tk()
screen.title("Password Manager")
pass_manage_img = PhotoImage(file="Untitled.png")
canvas = Canvas(width=700,height=600,bg="#0a020f")
canvas.create_image(350,300,image=pass_manage_img)
canvas.pack()

def PASS_GEN():
    char_small = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    char_big = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    digit = ['0','1','2','3','4','5','6','7','8','9']
    special_char = ['@','&','!','#','$','%','*']

    pass_entry.delete(0,END)
    pas_code = []
    for i in range(3):
        pas_code.append(choice(char_small))
        pas_code.append(choice(char_big))
        pas_code.append(choice(digit))
        pas_code.append(choice(special_char))
    shuffle(pas_code)
    password = "".join(pas_code)

    pass_entry.insert(0,password)

def PASSWORD_STRENGTH(password):
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in "@&!#$%*" for c in password): score += 1
    if len(password) >= 12: score += 1
    labels = {1: "Weak 🔴", 2: "Fair 🟠", 3: "Good 🟡", 4: "Strong 🟢", 5: "Very Strong 💪"}
    return labels.get(score, "Weak 🔴")

def ADD():
    website = web_entry.get()
    email = id_entry.get()
    pas = pass_entry.get()
    date_string = datetime.now().strftime("Dated %d %B at %H:%M")

    if 0 <= len(website) <=3:
        messagebox.showerror(title="Error",message="Web-site entry is too short..!!")
        return

    entry = {website: {"Email": email, "password": pas, "Registered on ": date_string, }}

    try:
        with open("user_data.json", mode="r") as file:
            data = json.load(file)

    except (FileNotFoundError,json.JSONDecodeError):
        data = {}

    data.update(entry)
    with open("user_data.json",mode="w") as file:
        json.dump(data,file, indent=4)
        pyperclip.copy(pas)
        messagebox.showinfo("Saved!", f"Password for {website} saved.\nStrength of password is:- \n{PASSWORD_STRENGTH(pas)}")
        web_entry.delete(0, END)
        pass_entry.delete(0, END)

web_entry = Entry(font=("Times New Roman",14,"bold"),bg="#2b73b3",fg="#ffed26")
web_entry.focus()
web_entry.place(x=350,y=405,width=300)

id_entry = Entry(font=("Times New Roman",14,"bold"),bg="#2b73b3",fg="#b6fcfc")
id_entry.insert(0,"koustavmodak2006@gmail.com")
id_entry.place(x=350,y=455,width=300)

pass_entry = Entry(font=("Times New Roman",14,"bold"),bg="#2b73b3",fg="#4fff5b")
pass_entry.place(x=350,y=505,width=160)

gen_pass_image = PhotoImage(file="Gen_pass.png")
pass_gen = Button(image=gen_pass_image,fg="red",padx=40,font=("Arial",11,"bold"),command=PASS_GEN,highlightthickness=0,highlightbackground="#2b73b3")
pass_gen.place(x=528,y=494)

add_button = PhotoImage(file="add.png")
final = Button(image=add_button,command=ADD,padx=150,font=("Arial",11,"bold"),highlightthickness=0)
final.place(x=353,y=555)

screen.mainloop()



# show_pass = False
# def toggle_pass():
#     global show_pass
#     show_pass = not show_pass
#     pass_entry.config(show="" if show_pass else "*")
#
# pass_entry.config(show="*")  # Hide by default
# toggle_btn = Button(text="👁", command=toggle_pass)
# toggle_btn.place(x=490, y=505)