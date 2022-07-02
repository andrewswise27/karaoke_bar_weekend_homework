import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Bad Blood", "Nao")
        self.song2 = Song("This is America", "Childish Gambino")

    def test_song_has_name(self):
        self.assertEqual("Bad Blood", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Childish Gambino", self.song2.artist)