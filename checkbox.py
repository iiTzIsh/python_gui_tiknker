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


check_val = [tk.StringVar(),tk.StringVar()]
label_var = tk.StringVar()

def checkbox_result():
    output_string = "Selected language : "+check_val[0].get() +" "+ check_val[1].get()
    label_var.set(output_string)
    
                                                                           #onvalue ek tma display wenne
check1 = ttk.Checkbutton(root,text='Python',variable=check_val[0],onvalue='Python',offvalue='')   
check1.pack()

check2 = ttk.Checkbutton(root,text='Java',variable=check_val[1],onvalue='Java',offvalue='')
check2.pack()


button = ttk.Button(root,text="Click me",command=checkbox_result)
button.pack()


label = ttk.Label(root,textvariable=label_var)
label.pack()




# ---------------------------------


#run the window
root.mainloop()