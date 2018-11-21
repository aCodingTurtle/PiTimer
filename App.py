#THE TKINTER PROGRAM WILL BE PUT ON PAUSE WHILE OTHER FUNTIONS ARE WORKED ON.

#
# OUTDATED - KIVY WILL PROBABLY BE THE ACTUAL GUI TOOLKIT
#

# -- Tk Program Starts Here -- #
BOXX = 1200
BOXY = 700
BOXGEO = str(BOXX) + 'x' + str(BOXY)

window = tk.Tk()
window.geometry('1200x700')

titleBar = tk.Label(window, text="PiTimer", fg="orange", bg="white", font = "Courier 14")
titleBar.grid(column=3, row=2)

#  Menu Bar  #
menu = tk.Menu(window)

scrambleMenu = tk.Menu(menu)
scrambleMenu.add_command(label="New Scramble")
menu.add_cascade(label="Scramble", menu=scrambleMenu)

sessionMenu = tk.Menu(menu)
sessionMenu.add_command(label="New Session")
menu.add_cascade(label="Session", menu=sessionMenu)

window.config(menu=menu)

#  Scramble Bar  #
scrambleDisp = tk.Label(window,
                        text=scramble2.generateScramble(),
                        fg="orange",
                        bg="white",
                        font="Courier 16 bold")
scrambleDisp.grid(column=0, columnspan=3, pady=5, row=0)

#  Timer  #
timer = tk.Message(window,
                   text="00 : 00 : 0",
                   fg="black",
                   bg="white",
                   font = "Courier 48")
timer.grid(column=0, columnspan=3, row=1)

#  Stats Bar  #
stats = tk.Message(window,
                   text="Stats for a sesson will appear here.",
                   fg="grey",
                   bg="white",
                   font="Courier 16 italic",
                   relief="sunken")
stats.grid(column=0, columnspan=2, row=2)

window.mainloop()
