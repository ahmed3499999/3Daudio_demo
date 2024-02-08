import tkinter as tk
from PIL import Image, ImageTk
import sound as snd

x, y = 0, 0
h, w = 500, 500
soundIconH, soundIconW = 50, 50
isButtonDown = False

window = tk.Tk()

playbackFrame = tk.Frame(master=window, background='grey', height= 50)
playbackFrame.pack(expand=True, fill=tk.X)
playBtn = tk.Button(master=playbackFrame, background='orange', text="play", command=snd.play)
pauseBtn = tk.Button(master=playbackFrame, background='orange', text="pause", command=snd.pause)
fileNameEntry = tk.Entry(master=playbackFrame)
loadBtn = tk.Button(master=playbackFrame, background='orange', text='load')
playBtn.grid(row=0, column=0,sticky=tk.E, padx=20)
pauseBtn.grid(row=0, column=1, sticky=tk.E, padx=20)
fileNameEntry.grid(row=0, column=2, sticky=tk.E, padx=20)
loadBtn.grid(row=0, column=3, sticky=tk.E, padx=20)

image = Image.open("speaker.png").resize((75,75))
soundIconImg = ImageTk.PhotoImage(image)
image = Image.open("headphones.png").resize((75,75))
sourceIconImg = ImageTk.PhotoImage(image)

canvas = tk.Canvas(master=window, height=h, width=w, background="white")
soundIconID = canvas.create_image(0, 0, image = soundIconImg)
sourceIconID = canvas.create_image(h/2, w/2, image = sourceIconImg)
canvas.pack()

def onLoadButton(event):
    snd.load_sound(fileNameEntry.get())

def onMotion(event):
    global x, y, isButtonDown
    x = event.x
    y = event.y
    updateSoundIcon()
    if isButtonDown: snd.updateSourcePos(x - h/2, y - h/2)

def updateSoundIcon():
    if not isButtonDown: return
    canvas.moveto(soundIconID, x=(-soundIconW/2 + x), y=(-soundIconH/2 + y))

def toggleButton(e):
    global isButtonDown
    isButtonDown = not isButtonDown
    if isButtonDown: updateSoundIcon()

def deinit():
    snd.deinit()
    window.quit()

loadBtn.bind("<Button-1>", onLoadButton)
canvas.bind("<Motion>", onMotion)
canvas.bind("<Button-1>", toggleButton)
canvas.bind("<ButtonRelease-1>", toggleButton)
window.protocol("WM_DELETE_WINDOW", deinit)

snd.init()
tk.mainloop()