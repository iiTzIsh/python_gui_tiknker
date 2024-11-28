import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Todo App")
root.geometry('400x500')
root.resizable(False,False)
root.iconbitmap('my.ico')



heading = ttk.Label(root,text='All Tasks',font='arial 20 bold')
heading.pack(pady=20)

#--------------
frame = ttk.Frame(root,width=400,height=50) 
frame.pack()

taskentry = ttk.Entry(frame,font='arial 18',width=25)
taskentry.pack()


task_list = []

def add_task(event):
    task = taskentry.get()
    taskentry.delete(0,tk.END)

    if task: 
        with open('tasklist.txt', 'a') as file:         #save in txt
            file.write(f'{task}\n')
        listbox.insert(tk.END, task)
        task_list.append(task)

taskentry.bind('<Return>',add_task)


#--------------






#--------------

def delete_task():
    task = listbox.get(tk.ANCHOR)
    listbox.delete(tk.ANCHOR)
    task_list.remove(task)
    with open('tasklist.txt','w') as file:
        for task in task_list:
            file.write(f'{task}\n')



def opentask():
    with open('Ishtasklist.txt','r') as file:
        tasks = file.readlines()

    for task in tasks:
        if task != '\n':
            listbox.insert(tk.END,task)
            task_list.append(task)




frame1 = ttk.Frame(root,width=300,height=250) 
frame1.pack()

listbox = tk.Listbox(frame1,font='arial 12',width=40,height=16)
listbox.pack()

opentask()


deletebtn = ttk.Button(root,text='Delete',command=delete_task)
deletebtn.pack(side='bottom',pady=12,ipadx=5,ipady=5)
#--------------


root.mainloop()