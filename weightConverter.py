import tkinter as tk


# functions

def isNum(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

def convertToG(num):
    if (isNum(num) == False):
        warning.place(relx=0.5, y=float(gui_height)-170, anchor="center")
        entry2.delete(0, len(entry2.get()))
        entry2.insert(0, "Are you dumb?")
        # print("warning")
    else:
        print("convert")
        num = int(num)
        entry2.delete(0, len(entry2.get()))
        entry2.insert(0, num*1000)

def convertToKG(num):
    return num/1000

def pressEnter(event):
    print(event)
    convertToG(convertToG(entry1.get()))



gui_width = "600"
gui_height = "370"

gui = tk.Tk()
gui.title("Unit Converter")
gui.geometry(gui_width+"x"+gui_height)
gui.resizable(0,0)
gui.config(background="#F9F7E8")

photo = tk.PhotoImage(file='D:\Side-Projects\Python\Weight Converter\icon.png')
gui.iconphoto(False, photo)


label = tk.Label(gui, text="Unit Converter", font=("Helvetica", 30, "bold"), fg="#61BFAD", height=3, background="#F9F7E8")
label.pack()


frame = tk.Frame(gui, width=150, height=150, background="#F9F7E8")
frame.pack()


# first unit
entry1 = tk.Entry(frame, border=0, font=("Helvetica", 13))
entry1.grid(row=0, column=0)

l1 = tk.Label(frame, text="Killograms", background="#F9F7E8", fg="#61BFAD", font=("Helvetica", 13, "bold"))
l1.grid(row=1, column=0)


# equals sign
equalsSign = tk.Label(frame, text="=", background="#F9F7E8", fg="#61BFAD", font=("Helvetica", 13, "bold"))
equalsSign.grid(row=0, column=1)


#second unit
entry2 = tk.Entry(frame, border=0, font=("Helvetica", 13))
entry2.grid(row=0, column=2)

l2 = tk.Label(frame, text="Grams", background="#F9F7E8", fg="#61BFAD", font=("Helvetica", 13, "bold"))
l2.grid(row=1, column=2)


# convert button
convert = tk.Button(gui, text="Convert", command=lambda:convertToG(entry1.get()), height=2, width=13, border=0, background="#FF8B8B", fg="White", font=("Helvetica", 13, "bold"))
convert.place(relx=0.5, y=float(gui_height)-120, anchor="center")


#warning
warning = tk.Label(gui, text="Invalid Entry", background="#F9F7E8", font=("Helvetica", 11, "bold"), fg="#E54B4B")


# convert with enter key
gui.bind("<Return>", pressEnter)



gui.mainloop()