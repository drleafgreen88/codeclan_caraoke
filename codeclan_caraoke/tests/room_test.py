from classes.room import *
from classes.song import *
from classes.guest import *
from classes.karaoke import *

import unittest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("2010s Room")
        self.songs = Song("Blinding Lights")
        self.guests = Guest("Mick Fleetwood")
        

    def test_guest_has_name(self):
        self.assertEqual("Mick Fleetwood", self.guests.name)

    def test_room_has_name(self):
        self.assertEqual("2010s Room", self.room.room_name)