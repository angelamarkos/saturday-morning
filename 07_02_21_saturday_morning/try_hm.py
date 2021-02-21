class Song:
    def __init__(self, artst, title):
        self.artist = artst
        self.title = title

    def add_to_playlist(self, playlist):
        return PlaylistSong(playlist, self)

    def __str__(self):
        return f'{self.artist}-{self.title}'

class Artist:
    def __init__(self):
        pass


class Playlist:
    def __init__(self, name):
        self.name = name

    def add_songs(self, songs):
        for song in songs:
            yield PlaylistSong(self, song)


class PlaylistSong:
    def __init__(self, playlist, song):
        self.playlist = playlist
        self.song = song


playlist = Playlist('Playlist_1')
song_1 = Song('Artist_1', 'title_1')
song_2 = Song('Artist_2', 'title_2')
song_3 = Song('Artist_3', 'title_3')
song_4 = Song('Artist_4', 'title_4')
playlist_2 = Playlist('Playlist_2')

playlist_song_couple = list(playlist.add_songs([song_1, song_2, song_3]))
playlist_song_couple += list(playlist_2.add_songs([song_4, song_2, song_3]))

playlist_1_songs = [ps.song for ps in playlist_song_couple if ps.playlist.name == playlist.name]

for song in playlist_1_songs:

    print(song)

