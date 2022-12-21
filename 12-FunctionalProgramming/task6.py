class Music:
        def __init__(self, artist, song, album, year):
            self.artist = artist
            self.song = song
            self.album = album
            self.year = year
        
        def __str__(self):
            return  f"""Performer : {self.artist}
                        Song : {self.song}
                        Album : {self.album}
                        Year : {self.year}"""

music_info = Music("Ed Sheeran","Hearts Don't Break Around Here", "Divide","2017")
music_info1 = Music("Queen", "Bohemian Rhapsody", "Album","1978")
music_info2 = Music("Kiss", "I was made for lovin' you", "Dynasty","1979")
print(music_info)       
print(music_info1) 
print(music_info2)        


