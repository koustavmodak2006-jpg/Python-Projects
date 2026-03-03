from tkinter import *
from tkinter import messagebox,simpledialog

def Petrol(rupees,liter):
    canvas.create_text(240, 180, text=PETROL_RATE, font=("Arial", 18, "normal"), fill="#2596be")
    canvas.create_text(240, 80, text=rupees, font=("Arial", 18, "normal"), fill="#2596be")
    canvas.create_text(240, 130, text=liter, font=("Arial", 18, "normal"), fill="#2596be")

def Diesel(rupees,liter):
    canvas.create_text(240, 180, text=DIESEL_RATE, font=("Arial", 18, "normal"), fill="#2596be")
    canvas.create_text(240, 80, text=rupees, font=("Arial", 18, "normal"), fill="#2596be")
    canvas.create_text(240, 130, text=liter, font=("Arial", 18, "normal"), fill="#2596be")

PETROL_RATE = 113.36
DIESEL_RATE = 91.73

window = Tk()
window.title("Petrol_Pump")
window.config(height=600,width=400)

fuel_pump_img = PhotoImage(file="Fuel_Pump.png")
canvas = Canvas(height=475,width=700,highlightthickness=0)
canvas.create_image(353,238,image=fuel_pump_img)
canvas.grid(row=0,column=0)

is_liter = messagebox.askquestion(title=None,message="Do you want Fuel in Litres..?")
if is_liter == 'yes':
    is_petrol = messagebox.askyesno(title=None, message="Do you want Petrol (in L) ?")
    var = "(L)"
    if is_petrol:
        Liter = simpledialog.askfloat(title=None, prompt="How Much (Liter) Petrol do you want ?")
        if Liter != None:
            Petrol(round(Liter*PETROL_RATE,2),Liter)
            cal_c_amount = canvas.create_text(490, 275, text=f"{float(Liter)} {var}", font=("Arial", 14, "normal"))
        else:
            print("Invalid Input..!!")
            window.destroy()
    else:
        is_diesel = messagebox.askyesno(title=None,message="Do you want Diesel (in L)?")
        if is_diesel:
            Liter = simpledialog.askfloat(title=None, prompt="How Much (Liter) Diesel do you want?")
            if Liter != None:
                Diesel(round(Liter*DIESEL_RATE,2),Liter)
                cal_c_amount = canvas.create_text(490, 275, text=f"{float(Liter)} {var}", font=("Arial", 14, "normal"))
            else:
                print("Invalid Input..!!")
                window.destroy()
        else:
            print("Why then you wasted my time...!!!!")
            window.destroy()
else:
    is_fuel = messagebox.askyesno(title=None, message="Do you want Fuel (in ₹) ?")
    if is_fuel:
        var = "(₹)"
        is_petrol = messagebox.askyesno(title="", message="Click 'YES' for Petrol (in ₹).")
        if is_petrol:
            Rupees = simpledialog.askfloat(title=None, prompt="How Much Amount (in ₹) Petrol you want :-")

            if Rupees != None:
                Petrol(round((Rupees / PETROL_RATE), 2),round((Rupees/PETROL_RATE),2))
                cal_c_amount = canvas.create_text(490, 275, text=f"{float(Rupees)} {var}", font=("Arial", 14, "normal"))
            else:
                print("Invalid Input")
                window.destroy()
        else:
            is_diesel = messagebox.askyesno(title="", message="Click 'YES' for Diesel (in ₹)..")
            if is_diesel:
                Rupees = simpledialog.askfloat(title=None, prompt="How Much Amount (in ₹) Diesel you want :-")
                if Rupees != None:
                    Diesel(round((Rupees / DIESEL_RATE), 2),round((Rupees/DIESEL_RATE),2))
                    cal_c_amount = canvas.create_text(490, 275, text=f"{float(Rupees)} {var}", font=("Arial", 14, "normal"))
                else:
                    print("Invalid Input..!!")
                    window.destroy()
            else:
                print("Why then you wasted my time...!!!!")
                window.destroy()
    else:

        window.destroy()
window.mainloop()
