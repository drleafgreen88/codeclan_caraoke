from classes.guest import *
from classes.room import *
from classes.song import *

import unittest

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.name = "Mick Fleetwood"