import pygame
import mutagen.mp3
import tkinter as tk
from tkinter import *


class main(object):
    def __init__(self,master):
        self.master = master
        pygame.init()
        self.file = "test1.mp3"
        self.playing = False
        self.icon_back = PhotoImage(file="back.png").subsample(15,15)
        self.icon_next = PhotoImage(file="next.png").subsample(15,15)
        self.icon_pause = PhotoImage(file="pause.png").subsample(15,15)
        self.icon_resume = PhotoImage(file = "resume.png").subsample(15,15)
        self.back_button = tk.Button(player, width=50, height=50, image=self.icon_back, command=self.resume)
        self.back_button.grid(row = 1, column = 0,sticky = S)
        self.resume_button = tk.Button(player, width=50, height=50, image = self.icon_resume, command=self.resume)
        self.resume_button.grid(row = 1, column = 1)
        self.next_button = tk.Button(player, width=50, height=50, image = self.icon_next, command=self.resume)
        self.next_button.grid(row = 1, column = 2)
    def resume(self):
        if self.playing is True:
            pygame.mixer_music.unpause()
            self.resume_button["image"] = self.icon_pause
            self.resume_button["command"] = self.pause
        else:
            self.play()
    def play(self):
        self.playing = True
        mp3 = mutagen.mp3.MP3(self.file)
        pygame.mixer.init(frequency=46000)
        pygame.mixer_music.load(self.file)
        pygame.mixer_music.play()
        self.resume_button["image"] = self.icon_pause
        self.resume_button["command"] = self.pause
    def pause(self):
        self.resume_button["image"] = self.icon_resume
        self.resume_button["command"] = self.resume
        pygame.mixer_music.pause()




if __name__ == "__main__":
    player = tk.Tk()
    player.title("Music Player")
    player.geometry("200x340")
    m=main(player)
    player.mainloop()