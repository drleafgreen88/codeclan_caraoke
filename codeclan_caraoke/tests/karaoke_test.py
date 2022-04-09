from classes.room import *
from classes.song import *
from classes.guest import *
from classes.karaoke import *

import unittest

class TestKaraoke(unittest.TestCase):

    def setUp(self):
        self.karaoke = Karaoke("CodeClan Caraoke")
        # self.name = "CodeClan Caraoke"
        # self.rooms_list = ["1980s Room", "1990s Room", "2000s Room"]
        # self.songs_list = ["Don't Stop Believing", "Bat Out of Hell", "Paradise City"]
        # self.guest_list = ["Tom Petty", "Bruce Springsteen", "Bob Dylan"]

    def test_add_new_room(self):
        self.karaoke.add_new_room(Room("2010s Room"))
        self.assertEqual(1, len(self.karaoke.rooms_list))
        self.assertEqual("2010s Room", self.karaoke.rooms_list[0].room_name)

    def test_add_new_song(self):
        self.karaoke.add_new_song(Song("Blinding Lights"))
        self.assertEqual(1, len(self.karaoke.songs_list))

    def test_add_new_guest(self):
        self.karaoke.add_new_guest(Guest("Mick Fleetwood"))
        self.assertEqual(1, len(self.karaoke.guest_list))

    def test_add_guest_to_room(self):
