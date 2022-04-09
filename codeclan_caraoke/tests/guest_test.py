from classes.guest import *
from classes.room import *
from classes.song import *
from classes.karaoke import *

import unittest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Mick Fleetwood")

    def test_guest_has_name(self):
        self.assertEqual("Mick Fleetwood", self.guest.name)