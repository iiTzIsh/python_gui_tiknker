import tkinter as tk



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



from tkinter import ttk


number1 = tk.IntVar()
number2 = tk.IntVar()
answer = tk.StringVar()


def button_func(num1,num2):
    sum = num1+num2
    answer.set(f'Answer is : {sum}')



entry1 = ttk.Entry(root,textvariable=number1)
entry1.pack()

entry2 = ttk.Entry(root,textvariable=number2)
entry2.pack()

button = ttk.Button(root,text="Add Numbers",command=lambda: button_func(number1.get(),number2.get()))
button.pack()

label = ttk.Label(root,textvariable=answer)
label.pack()




# ---------------------------------


#run the window
root.mainloop()