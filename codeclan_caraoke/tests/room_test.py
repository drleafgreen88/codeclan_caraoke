from classes.room import *
from classes.song import *
from classes.guest import *

import unittest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room_name = Room("2010s Room", "Alligator", "Stevie Nicks")
        self.songs = Song("Go Your Own Way")
        self.guests = Guest("Mick Fleetwood")
        self.input_songs = []
        self.input_guests = []

    def test_guest_has_name(self):
        self.assertEqual("Mick Fleetwood", self.guests)