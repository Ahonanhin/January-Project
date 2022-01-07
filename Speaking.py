import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import speech_recognition as sr
import tkinter as tk
import Data_viewer as dv

mic = sr.Microphone()
r = sr.Recognizer()

def find_capital(words):
    for element in words:
            if element in dv.list_of_countries:
                dv.say_capital(element)

def find_country(words):
    for element in words:
            if element in dv.list_of_capitals:
                dv.say_country(element)

def find_currency(words):
    for element in words:
            if element in dv.list_of_countries:
                dv.say_currency(element)
def find():
    with mic as source:
         r.adjust_for_ambient_noise(source)
         audio = r.listen(source)
    words = r.recognize_google(audio)
    words = words.split(" ")
    print(words)
    if any(elem in dv.keywords_3 for elem in words):
        find_country(words)
    elif any(elem in dv.keywords_2 for elem in words):
        find_capital(words)
    else:
        find_currency(words)

app = Tk()
app.title("Countrynator")
app.geometry("1200x1000")
app.minsize(700,400)
app.maxsize(1500,1200)
app.configure( bg = "black")


button = tk.Button(app, text = "Find", command = find, width =300, height= 10)
button.pack()


app.mainloop()



