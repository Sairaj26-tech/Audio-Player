#import pygame
import tkinter as tkr
import os

"""window geometry"""
player=tkr.Tk() 
player.title("Audio Player")
player.geometry("300x500")

"""playlist register"""
os.chdir("songs")
print(os.getcwd)
songlist=os.listdir()

"""volume input"""
VolumeLevel=tkr.Scale(player,from_=0.0,to_=1.0,orient=tkr.HORIZONTAL,resolution=0.1 )

"""PLAYLIST"""
playlist=tkr.Listbox(player,highlightcolor="blue",selectmode=tkr.SINGLE)
print(songlist)
for item in songlist:
    pos=0
    playlist.insert(pos,item)
    pos=pos+1
    
"""action"""
def Play():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(playlist.get(tkr.ACTIVE))
    var.set(playlist.get(tkr.ACTIVE))
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(VolumeLevel.get()) 
    print(pygame.mixer.music.get_volume())
    print(VolumeLevel.get())

def Stop():
    pygame.mixer.music.stop()    

def pause():
    pygame.mixer.music.pause()
    
def Unpause():
    pygame.mixer.music.unpause()
    
"""inserting buttons"""
buttton1=tkr.Button(player,width=5,height=3,text="play",command=Play)

buttton2=tkr.Button(player,width=5,height=3,text="Stop",command=Stop)

buttton3=tkr.Button(player,width=5,height=3,text="pause",command=pause)

buttton4=tkr.Button(player,width=5,height=3,text="Unpause",command=Unpause)

var=tkr.StringVar()
songtitle=tkr.Label(player,textvariable=var)

"""arrangment"""
songtitle.pack()
buttton1.pack(fill="x")
buttton2.pack(fill="x")
buttton3.pack(fill="x")
buttton4.pack(fill="x")
VolumeLevel.pack(fill="x")
playlist.pack(fill="both",expand="yes")


player.mainloop()