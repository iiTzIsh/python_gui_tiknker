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

# only can select 1 in radio

radio_var = tk.StringVar()


def select_radio():
    label.configure(text=radio_var.get())


radio1 = ttk.Radiobutton(root,text='python',value='python',variable=radio_var,command=select_radio)
radio1.pack()

radio2 = ttk.Radiobutton(root,text='Java',value='Java',variable=radio_var,command=select_radio)
radio2.pack()

radio3 = ttk.Radiobutton(root,text='C++',value='C++',variable=radio_var,command=select_radio)
radio3.pack()


label = ttk.Label(root)
label.pack()





# ---------------------------------


#run the window
root.mainloop()