import unittest
from src.room import Room

class TestRoom(unittest.TestCase):

    def setUp(self):
        self.room = Room("Room 1", ["Panic Room", "Blue Lights", "Crashed the Wedding"], ["John", "Javier"], 4)
        self.room2 = Room("Room 2", ["This is America", "Teletubbies Theme", "Angeleyes"], ["Jim", "Jimbo", "Greg", "Steve"], 4)

    def test_room_has_name(self):
        self.assertEqual("Room 1", self.room.room_num)

    def test_room_has_playlist(self):
        self.assertEqual(["Panic Room", "Blue Lights", "Crashed the Wedding"], self.room.song)

    def test_room_has_guest(self):
        self.assertEqual(["John", "Javier"], self.room.guest)
    
    def test_room_has_capacity(self):
        self.assertEqual(4, self.room.capacity)

    def test_can_add_guest_to_room(self):
        self.assertEqual(["John", "Javier", "James"], self.room.add_guest_to_room("James"))

    def test_can_add_song_to_room(self):
        self.assertEqual(["Panic Room", "Blue Lights", "Crashed the Wedding", "Bad Habits"], self.room.add_song_to_room("Bad Habits"))
    
    def test_can_remove_guest_from_room(self):
        self.assertEqual(["John"], self.room.remove_guest_from_room("Javier"))
    
    def test_room_cannot_exceed_capacity(self):
        self.assertEqual(["Jim", "Jimbo", "Greg", "Steve"], self.room2.add_guest_to_room("Billybob"))