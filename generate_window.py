import os.path
import tkinter
from tkinter import *

from PIL import ImageTk, Image


def render_team():
    window = Tk()
    window.title("Tims Team")
    window.geometry("576x96")
    image = Image.open("background.png")
    img = ImageTk.PhotoImage(image)
    label = tkinter.Label(image=img)
    label.place(x=0, y=0)

    if os.path.isfile("pokemon_pictures/p1.png"):
        image1 = Image.open("pokemon_pictures/p1.png")
        img1 = ImageTk.PhotoImage(image1)
        label1 = tkinter.Label(image=img1)
        label1.place(x=0, y=0)

    if os.path.isfile("pokemon_pictures/p2.png"):
        image2 = Image.open("pokemon_pictures/p2.png")
        img2 = ImageTk.PhotoImage(image2)
        label2 = tkinter.Label(image=img2)
        label2.place(x=96, y=0)

    if os.path.isfile("pokemon_pictures/p3.png"):
        image3 = Image.open("pokemon_pictures/p3.png")
        img3 = ImageTk.PhotoImage(image3)
        label3 = tkinter.Label(image=img3)
        label3.place(x=192, y=0)

    if os.path.isfile("pokemon_pictures/p4.png"):
        image4 = Image.open("pokemon_pictures/p4.png")
        img4 = ImageTk.PhotoImage(image4)
        label4 = tkinter.Label(image=img4)
        label4.place(x=288, y=0)

    if os.path.isfile("pokemon_pictures/p5.png"):
        image5 = Image.open("pokemon_pictures/p5.png")
        img5 = ImageTk.PhotoImage(image5)
        label5 = tkinter.Label(image=img5)
        label5.place(x=384, y=0)

    if os.path.isfile("pokemon_pictures/p6.png"):
        image6 = Image.open("pokemon_pictures/p6.png")
        img6 = ImageTk.PhotoImage(image6)
        label6 = tkinter.Label(image=img6)
        label6.place(x=480, y=0)
    window.mainloop()
