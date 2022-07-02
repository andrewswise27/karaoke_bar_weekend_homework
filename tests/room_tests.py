import unittest
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room 1 ", ["Panic Room", "Blue Lights", "Crashed the Wedding"], [], 4)