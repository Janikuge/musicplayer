
from tkinter import *
import pygame
import os

# creating main window
root = Tk()
root.title('Music Player')
root.geometry('600x400')

# initalizing pygame
pygame.init()

# creating play list
playlist = []
for file in os.listdir('songs/'):
    if file.endswith('.mp3'):
        realdir = os.path.realpath('songs/' + file)
        playlist.append(realdir)

# creating pygame mixer
pygame.mixer.init()
# setting up volume
pygame.mixer.music.set_volume(0.7)

# creating track variables
track = StringVar()
status = StringVar()

# creating functions
def play():
    # getting selected song
    pygame.mixer.music.load(track.get())
    # playing the song
    pygame.mixer.music.play()
    # updating status
    status.set('Playing')

def pause():
    # pausing the song
    pygame.mixer.music.pause()
    # updating status
    status.set('Paused')

def resume():
    # resuming the song
    pygame.mixer.music.unpause()
    # updating status
    status.set('Playing')

def stop():
    # stopping the song
    pygame.mixer.music.stop()
    # updating status
    status.set('Stopped')

# creating track frame
trackframe = Frame(root)
trackframe.pack(pady=20)

# creating label
tracklabel = Label(trackframe, text='Track :', font='Arial 15 bold')
tracklabel.grid(row=0, column=0, padx=20, pady=10)

# creating track list
tracklist = Listbox(trackframe, width=60, selectbackground='gray')
tracklist.grid(row=0, column=1, padx=20)

# adding playlist to track list
for item in playlist:
    tracklist.insert(END, item)

# creating bottom frame
bottomframe = Frame(root)
bottomframe.pack()

# creating play button
playbtn = Button(bottomframe, width=8, text='PLAY', command=play)
playbtn.grid(row=0, column=0, padx=10, pady=20)

# creating pause button
pausebtn = Button(bottomframe, width=8, text='PAUSE', command=pause)
pausebtn.grid(row=0, column=1, padx=10, pady=20)

# creating resume button
resumebtn = Button(bottomframe, width=8, text='RESUME', command=resume)
resumebtn.grid(row=0, column=2, padx=10, pady=20)

# creating stop button
stopbtn = Button(bottomframe, width=8, text='STOP', command=stop)
stopbtn.grid(row=0, column=3, padx=10, pady=20)

# creating status bar
statusbar = Label(root, textvariable=status, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

# setting track
def set_track(event):
    # getting selected song
    track_selection = tracklist.curselection()
    # setting selected song
    track.set(tracklist.get(track_selection[0]))

# adding double click function
tracklist.bind('<Double-Button-1>', set_track)

# running main loop
root.mainloop()
