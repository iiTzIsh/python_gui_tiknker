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




#toplevel class
# -------------------------------

def increment_val():
    value.set(value.get()+1)

value = tk.IntVar(value=0)

def create_subwindow():
    global subwindow
    subwindow = tk.Toplevel()
    subwindow.title("subwindow")
    subwindow.geometry(f'400x400+{left}+{top}') 

    sub_but = ttk.Button(subwindow,text='click me',command=increment_val)
    sub_but.pack()

    sub_le = ttk.Label(subwindow,textvariable=value)
    sub_le.pack()


def close_subwindow():
    subwindow.destroy()

main_button = ttk.Button(root,text = 'open sub window',command=create_subwindow)
main_button.pack()


close_button = ttk.Button(root,text = 'close sub window',command=close_subwindow)
close_button.pack()


# ---------------------------------


#run the window
root.mainloop()