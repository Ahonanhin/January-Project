import speech_recognition as sr
import tkinter as tk
mic = sr.Microphone()
r = sr.Recognizer()


from tkinter import*


window = Tk()
window.title("Speech-to-text")
window.configure(width = 1400, height = 1000, bg = "lightblue")
# title = tk.Label(window, text = "", font = "Times 14")
name = tk.StringVar()

speech = tk.Label(window,text = name ,font = "Times 14")
speech.grid(row = 1, column = 5)


def speak_and_write():
     with mic as source:
         r.adjust_for_ambient_noise(source)
         audio = r.listen(source)
     words = r.recognize_google(audio)
     speech.config(text = ""+ words)

button = tk.Button(window, text = "Speak", command = speak_and_write)
button.grid(row = 4, column = 2)


def click ():
    print(name.get())

button2 =tk.Button(window, text = "print", command = click)
button2.grid(row =5, column = 3)
window.mainloop()

