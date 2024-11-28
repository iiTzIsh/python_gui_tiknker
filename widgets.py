import tkinter as tk



root = tk.Tk()

root.title("Basic Widgets")
root.iconbitmap('my.ico')


#open with center
display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()
left = int(display_width/2 - 400/2)
top = int(display_height/2 - 400/2)
root.geometry(f'400x400+{left}+{top}') 

# -------------------------------

from tkinter import ttk   #modern widget can use

def button_click_func():
    entry_field_value = entry.get()
    label.configure(text=entry_field_value)

    button.configure(state='disabled')   #disable button 1 time only


entry = ttk.Entry(root)
entry.pack()

button = ttk.Button(root,text='Click me',command=button_click_func)
button.pack()

label = ttk.Label(root)
label.pack()
# label.configure(text = 'ish')     --> display text normally



# ---------------------------------


#run the window
root.mainloop()