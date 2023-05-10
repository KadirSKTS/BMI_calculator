from tkinter import *

FONT = ("arial",20,"normal")
window = Tk()
window.title("BMI calculator")
window.minsize(width= 350, height= 350)

label_height = Label(text="enter your height(m)", font=("arial",16,"normal"))
label_height.pack()

entry_height = Entry(width=20)
entry_height.focus()
entry_height.pack()

label_weight = Label(text="enter your weight(kg)", font=("arial",16,"normal"))
label_weight.pack()

entry_weight = Entry(width=20)

entry_weight.pack()

def calculate():
    try:
        BMI = float(entry_weight.get()) / float(entry_height.get()) **2

        if BMI <18.5:
            label_result.config(text=f"BMI: {BMI:.2f}. You are underwight")

        elif 18<= BMI < 24.9:
            label_result.config(text=f"BMI: {BMI:.2f}. You are normal weight")

        elif 25.0 <= BMI <29.9:
            label_result.config(text=f"BMI: {BMI:.2f}. You are overweight")

        elif 30.0 <= BMI < 34.9:
            label_result.config(text=f"BMI: {BMI:.2f}. You are obese")

        elif 35 <= BMI :
            label_result.config(text=f"BMI: {BMI:.2f}. You are extremly obese")

        if float(entry_weight.get()) == 0:
            label_result.config(text="weight can not be zero")




    except ValueError:
        label_result.config(text="doğru değer girdiğinizden emin misiniz?",font=("arial",14,"normal"))
    except ZeroDivisionError:
        label_result.config(text="uzunluk 0 olamaz", font=("arial", 14, "normal"))


button_for_height = Button(text="calculate", command= calculate)
button_for_height.pack()

label_result = Label(text=" ",font=FONT)
label_result.pack()

window.mainloop()
