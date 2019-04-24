from tkinter import *
from tkinter import ttk

def buttonNumber():
    # global button_Number
    # button_Number += 1
    # if button_Number == 9:
    #     button_Number = 1
#string/interger problems
    if button1["text"] == "":
        button1["text"] = "1"
    elif button1["text"] == "1":
        button1["text"] = "2"
    elif button1["text"] == "2":
        button1["text"] = "3"
    elif button1["text"] == "3":
        button1["text"] = "4"
    elif button1["text"] == "4":
        button1["text"] = "5"
    elif button1["text"] == "5":
        button1["text"] = "6"
    elif button1["text"] == "6":
        button1["text"] = "7"
    elif button1["text"] == "7":
        button1["text"] = "8"
    elif button1["text"] == "8":
        button1["text"] = "9"
    elif button1["text"] == "9":
        button1["text"] = "1"


root = Tk()
root.title("Sudoku")
#themed frame widget so that colors are correct between mainroot window and widgets
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

#must write simpler

button1= ttk.Button(mainframe, text="", width=3, command= buttonNumber)
button1.grid(column=1, row=1, sticky=W)
ttk.Button(mainframe, text="", width=3).grid(column=1, row=2, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=1, row=3, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=1, row=4, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=1, row=5, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=1, row=6, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=1, row=7, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=1, row=8, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=1, row=9, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=2, row=1, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=2, row=2, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=2, row=3, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=2, row=4, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=2, row=5, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=2, row=6, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=2, row=7, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=2, row=8, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=2, row=9, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=3, row=1, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=3, row=2, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=3, row=3, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=3, row=4, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=3, row=5, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=3, row=6, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=3, row=7, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=3, row=8, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=3, row=9, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=4, row=1, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=4, row=2, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=4, row=3, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=4, row=4, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=4, row=5, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=4, row=6, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=4, row=7, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=4, row=8, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=4, row=9, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=5, row=1, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=5, row=2, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=5, row=3, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=5, row=4, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=5, row=5, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=5, row=6, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=5, row=7, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=5, row=8, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=5, row=9, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=6, row=1, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=6, row=2, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=6, row=3, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=6, row=4, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=6, row=5, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=6, row=6, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=6, row=7, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=6, row=8, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=6, row=9, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=7, row=1, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=7, row=2, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=7, row=3, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=7, row=4, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=7, row=5, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=7, row=6, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=7, row=7, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=7, row=8, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=7, row=9, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=8, row=1, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=8, row=2, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=8, row=3, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=8, row=4, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=8, row=5, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=8, row=6, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=8, row=7, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=8, row=8, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=8, row=9, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=9, row=1, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=9, row=2, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=9, row=3, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=9, row=4, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=9, row=5, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=9, row=6, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=9, row=7, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=9, row=8, sticky=W) #command
ttk.Button(mainframe, text="", width=3).grid(column=9, row=9, sticky=W) #command



for child in mainframe.winfo_children(): child.grid_configure(padx=1, pady=1) #padding
#Puts the focus on our entry widget. That way the cursor will start in that field,
#so the user doesn't have to click in it before starting to type.
root.mainloop()
