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

from tkinter import messagebox


def open_messagebox():
    #messagebox.showerror("Error title","This is an error")
    #messagebox.showinfo("Info title","This is an Information")
    #messagebox.showwarning("warning title","This is an warning")

    #messagebox.askokcancel('Ishara madusanka','this is massage')   #ok and cancel buttons
    messagebox.askretrycancel('Ishara madusanka','this is massage') 



button = ttk.Button(root,text='click me',command=open_messagebox)
button.pack()







# ---------------------------------


#run the window
root.mainloop()