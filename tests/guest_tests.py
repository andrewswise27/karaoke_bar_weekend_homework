import unittest
from src.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("John", 25, "Panic Room")
    
    def test_guest_has_name(self):
        self.assertEqual("John", self.guest.name)

    def test_guest_has_money(self):
        self.assertEqual(25, self.guest.money)
    
    def test_guest_has_fav_song(self):
        self.assertEqual("Panic Room", self.guest.fav_song)