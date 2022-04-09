from classes.room import *
from classes.song import *
from classes.guest import *

import unittest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_name = Room("2010s Room")
        # self.rooms_list = ["80s Room", "90s Room", "00s Room"]
        self.songs = Song("Go Your Own Way")
        self.guests = Guest("Mick Fleetwood")

    # def test_can_add_new_room (self):
        # self.assertEqual("10s Room", self.rooms_list)

    def test_room_has_name(self):
        self.assertEqual("2010s Room", self.room_name)