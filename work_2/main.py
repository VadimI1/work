import random
from tkinter import *
from tkinter import colorchooser

import self as self


class Engine2D():

    def __init__(self):
        self.root = Tk()
        self.root.title("METANIT.COM")
        self.root.geometry("900x600")

        self.canvas = Canvas(bg="white", width=900, height=600)
        self.canvas.pack(anchor=CENTER, expand=1)

        self.col = colorchooser.askcolor()
        print(f"Pencil color: {self.col[1]}")

    #функция очищения холста
    def clear_canvas(self):
        self.canvas.delete("all")

        button1 = Button(text="Quit", command=quit, anchor=W)
        button1.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button1_window = self.canvas.create_window(760, 550, anchor=NW, window=button1)

        button2 = Button(text="Circle", command=lambda: self.draw_circle(color = self.col[1]), anchor=W)
        button2.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button2_window = self.canvas.create_window(10, 550, anchor=NW, window=button2)

        button3 = Button(text="Square", command=lambda: self.draw_square(color = self.col[1]), anchor=W)
        button3.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button3_window = self.canvas.create_window(150, 550, anchor=NW, window=button3)

        button4 = Button(text="Triangle", command=lambda: self.draw_triangle(color = self.col[1]), anchor=W)
        button4.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button4_window = self.canvas.create_window(290, 550, anchor=NW, window=button4)

        button5 = Button(text="Color selection", command=lambda: self.color_selection(), anchor=W)
        button5.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button5_window = self.canvas.create_window(430, 550, anchor=NW, window=button5)

        button6 = Button(text="Cleaning the canvas", command=lambda: self.clear_canvas(), anchor=W)
        button6.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button6_window = self.canvas.create_window(580, 550, anchor=NW, window=button6)



    def draw_circle(self, color = None):
        x, y, r = self.random()
        self.canvas.create_oval(x - r, y - r, x + r, y + r, fill=color, outline="#004D40")
        print(f"Drawing Circle: ({x}, {y}) with radius {r}.")


    def draw_square(self, color = None):
        x, y, r = self.random()
        self.canvas.create_rectangle(x - r, y - r, x + r, y + r, fill=color, outline="#004D40")
        print(f"Drawing Square: ({x-r}, {y-r}), ({x+r}, {y-r}), ({x-r}, {y+r}), ({x+r}, {y+r}).")

    def draw_triangle(self, color = None):
        x, y, r = self.random()
        points = (
            (x, y),
            (x + r, y),
            (x + r/2,y/2)
        )
        self.canvas.create_polygon(*points, fill=color, outline="#004D40")
        print(f"Drawing Triangle: ({x}, {y}), ({x+r}, {y}), ({x+r/2}, {y/2}).")

    def color_selection(self):
        self.col = colorchooser.askcolor()
        print(f"Pencil color: {self.col[1]}")

    def random(self):
        x = random.randint(50, 850)
        y = random.randint(50, 550)
        r = random.randint(10,100)
        return x, y, r


    def start(self):

        button1 = Button(text="Quit", command=quit, anchor=W)
        button1.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button1_window = self.canvas.create_window(760, 550, anchor=NW, window=button1)

        button2 = Button(text="Circle", command=lambda : self.draw_circle(color = self.col[1]), anchor=W)
        button2.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button2_window = self.canvas.create_window(10, 550, anchor=NW, window=button2)

        button3 = Button(text="Square", command=lambda : self.draw_square(color = self.col[1]), anchor=W)
        button3.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button3_window = self.canvas.create_window(150, 550, anchor=NW, window=button3)

        button4 = Button(text="Triangle", command=lambda : self.draw_triangle(color = self.col[1]), anchor=W)
        button4.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button4_window = self.canvas.create_window(290, 550, anchor=NW, window=button4)

        button5 = Button(text="Color selection", command=lambda: self.color_selection(), anchor=W)
        button5.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button4_window = self.canvas.create_window(430, 550, anchor=NW, window=button5)

        button6 = Button(text="Cleaning the canvas", command=lambda: self.clear_canvas(), anchor=W)
        button6.configure(width=15, activebackground="#33B5E5", relief=FLAT)
        button4_window = self.canvas.create_window(580, 550, anchor=NW, window=button6)


        self.root.mainloop()



cir = Engine2D()
cir.start()

