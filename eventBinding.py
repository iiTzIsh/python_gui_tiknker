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

btn = ttk.Button(root,text='Click me')
btn.pack()

          #<Motion>  <Enter> <Leave>
btn.bind('<Key>',lambda event: print("Hello"))

entry = ttk.Entry(root)
entry.pack()

entry.bind('<FocusIn>',lambda event:print("Entry Field Selected"))
entry.bind('<FocusOut>',lambda event:print("Entry Field deSelected"))

# ---------------------------------


#run the window
root.mainloop()