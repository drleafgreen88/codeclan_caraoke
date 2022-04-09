from classes.room import *
from classes.song import *
from classes.guest import *
from classes.karaoke import *

import unittest

class TestKaraoke(unittest.TestCase):

    def setUp(self):
        self.name = "CodeClan Caraoke"
        self.rooms_list = ["1980s Room", "1990s Room", "2000s Room"]
        self.songs_list = ["Don't Stop Believing", "Bat Out of Hell", "Paradise City"]
        self.guest_list = ["Tom Petty", "Bruce Springsteen", "Bob Dylan"]

    # def test_add_new_room(self):
    #     self.assertEqual("2010s Room", self.rooms_list)