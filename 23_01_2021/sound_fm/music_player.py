# from __future__ import generator_stop
import string

class Person:

    def __init__(self, first_name,
          last_name,
          email,
          password=None,
          profile_pic=None,
          birth_date=None):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password or Person.generate_password()
        self.profile_pic = profile_pic
        self.birth_date = birth_date

    def validate(self):
        if not '@' in self.email:
            raise Exception('Imput correct value for email.')
        if set(self.birth_date) > set(string.digits + ':'):
            raise Exception('Input correct value for datetime.')

    @staticmethod
    def generate_password(p: 'Person'):
        pass

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self):
        dict_person = {"first_name": self.first_name,
                       'last_name': self.last_name}

    @staticmethod
    def get(email):
        return 'Person'



class Song:
    SONGS_COUNT = 0
    def __init__(self, title, artist, duration, genre, album):
        self.title = title
        self.artist = artist
        self.duration = duration
        self.genre = genre
        self.album = album
        self.__views = 0

        Song.SONGS_COUNT += 1

    def play(self):
        self.__views += 1

    def __str__(self):
        return f'{self.title} - {self.artist}'

    @property
    def view(self):
        return self.__views


class Playlist:
    def __init__(self, title, songs, created_by):
        self.title = title
        self.songs = songs
        self.created_by = created_by


class PersonPlaylist:

    def __init__(self, person, playlist):
        self.person = person
        self.playlist = playlist



if __name__ == '__main__':
    person_attrs = input('Input Person first name, last name, email, password, profile picture, birth date: ').split(',')
    song_attrs = input('Input Song title, artist, duration, genre, album: ').split(',')
    song_1 = Song(*song_attrs)
    song_1.play()
    print(song_1.view)
    person = Person(*person_attrs)

    print(song_1)
    print(person)

# Angela, Markosyan, ang@ru.sd, password, https://google.com, 1995:01:01
# Stairway to Heaven, Led Zeppelin, 4:15, rock, Album-1