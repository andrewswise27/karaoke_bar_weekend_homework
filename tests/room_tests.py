import unittest
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room 1", ["Panic Room", "Blue Lights", "Crashed the Wedding"], ["John"], 4)

    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room.room_num)

    def test_room_has_playlist(self):
        self.assertEqual(["Panic Room", "Blue Lights", "Crashed the Wedding"], self.room.song)

    def test_room_has_guest(self):
        self.assertEqual(["John"], self.room.guest)
    
    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)