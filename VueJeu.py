from tkinter import *

def affichageMessage(toile, message, x0=500, y0=200, size=48):
    toile.create_text(x0, y0, text=message, font=("Purisa", size))
