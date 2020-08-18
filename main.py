import tkinter as tk
from tkinter.ttk import *
import os
root = tk.Tk()
root.title('P0NG by Taulantët LTD')

fname = "qepe.gif"
bg_image = tk.PhotoImage(file=fname)

w = bg_image.width()
h = bg_image.height()

width = w
height = h

screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()

x = (screenWidth / 2) - (width / 2)
y = (screenHeight / 2) - (height / 2)

root.geometry("%dx%d+%d+%d" % (w, h, x, y))

cv = tk.Canvas(width=w, height=h)
cv.pack(side='top', fill='both', expand='yes')
cv.create_image(0, 0, image=bg_image, anchor='nw')


def callback():
    root.destroy()
    os.system('gamecorrect105PM.py')
    root.destroy()

btn1 = tk.Button(cv, text="PLAY", command = callback, height = 1, width = 5)

btn1.pack(side='top', padx=0, pady=150, anchor='center')
btn2 = tk.Button(cv, text="Quit", command=root.destroy)

btn2.pack(side='top', padx=0, pady=50, anchor='center')
root.mainloop()