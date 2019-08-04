import eyed3

__version__ = 0.1


class MusicMetadata:

    def __init__(self, music_address):
        """
        :param music_address: Music File address
        """
        self.music_address = music_address
        self.audiofile = eyed3.load(self.music_address)

    def metadata(self):
        return {'album': self.audiofile.tag.album,
                'album_artist': self.audiofile.tag.album_artist,
                'artist': self.audiofile.tag.artist,
                'genre': str(self.audiofile.tag.genre),
                'title': self.audiofile.tag.title,
                'track_num': self.audiofile.tag.track_num
                }

    def metadata_setter(self, data):

        try:
            self.audiofile.tag.album = data['album'].decode('utf-8')
        except:
            pass

        try:
            self.audiofile.tag.album_artist = data['album_artist'].decode('utf-8')
        except:
            pass

        try:
            self.audiofile.tag.artist = data['artist'].decode('utf-8')
        except:
            pass

        try:
            self.audiofile.tag.genre = data['genre'].decode('utf-8')
        except:
            pass

        try:
            self.audiofile.tag.title = data['title'].decode('utf-8')
        except:
            pass

        try:
            self.audiofile.tag.track_num = int(data['track_num'])
        except:
            pass

        try:
            if data['lyric']:
                track = eyed3.load(self.music_address)
                track.tag.lyrics.set(data['lyric'].decode('utf-8'))
                track.tag.save()
        except:
            pass

        self.audiofile.tag.save()

        return True
