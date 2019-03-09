import ctypes
import requests
import os
from os.path import basename
from bs4 import BeautifulSoup


class App:
    def __init__(self):

        try:
            with open('D:/RZECZY/mystuff/PYTHON/wallpaper_changer/id.txt') as f:
                self.id = int(f.read())
        except FileNotFoundError:
            self.id = 0

        self.html = 'https://alpha.wallhaven.cc/search?q=&categories=100&purity=100&resolutions=1366x768&sorting=views&order=desc&page=' + str(self.id // 24 +1)
    def get_image(self):

        req = requests.get(self.html)
        soup = BeautifulSoup(req.content, 'lxml')

        ## MAIN PAGE ##

        link = soup.select('div > section > ul > li')[int(self.id%24)].a['href']


        ## PAGE WITH IMAGE ##
        soup = BeautifulSoup(requests.get(link).content, 'lxml')
        link = soup.select('main > section > div > img')[0]['src']

        lnk = 'https:'+link


        with open('D:\\RZECZY\\FOTY\\tapety\\%s.jpg' % (self.id%24), 'wb') as f:
            f.write(requests.get(lnk).content)



    def set_wallpaper(self):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, "D:\\RZECZY\\FOTY\\tapety\\%s.jpg" % (self.id%24) , 0)

    def run(self):
        print(self.id)
        self.get_image()
        self.set_wallpaper()
        self.write_id()

    def write_id(self):
        self.id += 1
        with open('D:\\RZECZY\\mystuff\\PYTHON\\wallpaper_changer\\id.txt', 'w') as f:
            f.write(str(self.id))

if __name__ == '__main__':
    app = App()
    app.run()
