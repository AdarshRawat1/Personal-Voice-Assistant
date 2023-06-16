import tkinter as tk
from PIL import Image,ImageTk,ImageSequence
import time 
import os
from pygame import mixer
mixer.init()

import sys
sys.path.append("B:\Ai Assistant\Ai Voice Assistant")
gif_path = r'static\assets\gif\Loading.gif'
audio_path=r'static\assets\audio\intro.mp3'

root=tk.Tk()
root.geometry("800x600")

def play_gif():
    root.lift()
    root.attributes("-topmost",True)
    global img 
    img=Image.open(gif_path)
    lbl=tk.Label(root)
    lbl.place(x=0,y=0)
    mixer.music.load(audio_path)
    mixer.music.play()
    for img in ImageSequence.Iterator(img):
        img= ImageTk.PhotoImage(img)
        lbl.config(image=img)
        root.update()
        time.sleep(0.05)
    root.destroy()
