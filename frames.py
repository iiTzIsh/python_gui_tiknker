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


frame1 = ttk.Frame(root,width=300,height=100,relief=tk.GROOVE)
frame1.pack_propagate(False)
frame1.pack(side='left')

entry = ttk.Entry(frame1)
entry.pack(pady=10)

button = ttk.Button(frame1,text='submit')
button.pack()






frame2 = ttk.Frame(root,width=300,height=100,relief=tk.GROOVE)
frame2.pack_propagate(False)   #border ek balagn onnm
frame2.pack(side='right')        #align to right

label = ttk.Label(frame2,text='welcome')
label.pack(pady=10)

button2 = ttk.Button(frame2,text='click me')
button2.pack()





# ---------------------------------


#run the window
root.mainloop()