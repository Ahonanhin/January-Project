import tkinter as tk

from tkinter import *
from PIL import ImageTk, Image
app = Tk()
app.title("Countrynator")
app.geometry("1200x1000")
app.minsize(700,400)
app.maxsize(1500,1200)
app.configure( bg = "black")

image = Image.open("map.gif")
pic = ImageTk.PhotoImage(image)

img_label = Label(image = pic)
img_label.pack()

main_text = Label(app, text = "Welcome to the Countrynator.\n Do you want to speak or type?", font = "Times 40", bg = "black", fg = "white")
main_text.pack()

speak_button = Button(app, text = "Speak", bd = "10", bg = "White", fg = "black", font = "Agency_FB", borderwidth = 2)
speak_button.pack()

type_button = Button(app, text = " Type ", bd = "10", bg = "White", fg = "black", font = "Agency_FB", borderwidth = 2)
type_button.pack()
# cover_label = Canvas(app, width = 500, height = 400, bg = "lightgreen")
# cover_label.grid(row = 2, column = 2)
# photo_1 = ImageTk.PhotoImage(Image.open("map.jpg"))
# photo_1.create_image( 20,20, ANCHOR = NW, image = photo_1)
# cover_label = Label(image = photo_1)
# cover_label.pack()












app.mainloop()