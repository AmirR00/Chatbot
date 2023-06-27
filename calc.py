import tkinter as tk
win = tk.Tk()
win.title("AdvancedCalculator")
win.geometry("500x350")
win.config(bg="#060426")

def Numplacer(num):
    data = entry.get()
    a = str(num)
    if data[-1] in "+-÷×" and a in "+-÷×":
        pass
    else:
        entry.delete(0, "end")
        entry.insert(0, data+a) 

def equal():
    data = entry.get()
    data = data.replace("×", "*")
    data = data.replace("÷", "/")
    entry.delete(0, tk.END)
    entry.insert(0, eval(data))

def clear():
    entry.delete(0, 'end')

c = tk.Button(win, text="C", font=("consolas", 22), foreground="#09053d" , background="#01041a", width=1, command=clear)
c.place(x=35, y=65)

entry = tk.Entry(win, font=("consolas", 22), foreground="#fefcff", background="#09053d")
entry.place(x=95, y=15)
entry.insert(0, " ")
B1 = tk.Button(win, text="7", font=("consolas", 22), foreground="#09053d" , background="#01041a", width=1, command=lambda:Numplacer(7))
B1.place(x=95, y=65)

B2 = tk.Button(win, text="8", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer(8)   )
B2.place(x=160, y=65)

B3 = tk.Button(win, text="9", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer(9)  )
B3.place(x=225, y=65)

B4 = tk.Button(win, text="÷", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer("÷")  )
B4.place(x=337, y=65)

B5 = tk.Button(win, text="4", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer(4)  )
B5.place(x=95, y=120)

B6 = tk.Button(win, text="5", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer(5)  )
B6.place(x=160, y=120)

B7 = tk.Button(win, text="6", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer(6)  )
B7.place(x=225, y=120)

B8 = tk.Button(win, text="×", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer("×")  )
B8.place(x=337, y=120)

B9 = tk.Button(win, text="1", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer(1)  )
B9.place(x=95, y=175)

B10 = tk.Button(win, text="2", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer(2)  )
B10.place(x=160, y=175)

B11 = tk.Button(win, text="3", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer(3)  )
B11.place(x=225, y=175)

B12 = tk.Button(win, text="- ", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer("-")  )
B12.place(x=337, y=175)

B13 = tk.Button(win, text="0", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer(0)  )
B13.place(x=95, y=230)

B14 = tk.Button(win, text=".", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer(".")  )
B14.place(x=160, y=230)

B15 = tk.Button(win, text="=", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=equal )
B15.place(x=225, y=230)

B16 = tk.Button(win, text="+", font=("consolas", 22), foreground="#000000" , background="#01041a", width=1, command=lambda:Numplacer("+")  )
B16.place(x=337, y=230)


win.mainloop()







