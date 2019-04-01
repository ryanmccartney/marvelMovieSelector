#NAME: select.py
#DATE: 31/03/2019

import json
import time
import random
import tkinter as tk
from PIL import Image, ImageTk

coverPath = "noimage.png"

def generate():

    #Open Movie File
    marvelMovies = open('movies.json').read()
    marvel = json.loads(marvelMovies)

    #Select Random Phase
    print("Selecting a Marvel Phase.")
    phases = len(marvel['marvel'])
    phase = random.randint(0, phases-1)
    print("Selecting a movie from Phase "+str(marvel['marvel'][phase]['phase'])+".")

    #Select Movie from phase
    phaseTitles = marvel['marvel'][phase]['movies']
    titles = len(phaseTitles)
    selctedMovie = random.randint(0, titles-1)

    title = phaseTitles[selctedMovie]['title']
    year = phaseTitles[selctedMovie]['year']
    coverPath = phaseTitles[selctedMovie]['cover']

    selectedTitle["text"] = str(title)
    releaseYear["text"] = str(year)
    phaseText["text"] = "Phase "+str(marvel['marvel'][phase]['phase'])

    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    cover = Image.open(coverPath)
    cover = cover.resize((400, 650), Image.ANTIALIAS) 
    coverImage = ImageTk.PhotoImage(cover)
    poster.configure(image=coverImage)
    vlabel.pack()

    print("You should watch "+title+".")

root = tk.Tk()
root.title("Marvel Movie Generator")
root.configure(background='black')

#size of the window
root.geometry("450x880")

frame = tk.Frame(root)
frame.pack()
        
buttonGenerate = tk.Button(frame,text="Generate",fg="white",bg="green",font=("Arial", 16), height=2, width=10, command=generate)

buttonGenerate.pack(side=tk.LEFT)

buttonQuit = tk.Button(frame,text="Quit",fg="white",bg="red",font=("Arial", 16), height=2,width=10, command=quit)
buttonQuit.pack(side=tk.LEFT)

selectedTitle = tk.Label(root, bg="black",fg="white")
selectedTitle.config(font=("Arial", 16))
selectedTitle.pack()
releaseYear = tk.Label(root, bg="black",fg="white")
releaseYear.config(font=("Arial", 20))
releaseYear.pack()

#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
cover = Image.open(coverPath)
cover = cover.resize((400, 650), Image.ANTIALIAS) 
coverImage = ImageTk.PhotoImage(cover)
poster = tk.Label(root, bg="black", image=coverImage)

#The Pack geometry manager packs widgets in rows or columns.
poster.pack(fill = "both", expand = "yes")

phaseText = tk.Label(root, bg="black",fg="white")
phaseText.config(font=("Arial", 18),padx=10, pady=20)
phaseText.pack()

root.mainloop()