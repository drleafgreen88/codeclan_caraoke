from classes.guest import *
from classes.room import *
from classes.song import *

class Karaoke:
    def __init__ (self, name):
        self.name = name
        self.rooms_list = []
        self.guest_list = []
        self.songs_list = []

    def add_new_room(self, room):
        self.rooms_list.append(room)

    def add_new_song(self, song):
        self.songs_list.append(song)

    def add_new_guest(self, guest):
        self.guest_list.append(guest)