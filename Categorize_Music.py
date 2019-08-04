import json
import os
import shutil

from Logger import Logger
from Music_metadata import MusicMetadata

__version__ = 0.1


class CategorizeMusic:

    def __init__(self, music_list):
        """
        :param music_list: get Music List
        """

        self.music_list = music_list
        self.logger = Logger().log

        # Loading Necessary Information from Config File
        with open("/home/milad/College/Medify/config/config.json") as config_file:
            config_data = json.load(config_file)
            self.music_location = config_data['music']['location']

        self.move_file()

    def artist(self, track_metadata):
        file_dst = self.music_location + 'Artists/' + track_metadata['artist'] + '/' + track_metadata['album']
        return file_dst

    def album(self, track_metadata):
        file_dst = self.music_location + 'Albums/' +  track_metadata['album']
        return file_dst

    def genre(self, track_metadata):
        file_dst = self.music_location + 'Genres/' + track_metadata['genre']
        return file_dst

    def move_track(self, file_dst, music_file):

        # Create directories and move file
        if not os.path.exists(file_dst):
            os.makedirs(file_dst)
            self.logger('info', 'directory not found!\nCreating directory: ' + file_dst)

        try:
            shutil.move(src=music_file['address'], dst=file_dst)
        except shutil.Error as shutil_error:
            self.logger('error', "File can't be moved\n" + str(shutil_error))
        except IOError as io_error:
            self.logger('error', str(io_error))
        except:
            self.logger('error', 'Unknown Error')

    def link_track(self, file_dst, music_file):

        # Create directories and move file
        if not os.path.exists(file_dst):
            os.makedirs(file_dst)
            self.logger('info', 'directory not found!\nCreating directory: ' + file_dst)

        try:
            os.symlink(music_file['address'], file_dst + '/' + music_file['name'])
        except os.error as os_error:
            self.logger('error', "File can't be moved\n" + str(os_error))
        except IOError as io_error:
            self.logger('error', str(io_error))
        except:
            self.logger('error', 'Unknown Error')

    def move_file(self):

        for music_file in self.music_list:
            metadata = MusicMetadata(music_file['address']).metadata()  # Get Metadata

            self.link_track(self.artist(metadata), music_file)
            self.link_track(self.album(metadata), music_file)
            self.link_track(self.genre(metadata), music_file)
