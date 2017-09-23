from tkinter import *

root = Tk()
root.mainloop()

def f():
    root = Tk()

    def validate():
        x = btn.get()
        print(x)

    btn = StringVar()
    rad = Radiobutton(root, text="Hello", variable=btn, value="Hello")

    but1 = Button(root, text="Submit", command=validate)
    rad.pack()
    but1.pack()
    root.mainloop()

f()
