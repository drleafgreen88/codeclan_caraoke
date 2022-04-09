from classes.room import *
from classes.song import *
from classes.guest import *
from classes.karaoke import *

import unittest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.name = "CodeClan Caraoke"
        self.rooms_list = ["2000s Room", "1990s Room", "1980s Room"]
        self.songs_list = ["Don't Stop Believing", "Bat Out of Hell", "Paradise City"]
        self.guest_list = ["Tom Petty", "Bruce Springsteen", "Bob Dylan"]

    # def test_add_new_room(self, input_room_name):
        