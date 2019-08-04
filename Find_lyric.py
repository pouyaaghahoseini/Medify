import lyricsgenius as genius

from Logger import Logger
from Music_metadata import MusicMetadata

api = genius.Genius('jMBPEUpYtfpxRiLxuAkrl_qkD_yOnwYOogk0lQcRmGAJCQE3PfE-UPkfe4tJqyls')


def get_lyric(track_address):
    track_data = MusicMetadata(track_address)
    track_metadata = track_data.metadata()
    artist = track_metadata['artist']
    title = track_metadata['title']

    log = Logger().log

    try:
        lyric = api.search_song(song_title=title, artist_name=artist).save_lyrics(filename='tmp_lyric.txt',
                                                                                  overwrite=True)
        log('info', 'Lyric FOUND')
    except:
        log('error', 'Unknown error happened while downloading ' + str(title) + " " + str(artist) + " cover")
        return 0

    log('info', 'Changing Lyric')
    track_data.metadata_setter({'lyric': lyric})

    return True


if __name__ == '__main__':
    music_address = input()
    get_lyric(music_address)
