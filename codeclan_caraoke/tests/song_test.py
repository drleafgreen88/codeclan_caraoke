from classes.song import *
from classes.room import *
from classes.guest import *
from classes.karaoke import *

import unittest

class TestSong(unittest.TestCase):

    def setUp(self):
        self.title = "Blinding Lights"

    # @unittest.skip("delete this line to run the test")   