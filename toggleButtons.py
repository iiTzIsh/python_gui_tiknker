import tkinter as tk

from tkinter import ttk


root = tk.Tk()

root.title("Simple Add App")
root.iconbitmap('my.ico')


#open with center
display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()
left = int(display_width/2 - 400/2)
top = int(display_height/2 - 400/2)
root.geometry(f'400x400+{left}+{top}') 





# -------------------------------

bulb_state = tk.BooleanVar(value='False')

def change_state():
    if bulb_state.get():
        bulb_state.set(False)
        bulb.config(text='OFF')
    else:
        bulb_state.set(True)
        bulb.config(text='ON')


switch = ttk.Button(root,text='Switch',command=change_state)
switch.pack(side='bottom',pady=20)

bulb = ttk.Label(root,text='OFF')
bulb.place(relx=0.5,rely=0.4)



# ---------------------------------


#run the window
root.mainloop()