# https://blog.naver.com/kiddwannabe/221790727905
# https://hello-bryan.tistory.com/249

import sys
from pytube import YouTube
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QFileDialog


class MainClass(QMainWindow):
    def __init__(self):
        super(MainClass, self).__init__()
        self.ui = uic.loadUi("./ui/YouDown.ui", self)
        self.ui.show()
        self.fPath = None
        self.find_btn.clicked.connect(self.findVideo)
        self.pushButton.clicked.connect(self.down)
        self.pushButton_2.clicked.connect(self.setPath)

    def setPath(self):
        self.fPath = QFileDialog.getExistingDirectory(self, 'Open file', './')
        self.path_label.setText(self.fPath)

    def down(self):
        if self.fPath:
            self.vlist[self.comboBox.currentIndex()].download(self.fPath)
        else:
            QMessageBox.information(self, "Check the Path", "Please check the Path.", buttons=QMessageBox.Ok)

    def findVideo(self):
        self.comboBox.clear()
        if self.videolink_lineEdit.text():
            try:
                video_url = self.videolink_lineEdit.text()
                yt = YouTube(video_url)
                self.title_label.setText("[Title] " + yt.title)    
                self.author_label.setText("[Author] " + yt.author)
                self.views_label.setText("[Views] " + str(yt.views))
                self.rating_label.setText("[Rating] " + str(yt.rating))
                self.time_label.setText("[Time(second)] " + str(yt.length))
                self.age_restricted_label.setText("[Age Restricted] " + str(yt.age_restricted))
                self.description_textEdit.setText(yt.description)
                print("[썸네일URL]", yt.thumbnail_url) # 썸네일 url 주소
                self.vlist = yt.streams.all()
                print(type(self.vlist))
                for i in range(len(self.vlist)):
                    vvv = str(self.vlist[i]).split(" ")
                    print(vvv[i])
                    if "video" in vvv[-1]:
                        vType = (vvv[2].split("\""))[1].split("/")[-1]
                        vRes = vvv[3].split("\"")[1]
                        vFps = vvv[4].split("\"")[1]
                        name = f"Video / {vType} / {vRes} / {vFps}"
                        self.comboBox.addItem(name)
                    elif "audio" in vvv[-1]:
                        vType = (vvv[2].split("\""))[1].split("/")[-1]
                        vabr = vvv[3].split("\"")[1]
                        name = f"Audio / {vType} / {vabr}"
                        self.comboBox.addItem(name)
            except:
                QMessageBox.information(self, "Check the Link", "Please check the link.", buttons=QMessageBox.Ok)
        else:
            QMessageBox.information(self, "Enter the Link", "Please enter the link.", buttons=QMessageBox.Ok)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainClass()
    app.exec_()
