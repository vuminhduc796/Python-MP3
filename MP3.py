import pygame
import mutagen.mp3
import tkinter as tk
from tkinter import *


class main(object):
    def __init__(self,master):
        self.master = master
        pygame.init()
        self.file = "test1.mp3"
        self.play_button = tk.Button(player, width=5, height=3, text="Play", command=self.play)
        self.play_button.grid(row = 0,column = 0)
        self.stop_button = tk.Button(player, width=5, height=3, text="Play", command=self.exit)
        self.stop_button.grid(row = 0, column = 1)
        self.icon_back = PhotoImage(file="back.png").subsample(15,15)
        self.icon_next = PhotoImage(file="next.png").subsample(15,15)
        self.stop_button = tk.Button(player, width=50, height=50, image=self.icon_back, command=self.exit)
        self.stop_button.grid(row = 1, column = 0)
        self.stop_button = tk.Button(player, width=50, height=50, image = self.icon_next, command=self.exit)
        self.stop_button.grid(row = 1, column = 1)

    def play(self):
        mp3 = mutagen.mp3.MP3(self.file)
        pygame.mixer.init(frequency=44100)
        pygame.mixer_music.load(self.file)
        pygame.mixer_music.play()

    def exit(self):
        pygame.mixer_music.stop()




if __name__ == "__main__":
    player = tk.Tk()
    player.title("Music Player")
    player.geometry("200x340")
    m=main(player)
    player.mainloop()