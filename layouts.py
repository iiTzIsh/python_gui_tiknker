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


hello_label = ttk.Label(root,text='Hello',background='orange')
welcome_lable = ttk.Label(root,text='welcome',background='yellow')

#---------
#pack method
#hello_label.pack(side='left',expand=True,fill='both')
#welcome_lable.pack()
#-------




#-------
#grid method
#root.columnconfigure(0,weight=1)
#root.columnconfigure(1,weight=1)
#root.columnconfigure(2,weight=1)
##root.rowconfigure(1,weight=1)


#hello_label.grid(row=1,column=1,sticky='nsew')
#welcome_lable.grid(row=0,column=2,sticky='nsew')
#---------




#-------
#place method

hello_label.place(x=100,y=100,width=100,height=100)
welcome_lable.place(relx=0.5,rely=0.5,width=100,height=100)   #relatively  0-1 athare

#---------



# ---------------------------------


#run the window
root.mainloop()