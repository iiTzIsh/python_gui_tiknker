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

canvas = tk.Canvas(root,bg='white')
canvas.pack()

# canvas.create_rectangle((10,10,100,200),fill='gray')
# canvas.create_oval((110,110,200,250),fill='green')                   
# canvas.create_line((0,0,300,250),fill='green',width=5) 

def draw(event):
    x= event.x
    y= event.y
    canvas.create_oval((x,y,x,y))

#canvas.bind('<Motion>',draw)

def start_draw(event):
    x= event.x
    y= event.y
    canvas.create_oval((x,y,x,y),fill='black')
    canvas.bind('<B1-Motion>',draw)

canvas.bind('<Button-1>',start_draw)


# ---------------------------------


#run the window
root.mainloop()