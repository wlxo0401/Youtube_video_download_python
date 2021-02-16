import sys

from pytube import YouTube
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow


class MainClass(QMainWindow):
    def __init__(self):
        super(MainClass, self).__init__()
        self.ui = uic.loadUi("./ui/YouDown.ui", self)
        self.ui.show()
        video_url = 'https://youtu.be/eKFTSSKCzWA'
        yt = YouTube(video_url)
        print("[영상 제목]", yt.title)  # 영상제목
        print("[영상 게시자]", yt.author) # 영상 게시자
        print("[조회수]", yt.views)
        print("[평균평점]", yt.rating) # 평균 평점
        print("[영상길이(초)]", yt.length)
        print("[연령제한여부]", yt.age_restricted)
        print("[영상 설명]", yt.description) # 영상 설명
        print("[썸네일URL]", yt.thumbnail_url) # 썸네일 url 주소


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainClass()
    app.exec_()
