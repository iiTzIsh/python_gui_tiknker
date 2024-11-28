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

spinbox_val = tk.StringVar()
                           
                            #values=[1,2,3,4,5,6,7,8,9]
spinBox = ttk.Spinbox(root,from_= 5, to=15,increment=2,textvariable=spinbox_val)
spinBox.pack()


label = ttk.Label(root,textvariable=spinbox_val)
label.pack()


# ---------------------------------


#run the window
root.mainloop()