import tkinter as tk

#create a window
root = tk.Tk()


root.title("Ishara Madusanka")
root.iconbitmap('my.ico')
# root.geometry('400x400')             #widthxheight
# root.geometry('400x400+300+300')     #widthxheight+left+top
# root.resizable(False,False)          #resizable krnn bari wen



#open with center
display_width = root.winfo_screenwidth()
display_height = root.winfo_screenheight()
left = int(display_width/2 - 400/2)
top = int(display_height/2 - 400/2)
root.geometry(f'400x400+{left}+{top}') 




#run the window
root.mainloop()