import string
import tkinter as tk

win = tk.Tk()
win.geometry("800x600")
win.title("PasswordChecker")
win.config(bg="#dafabb")

entry = tk.Entry(win, width=45, font=("Calibri", 22), 
                 highlightthickness=3, highlightbackground="#000000")
entry.place(x=70, y=30)

button = tk.Button(win, text="Check your password", width=41, font=("segoe ui", 23),
                   command=lambda: PasswordChecker(entry.get()) )
button.config(background="#f7fabb")
button.place(x=70, y=100)

Lenlabel = tk.Label(win, text="LENGTH", font=("segoe ui", 22,"bold"), bg="#dafabb")
Lenlabel.place(x=70, y=170)

Lenvalue = tk.Label(win, font=("segoe ui", 24), bg="#dafabb")
Lenvalue.place(x=630, y=170)

Caselabel = tk.Label(win, text="CASE", font=("segoe ui", 22,"bold"), bg="#dafabb")
Caselabel.place(x=70, y=240)

Casevalue = tk.Label(win, font=("segoe ui", 24), bg="#dafabb")
Casevalue.place(x=630, y=240)

SPCHlabel = tk.Label(win, text="SPECIAL CHARACTERS", font=("segoe ui", 22,"bold"), bg="#dafabb")
SPCHlabel.place(x=70, y=310)

SPCHvalue = tk.Label(win, font=("segoe ui", 24), bg="#dafabb")
SPCHvalue.place(x=630, y=310)

Numslabel = tk.Label(win, text="NUMBERS", font=("segoe ui", 22,"bold"), bg="#dafabb")
Numslabel.place(x=70, y=380)

Numsvalue = tk.Label(win, font=("segoe ui", 24), bg="#dafabb")
Numsvalue.place(x=630, y=380)

def PasswordChecker(a):
    marks = {"NUMS":0, "LENGTH":0, "U-CASE":0, "L-CASE":0, "SPL-CHARS":0}
    if len(a) > 8:
        marks["LENGTH"] = 100
    lower = False
    for i in a:
        lower = i.islower()
        if lower == True:
            marks["L-CASE"] = 100
            break
    Upper = False
    for i in a:
        Upper = i.isupper()
        if Upper == True:
            marks["U-CASE"] = 100
            break
    spch = string.punctuation
    for i in spch:
        if i in a:
            marks["SPL-CHARS"] = 100
            break
    Num = False
    for i in a:
        Num = i.isnumeric()
        if Num == True:
            marks["NUMS"] = 100
            break
    #Lenvalue  Casevalue  SPCHvalue  Numsvalue
    print(marks)
    if marks["L-CASE"] + marks["U-CASE"] == 200:
        Casevalue.config(text="PASS", fg="#027016")
    else:
        Casevalue.config(text="FAIL", fg="#bf0a00")
    
    if marks["LENGTH"] == 100:
        Lenvalue.config(text="PASS", fg="#027016")
    else:
        Lenvalue.config(text="FAIL", fg="#bf0a00")

    if marks["SPL-CHARS"] == 100:
        SPCHvalue.config(text="PASS", fg="#027016")
    else:
        SPCHvalue.config(text="FAIL", fg="#bf0a00")
    
    if marks["NUMS"] == 100:
        Numsvalue.config(text="PASS", fg="#027016")
    else:
        Numsvalue.config(text="FAIL", fg="#bf0a00")


    print(marks)
    marks.clear()

#userinp = input("Write your password right here: ")

#score = PasswordChecker(userinp)
#print(score)









win.mainloop()