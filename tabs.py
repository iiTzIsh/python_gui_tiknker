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

notebook = ttk.Notebook(root)

frame1 = ttk.Frame(notebook,width=200,height=100,relief=tk.GROOVE)
frame1.propagate(False)
frame1.pack()

frame2 = ttk.Frame(notebook,width=200,height=100,relief=tk.GROOVE)
frame2.propagate(False)
frame2.pack()

notebook.add(frame1,text='input')        # tabs widiyat gnne frames
notebook.add(frame2,text='output') 
notebook.pack()


entry_value = tk.StringVar()

def add_name():
    table.insert('',tk.END,values= entry_value.get())
    entry_value.set('')    #reset no display any text in entry field


#input tab
entry = ttk.Entry(frame1,textvariable=entry_value)
entry.pack(pady=10)

button = ttk.Button(frame1,text='submit',command=lambda: add_name())
button.pack()

#output tab
table = ttk.Treeview(frame2,columns=('Names'),show='headings')
table.column('Names',width=198)
table.heading('Names',text='Names')
table.pack()




# ---------------------------------


#run the window
root.mainloop()