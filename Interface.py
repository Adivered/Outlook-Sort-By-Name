import tkinter as tk
import os

root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def execute():  
    os.system('python Bot.py')
    label1 = tk.Label(root, text= 'Done!', fg='green', font=('helvetica', 12, 'bold'))
    canvas1.create_window(150, 200, window=label1)
    
button1 = tk.Button(text='Click Me',command=execute, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()