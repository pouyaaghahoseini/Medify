import os

from Logger import Logger

def search_directory(search_dir):
    log = Logger().log
    music_list = []
    # search in given directory
    log('info', 'searching directory to find music')
    for root, dirs, files in os.walk(search_dir):
        for file in files:
            # list of file types
            if file.endswith(".mp3"):
                music_list.append({'address': root + file, 'name': file})

    if music_list:
        log('info', 'searching complete\nmusic files: ' + str(music_list))
    else:
        log('info', 'empty directory. nothing to search')

    return music_list

