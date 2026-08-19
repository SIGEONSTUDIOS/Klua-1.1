from Klua import *
import tkinter as tk
import os



def window(title, geometry):
    win = tk.Tk()
    win.title(title)
    win.geometry(geometry)

    canvas = tk.Canvas(win, width=800, height=600)
    canvas.pack()

    return win, canvas


def makeobject_2D(canvas, type, size, color, x, y):
    sizes = {
        1: 20,
        2: 40,
        3: 60,
        4: 80,
        5: 100,
        6: 120,
        7: 140,
        8: 160,
        9: 180,
        10: 200,
    }

    s = sizes[size]

    if type == "triangle":
        canvas.create_polygon(
            x, y - s,
            x - s, y + s,
            x + s, y + s,
            fill=color
        )

    elif type == "circle":
        canvas.create_oval(
            x - s,
            y - s,
            x + s,
            y + s,
            fill=color
        )

    elif type == "square":
        canvas.create_rectangle(
            x - s,
            y - s,
            x + s,
            y + s,
            fill=color
        )


def openwindow(win):
    win.mainloop()