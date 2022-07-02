class Room:
    def __init__(self, _room_num, _song, _guest, _capacity):
        self.room_num = _room_num
        self.song = _song
        self.guest = _guest
        self.capacity = _capacity
        
    def add_guest_to_room(self, name):
        if len(self.guest) < 4:
            self.guest.append(name)
        return self.guest

    def remove_guest_from_room(self, name):
        self.guest.remove(name)
        return self.guest
    
    def add_song_to_room(self, song):
        self.song.append(song)
        return self.song
