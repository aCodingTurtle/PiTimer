#
#  Tk Test
#

import tkinter

window = tkinter.Tk()
window.title("TkTest")

def HelloWorld():
    print("Hello World!")

text = tkinter.Label(window, text="Hello World!").pack()
button = tkinter.Button(window, text="Click Me!", fg="blue", command=HelloWorld()).pack()

window.mainloop()
