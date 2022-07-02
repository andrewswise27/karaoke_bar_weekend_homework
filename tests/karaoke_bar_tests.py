import unittest
from src.karaoke_bar import KaraokeBar
from src.room import Room
from src.guest import Guest
from src.song import Song

class TestKaraokeBar(unittest.TestCase):

    def setUp(self):
        
        self.KaraokeBar = KaraokeBar("Little Karaoke Bar", 4, 1000)

        self.room = Room("Room 1", [], [], 4)
        self.room2 = Room("Room 2", [], [], 4)
        self.room3 = Room("Room 3", [], [], 4)
        self.room4 = Room("Room 4", [], [], 4)

        self.guest = Guest("John", 20, {"Post Malone": "Better Now"})
        self.guest2 = Guest("Dave", 50, {"Calvin Harris": "One Kiss"})
        self.guest3 = Guest("Julia", 40, {"Jorja Smith": "Blue Lights"})
        self.guest4 = Guest("Joseph", 35, {"Childish Gambino": "This is America"})
        self.guest5 = Guest("Dean", 25, {"George Ezra": "Shotgun"})
        self.guest6 = Guest("Tom", 55, {"James Arthur": "You Deserve Better"})
        self.guest7 = Guest("Jackie", 37, {"Panic! at the Disco": "High Hopes"})
        self.guest8 = Guest("Khalid", 55, {"DJ Khalid": "No Brainer"})
        self.guest9 = Guest("Nathan", 70, {"Busted": "Air Hostess"})
        self.guest10 = Guest("Joe", 22, {"Sigma": "Anywhere"})
        self.guest11 = Guest("Dwayne", 37, {"Kygo": "Born To Be Yours"})
        self.guest12 = Guest("Justin", 74, {"Sigala": "Just Got Paid"})
        self.guest13 = Guest("Steve", 90, {"Marshmallo": "Happier"})

        self.song = Song("Post Malone", "Better Now")
        self.song2 = Song("Calvin Harris", "One Kiss")
        self.song3 = Song("Jorja Smith", "Blue Lights")
        self.song4 = Song("Childish Gambino", "This is America")
        self.song5 = Song("George Ezra", "Shotgun")
        self.song6 = Song("James Arthur", "You Deserve Better")
        self.song7 = Song("Panic! at the Disco", "High Hopes")
        self.song8 = Song("DJ Khalid", "No Brainer")
        self.song9 = Song("Busted", "Air Hostess")
        self.song10 = Song("Sigma", "Anywhere")
        self.song11= Song("Kygo", "Born To Be Yours")
        self.song12 = Song("Sigala", "Just Got Paid")
        self.song13 = Song("Marshmallo", "Happier")
        

    def test_karaoke_bar_has_name(self):
        self.assertEqual("Little Karaoke Bar", self.KaraokeBar.name)

    def test_karaoke_bar_has_till(self):
        self.assertEqual(1000, self.KaraokeBar.till)

    def test_karaoke_bar_has_set_number_of_rooms(self):
        self.assertEqual(4, self.KaraokeBar.rooms)