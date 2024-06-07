import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

import pygame

class MusicPlayer:
    def __init__(self,master):
        self.master=master
        master.title("Music Player")

        pygame.init()
        pygame.mixer.init()

        self.playerframe=tk.Frame(master,bg="#333")
        self.playerframe.pack(pady=20)

        self.playlistframe=tk.Frame(master, bg="#333")
        self.playlistframe.pack()

        self.playbutton=tk.Button(self.playerframe,text="Play",command=self.playmusic,width=10,bg="#4CAF50",fg="white",font=("Arial",12),relief="flat")
        self.playbutton.pack(side="left",padx=10)

        self.pausebutton=tk.Button(self.playerframe,text="Pause",command=self.pausemusic,width=10,bg="#FFC107",fg="white",font=("Arial",12),relief="flat")
        self.pausebutton.pack(side="left",padx=10)

        self.stopbutton=tk.Button(self.playerframe,text="Stop",command=self.stopmusic,width=10,bg="#F44336",fg="white",font=("Arial",12),relief="flat")
        self.stopbutton.pack(side="left",padx=10)

        self.addbutton=tk.Button(self.playlistframe,text="Add Song",command=self.addsong,width=10,bg="#2196F3",fg="white",font=("Arial",12),relief="flat")
        self.addbutton.pack(side="left",padx=10) 

        self.removebutton=tk.Button(self.playlistframe,text="Remove Song",command=self.removesong,width=10,bg="#9C27B0",fg="white",font=("Arial",12),relief="flat")
        self.removebutton.pack(side="left",padx=10)   

        self.playlistbox=tk.Listbox(self.playlistframe,selectmode=tk.SINGLE,bg="#222",fg="#eee",font=("Arial",10),highlightthickness=0)
        self.playlistbox.pack(pady=10)

        self.currentsong=None
        self.playlist=[]

    def playmusic(self):
        if self.playlistbox.curselection():
            index=self.playlistbox.curselection()[0]
            song=self.playlist[index]

            if self.currentsong is not None:
                pygame.mixer.music.stop()
            
            pygame.mixer.music.load(song)
            pygame.mixer.music.play()
            self.currentsong=song
        else:
            tk.messagebox.showwarning("Warning", "Please select a song from the playlist.")

    def pausemusic(self):
        if self.currentsong is not None:
            pygame.mixer.music.pause()

    def stopmusic(self):
        if self.currentsong is not None:
            pygame.mixer.music.stop()
            self.currentsong=None

    def addsong(self):
        song=filedialog.askopenfilename(
            initialdir="/",
            title="Select Song",
            filetypes=(("MP3 Files","*.mp3"),)
        )
        if song:
            self.playlist.append(song)
            self.playlistbox.insert(tk.END,song)

    def removesong(self):
        if self.playlistbox.curselection():
            index=self.playlistbox.curselection()[0]
            pygame.mixer.music.stop()
            self.playlist.pop(index)
            self.playlistbox.delete(index)
            if self.currentsong == self.playlist[index]:
                self.currentsong=None


root=tk.Tk()
root.configure(bg="#222")
player = MusicPlayer(root)
root.mainloop()

