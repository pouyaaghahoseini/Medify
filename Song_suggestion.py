import os

import billboard

import Music_metadata
import Search_directory
import Logger
charts = [
    'hot-100',
    'r-b-hip-hop-songs',
    'pop-songs',
    'country-songs',
    'rock-songs',
    'dance-electronic-songs',
    'latin-songs'
]

logger = Logger.Logger().log

def checkSonginChart(source, des, chartname, chart):
    musicMD = Music_metadata.MusicMetadata(source)

    title = musicMD.metadata()['title']
    artist = musicMD.metadata()['artist']

    if not os.path.exists(des + '/' + chartname + '/'):  # Creating Chart Folder
        os.makedirs(des + '/' + chartname + '/')

    for song in chart:  # Searching For Song In Chart
        if song.title == title and song.artist == artist:
            if os.path.isfile(des + '/' + chartname + '/' + artist + "-" + title + ".mp3"):  # Check if shortcut exists
                logger('error', 'Symbolic Link for ' + title + ' already exist')
                break
            os.symlink(source, des + '/' + chartname + '/' + artist + "-" + title + ".mp3")  # Creating Shortcut
            logger('info', 'Creating Symbolic Link for ' + title + ' by ' + artist)


# source = '/home/pouya/Desktop/Drake Nice For What'
# des = '/home/pouya/Desktop'

def createPlaylists(source, des):
    folder_songs = Search_directory.search_directory(source)
    logger('info', 'Song Suggestion STARTED')
    for chart_name in charts:
        logger('info', 'Working on ' + chart_name)
        chart = billboard.ChartData(chart_name)
        for song in folder_songs:
            logger('info', "Checking : " + song['address'] + ' if exist in top charts')
            checkSonginChart(song['address'], des, chart_name, chart)
