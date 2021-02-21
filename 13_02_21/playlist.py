class User:
    def __init__(self):
        pass

    def delete_playlist(self, name):
        playlist = Playlist.get(name=name, created_by=self)
        playlist_songs = PlaylistSong.filter(playlist=playlist)
        playlist_songs.delete()

