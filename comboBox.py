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

from calendar import month_name


getmonth_names = [month_name[i] for i in range(1,13)]

selected_month = tk.StringVar()


cbox = ttk.Combobox(root, values=getmonth_names,textvariable=selected_month)
cbox.pack()

label = ttk.Label(root,textvariable=selected_month)
label.pack()

                    





# ---------------------------------


#run the window
root.mainloop()