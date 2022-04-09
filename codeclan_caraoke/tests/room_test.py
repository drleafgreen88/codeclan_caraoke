from classes.room import *
from classes.song import *
from classes.guest import *
from classes.karaoke import *

import unittest

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("2010s Room")
        self.room.guests.append(Guest("Mick Fleetwood"))
        
    def test_room_has_name(self):
        self.assertEqual("2010s Room", self.room.room_name)

    def test_add_guest_to_room(self):
        self.room.add_guest_to_room(Guest("Mick Fleetwood"))
        self.assertEqual(2, len(self.room.guests))

    def test_remove_guest_from_room(self):
        self.room.remove_guest_from_room(self.room.guests[0])
        self.assertEqual(0, len(self.room.guests))

    def test_add_song_to_room(self):
        self.room.add_song_to_room(Song("Blinding Lights"))
        self.assertEqual(1, len(self.room.songs))