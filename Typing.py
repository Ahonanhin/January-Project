import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
import Data_viewer as dv

app = Tk()
app.title("Countrynator")
app.geometry("1200x1000")
app.minsize(700,400)
app.maxsize(1500,1200)
app.configure( bg = "black")


txt = tk.StringVar()
text_entry = ttk.Entry(app, textvariable = txt, font= "Times 14", width= 700).pack()
text_output = ttk.Label(app, text= "", font = "Agency_FB 18")
text_output.pack()

def find_country(text):
     for capital in text:
         if capital in dv.list_of_capitals:
            text_output.config(text = dv.get_country_from_capital(capital))

def find_capital(text):
     for country in text:
         if country in dv.list_of_countries:
            text_output.config(text = dv.get_capital_from_country(country))

def find_currency(text):
     for country in text:
         if country in dv.list_of_countries:
            text_output.config(text = dv.get_currency_from_country(country))


def find():
    text = txt.get()
    text = text.split(" ")
    print(text)
    if any(elem in dv.keywords_3 for elem in text):
        find_country(text)
    elif any(elem in dv.keywords_2 for elem in text):
        find_capital(text)
    else:
        find_currency(text)

button = ttk.Button(app, text = "Find", command = find, width =300)
button.pack()
app.mainloop()