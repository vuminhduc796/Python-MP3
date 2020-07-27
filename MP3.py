import pygame
import mutagen.mp3
import tkinter as tk
import glob, os
from tkinter import *


class main(object):
    def __init__(self,master):
        self.master = master
        pygame.init()
        pygame.mixer.music.set_volume(0.5)
        os.chdir("./music")
        self.song_list = glob.glob("*.mp3")
        os.chdir("../icon")
        self.current_song = self.song_list[1]
        self.playing = False
        self.topFrame = Frame( master , bg="#edc0c3", width=400, height=50).grid(column = 0,row = 0, columnspan = 3)

        self.volume_label = Label(master,text = "Volume",font=("Comic Sans MS", 14, "bold")).grid(row = 1, column = 0, sticky = S )
        self.volume_widget = Scale(master, from_= 0, to = 100, orient=HORIZONTAL, length = 150, command = self.change_volume)
        self.volume_widget.set(50)
        self.volume = self.volume_widget.get()
        self.volume_widget.grid(row = 1,column = 1, columnspan = 2, sticky = N)

        self.speed_label = Label(master, text ="Speed", font=("Comic Sans MS", 14, "bold")).grid(row = 2, column = 0, sticky = S)

        self.speed_widget = Scale(master, from_= 0, to = 100, orient=HORIZONTAL, length = 150 ,command = self.change_speed)
        self.speed_widget.set(50)
        self.speed = self.volume_widget.get()
        self.speed_widget.grid(row = 2,column = 1, columnspan = 2, sticky = N)

        self.midFrame = Frame(master, bg="#edc0c3", width=400, height=350).grid(column=0, row=3, columnspan=3 , rowspan=len(self.song_list),pady = 20)
        self.name_label = Label(master, text="Song List",bg="#edc0c3", font=("Bernard MT Condensed", 17)).grid(row=3, column=0,
                                                                                                  columnspan = 3,sticky = N,pady = 20)

        self.icon_back = PhotoImage(file="back.png").subsample(15,15)
        self.icon_next = PhotoImage(file="next.png").subsample(15,15)
        self.icon_pause = PhotoImage(file="pause.png").subsample(15,15)
        self.icon_resume = PhotoImage(file = "resume.png").subsample(15,15)

        self.back_button = tk.Button(player, width=50, height=50, image=self.icon_back, command=self.back)
        self.back_button.grid(row = 10, column = 0,sticky = S + E)
        self.resume_button = tk.Button(player, width=50, height=50, image = self.icon_resume, command=self.resume)
        self.resume_button.grid(row = 10, column = 1)
        self.next_button = tk.Button(player, width=50, height=50, image = self.icon_next, command=self.next)
        self.next_button.grid(row = 10, column = 2, sticky = S + W)
        os.chdir("../music")
        self.update_songlist()

    def update_songlist(self):
        update_call = lambda x: (lambda p: self.change_song(x))
        for song_index in range(len(self.song_list)):
            song_label = Label(self.midFrame, text=self.song_list[song_index], fg="#381310", bg="#edc0c3", font=("Comic Sans MS", 12))
            song_label.grid(row=3 + song_index, column = 0, columnspan = 3,sticky = W,padx = 20)
            song_label.bind("<Button-1>", update_call(self.song_list[song_index]))

    def change_song(self,song):
        self.current_song = song
        self.play(5000)
    def change_speed(self,value):
        self.speed = int(value)


    def change_volume(self,value):
        pygame.mixer.music.set_volume(0.5*int(value)/50)

    def resume(self):
        if self.playing is True:
            pygame.mixer_music.unpause()
            self.resume_button["image"] = self.icon_pause
            self.resume_button["command"] = self.pause
        else:
            self.play(int(50000 * int(self.speed)/ 50))
    def play(self, speed):
        self.playing = True
        mp3 = mutagen.mp3.MP3(self.current_song)
        pygame.mixer.init(frequency=50000)

        pygame.mixer_music.load(self.current_song)
        pygame.mixer_music.play()
        self.resume_button["image"] = self.icon_pause
        self.resume_button["command"] = self.pause
        self.song_name = Label(self.topFrame, text=self.current_song[:-4], bg='#edc0c3', fg='#381310',
                               font=("Bernard MT Condensed", 25, "bold")).grid(column=1, row=0)
    def pause(self):
        self.resume_button["image"] = self.icon_resume
        self.resume_button["command"] = self.resume
        pygame.mixer_music.pause()

    def next(self):
        temp_index = self.song_list.index(self.current_song)
        if temp_index == len(self.song_list) -1 :
            self.current_song = self.song_list[0]
        else:
            self.current_song = self.song_list[temp_index+1]
        self.play(int(50000 * int(self.speed)/ 50))

    def back(self):
        temp_index = self.song_list.index(self.current_song)
        if temp_index == 0:
            self.current_song = self.song_list[len(self.song_list) - 1]
        else:
            self.current_song = self.song_list[temp_index - 1]
        self.play(int(50000 * int(self.speed)/ 50))

if __name__ == "__main__":
    player = tk.Tk()
    player.title("Music Player")
    player.geometry("400x600")
    m=main(player)
    player.mainloop()