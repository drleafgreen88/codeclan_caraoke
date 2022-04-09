from classes.song import *
from classes.guest import *

class Room:

    def __init__ (self, input_room_name):
        self.input_room_name = input_room_name
        self.input_songs = []
        self.input_guests = []


    # def add_new_room(self, input_rooms_list):
    #     self.input_room_name.append(self.input_rooms_list)