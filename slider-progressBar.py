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

scale_val = tk.DoubleVar()

scale = ttk.Scale(root,length=260,variable=scale_val,from_=0,to=100)    #orient = 'verticle'
scale.pack()

pbar = ttk.Progressbar(root,variable=scale_val)
pbar.pack()



# ---------------------------------


#run the window
root.mainloop()