from classes.song import *
from classes.guest import *

class Room:

    def __init__ (self, room_name):
        self.room_name = room_name
        self.songs = []
        self.guests = []


    # def add_new_room(self, input_rooms_list):
    #     self.input_room_name.append(self.input_rooms_list)