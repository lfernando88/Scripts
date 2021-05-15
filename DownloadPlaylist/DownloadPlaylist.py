from pytube import YouTube
from pytube import Playlist
import moviepy.editor as mp
import re
import os


class MovieToMp3:
    l = Playlist(input('Informe o link: '))
    p = input('Informe o diretório: ')

    def __init__(self, link=l, path=p):
        self.link = link
        self.path = path

    def download(self):
        for url in self.link.video_urls:
            try:
                print(url)
                lk = YouTube(url)
                print('Baixando...')
                lk.streams.filter(only_audio=True).first().download(self.path)
                print('Download Completo')
            except:
                print(f'Não foi possível fazer download da música: {url}')

    def converte(self):
        self.download()
        for file in os.listdir(self.path):
            if re.search('mp4', file):
                mp4_dir = os.path.join(self.path, file)
                mp3_dir = os.path.join(self.path, os.path.splitext(file)[0] + '.mp3')
                new_file = mp.AudioFileClip(mp4_dir)
                new_file.write_audiofile(mp3_dir)
                os.remove(mp4_dir)


a = MovieToMp3()
a.converte()
