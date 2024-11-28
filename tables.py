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
root.geometry(f'500x400+{left}+{top}') 





# -------------------------------

table = ttk.Treeview(root,columns=('name','age','email'),show='headings')
table.heading('name',text='Name')
table.heading('age',text='Age')
table.heading('email',text='Email')

table.column('age',width=100)   #set width

name = ['Ishara','nimal','saman','ish']
age = [34,22,25,23]

for idx, value in enumerate(name):
    table.insert('', idx, values=(name[idx], age[idx], f'{name[idx]}@gmail.com'))


table.pack()


def selected_items(event):
    label.configure(text=table.item(table.selection())['values'][0])

table.bind('<<TreeviewSelect>>',lambda event:selected_items(event))


label = ttk.Label(root)
label.pack()

# ---------------------------------


#run the window
root.mainloop()